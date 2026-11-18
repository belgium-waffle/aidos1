"""Build a vllm.LLM with Aidos enabled, from a head bundle.

A head bundle is a directory with the trained heads (head_<kind>.pt) and one runtime file per
cost setting (runtime_lam<λ>.json, the thresholds and calibrations chosen on validation data),
written by the research pipeline's export step. Released bundles: see README.

    rt = runtime_config("bundles/qwen2.5-7b-instruct", lam=1.0, retriever="corpus.jsonl")
    llm = make_llm("Qwen/Qwen2.5-7B-Instruct", rt)
    outs = llm.generate(prompts, SamplingParams(temperature=0, max_tokens=32,
                                                extra_args={QUERY_KEY: question}))

For `vllm serve`, write the runtime file and pass it through the environment instead:
    aidos config bundles/qwen2.5-7b-instruct --lam 1 --retriever corpus.jsonl -o aidos.json
    AIDOS_CONFIG=aidos.json vllm serve Qwen/Qwen2.5-7B-Instruct \
        --scheduler-cls aidos.engine.scheduler.AidosScheduler --no-async-scheduling
"""

from __future__ import annotations

import dataclasses
import json
import os
import tempfile
from pathlib import Path
from typing import Any

from ..utils import get_logger
from .config import ENV_VAR, RuntimeConfig

log = get_logger("aidos.factory")
SCHEDULER_CLS = "aidos.engine.scheduler.AidosScheduler"


def bundle_lams(bundle: str | os.PathLike) -> list[float]:
    return sorted(float(p.stem.split("lam", 1)[1]) for p in Path(bundle).glob("runtime_lam*.json"))


def runtime_config(bundle: str | os.PathLike, lam: float = 1.0, policy: str | None = None,
                   retriever: str | None = None, **overrides: Any) -> RuntimeConfig:
    """Runtime config from a head bundle at cost setting `lam` (must be one the bundle was
    calibrated for). `policy` overrides the bundle's policy (e.g. "observe" scores without
    acting); `retriever` is a BM25 index dir, a corpus .jsonl ({"title","text"} per line, BM25
    built in memory), a query->passages cache .jsonl, or "python:module:factory"."""
    b = Path(bundle).resolve()
    f = b / f"runtime_lam{lam:g}.json"
    if not f.exists():
        raise FileNotFoundError(f"{b} has no calibration for lam={lam:g}; available: {bundle_lams(b)}")
    kw = json.loads(f.read_text(encoding="utf-8"))
    kw["head_dir"] = str(b)
    if policy is not None:
        kw["policy"] = policy
    if retriever is not None:
        kw["retriever"] = retriever
    # RuntimeConfig itself refuses a retrieving policy without a retriever
    known = {fl.name for fl in dataclasses.fields(RuntimeConfig)}
    unknown = sorted((set(kw) | set(overrides)) - known)
    if unknown:
        raise ValueError(f"unknown runtime settings: {unknown}")
    kw.update(overrides)
    return RuntimeConfig(**kw)


def _engine_arg_names() -> set[str]:
    from vllm.engine.arg_utils import EngineArgs

    return {f.name for f in dataclasses.fields(EngineArgs)}


def make_llm(model: str, runtime: RuntimeConfig | None, config_path: str | os.PathLike | None = None, **engine_kwargs: Any):
    """vllm.LLM with Aidos (runtime given) or vanilla (runtime None). engine_kwargs go to vLLM."""
    from vllm import LLM

    kwargs: dict[str, Any] = dict(model=model)
    if runtime is None:
        os.environ.pop(ENV_VAR, None)
    else:
        path = Path(config_path) if config_path else Path(tempfile.mkdtemp(prefix="aidos-")) / "runtime.json"
        runtime.write(path)
        os.environ[ENV_VAR] = str(path.resolve())
        kwargs["scheduler_cls"] = SCHEDULER_CLS
        kwargs["async_scheduling"] = False
        from .plugin import register  # in-process patch too, for fork-started workers / uniproc executor

        register()
    kwargs.update(engine_kwargs)
    known = _engine_arg_names()
    dropped = [k for k in kwargs if k not in known]
    for k in dropped:
        if k == "scheduler_cls":
            raise RuntimeError("this vLLM build has no scheduler_cls engine arg; Aidos cannot run")
        kwargs.pop(k)
    if dropped:
        log.info("engine args not supported by this vLLM, dropped: %s", dropped)
    return LLM(**kwargs)

"""`aidos verify`: token-exactness tests of the engine mechanisms on YOUR GPU and vLLM build.

Each case runs in its own process (clean vLLM + plugin state) and saves its greedy output token
ids; the parent compares them. With greedy decoding the expected outputs are known exactly:

  observe == vanilla                     scoring every token never changes what is generated
  prefill-insert == ref(prompt+evidence) retrieval before the first token equals a fresh request
                                         with the evidence in its prompt
  mid-insert == ref(prompt+2 tokens+ev.) evidence inserted after 2 tokens reuses their KV and
                                         prefills only the evidence
  mid-insert-delayed == mid-insert       same with 300 ms retrieval latency (other requests keep
                                         decoding while one is paused)
  mid-insert-recompute == mid-insert     the recompute path (hybrid / linear-attention models)
  rewind-insert == ref(prompt+evidence)  the deployed mid-answer retrieval takes the unreleased
                                         answer back: result equals evidence at prefill
  retry-insert == ref(prompt+ev.1+ev.2)  a second attempt inserts next-ranked passages after the
                                         first evidence (whose KV is kept)
  forced-rollback completes              rollback every 3 steps

Insertion compares prefix reuse with a full prefill, whose bf16 kernels can flip a near-tie: a
mismatch is accepted only if, at the first divergent position, the engine took the reference's
runner-up and the reference's top-1/top-2 margin is below 1 nat. Observe must match exactly.
This is the same procedure as the paper's engine tests (24 prompts, max_num_seqs 1).

    aidos verify --model Qwen/Qwen2.5-7B-Instruct --bundle bundles/qwen2.5-7b-instruct [--out verify_out]
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import time
from pathlib import Path

N_PROMPTS = 24
MAX_TOKENS = 24
FORCE_AT = 2
NEAR_TIE = 1.0
K = 3
PASSAGE_CHARS = 600
REF_CASES = ("vanilla", "ref-prefill-insert", "ref-mid-insert", "ref-retry-insert")
CASES = ["vanilla", "observe", "ref-prefill-insert", "prefill-insert", "ref-mid-insert", "mid-insert",
         "mid-insert-delayed", "mid-insert-recompute", "rewind-insert", "ref-retry-insert", "retry-insert",
         "forced-rollback"]
QUESTIONS = [
    "Which planet is known as the Red Planet?", "Who wrote the novel Pride and Prejudice?",
    "What is the capital city of Australia?", "In which year did the Berlin Wall fall?",
    "What is the chemical symbol for gold?", "Who painted the Mona Lisa?",
    "Which ocean is the largest on Earth?", "What is the tallest mountain in Africa?",
    "Who was the first person to walk on the Moon?", "Which country hosted the 2016 Summer Olympics?",
    "What is the longest river in South America?", "Who composed the opera The Magic Flute?",
    "Which element has the atomic number 1?", "What is the official language of Brazil?",
    "Who discovered penicillin?", "In which city is the Colosseum located?",
    "What is the largest desert in Asia?", "Who developed the theory of general relativity?",
    "Which gas do plants absorb from the atmosphere?", "What is the currency of Japan?",
    "Who was the first President of the United States?", "Which bird is the national symbol of the USA?",
    "What is the smallest prime number?", "In which country is the city of Marrakesh?",
]


def fake_passages(q: str, i: int) -> list[dict]:
    """Six distinct passages: ranks 1..k for the first insertion, k+1..2k for a retry."""
    return [{"title": f"Reference note {i}", "text": f"This note discusses the question: {q} "
             "Consult an encyclopedia for the definitive answer."},
            {"title": "General knowledge", "text": "Many trivia questions concern history, geography and science."},
            {"title": "Archive", "text": f"Archived discussion number {i} about related topics."},
            {"title": "Second opinion", "text": f"A further source on: {q}"},
            {"title": "Almanac", "text": "Almanacs list dates, places and records."},
            {"title": "Index", "text": f"Index entry {i}: see the main article."}]


def run_case(model: str, bundle: str, out: Path, case: str, engine_kwargs: dict) -> None:
    from transformers import AutoTokenizer
    from vllm import SamplingParams

    from .data.qa import build_prompt_ids, rag_insertion_ids
    from .engine.factory import make_llm, runtime_config
    from .engine.scheduler import QUERY_KEY

    qs = QUESTIONS[:N_PROMPTS]
    tok = AutoTokenizer.from_pretrained(model)
    cache = out / "retrieval.jsonl"
    with open(cache, "w", encoding="utf-8") as f:
        for i, q in enumerate(qs):
            f.write(json.dumps({"query": q, "passages": fake_passages(q, i)}) + "\n")
    prompts = [build_prompt_ids(tok, q) for q in qs]
    ins = [rag_insertion_ids(tok, q, fake_passages(q, i)[:K], PASSAGE_CHARS) for i, q in enumerate(qs)]
    ins2 = [rag_insertion_ids(tok, q, fake_passages(q, i)[K:2 * K], PASSAGE_CHARS) for i, q in enumerate(qs)]
    sps = [SamplingParams(temperature=0.0, max_tokens=MAX_TOKENS, extra_args={QUERY_KEY: q}) for q in qs]
    tele = str(out / f"{case}.telemetry.jsonl")
    base = dict(telemetry_path=tele, retriever=str(cache), retrieve_k=K, passage_chars=PASSAGE_CHARS,
                eu_retrieve_signal="help", eu_option_table=None)
    rt = None
    rc = lambda policy, **kw: runtime_config(bundle, policy=policy, **kw)  # noqa: E731
    if case == "observe":
        rt = rc("observe", telemetry_path=tele, retriever=None)
    elif case == "ref-prefill-insert":
        prompts = [p + x for p, x in zip(prompts, ins)]
    elif case == "prefill-insert":
        rt = rc("retrieve", tau_gap=-1.0, tau_post=float("inf"), **base)
    elif case == "ref-mid-insert":
        v = json.loads((out / "vanilla.json").read_text())["tokens"]
        prompts = [p + t[:FORCE_AT] + x for p, t, x in zip(prompts, v, ins)]
        sps = [SamplingParams(temperature=0.0, max_tokens=MAX_TOKENS - FORCE_AT) for _ in qs]
    elif case.startswith("mid-insert"):
        extra = {"retrieval_delay_ms": 300.0} if case.endswith("delayed") else {}
        if case.endswith("recompute"):
            extra["rollback_mode"] = "recompute"
        rt = rc("retrieve", tau_gap=float("inf"), tau_post=float("inf"), force_retrieve_at=FORCE_AT,
                retrieve_rewind="span", **base, **extra)
    elif case == "rewind-insert":
        rt = rc("retrieve", tau_gap=float("inf"), tau_post=float("inf"), force_retrieve_at=FORCE_AT,
                retrieve_rewind="answer", **base)
    elif case == "ref-retry-insert":
        prompts = [p + x + y for p, x, y in zip(prompts, ins, ins2)]
    elif case == "retry-insert":
        rt = rc("retrieve", tau_gap=-1.0, tau_post=float("inf"), max_retrievals=2, force_retry=True, **base)
    elif case == "forced-rollback":
        rt = rc("rollback", tau_post=float("inf"), force_rollback_every=3, max_rollbacks=100,
                max_bans_per_position=100, telemetry_path=tele, retriever=None)
    elif case != "vanilla":
        raise ValueError(case)
    if case in REF_CASES:
        sps = [sp.clone() for sp in sps]
        for sp in sps:
            sp.logprobs = 2
    llm = make_llm(model, rt, config_path=out / f"runtime_{case}.json", max_num_seqs=1, **engine_kwargs)
    t0 = time.perf_counter()
    outs = llm.generate([{"prompt_token_ids": p} for p in prompts], sps)
    res = {"tokens": [list(o.outputs[0].token_ids) for o in outs], "texts": [o.outputs[0].text for o in outs],
           "wall_s": time.perf_counter() - t0}
    if case in REF_CASES:
        res["top2"] = [[sorted(([int(t), float(lp.logprob)] for t, lp in pos.items()), key=lambda z: -z[1])[:2]
                        for pos in (o.outputs[0].logprobs or [])] for o in outs]
    (out / f"{case}.json").write_text(json.dumps(res))


def match(a, b, top2=None) -> dict:
    exact = sum(x == y for x, y in zip(a, b))
    margins, unexplained = [], []
    for i, (x, y) in enumerate(zip(a, b)):
        if x == y:
            continue
        k = next((j for j, (u, v) in enumerate(zip(x, y)) if u != v), min(len(x), len(y)))
        t2 = top2[i][k] if top2 is not None and i < len(top2) and k < len(top2[i]) else None
        if t2 is not None and len(t2) == 2 and k < len(x):
            m = t2[0][1] - t2[1][1]
            margins.append(round(m, 4))
            if x[k] == t2[1][0] and m < NEAR_TIE:
                continue
        else:
            margins.append(None)
        unexplained.append(i)
    return {"exact": exact, "n": len(a), "near_tie_margins": margins, "unexplained": unexplained}


def compare(out: Path) -> dict:
    r = {c: json.loads((out / f"{c}.json").read_text()) for c in CASES}
    tok = {c: v["tokens"] for c, v in r.items()}
    early = [len(v) <= FORCE_AT for v in tok["vanilla"]]
    exp_mid = [v if e else v[:FORCE_AT] + c for v, c, e in zip(tok["vanilla"], tok["ref-mid-insert"], early)]
    t2_mid = [v if e else v[:FORCE_AT] + c for v, c, e in zip(r["vanilla"]["top2"], r["ref-mid-insert"]["top2"], early)]
    exp_rw = [v if e else p for v, p, e in zip(tok["vanilla"], tok["ref-prefill-insert"], early)]
    t2_rw = [v if e else p for v, p, e in zip(r["vanilla"]["top2"], r["ref-prefill-insert"]["top2"], early)]
    checks = {
        "observe == vanilla": match(tok["observe"], tok["vanilla"]),
        "prefill-insert == reference": match(tok["prefill-insert"], tok["ref-prefill-insert"], r["ref-prefill-insert"]["top2"]),
        "mid-insert == reference": match(tok["mid-insert"], exp_mid, t2_mid),
        "mid-insert-delayed == reference": match(tok["mid-insert-delayed"], exp_mid, t2_mid),
        "mid-insert-recompute == reference": match(tok["mid-insert-recompute"], exp_mid, t2_mid),
        "rewind-insert == prefill reference": match(tok["rewind-insert"], exp_rw, t2_rw),
        "retry-insert == reference": match(tok["retry-insert"], tok["ref-retry-insert"], r["ref-retry-insert"]["top2"]),
    }
    for name, m in checks.items():
        m["pass"] = m["exact"] == m["n"] if name.startswith("observe") else not m["unexplained"]
    rb = r["forced-rollback"]["texts"]
    checks["forced-rollback completes"] = {"pass": len(rb) == N_PROMPTS, "n": len(rb), "exact": len(rb)}
    ok = all(c["pass"] for c in checks.values())
    (out / "result.json").write_text(json.dumps({"pass": ok, "checks": checks}, indent=1))
    return {"pass": ok, "checks": checks}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="aidos verify", description=__doc__.split("\n\n")[0])
    ap.add_argument("--model", required=True)
    ap.add_argument("--bundle", required=True, help="head bundle for this model")
    ap.add_argument("--out", default="aidos_verify")
    ap.add_argument("--tensor-parallel-size", type=int, default=1)
    ap.add_argument("--max-model-len", type=int, default=2048)
    ap.add_argument("--case", help=argparse.SUPPRESS)  # internal: run one case in this process
    a = ap.parse_args(argv)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    ek = {"tensor_parallel_size": a.tensor_parallel_size, "max_model_len": a.max_model_len,
          "enable_prefix_caching": True, "seed": 0}
    if a.case:
        run_case(a.model, a.bundle, out, a.case, ek)
        return 0
    for case in CASES:
        print(f"[aidos verify] case {case}", flush=True)
        cmd = [sys.executable, "-m", "aidos.verify", "--model", a.model, "--bundle", a.bundle, "--out", str(out),
               "--tensor-parallel-size", str(a.tensor_parallel_size), "--max-model-len", str(a.max_model_len),
               "--case", case]
        subprocess.run(cmd, check=True)
    res = compare(out)
    for name, m in res["checks"].items():
        print(f"  {'PASS' if m['pass'] else 'FAIL'}  {name}  ({m.get('exact')}/{m.get('n')} exact)")
    print("aidos verify:", "ALL PASS" if res["pass"] else "FAILURES (see result.json)")
    return 0 if res["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

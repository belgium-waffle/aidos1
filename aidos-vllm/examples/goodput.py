"""Goodput under load: Aidos vs vanilla vLLM on the same questions, same GPU, same engine settings.

    python examples/goodput.py --model Qwen/Qwen2.5-7B-Instruct --bundle bundles/qwen2.5-7b-instruct \
        --retriever /path/to/dpr_bm25 --questions qa.jsonl --out goodput_out [--loads 32 128 256] [--n 2000]

qa.jsonl: one {"question": ..., "answers": [...]} per line. Each (condition, load) runs in a fresh process
(one engine per process; the scheduler class is fixed at engine start). Conditions:
  vanilla        plain vLLM, greedy, closed-book (Aidos plugin disabled: VLLM_PLUGINS="")
  vanilla_sync   as vanilla with synchronous scheduling (Aidos requires it): the like-for-like overhead baseline
  always_rag     plain vLLM; BM25 top-k for every question (timed, part of wall time), then a RAG prompt
  aidos_observe  Aidos scheduler scoring every step but never acting (measures the scoring overhead)
  aidos          Aidos with the bundle's runtime at --lam (route-eu: answer, retrieve in-loop, or abstain)
Per run: wall time, requests/s, output tokens/s, accuracy, abstention, hallucination (wrong and not
abstained), goodput = correct answers per second, safe goodput = (correct + abstained) per second.
Both RAG conditions use the same retriever spec, --workers concurrent retrievals and --delay-ms injected latency
(a query cache .jsonl isolates engine cost from retrieval cost; a BM25 index dir measures live retrieval).
Writes <out>/runs.jsonl (appended; one line per run) and <out>/summary.md.
"""
import argparse
import json
import os
import subprocess
import sys
import time
from pathlib import Path

CONDITIONS = ("vanilla", "vanilla_sync", "always_rag", "aidos_observe", "aidos")


def run_one(a):
    from transformers import AutoTokenizer
    from vllm import SamplingParams

    from aidos.data.qa import build_prompt_ids, build_rag_prompt_ids, is_correct
    from aidos.engine.scheduler import QUERY_KEY

    rows = [json.loads(l) for l in open(a.questions, encoding="utf-8") if l.strip()][: a.n]
    qs = [r["question"] for r in rows]
    if not qs:
        raise SystemExit(f"no questions in {a.questions}")
    tok = AutoTokenizer.from_pretrained(a.model)
    eng = dict(max_model_len=2048, max_num_seqs=a.load, gpu_memory_utilization=0.85, seed=0)
    if a.condition in ("vanilla", "vanilla_sync", "always_rag"):
        from vllm import LLM
        llm = LLM(model=a.model, **eng, **({"async_scheduling": False} if a.condition == "vanilla_sync" else {}))
    else:
        from aidos import make_llm, runtime_config
        over = {"policy": "observe"} if a.condition == "aidos_observe" else {}
        rt = runtime_config(a.bundle, lam=a.lam, retriever=a.retriever, retrieval_delay_ms=a.delay_ms,
                            retrieval_workers=a.workers, **over)
        llm = make_llm(a.model, rt, config_path=Path(a.out) / f"runtime_{a.condition}_{a.load}.json", **eng)
    sp = lambda q: SamplingParams(temperature=0, max_tokens=32, extra_args={QUERY_KEY: q})  # noqa: E731
    # warm-up (compilation, CUDA graphs), not timed
    llm.generate([{"prompt_token_ids": build_prompt_ids(tok, q)} for q in qs[:a.load]], [sp(q) for q in qs[:a.load]],
                 use_tqdm=False)
    t0 = time.perf_counter()
    t_ret = 0.0
    if a.condition == "always_rag":
        from aidos.retrieval import load_retriever
        from concurrent.futures import ThreadPoolExecutor
        ret = load_retriever(a.retriever)

        def fetch(q):  # same retriever, worker count and injected latency as Aidos's in-engine retrieval
            if a.delay_ms:
                time.sleep(a.delay_ms / 1000)
            return ret.search(q, 3)
        tr = time.perf_counter()
        with ThreadPoolExecutor(max_workers=a.workers) as pool:
            hits = list(pool.map(fetch, qs))
        prompts = [{"prompt_token_ids": build_rag_prompt_ids(tok, q, h)} for q, h in zip(qs, hits)]
        t_ret = time.perf_counter() - tr
    else:
        prompts = [{"prompt_token_ids": build_prompt_ids(tok, q)} for q in qs]
    outs = llm.generate(prompts, [sp(q) for q in qs], use_tqdm=False)
    wall = time.perf_counter() - t0
    abst = [o.outputs[0].stop_reason == "aidos_abstain" for o in outs]
    corr = [(not ab) and is_correct(o.outputs[0].text, r["answers"]) for o, r, ab in zip(outs, rows, abst)]
    ntok = sum(len(o.outputs[0].token_ids) for o in outs)
    n = len(qs)
    rec = {"condition": a.condition, "load": a.load, "n": n, "lam": a.lam if a.condition == "aidos" else None,
           "retriever": a.retriever, "delay_ms": a.delay_ms, "workers": a.workers,
           "wall_s": wall, "retrieval_s": t_ret, "req_per_s": n / wall, "out_tok_per_s": ntok / wall,
           "accuracy": sum(corr) / n, "abstain": sum(abst) / n,
           "hallucination": sum((not c) and (not ab) for c, ab in zip(corr, abst)) / n,
           "goodput": sum(corr) / wall, "safe_goodput": (sum(corr) + sum(abst)) / wall,
           "time": time.strftime("%F %T")}
    with open(Path(a.out) / "runs.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(rec) + "\n")
    print(json.dumps(rec), flush=True)


def summarize(out):
    recs = [json.loads(l) for l in open(out / "runs.jsonl", encoding="utf-8")]
    lines = ["| retriever | delay ms | condition | load | req/s | out tok/s | accuracy | abstain | hallucination | goodput (correct/s) | safe goodput |",
             "|---|---|---|---|---|---|---|---|---|---|---|"]
    for r in sorted(recs, key=lambda r: (str(r.get("retriever")), r.get("delay_ms") or 0, r["load"], CONDITIONS.index(r["condition"]))):
        lines.append(f"| {Path(str(r.get('retriever'))).name} | {r.get('delay_ms', 0):g} | {r['condition']} | {r['load']} | {r['req_per_s']:.1f} | {r['out_tok_per_s']:.0f} | {r['accuracy']:.3f} | "
                     f"{r['abstain']:.3f} | {r['hallucination']:.3f} | {r['goodput']:.1f} | {r['safe_goodput']:.1f} |")
    (out / "summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines), flush=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--retriever", required=True)
    ap.add_argument("--questions", required=True)
    ap.add_argument("--out", default="goodput_out")
    ap.add_argument("--lam", type=float, default=1.0)
    ap.add_argument("--n", type=int, default=2000)
    ap.add_argument("--loads", type=int, nargs="+", default=[32, 128, 256])
    ap.add_argument("--delay-ms", type=float, default=0.0, help="latency added to every retrieval (both RAG conditions)")
    ap.add_argument("--workers", type=int, default=8, help="concurrent retrievals (both RAG conditions)")
    ap.add_argument("--conditions", nargs="+", default=[c for c in CONDITIONS if c != "vanilla_sync"])
    ap.add_argument("--condition", help=argparse.SUPPRESS)
    ap.add_argument("--load", type=int, help=argparse.SUPPRESS)
    a = ap.parse_args()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    if a.condition:
        return run_one(a)
    for load in a.loads:
        for c in a.conditions:
            env = dict(os.environ)
            if c in ("vanilla", "vanilla_sync", "always_rag"):
                env["VLLM_PLUGINS"] = ""
            cmd = [sys.executable, __file__, "--model", a.model, "--bundle", a.bundle, "--retriever", a.retriever,
                   "--questions", a.questions, "--out", a.out, "--lam", str(a.lam), "--n", str(a.n),
                   "--delay-ms", str(a.delay_ms), "--workers", str(a.workers),
                   "--condition", c, "--load", str(load)]
            print(f"== {c} load {load} {time.strftime('%F %T')}", flush=True)
            if subprocess.run(cmd, env=env).returncode != 0:
                print(f"!! {c} load {load} FAILED", flush=True)
    summarize(out)


if __name__ == "__main__":
    main()

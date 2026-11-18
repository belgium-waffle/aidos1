"""Record a live-view session: serve a batch with Aidos and snapshot the scheduler's status file.

    python examples/demo_capture.py --model Qwen/Qwen2.5-7B-Instruct --bundle bundles/qwen2.5-7b-instruct \
        --retriever /path/to/dpr_bm25 --questions questions.txt --out demo_out [--delay-ms 300]

Writes demo_out/status_trace.jsonl (one snapshot per 0.2 s, for replaying the live view in a
screencast), demo_out/telemetry.jsonl (per-request decisions) and demo_out/answers.jsonl.
--delay-ms adds latency to every retrieval so pauses are visible (the batch keeps decoding meanwhile).
"""
import argparse
import json
import threading
import time
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--bundle", required=True)
    ap.add_argument("--retriever", required=True)
    ap.add_argument("--questions", required=True, help="one question per line")
    ap.add_argument("--out", default="demo_out")
    ap.add_argument("--lam", type=float, default=1.0)
    ap.add_argument("--delay-ms", type=float, default=300.0)
    ap.add_argument("--max-num-seqs", type=int, default=16)
    a = ap.parse_args()
    from transformers import AutoTokenizer
    from vllm import SamplingParams

    from aidos import make_llm, runtime_config
    from aidos.data.qa import build_prompt_ids
    from aidos.engine.scheduler import QUERY_KEY

    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    status = out / "status.json"
    rt = runtime_config(a.bundle, lam=a.lam, retriever=a.retriever, status_path=str(status.resolve()),
                        status_interval_s=0.1, telemetry_path=str((out / "telemetry.jsonl").resolve()),
                        retrieval_delay_ms=a.delay_ms)
    llm = make_llm(a.model, rt, config_path=out / "runtime.json", max_model_len=2048, max_num_seqs=a.max_num_seqs)
    tok = AutoTokenizer.from_pretrained(a.model)
    qs = [l.strip() for l in open(a.questions, encoding="utf-8") if l.strip()]
    stop = threading.Event()

    def snap():
        last = None
        with open(out / "status_trace.jsonl", "w", encoding="utf-8") as f:
            while not stop.is_set():
                try:
                    s = status.read_text(encoding="utf-8")
                    if s != last:
                        f.write(s.strip() + "\n"); last = s
                except FileNotFoundError:
                    pass
                time.sleep(0.2)

    th = threading.Thread(target=snap, daemon=True); th.start()
    t0 = time.time()
    outs = llm.generate([{"prompt_token_ids": build_prompt_ids(tok, q)} for q in qs],
                        [SamplingParams(temperature=0, max_tokens=32, extra_args={QUERY_KEY: q}) for q in qs])
    wall = time.time() - t0
    time.sleep(0.5); stop.set(); th.join()
    with open(out / "answers.jsonl", "w", encoding="utf-8") as f:
        for q, o in zip(qs, outs):
            c = o.outputs[0]
            f.write(json.dumps({"question": q, "answer": c.text, "abstained": c.stop_reason == "aidos_abstain"}) + "\n")
    n_abs = sum(o.outputs[0].stop_reason == "aidos_abstain" for o in outs)
    print(f"{len(qs)} questions in {wall:.1f}s; abstained {n_abs}; trace -> {out / 'status_trace.jsonl'}")


if __name__ == "__main__":
    main()

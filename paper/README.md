# Paper materials

Figures and the measurements behind them for the Aidos system demonstration paper. Paths that pointed to our
cluster have been replaced by neutral names (`retrieval_cache_qwen2.5-7b.jsonl`, `dpr_bm25_index`,
`Qwen/Qwen2.5-7B-Instruct`).

## Figures

| File | Content | Made from |
|---|---|---|
| `figures/fig1_architecture.svg` | Architecture: worker, fused scoring kernel, side channel, scheduler, retrieval threads, commit horizon | drawn by hand |
| `figures/fig2_live_view.png` | Live view, 8.4 s into a 64-question batch (Qwen2.5-7B, live BM25 over 21M passages, 300 ms added retrieval latency): 6 requests paused for retrieval, 8 decoding, 3 of the just-finished requests abstained | `results/live_view_recording/status_trace.jsonl`, snapshot 24 |
| `figures/fig3_cost_explorer.png` | Cost explorer at λ = 1 (Qwen2.5-7B, in domain) | `aidos lambda` |
| `figures/fig_lamsweep.{pdf,png,svg}` | Accuracy and correct answers per second against hallucination rate, Aidos at λ ∈ {0.1, 0.25, 0.5, 1, 2, 4} vs always-retrieve, full test split | `results/goodput_full_test_split/` |

Re-draw the λ figure: merge `results/goodput_full_test_split/d0` (load 256) and `.../lam` runs into one `runs.jsonl` and run `python paper/scripts/paper2_figs.py lamsweep <dir>`.

Replay the live view at the figure's snapshot (then open http://127.0.0.1:8765):

```bash
python paper/scripts/replay_live.py aidos-vllm/src/aidos/demo paper/results/live_view_recording/status_trace.jsonl 24
```

Omit the last argument to replay the whole recording in a loop.

## Results

| Folder | What | How |
|---|---|---|
| `results/verify_qwen2.5-7b/` | The eight exactness checks, 24 prompts each, Qwen2.5-7B, vLLM 0.21.0, one GPU: all pass | `aidos verify` from this package on a fresh node |
| `results/serve_check/` | `vllm serve` with the README flags: config, server log, an OpenAI-style chat response (HTTP 200) and the status snapshot | `aidos config` + `vllm serve` + one `curl` request |
| `results/live_view_recording/` | 37 status snapshots of a 64-question batch, the answers, and the runtime config | `examples/demo_capture.py` |
| `results/goodput_full_test_split/` | Throughput and answer quality on the full test split (3,176 questions): `d0` at 32 / 128 / 256 concurrent requests (closed-book vLLM, always-retrieve, Aidos scoring-only, Aidos λ = 1); `lam` (λ = 0.1–4 at 256); `d50` (+50 ms per search); `live` (live BM25 over 21M passages); tables in the paper | `examples/goodput.py` |
| `results/goodput_subset2000/` | Earlier runs on a 2,000-question subset (80% TriviaQA), incl. the overhead runs against vLLM with the same synchronous scheduling | `examples/goodput.py` |
| `results/answer_quality/` | Utility against the five adaptive-retrieval pipelines on the test split (`audit_all_models.md`) and the sealed set (`sealed/`), with paired bootstrap intervals and Holm-corrected p-values | research pipeline |

**Throughput numbers in the paper** come from the full test split (`goodput_full_test_split`). The earlier subset was
80% TriviaQA (closed-book accuracy 0.479 vs 0.366 on the full split) and is kept only for the overhead comparison.

Each `runs.jsonl` line is one run: condition, concurrency (`load`), λ, retriever, added latency, wall time,
requests and output tokens per second, accuracy, abstention and hallucination rates, and correct answers per
second (`goodput`).

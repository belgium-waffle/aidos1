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
| `figures/fig_lamsweep.{pdf,png,svg}` | Accuracy and correct answers per second against hallucination rate, Aidos at λ ∈ {0.25, 0.5, 1, 2, 4} vs always-retrieve | `results/goodput/lambda_sweep/runs.jsonl` |

Re-draw the λ figure: `python paper/scripts/paper2_figs.py lamsweep paper/results/goodput/lambda_sweep`.

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
| `results/goodput/cache_d0/`, `cache_d50/`, `live/` | Throughput and answer quality at 32 / 128 / 256 concurrent requests: closed-book vLLM, always-retrieve, Aidos scoring-only, Aidos λ = 1; cached retrieval with 0 ms or +50 ms per search, and live BM25 over 21M passages | `examples/goodput.py` |
| `results/goodput/overhead_sync_baseline/` | Scoring overhead against vLLM with the same synchronous scheduling, 2 repetitions | `examples/goodput.py --conditions vanilla vanilla_sync aidos_observe` |
| `results/goodput/lambda_sweep/` | Aidos at λ ∈ {0.25, 0.5, 1, 2, 4} plus references, 256 concurrent requests | `examples/goodput.py --lam ...` |
| `results/goodput/table_*.md` | The tables in the paper | `paper/scripts/paper2_figs.py` |
| `results/answer_quality/` | Utility against the five adaptive-retrieval pipelines on the test split (`audit_all_models.md`) and the sealed set (`sealed/`), with paired bootstrap intervals and Holm-corrected p-values | research pipeline |

**Note on the throughput subset.** The throughput runs used the first 2,000 questions of the test split, which
are 80% TriviaQA (the full split is 50/50 TriviaQA / PopQA), so absolute accuracies are higher than on the full
split (closed-book 0.479 against 0.366). Comparisons between systems use the same questions and are unaffected in
kind; runs on the full split will replace these.

Each `runs.jsonl` line is one run: condition, concurrency (`load`), λ, retriever, added latency, wall time,
requests and output tokens per second, accuracy, abstention and hallucination rates, and correct answers per
second (`goodput`).

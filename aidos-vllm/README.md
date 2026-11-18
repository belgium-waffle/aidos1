# Aidos: answer, retrieve or abstain from inside vLLM

Aidos is a plugin for **vLLM V1** that decides, inside the decode loop, whether a request should
answer, fetch evidence, or abstain. It reads small linear probes from the model's hidden states at
every step (one fused kernel, no extra synchronisation) and acts on them in the scheduler:

- **Pause and insert:** a request that needs evidence is paused with its KV cache intact while the
  rest of the batch keeps decoding; the evidence is appended as tokens and only those are prefilled.
- **Rollback:** the KV cache can be rewound mid-answer; a commit horizon means text already sent to
  the client is never retracted.
- **Abstain:** a single cost parameter λ (how much a wrong answer costs relative to a right one)
  sets how much the model answers.
- **Exact:** insertion and rollback produce the same tokens as recomputing from scratch
  (`aidos verify` checks this on your GPU and vLLM build).

It is a plugin, not a fork: it does nothing unless `AIDOS_CONFIG` is set, and every touch-point with
vLLM internals lives in one module (`aidos/engine/compat.py`) checked by contract tests.

## Install

```bash
git clone https://github.com/belgium-waffle/aidos1
cd aidos1/aidos-vllm
pip install -e ".[bm25]"              # pins vllm 0.21.*; [bm25] adds BM25 over your own corpus
aidos info                            # versions, and whether vLLM sees the plugin
python examples/quickstart.py         # three example questions on a two-document corpus
```

The released head bundles live in `bundles/` in the clone, and the examples refer to them by that path. To install
the plugin alone (for example with your own bundles):
`pip install "aidos-vllm[bm25] @ git+https://github.com/belgium-waffle/aidos1#subdirectory=aidos-vllm"`.
Not yet on PyPI.

## Quickstart

Released head bundles (heads plus calibrated thresholds) are in `bundles/`:

| Bundle | Model |
|---|---|
| `qwen2.5-7b-instruct` | Qwen/Qwen2.5-7B-Instruct |
| `llama-3.1-8b-instruct` | meta-llama/Llama-3.1-8B-Instruct |
| `mistral-7b-instruct-v0.3` | mistralai/Mistral-7B-Instruct-v0.3 |
| `qwen2.5-32b-instruct` | Qwen/Qwen2.5-32B-Instruct |
| `llama-3.3-70b-instruct` | meta-llama/Llama-3.3-70B-Instruct (tensor parallel 2) |
| `qwen3-8b` | Qwen/Qwen3-8B (thinking off) |

Each bundle is calibrated for λ ∈ {0.1, 0.25, 0.5, 1, 2, 4}.

```python
from aidos import make_llm, runtime_config
from aidos.data.qa import build_prompt_ids
from aidos.engine.scheduler import QUERY_KEY
from transformers import AutoTokenizer
from vllm import SamplingParams

rt = runtime_config("bundles/qwen2.5-7b-instruct", lam=1.0, retriever="my_corpus.jsonl")
llm = make_llm("Qwen/Qwen2.5-7B-Instruct", rt, max_model_len=2048)
tok = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B-Instruct")
q = "In which town was Zorvath Labs founded?"
out = llm.generate([{"prompt_token_ids": build_prompt_ids(tok, q)}],
                   [SamplingParams(temperature=0, max_tokens=32, extra_args={QUERY_KEY: q})])
print(out[0].outputs[0].text, out[0].outputs[0].stop_reason)   # stop_reason "aidos_abstain" = abstained
```

Full example: `examples/quickstart.py`.

### Serving (OpenAI-compatible)

```bash
aidos config bundles/qwen2.5-7b-instruct --lam 1 --retriever my_corpus.jsonl --status aidos_status.json -o aidos.json
AIDOS_CONFIG=$PWD/aidos.json vllm serve Qwen/Qwen2.5-7B-Instruct \
    --scheduler-cls aidos.engine.scheduler.AidosScheduler --no-async-scheduling
```

Without a query key the retriever is queried with the decoded prompt; pass the user question
through `extra_args` (`aidos_query`) for cleaner retrieval.

## Retrievers

`retriever=` accepts:

| Spec | Meaning |
|---|---|
| `corpus.jsonl` with `{"title", "text"}` lines | BM25 built in memory (needs `[bm25]`) |
| `cache.jsonl` with `{"query", "passages"}` lines | precomputed results |
| a directory | a prebuilt BM25 index (e.g. the 21M-passage DPR Wikipedia split used in the paper) |
| `python:my_module:factory` | your own: `factory()` returns an object with `search(query, k) -> [{"title", "text"}]` |

Retrieval runs in worker threads; the paused request keeps its batch slot and KV blocks.

## Demo tools

```bash
aidos live --status aidos_status.json   # live view: request states, retrievals, per-token risk
aidos lambda                            # cost explorer: move λ, watch coverage and errors move
aidos verify --model Qwen/Qwen2.5-7B-Instruct --bundle bundles/qwen2.5-7b-instruct
```

- **Live view** reads the snapshot the scheduler writes when `status_path` is set (rate-limited,
  atomic; off by default).
- **Cost explorer** shows measured results from the paper's runs: Aidos re-plans how much it answers
  as λ changes, while a reasoning model told the same λ stays at the same point.
- **`aidos verify`** runs the paper's eight engine checks (observe = vanilla, insertion at prefill,
  mid-answer, with 300 ms retrieval latency, on the recompute path, rewind, second attempt, forced
  rollback) on 24 prompts and reports pass / fail. A mismatch is accepted only at a bf16 near-tie
  (the reference's runner-up token, margin below 1 nat).

## Requirements and limits

- vLLM V1, 0.21.x. Synchronous scheduling is required (`--no-async-scheduling`); no speculative
  decoding or pipeline parallelism. Tensor parallelism works.
- Requests that ask for logprobs or structured output are left untouched.
- Overhead: per decode step about 2–3% at 32–70B and 9–10% at 7–8B; end to end at 7B, 2–3% fewer requests per
  second than vLLM with the same synchronous scheduling, plus about 5% from giving up vLLM's asynchronous scheduling.
- The heads are trained per model on short-answer QA (TriviaQA, PopQA); the hallucination-budget
  guarantee assumes your questions resemble the calibration data and does not hold under
  distribution shift.
- Run `pytest tests/test_vllm_contract.py` and `aidos verify` after any vLLM upgrade.

## Citation

Paper under review; citation to follow.

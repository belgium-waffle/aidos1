"""Answer, retrieve or abstain inside vLLM, on your own documents.

    pip install -e ".[bm25]"        # from aidos-vllm/ in a clone of the repository
    python examples/quickstart.py   # run from aidos-vllm/ so bundles/ resolves
"""
import json
from pathlib import Path

from transformers import AutoTokenizer
from vllm import SamplingParams

from aidos import make_llm, runtime_config
from aidos.data.qa import build_prompt_ids
from aidos.engine.scheduler import QUERY_KEY

MODEL = "Qwen/Qwen2.5-7B-Instruct"
BUNDLE = "bundles/qwen2.5-7b-instruct"

# 1. your corpus: one {"title", "text"} per line (BM25 is built in memory)
corpus = Path("my_corpus.jsonl")
corpus.write_text("".join(json.dumps(d) + "\n" for d in [
    {"title": "Aidos", "text": "Aidos is a vLLM plugin that decides inside the decode loop whether to answer, "
                               "retrieve evidence or abstain."},
    {"title": "Zorvath Labs", "text": "Zorvath Labs was founded in 2019 in the town of Meldrick."},
]))

# 2. runtime: the bundle's calibration for lambda = 1 (a wrong answer costs as much as a right one earns)
rt = runtime_config(BUNDLE, lam=1.0, retriever=str(corpus), status_path="aidos_status.json",
                    telemetry_path="aidos_telemetry.jsonl")
llm = make_llm(MODEL, rt, max_model_len=2048)

tok = AutoTokenizer.from_pretrained(MODEL)
questions = ["What is the capital of France?", "In which town was Zorvath Labs founded?",
             "Who won the 1987 Tour de Meldrick?"]
outs = llm.generate([{"prompt_token_ids": build_prompt_ids(tok, q)} for q in questions],
                    [SamplingParams(temperature=0, max_tokens=32, extra_args={QUERY_KEY: q}) for q in questions])
for q, o in zip(questions, outs):
    c = o.outputs[0]
    print(f"{q}\n  -> {'[abstained]' if c.stop_reason == 'aidos_abstain' else c.text!r}")
# per-request decisions (retrievals, rollbacks, scores): aidos_telemetry.jsonl
# live view while serving: aidos live --status aidos_status.json

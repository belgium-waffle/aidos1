"""Aidos: answer, retrieve or abstain from inside the vLLM decode loop.

    from aidos import make_llm, runtime_config
    rt = runtime_config("heads/qwen2.5-7b", lam=1.0, retriever="my_corpus.jsonl")
    llm = make_llm("Qwen/Qwen2.5-7B-Instruct", rt)
"""

__version__ = "0.1.0"

from .engine.factory import make_llm, runtime_config  # noqa: E402,F401

"""Retrieval backends used by the retrieve* / route policies and the offline RAG runs.

Every backend has the same interface:

    search(query: str, k: int) -> list[dict(title, text, score)]

  * BM25Retriever   - live BM25 over the DPR Wikipedia split (21M passages); what the
                      engine uses to measure real retrieval latency
  * CachedRetriever - precomputed results (retrieval.jsonl, written by the research pipeline,
                      the top STORE_K=10 per query: enough for a second attempt at k<=5);
                      makes engine runs and offline RAG runs see IDENTICAL passages, and
                      lets small integration tests run without the 21M-passage index

load_retriever(spec): spec is an index directory, a .jsonl cache, or "cache.jsonl|index_dir"
(cache first, live BM25 on a miss).
"""

from __future__ import annotations

from pathlib import Path


class CachedRetriever:
    def __init__(self, path: str | Path, fallback=None):
        import json

        self.table: dict[str, list[dict]] = {}
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    self.table[r["query"]] = r["passages"]
        self.fallback = fallback
        self.misses = 0

    def search(self, query: str, k: int) -> list[dict]:
        hit = self.table.get(query)
        if hit is not None:
            return hit[:k]
        self.misses += 1
        return self.fallback.search(query, k) if self.fallback is not None else []


def _is_query_cache(path: str) -> bool:
    import json

    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                return "query" in json.loads(line)
    return True


def load_retriever(spec: str):
    """spec: BM25 index dir | query cache .jsonl ({"query", "passages"}) | corpus .jsonl
    ({"title", "text"}: in-memory BM25) | "cache.jsonl|index_dir" | "python:module:factory"
    (factory() returns an object with search(query, k) -> [{"title", "text", ...}])."""
    if spec.startswith("python:"):
        import importlib

        mod, _, attr = spec[len("python:"):].partition(":")
        return getattr(importlib.import_module(mod), attr or "make_retriever")()
    if spec.endswith(".jsonl") and "|" not in spec and not _is_query_cache(spec):
        from .memory import MemoryBM25

        return MemoryBM25(spec)
    if "|" in spec:
        cache, index = spec.split("|", 1)
        from .bm25 import BM25Retriever

        return CachedRetriever(cache, fallback=_batched(BM25Retriever(index)))
    if spec.endswith(".jsonl"):
        return CachedRetriever(spec)
    from .bm25 import BM25Retriever

    return _batched(BM25Retriever(spec))


def _batched(r):
    """Concurrent engine searches -> one multi-threaded search_many (identical results)."""
    from .batching import BatchingRetriever

    return BatchingRetriever(r)

"""In-memory BM25 over a small corpus (a .jsonl file with one {"title", "text"} object per line).

For your own documents (up to a few million short passages). Same tokenizer as the Wikipedia
index (English stopwords + Snowball stemmer). Needs `bm25s` and `PyStemmer`.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..utils import get_logger
from .bm25 import _tokenizer

log = get_logger("aidos.retrieval")


class MemoryBM25:
    def __init__(self, path: str | Path):
        import bm25s

        self.docs = []
        with open(path, encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    r = json.loads(line)
                    self.docs.append({"title": str(r.get("title", "")), "text": str(r["text"])})
        if not self.docs:
            raise ValueError(f"{path}: empty corpus")
        self.tok = _tokenizer()
        ids = self.tok.tokenize([f"{d['title']} {d['text']}" for d in self.docs], return_as="ids", show_progress=False)
        self.index = bm25s.BM25()
        self.index.index(bm25s.tokenization.Tokenized(ids=ids, vocab=self.tok.get_vocab_dict()), show_progress=False)
        log.info("in-memory BM25: %d passages from %s", len(self.docs), path)

    def search(self, query: str, k: int) -> list[dict]:
        k = min(k, len(self.docs))
        if k <= 0:
            return []
        q = self.tok.tokenize([query], return_as="ids", update_vocab=False, show_progress=False)
        res, scores = self.index.retrieve(q, k=k, show_progress=False)
        return [{**self.docs[int(i)], "score": float(s)} for i, s in zip(res[0], scores[0]) if float(s) > 0]

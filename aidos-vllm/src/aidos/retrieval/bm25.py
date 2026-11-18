"""BM25 over the DPR Wikipedia split (Dec 2018 dump, 21M passages of 100 words).

This is the corpus and the sparse retriever used by the PopQA / TriviaQA / NQ
retrieval-augmentation literature, so retrieval quality is comparable to prior work.

Index layout (<index_dir>/):
    bm25s index files (CSC matrix, memory-mapped at load)
    vocab.tokenizer.json, stopwords.tokenizer.json   query tokenizer (same stemming as the index)
    passages.txt + offsets.npy                       "title\\ttext\\n" per passage, O(1) lookup by row

Build once on a CPU node (about 1 h, ~150 GB RAM for 21M passages):
    the research pipeline's build-index stage
"""

from __future__ import annotations

import gzip
import threading
from array import array
from pathlib import Path

import numpy as np

from ..utils import get_logger

log = get_logger("aidos.retrieval")


def _tokenizer():
    import Stemmer
    from bm25s.tokenization import Tokenizer

    return Tokenizer(stopwords="en", stemmer=Stemmer.Stemmer("english"))


def iter_dpr_tsv(path: str | Path, limit: int | None = None):
    """Yields (title, text) from psgs_w100.tsv[.gz] (columns: id, text, title)."""
    opener = gzip.open if str(path).endswith(".gz") else open
    with opener(path, "rt", encoding="utf-8") as f:
        header = f.readline()
        if not header.startswith("id"):
            raise ValueError(f"unexpected header in {path}: {header[:80]!r}")
        for i, line in enumerate(f):
            if limit is not None and i >= limit:
                break
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            text = parts[1].strip('"').replace('""', '"')
            title = parts[2].strip('"').replace('""', '"')
            yield title, text


def build_index(corpus: str | Path, out_dir: str | Path, chunk: int = 500_000, limit: int | None = None) -> int:
    import bm25s
    from bm25s.tokenization import Tokenized

    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    tok = _tokenizer()
    ids: list[list[int]] = []
    offsets = array("q")
    batch: list[str] = []
    n = 0
    with open(out / "passages.txt", "wb") as pf:
        for title, text in iter_dpr_tsv(corpus, limit):
            offsets.append(pf.tell())
            pf.write(f"{title}\t{text}\n".encode("utf-8"))
            batch.append(f"{title} {text}")  # index title + text, as in the DPR BM25 baseline
            if len(batch) >= chunk:
                ids.extend(tok.tokenize(batch, update_vocab=True, show_progress=False, return_as="ids"))
                n += len(batch)
                batch = []
                log.info("tokenized %d passages", n)
        if batch:
            ids.extend(tok.tokenize(batch, update_vocab=True, show_progress=False, return_as="ids"))
            n += len(batch)
        offsets.append(pf.tell())  # end sentinel
    np.save(out / "offsets.npy", np.frombuffer(offsets, dtype=np.int64))
    log.info("indexing %d passages (vocab %d)", n, len(tok.get_vocab_dict()))
    retriever = bm25s.BM25()
    retriever.index(Tokenized(ids=ids, vocab=tok.get_vocab_dict()), show_progress=False)
    del ids
    retriever.save(out, show_progress=False)
    tok.save_vocab(str(out))
    tok.save_stopwords(str(out))
    log.info("BM25 index written to %s", out)
    return n


class BM25Retriever:
    """Everything lives in RAM: on Lustre, memory-mapped posting lists and per-passage
    file reads turn every query into network round trips (the dev run managed ~1.7
    queries/s mmapped, ~7/s with the matrix in RAM but passages read one by one).
      mmap=False            the ~1 GB posting matrix is loaded into RAM
      passages_in_ram=True  passages.txt (~7 GB) is read once, sequentially; a passage is
                            then a slice (deep candidate lists need 50 passages per query)
    n_threads parallelizes batch search (search_many); the numba backend is used when
    installed."""

    def __init__(self, index_dir: str | Path, mmap: bool = False, n_threads: int | None = None,
                 passages_in_ram: bool = True):
        import os

        import bm25s

        d = Path(index_dir)
        self.dir = d
        self.n_threads = n_threads or max(1, len(os.sched_getaffinity(0)) if hasattr(os, "sched_getaffinity") else 1)
        self.bm25 = bm25s.BM25.load(d, mmap=mmap, show_progress=False)
        self.tok = _tokenizer()
        self.tok.load_vocab(str(d))
        self.tok.load_stopwords(str(d))
        self.offsets = np.load(d / "offsets.npy", mmap_mode=None if passages_in_ram else "r")
        self._blob: bytes | None = None
        self._pf = None
        if passages_in_ram:
            with open(d / "passages.txt", "rb") as f:
                self._blob = f.read()
        else:
            self._pf = open(d / "passages.txt", "rb")
        self._lock = threading.Lock()  # around bm25s.retrieve
        self._plock = threading.Lock()  # around the shared passages file handle
        try:
            import numba  # noqa: F401

            self.backend = "numba"
        except ImportError:
            self.backend = "auto"
        log.info("BM25 index loaded from %s (%d passages, passages %s, backend %s, %d threads)", d,
                 len(self.offsets) - 1, "in RAM" if passages_in_ram else "on disk", self.backend, self.n_threads)

    def passage(self, i: int) -> dict:
        a, b = int(self.offsets[i]), int(self.offsets[i + 1])
        if self._blob is not None:
            raw = self._blob[a:b]
        else:
            with self._plock:
                self._pf.seek(a)
                raw = self._pf.read(b - a)
        title, _, text = raw.decode("utf-8").rstrip("\n").partition("\t")
        return {"id": int(i), "title": title, "text": text}

    def search_many(self, queries: list[str], k: int) -> list[list[dict]]:
        toks = self.tok.tokenize(queries, update_vocab=False, show_progress=False, return_as="string")
        toks = [t if t else ["the"] for t in toks]  # empty query -> no-op token
        # bm25s is not documented as thread-safe across callers; one batch at a time, each
        # batch multi-threaded internally (single in-engine queries stay single-threaded)
        with self._lock:
            kw = dict(k=k, show_progress=False, n_threads=self.n_threads if len(toks) > 1 else 1)
            try:
                docs, scores = self.bm25.retrieve(toks, backend_selection=self.backend, **kw)
            except (TypeError, ValueError, ImportError):  # older bm25s / numba backend unusable
                self.backend = "auto"
                docs, scores = self.bm25.retrieve(toks, **kw)
        out = []
        for row_d, row_s in zip(docs, scores):
            out.append([{**self.passage(int(i)), "score": float(s)} for i, s in zip(row_d, row_s)])
        return out

    def search(self, query: str, k: int) -> list[dict]:
        return self.search_many([query], k)[0]

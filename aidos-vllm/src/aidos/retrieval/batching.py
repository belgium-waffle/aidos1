"""Coalesce concurrent single-query searches into one batched call.

The engine retrieves from a thread pool, one query per paused request. A backend that has
search_many (BM25Retriever) serializes single searches behind its lock, each single-threaded,
so k simultaneous pauses cost k sequential searches (~1 s each over 21M passages). This wrapper
queues queries; one worker thread takes everything pending (waiting at most `window_ms` for
more, up to `max_batch`), runs search_many per k (multi-threaded), and hands each caller its
own result. Results are identical to search(); only the scheduling of the work changes.
"""
from __future__ import annotations

import queue
import threading
import time
from concurrent.futures import Future


class BatchingRetriever:
    def __init__(self, base, window_ms: float = 2.0, max_batch: int = 64):
        self.base, self.window, self.max_batch = base, window_ms / 1000, max_batch
        self.q: queue.Queue = queue.Queue()
        self.batches = self.queries = 0
        threading.Thread(target=self._loop, daemon=True, name="aidos-retrieve-batch").start()

    def search(self, query: str, k: int) -> list[dict]:
        f: Future = Future()
        self.q.put((query, k, f))
        return f.result()

    def search_many(self, queries: list[str], k: int) -> list[list[dict]]:
        return self.base.search_many(queries, k)

    def __getattr__(self, name):  # passage(), dir, ... of the wrapped backend
        return getattr(self.base, name)

    def _loop(self):
        while True:
            items = [self.q.get()]
            end = time.monotonic() + self.window
            while len(items) < self.max_batch:
                try:
                    items.append(self.q.get(timeout=max(0.0, end - time.monotonic())))
                except queue.Empty:
                    break
            byk: dict[int, list] = {}
            for it in items:
                byk.setdefault(it[1], []).append(it)
            for k, its in byk.items():
                try:
                    res = self.base.search_many([q for q, _, _ in its], k)
                    for (_, _, f), r in zip(its, res):
                        f.set_result(r)
                except BaseException as e:  # noqa: BLE001 - deliver the error to every caller
                    for _, _, f in its:
                        if not f.done():
                            f.set_exception(e)
            self.batches += 1
            self.queries += len(items)

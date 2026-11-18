"""Small shared helpers: logging, JSONL I/O, hashing, seeding."""

from __future__ import annotations

import hashlib
import json
import logging
import os
import random
import time
from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterable, Iterator


def get_logger(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logging.getLogger().handlers and not logger.handlers:
        logging.basicConfig(
            level=os.environ.get("AIDOS_LOGLEVEL", "INFO"),
            format="%(asctime)s %(levelname)s %(name)s: %(message)s",
            datefmt="%H:%M:%S",
        )
    return logger


_LABELS: dict | None = None


def _label_map() -> dict:
    """TW_LABELS=<labels.jsonl> (stage `relabel`): (qid, normalized answer) -> validated label."""
    global _LABELS
    if _LABELS is None:
        _LABELS = {}
        p = os.environ.get("TW_LABELS")
        if p:
            with open(p, encoding="utf-8") as f:
                for line in f:
                    r = json.loads(line)
                    _LABELS[r["qid"], r["norm"]] = bool(r["label"])
    return _LABELS


def _relabel(rec: dict, M: dict) -> dict:
    """Replace the alias label of every answer in the record that has a validated label."""
    q = rec.get("qid") if isinstance(rec, dict) else None
    if q is None:
        return rec
    from .data.qa import normalize_answer

    stack = [rec]
    while stack:
        d = stack.pop()
        if d.get("correct") is not None and not d.get("abstained"):
            t = d.get("answer") if isinstance(d.get("answer"), str) else d.get("text")
            if isinstance(t, str):
                v = M.get((q, normalize_answer(t)))
                if v is not None:
                    d["correct"] = v
        for x in d.values():
            if isinstance(x, dict):
                stack.append(x)
            elif isinstance(x, list) and x and isinstance(x[0], dict):
                stack.extend(y for y in x if isinstance(y, dict))
    return rec


def read_jsonl(path: str | os.PathLike) -> list[dict[str, Any]]:
    M = _label_map()
    with open(path, encoding="utf-8") as f:
        rows = [json.loads(line) for line in f if line.strip()]
    return [_relabel(r, M) for r in rows] if M else rows


def iter_jsonl(path: str | os.PathLike) -> Iterator[dict[str, Any]]:
    M = _label_map()
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.strip():
                r = json.loads(line)
                yield _relabel(r, M) if M else r


def write_jsonl(path: str | os.PathLike, rows: Iterable[dict[str, Any]]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def append_jsonl(path: str | os.PathLike, row: dict[str, Any]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def append_jsonl_many(path: str | os.PathLike, rows: list[dict[str, Any]]) -> None:
    """Append several rows with one open() and one write()."""
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))


def write_json(path: str | os.PathLike, obj: Any) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def read_json(path: str | os.PathLike) -> Any:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def fresh_dir(path: str | os.PathLike) -> Path:
    """An empty output directory at `path`. Results are never overwritten: an existing
    non-empty directory is renamed to <path>.prev-<YYYYmmdd-HHMMSS> first (kept, not deleted)."""
    p = Path(path)
    if p.exists() and any(p.iterdir()):
        p.rename(p.with_name(f"{p.name}.prev-{time.strftime('%Y%m%d-%H%M%S')}"))
    p.mkdir(parents=True, exist_ok=True)
    return p


def stable_hash(s: str) -> int:
    """Process-independent 48-bit hash (Python's hash() is salted per process)."""
    return int(hashlib.sha1(s.encode("utf-8")).hexdigest()[:12], 16)


def prompt_hash(token_ids: Iterable[int]) -> str:
    """Identifies a request by its prompt tokens. Used to join engine telemetry
    (keyed by internal request ids) with frontend outputs."""
    return hashlib.sha1(",".join(map(str, token_ids)).encode()).hexdigest()[:16]


def seed_everything(seed: int) -> None:
    random.seed(seed)
    try:
        import numpy as np

        np.random.seed(seed)
    except ImportError:
        pass
    try:
        import torch

        torch.manual_seed(seed)
    except ImportError:
        pass


@contextmanager
def timer() -> Iterator[dict[str, float]]:
    out: dict[str, float] = {}
    t0 = time.perf_counter()
    try:
        yield out
    finally:
        out["seconds"] = time.perf_counter() - t0

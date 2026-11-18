"""Side channel between the scheduler (engine core) and the GPU workers.

Instead of adding a new IPC path, Aidos attaches one small dict to the objects that
already cross the process boundary every step:

    scheduler -> worker : SchedulerOutput     ._aidos = {"truncate": {req: n_tokens}, "bans": {req: [tok]}}
    worker -> scheduler : ModelRunnerOutput   ._aidos = {"risks": {req: (post, pre)}}

Both are plain dataclasses, so the attribute survives pickling in the multiprocess
executor (TP > 1) and is free in the single-process executor (TP = 1). If an object ever
rejects attributes (e.g. slots), we fall back to a process-local table, which is still
correct for the uniprocess executor.
"""

from __future__ import annotations

from typing import Any

KEY = "_aidos"
_LOCAL: dict[int, Any] = {}


def attach(obj: Any, payload: dict) -> None:
    try:
        setattr(obj, KEY, payload)
    except (AttributeError, TypeError):
        _LOCAL[id(obj)] = payload


def take(obj: Any) -> dict | None:
    if obj is None:
        return None
    payload = getattr(obj, KEY, None)
    if payload is None:
        payload = _LOCAL.pop(id(obj), None)
    return payload

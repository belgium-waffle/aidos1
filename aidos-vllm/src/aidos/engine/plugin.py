"""vLLM general-plugin entry point (registered in pyproject.toml).

vLLM calls every `vllm.general_plugins` entry point in every process it starts
(frontend, engine core, workers). We patch the worker's GPUModelRunner there. The
scheduler half is selected explicitly via scheduler_cls, so it needs no patching.
Dormant unless AIDOS_CONFIG is set: installing the package never changes vanilla vLLM.
"""

from __future__ import annotations

from ..utils import get_logger
from .config import load_runtime_config

log = get_logger("aidos.plugin")


def register() -> None:
    if load_runtime_config() is None:
        return
    try:
        from vllm.v1.worker.gpu_model_runner import GPUModelRunner
    except ImportError as e:  # pragma: no cover - depends on vLLM build
        log.error("aidos: cannot import vLLM V1 GPUModelRunner (%s); plugin inactive", e)
        return
    from .runner import patch_runner_class

    patch_runner_class(GPUModelRunner)

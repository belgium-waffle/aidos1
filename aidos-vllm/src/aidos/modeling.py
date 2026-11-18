"""Locate the text decoder inside plain CausalLMs and multimodal wrappers.

Plain CausalLMs (Qwen2.5) keep decoder layers at `model.model.layers`; multimodal
wrappers (Qwen3-VL style) nest them under a language model. The same lookup is used
for HF models (feature extraction, parity) and vLLM models (hook fallback).
"""

from __future__ import annotations

from typing import Any

_DECODER_PATHS = (
    "model.language_model",   # HF Qwen3-VL / Qwen3.5 multimodal
    "language_model.model",   # vLLM multimodal wrappers
    "model.text_model",
    "language_model",
    "model",                  # plain *ForCausalLM (HF and vLLM)
)


def find_text_decoder(model: Any) -> Any:
    """Return the module that owns `.layers` (the text decoder stack)."""
    for path in _DECODER_PATHS:
        obj = model
        for part in path.split("."):
            obj = getattr(obj, part, None)
            if obj is None:
                break
        if obj is not None and hasattr(obj, "layers"):
            return obj
    if hasattr(model, "layers"):
        return model
    raise AttributeError(f"cannot find decoder layers in {type(model).__name__}")


def load_hf_lm(name: str, **kwargs: Any) -> Any:
    """AutoModelForCausalLM, falling back to the image-text-to-text auto class for
    multimodal checkpoints. Only the text path is ever run."""
    from transformers import AutoConfig, AutoModelForCausalLM
    from transformers.models.auto.modeling_auto import MODEL_FOR_CAUSAL_LM_MAPPING

    # choose the auto class from the config, so a real load error is never masked by
    # a confusing "unrecognized configuration" error from the fallback class
    if type(AutoConfig.from_pretrained(name)) in MODEL_FOR_CAUSAL_LM_MAPPING:
        return AutoModelForCausalLM.from_pretrained(name, **kwargs)
    from transformers import AutoModelForImageTextToText

    return AutoModelForImageTextToText.from_pretrained(name, **kwargs)


def text_hidden_size(config: Any) -> int:
    tc = config.get_text_config() if hasattr(config, "get_text_config") else config
    return int(tc.hidden_size)

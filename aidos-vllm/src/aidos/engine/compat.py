"""Every assumption Aidos makes about vLLM V1 internals lives here.

vLLM's internals change between releases. Keeping all touch-points in one file means a
version bump is a review of this file plus `pytest tests/test_vllm_contract.py`, which
asserts each assumption below against the installed vLLM.

Assumptions (vLLM V1, sync scheduling, no spec decode, PP = 1):
  worker  : GPUModelRunner.{load_model, execute_model[, sample_tokens]}, .model,
            .input_batch.{num_reqs, req_ids, req_id_to_index, num_tokens[_no_spec]},
            .requests[req_id].output_token_ids, .query_start_loc(.gpu), .positions(.gpu)
  model   : set_aux_hidden_state_layers(layers) (EAGLE-3 support) -> forward returns
            (hidden, [aux...]); otherwise decoder layers at .model.layers (hook fallback)
  sched   : Scheduler.{schedule, update_from_output, add_request, finish_requests},
            .requests, .kv_cache_manager, .block_size
  request : ._output_token_ids, ._all_token_ids, .num_computed_tokens, .block_hashes,
            .num_tokens, .num_prompt_tokens, .num_output_tokens,
            .sampling_params.eos_token_id (0.21; older vLLM: request.eos_token_id)
  verified against vLLM 0.21.0 (2026-10-05): all of the above; Qwen2 aux index k =
            hidden+residual entering layer k (== HF hidden_states[k])
  kv      : kv_cache_manager.{enable_caching, block_pool._maybe_evict_cached_block,
            coordinator.single_type_managers[*].{block_size, req_to_blocks, num_cached_block}}
  hybrid  : scheduler.kv_cache_config.kv_cache_groups[*].kv_cache_spec (MambaSpec => recurrent
            state), Scheduler._preempt_request or {running, waiting.prepend_request}
  insert  : Request.append_output_token_ids (extends block hashes), Request.max_tokens,
            SamplingParams.extra_args (retrieval query); a running request with
            num_tokens > num_computed_tokens gets the difference scheduled (chunked if needed);
            the worker drops unscheduled requests from InputBatch and re-adds them from
            CachedRequestState; discard_request_mask skips sampling on partial chunks
  pause   : Scheduler.max_num_running_reqs (admission cap, `len(running) == cap` check),
            Scheduler.get_num_unfinished_requests (engine idles when it returns 0)
"""

from __future__ import annotations

from typing import Any

import torch

from ..utils import get_logger

log = get_logger("aidos.compat")


def vllm_version() -> str:
    try:
        import vllm

        return vllm.__version__
    except Exception:
        return "unavailable"


def _gpu(buf: Any) -> torch.Tensor:
    """CpuGpuBuffer (newer vLLM) or plain tensor (older)."""
    return buf.gpu if hasattr(buf, "gpu") else buf


# ----------------------------------------------------------------------------- worker
def query_start_loc_gpu(runner) -> torch.Tensor:
    return _gpu(runner.query_start_loc)


def positions_gpu(runner) -> torch.Tensor:
    return _gpu(runner.positions)


def max_num_reqs(runner) -> int:
    for obj, attr in ((runner, "max_num_reqs"), (runner.input_batch, "max_num_reqs")):
        if hasattr(obj, attr):
            return int(getattr(obj, attr))
    return int(runner.scheduler_config.max_num_seqs)


def unwrap_model(model: Any) -> Any:
    """Peel CUDAGraphWrapper / UBatchWrapper / our proxy to reach the nn.Module."""
    seen = set()
    m = model
    while id(m) not in seen:
        seen.add(id(m))
        if hasattr(m, "set_aux_hidden_state_layers") or hasattr(m, "model") and hasattr(getattr(m, "model"), "layers"):
            return m
        for attr in ("_tw_inner", "runnable", "unwrap"):
            nxt = getattr(m, attr, None)
            if nxt is None:
                continue
            m = nxt() if attr == "unwrap" and callable(nxt) else nxt
            break
        else:
            break
    return m


class HookStore:
    """Fallback aux capture via forward pre-hooks (requires enforce_eager: hooks do not
    replay inside CUDA graphs)."""

    def __init__(self, decoder_layers, layers: list[int]):
        self.buf: list[torch.Tensor] = []
        self.handles = []
        for li in layers:
            self.handles.append(decoder_layers[li].register_forward_pre_hook(self._hook, with_kwargs=True))

    def _hook(self, module, args, kwargs):
        # vLLM decoder layer signature: (positions, hidden_states, residual)
        hs = args[1] if len(args) > 1 else kwargs["hidden_states"]
        res = args[2] if len(args) > 2 else kwargs.get("residual")
        self.buf.append(hs if res is None else hs + res)

    def take(self) -> list[torch.Tensor]:
        out, self.buf = self.buf, []
        return out


def enable_aux_capture(model: Any, layers: list[int], mode: str, enforce_eager: bool) -> tuple[str, HookStore | None]:
    inner = unwrap_model(model)
    if mode in ("auto", "eagle3") and hasattr(inner, "set_aux_hidden_state_layers"):
        inner.set_aux_hidden_state_layers(tuple(layers))
        return "eagle3", None
    if mode == "eagle3":
        raise RuntimeError(f"{type(inner).__name__} has no EAGLE-3 aux hidden-state support; use aux_mode=hooks")
    if not enforce_eager:
        raise RuntimeError(
            f"{type(inner).__name__} lacks set_aux_hidden_state_layers; hook-based capture needs "
            "enforce_eager=true (hooks are not replayed inside CUDA graphs)"
        )
    from ..modeling import find_text_decoder

    log.warning("falling back to forward-hook aux capture for %s", type(inner).__name__)
    return "hooks", HookStore(find_text_decoder(inner).layers, layers)


def truncate_worker_request(runner, req_id: str, new_num_tokens: int) -> bool:
    """Rewind the worker's copy of a request to `new_num_tokens` total tokens.
    num_computed_tokens is NOT touched here: the scheduler sends the new value in the
    next SchedulerOutput and _update_states applies it."""
    req_state = runner.requests.get(req_id)
    if req_state is None:
        return False
    n_prompt = len(req_state.prompt_token_ids) if req_state.prompt_token_ids is not None else req_state.num_prompt_tokens
    keep = new_num_tokens - n_prompt
    out_ids = req_state.output_token_ids
    if keep < 0 or keep >= len(out_ids):
        return False
    del out_ids[keep:]  # same list object the InputBatch holds for this request
    ib = runner.input_batch
    idx = ib.req_id_to_index.get(req_id)
    if idx is not None:
        other = ib.req_output_token_ids[idx] if hasattr(ib, "req_output_token_ids") else None
        if other is not None and other is not out_ids and len(other) > keep:
            del other[keep:]
        for attr in ("num_tokens", "num_tokens_no_spec"):
            arr = getattr(ib, attr, None)
            if arr is not None:
                arr[idx] = new_num_tokens
    return True


def append_worker_request(runner, req_id: str, keep_tokens: int, tokens: list[int]) -> bool:
    """Evidence insertion on the worker: rewind the request to `keep_tokens` total tokens,
    then append `tokens` (as if they were outputs). The request is normally NOT in the
    persistent batch at this point (it was paused, and _update_states drops unscheduled
    requests), in which case the batch row is rebuilt from req_state when it is scheduled
    again. If it is still in the batch, its row is patched in place."""
    req_state = runner.requests.get(req_id)
    if req_state is None:
        return False
    n_prompt = len(req_state.prompt_token_ids) if req_state.prompt_token_ids is not None else req_state.num_prompt_tokens
    keep = keep_tokens - n_prompt
    out_ids = req_state.output_token_ids
    if keep < 0 or keep > len(out_ids):
        return False
    del out_ids[keep:]
    out_ids.extend(int(t) for t in tokens)
    ib = runner.input_batch
    idx = ib.req_id_to_index.get(req_id)
    if idx is not None:
        other = ib.req_output_token_ids[idx] if hasattr(ib, "req_output_token_ids") else None
        if other is not None and other is not out_ids:
            del other[keep:]
            other.extend(int(t) for t in tokens)
        end = keep_tokens + len(tokens)
        if end > ib.token_ids_cpu.shape[1]:
            return False
        ib.token_ids_cpu[idx, keep_tokens:end] = tokens
        for attr in ("num_tokens", "num_tokens_no_spec"):
            arr = getattr(ib, attr, None)
            if arr is not None:
                arr[idx] = end
    return True


def is_model_runner_output(obj: Any) -> bool:
    return obj is not None and hasattr(obj, "sampled_token_ids") and hasattr(obj, "req_ids")


def eager_mode(runner) -> bool:
    mc = getattr(runner, "model_config", None)
    return bool(getattr(mc, "enforce_eager", False))


# -------------------------------------------------------------------------- scheduler
def eos_token_id(request) -> int | None:
    # vLLM 0.21: EOS lives on SamplingParams (eos_token_id property); older: on Request
    sp = getattr(request, "sampling_params", None)
    for obj in (sp, request):
        eos = getattr(obj, "eos_token_id", None)
        if eos is not None:
            return int(eos)
    for attr in ("all_stop_token_ids", "stop_token_ids"):
        ids = getattr(sp, attr, None)
        if ids:
            return int(next(iter(ids)))
    return None


def truncate_request(request, drop: int, hash_block_size: int) -> None:
    if drop > 0:
        del request._output_token_ids[-drop:]
        del request._all_token_ids[-drop:]
    hashes = getattr(request, "block_hashes", None)
    if isinstance(hashes, list):
        del hashes[request.num_tokens // hash_block_size:]
    request.num_computed_tokens = request.num_tokens - 1


def insert_tokens(request, tokens: list[int]) -> None:
    """Scheduler side of evidence insertion. The request has already been truncated to
    its kept tokens, all of which have valid KV. The inserted tokens become output tokens
    (never sent to the client: the frontend only sees sampled tokens), get prefilled by the
    next schedule() like any running request with num_tokens > num_computed_tokens, and
    the token sampled after them continues the answer. max_tokens is raised so evidence
    does not eat the answer budget. append_output_token_ids also extends block hashes, so
    the new full blocks are prefix-cacheable."""
    kept = request.num_tokens
    request.append_output_token_ids(list(tokens))
    request.num_computed_tokens = kept
    if getattr(request, "max_tokens", None) is not None:
        request.max_tokens += len(tokens)


def _single_type_managers(kv_cache_manager) -> list:
    coord = getattr(kv_cache_manager, "coordinator", None)
    if coord is not None and hasattr(coord, "single_type_managers"):
        return list(coord.single_type_managers)
    if hasattr(kv_cache_manager, "single_type_manager"):
        return [kv_cache_manager.single_type_manager]
    raise RuntimeError("cannot locate single-type KV cache managers in this vLLM version")


def rollback_kv(kv_cache_manager, req_id: str, new_num_tokens: int, dry_run: bool) -> bool:
    """O(1) KV rollback.

    Blocks are NOT freed: the request keeps them and the next tokens simply overwrite the
    stale slots (allocate_slots only adds blocks when it needs more). What must change is
    the prefix cache: a *full* block that already got a hash for the hallucinated tokens
    would otherwise be served to future requests with that (old) prefix after we overwrite
    it. So: evict the hash of every block holding a dropped position and lower the
    request's cached-block watermark. A block shared with another request (ref_cnt > 1)
    cannot be rewritten in place -> refuse the rollback (dry_run reports that).
    """
    if not getattr(kv_cache_manager, "enable_caching", False):
        return True
    pool = kv_cache_manager.block_pool
    for mgr in _single_type_managers(kv_cache_manager):
        bs = mgr.block_size
        blocks = mgr.req_to_blocks.get(req_id, [])
        first = new_num_tokens // bs
        affected = blocks[first:]
        if dry_run:
            if any(getattr(b, "ref_cnt", 1) > 1 for b in affected):
                return False
            continue
        for b in affected:
            if getattr(b, "block_hash", None) is not None:
                pool._maybe_evict_cached_block(b)
        if req_id in mgr.num_cached_block:
            mgr.num_cached_block[req_id] = min(mgr.num_cached_block[req_id], first)
    return True


def is_hybrid(scheduler) -> bool:
    """True if any KV-cache group holds recurrent (Mamba / linear-attention) state.
    Qwen2.5 (pure attention) -> False."""
    kcc = getattr(scheduler, "kv_cache_config", None)
    for group in getattr(kcc, "kv_cache_groups", None) or []:
        spec_name = type(getattr(group, "kv_cache_spec", None)).__name__
        if "Mamba" in spec_name or "LinearAttention" in spec_name:
            return True
    return bool(getattr(scheduler.vllm_config.model_config, "is_hybrid", False))


def preempt_for_recompute(scheduler, request) -> bool:
    """Recompute rollback for hybrid models: hand the (already truncated) request to
    vLLM's own preemption path. It frees the request's KV/state blocks, resets
    num_computed_tokens to 0 and puts it at the front of the waiting queue, so the
    next schedule() re-prefills prompt + kept tokens and rebuilds the recurrent state
    exactly. Correct by construction; costs one prefill of a short sequence."""
    if request.is_finished() or request.request_id not in scheduler.requests:
        return False
    if hasattr(scheduler, "_preempt_request"):
        import time

        scheduler._preempt_request(request, time.monotonic())
    else:
        from vllm.v1.request import RequestStatus

        scheduler.kv_cache_manager.free(request)
        enc = getattr(scheduler, "encoder_cache_manager", None)
        if enc is not None and hasattr(enc, "free"):
            enc.free(request)
        request.status = RequestStatus.PREEMPTED
        request.num_computed_tokens = 0
        if hasattr(request, "num_preemptions"):
            request.num_preemptions += 1
        scheduler.waiting.prepend_request(request)
    if request in scheduler.running:
        scheduler.running.remove(request)
    return True


def iter_engine_core_outputs(outputs: Any):
    """update_from_output returns dict[client_index, EngineCoreOutputs] (newer) or one object."""
    if isinstance(outputs, dict):
        return list(outputs.values())
    return [outputs] if outputs is not None else []


def has_structured_output(sampling_params) -> bool:
    for attr in ("structured_outputs", "guided_decoding"):
        if getattr(sampling_params, attr, None) is not None:
            return True
    return False

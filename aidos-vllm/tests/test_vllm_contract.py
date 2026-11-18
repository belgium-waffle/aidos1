"""Contract tests: assert every vLLM-internal assumption listed in engine/compat.py
against the INSTALLED vLLM. Run this first after any vLLM upgrade:

    pytest tests/test_vllm_contract.py -v
"""

import dataclasses
import inspect

import pytest

vllm = pytest.importorskip("vllm")


def test_runner_methods():
    from vllm.v1.worker.gpu_model_runner import GPUModelRunner

    for name in ("load_model", "execute_model", "get_model"):
        assert hasattr(GPUModelRunner, name), name


def test_scheduler_methods():
    from vllm.v1.core.sched.scheduler import Scheduler

    for name in ("schedule", "update_from_output", "add_request", "finish_requests"):
        assert hasattr(Scheduler, name), name


def test_engine_args():
    from vllm.engine.arg_utils import EngineArgs

    names = {f.name for f in dataclasses.fields(EngineArgs)}
    assert "scheduler_cls" in names


def test_request_fields():
    from vllm.v1.request import Request

    from vllm import SamplingParams

    src = inspect.getsource(Request)
    for attr in ("_output_token_ids", "_all_token_ids", "num_computed_tokens", "block_hashes"):
        assert attr in src, attr
    for prop in ("num_tokens", "num_output_tokens", "num_prompt_tokens"):
        assert hasattr(Request, prop) or prop in src, prop
    # abstain needs an EOS id: on SamplingParams (vLLM >= 0.2x) or on Request (older)
    assert hasattr(SamplingParams, "eos_token_id") or "eos_token_id" in src


def test_insertion_and_pause_contract():
    """Evidence insertion + paused requests (engine/scheduler.py, compat.insert_tokens)."""
    from vllm.v1.core.sched.scheduler import Scheduler
    from vllm.v1.request import Request

    from vllm import SamplingParams

    src = inspect.getsource(Request)
    assert "def append_output_token_ids" in src and "update_block_hashes" in src
    assert "self.max_tokens" in src  # raised by the inserted length
    assert "extra_args" in inspect.signature(SamplingParams).parameters  # retrieval query channel
    sched = inspect.getsource(Scheduler)
    assert "self.max_num_running_reqs" in sched  # admission cap while requests are paused
    assert hasattr(Scheduler, "get_num_unfinished_requests")
    # admission compares running with the cap: running + paused <= max_num_seqs must hold
    assert "len(self.running) == self.max_num_running_reqs" in sched
    # running requests get num_tokens - num_computed new tokens scheduled (evidence prefill)
    assert "request.num_tokens_with_spec" in sched


def test_worker_rebuilds_unscheduled_requests_from_state():
    """A paused request leaves the persistent batch and is re-added from req_state."""
    from vllm.v1.worker.gpu_model_runner import GPUModelRunner

    src = inspect.getsource(GPUModelRunner._update_states)
    assert "unscheduled_req_ids" in src and "remove_request" in src
    disc = inspect.getsource(GPUModelRunner)
    assert "discard_request_mask" in disc  # partial evidence chunks sample nothing


def test_scheduler_preempt_contract():
    from vllm.v1.core.sched.scheduler import Scheduler

    # recompute-mode resume waits while the request is in prev_step_scheduled_req_ids
    assert "prev_step_scheduled_req_ids" in inspect.getsource(Scheduler)
    if hasattr(Scheduler, "_preempt_request"):
        src = inspect.getsource(Scheduler._preempt_request)
        assert "prepend_request" in src and "num_computed_tokens = 0" in src


def test_kv_manager_internals():
    from vllm.v1.core import block_pool, kv_cache_manager, single_type_kv_cache_manager

    assert hasattr(block_pool.BlockPool, "_maybe_evict_cached_block")
    src = inspect.getsource(single_type_kv_cache_manager)
    assert "req_to_blocks" in src and "num_cached_block" in src
    assert "coordinator" in inspect.getsource(kv_cache_manager.KVCacheManager)


def test_model_runner_output_is_plain_dataclass():
    from vllm.v1.outputs import ModelRunnerOutput

    assert dataclasses.is_dataclass(ModelRunnerOutput)
    assert not hasattr(ModelRunnerOutput, "__slots__") or "__dict__" in getattr(ModelRunnerOutput, "__slots__", ())
    fields = {f.name for f in dataclasses.fields(ModelRunnerOutput)}
    assert {"req_ids", "req_id_to_index", "sampled_token_ids"} <= fields


def test_qwen_supports_eagle3_aux():
    from vllm.model_executor.models import qwen2, qwen3

    q2 = hasattr(qwen2.Qwen2ForCausalLM, "set_aux_hidden_state_layers")
    q3 = hasattr(qwen3.Qwen3ForCausalLM, "set_aux_hidden_state_layers")
    if not (q2 and q3):
        pytest.skip(f"eagle3 aux support: qwen2={q2} qwen3={q3} (hook fallback needs enforce_eager)")

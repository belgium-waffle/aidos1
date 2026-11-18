"""Worker half: wraps vLLM V1's GPUModelRunner.

Per step (all on the GPU stream, no host sync added):

  1. apply truncation directives from the scheduler (rolled-back requests)
  2. model forward with EAGLE-3 aux capture -> residual stream at the head's layers
     (the forward, incl. CUDA graphs / torch.compile, is untouched; aux tensors are graph outputs)
  3. rows = query_start_loc[1:num_reqs+1] - 1   (last scheduled token of each request)
  4. fused Triton gather-GEMV -> risk[num_reqs, K]  (one launch)
  5. risk -> pinned host buffer with non_blocking copy + CUDA event
  6. compute_logits: banned tokens for rolled-back requests -> -inf  (device-side index_put)
  7. sampler runs; vLLM itself syncs to read sampled token ids
  8. after that sync the event is (almost always) complete -> read risks for free and
     attach them to ModelRunnerOutput for the scheduler

The head runs OUTSIDE the CUDA graph, on its outputs, so the graph-capture constraints
in the original prompt (static shapes, no host control flow) never apply to it.
"""

from __future__ import annotations

import functools

import torch

from ..kernels.score import head_scores
from ..utils import get_logger
from . import channel, compat
from .config import RuntimeConfig, load_runtime_config
from .heads import KINDS, HeadBank

log = get_logger("aidos.runner")
_PATCHED_FLAG = "_aidos_patched"


class AidosModelProxy:
    """Stands in for runner.model: strips aux outputs (so vLLM sees a plain model) and
    hooks scoring + bans. Everything else is forwarded to the wrapped model."""

    def __init__(self, inner, state: "RunnerState"):
        object.__setattr__(self, "_tw_inner", inner)
        object.__setattr__(self, "_tw_state", state)

    def __getattr__(self, name):
        return getattr(object.__getattribute__(self, "_tw_inner"), name)

    def __setattr__(self, name, value):
        setattr(self._tw_inner, name, value)

    def __call__(self, *args, **kwargs):
        out = self._tw_inner(*args, **kwargs)
        st = self._tw_state
        aux = None
        if isinstance(out, tuple) and len(out) == 2 and isinstance(out[1], (list, tuple)):
            out, aux = out
        elif st.hooks is not None:
            aux = st.hooks.take()
        if st.in_step and aux:
            st.score(list(aux))
        return out

    def compute_logits(self, *args, **kwargs):
        logits = self._tw_inner.compute_logits(*args, **kwargs)
        st = self._tw_state
        if st.in_step and logits is not None:
            st.apply_bans(logits)
        return logits


class RunnerState:
    def __init__(self, runner, cfg: RuntimeConfig):
        self.runner = runner
        self.cfg = cfg
        self.bank = HeadBank.from_dir(cfg.head_dir, cfg.post_head).to(runner.device)
        self.in_step = False
        self.pending: tuple[list[str], int, bool] | None = None
        self.bans: dict[str, list[int]] = {}
        self.host = torch.zeros((compat.max_num_reqs(runner), self.bank.num_heads), dtype=torch.float32).pin_memory()
        self.event = torch.cuda.Event()
        # column of each head kind in the bank (None = head not present), in KINDS order
        self.ks = tuple(self.bank.index(k) for k in KINDS)
        self.aux_mode, self.hooks = compat.enable_aux_capture(
            runner.model, self.bank.layers, cfg.aux_mode, compat.eager_mode(runner)
        )
        self.stats = {"steps": 0, "event_already_done": 0}
        self.dump: list | None = [] if cfg.dump_features_path else None
        log.info("aidos runner: heads=%s layers=%s aux=%s triton=%s", self.bank.kinds,
                 self.bank.layers, self.aux_mode, cfg.use_triton)

    def ensure_proxy(self) -> None:
        if not isinstance(self.runner.model, AidosModelProxy):
            self.runner.model = AidosModelProxy(self.runner.model, self)

    # --------------------------------------------------------------- GPU side
    def score(self, aux: list[torch.Tensor]) -> None:
        runner = self.runner
        n = runner.input_batch.num_reqs
        if n == 0:
            return
        qsl = compat.query_start_loc_gpu(runner)
        rows = (qsl[1 : n + 1] - 1).long()
        probs = head_scores(aux, rows, self.bank.W, self.bank.b, use_triton=self.cfg.use_triton)
        self.host[:n].copy_(probs, non_blocking=True)
        self.event.record()
        self.pending = (list(runner.input_batch.req_ids[:n]), n, False)
        if self.dump is not None:
            self._dump(aux, rows, n)

    def apply_bans(self, logits: torch.Tensor) -> None:
        if not self.bans:
            return
        idx_map = self.runner.input_batch.req_id_to_index
        rs, ts = [], []
        for rid, toks in self.bans.items():
            i = idx_map.get(rid)
            if i is None or i >= logits.shape[0]:
                continue
            for t in toks:
                if 0 <= t < logits.shape[-1]:
                    rs.append(i)
                    ts.append(t)
        if rs:
            r = torch.tensor(rs, dtype=torch.long).pin_memory().to(logits.device, non_blocking=True)
            t = torch.tensor(ts, dtype=torch.long).pin_memory().to(logits.device, non_blocking=True)
            logits.index_put_((r, t), torch.tensor(float("-inf"), device=logits.device, dtype=logits.dtype))

    # -------------------------------------------------------------- host side
    def finalize(self, out):
        if self.pending is None or not compat.is_model_runner_output(out):
            return out
        req_ids, n, _ = self.pending
        self.pending = None
        self.stats["steps"] += 1
        if self.event.query():  # vLLM's own sampled-token sync already covered our copy
            self.stats["event_already_done"] += 1
        self.event.synchronize()
        vals = self.host[:n].tolist()
        # (post, pre, know, help, pre_rag, post_rag, gain, harm) per request (heads.KINDS order);
        # know is the head's P(knows the answer) as is
        risks = {rid: tuple(v[k] if k is not None else None for k in self.ks) for rid, v in zip(req_ids, vals)}
        channel.attach(out, {"risks": risks})
        return out

    def _dump(self, aux, rows, n) -> None:  # debug/parity only: syncs every step
        pos = compat.positions_gpu(self.runner).index_select(0, rows).cpu()
        feats = torch.stack([a.index_select(0, rows) for a in aux], 1).to(torch.float16).cpu()
        self.dump.append({"req_ids": list(self.runner.input_batch.req_ids[:n]), "positions": pos, "x": feats})
        torch.save({"layers": self.bank.layers, "steps": self.dump}, self.cfg.dump_features_path)


def _wrap_get_model(orig):
    """get_model() must return the raw nn.Module: vLLM checks the model's interface on it
    (e.g. is_text_generation_model inspects __init__/forward signatures), which our proxy
    does not reproduce. Unwrap the proxy, then let vLLM peel its own wrappers."""

    @functools.wraps(orig)
    def get_model(self):
        model = self.__dict__.get("model")
        if isinstance(model, AidosModelProxy):
            self.model = model._tw_inner
            try:
                return orig(self)
            finally:
                self.model = model
        return orig(self)

    return get_model


def _wrap_load_model(orig):
    @functools.wraps(orig)
    def load_model(self, *args, **kwargs):
        result = orig(self, *args, **kwargs)
        cfg = load_runtime_config()
        if cfg is not None:
            self._tw_state = RunnerState(self, cfg)
            self._tw_state.ensure_proxy()
        return result

    return load_model


def _wrap_step(orig, apply_directives: bool):
    @functools.wraps(orig)
    def step(self, *args, **kwargs):
        st = getattr(self, "_tw_state", None)
        if st is None:
            return orig(self, *args, **kwargs)
        if apply_directives:
            payload = channel.take(args[0] if args else kwargs.get("scheduler_output")) or {}
            for rid, n_tokens in payload.get("truncate", {}).items():
                compat.truncate_worker_request(self, rid, n_tokens)
            for rid, (keep, tokens) in payload.get("insert", {}).items():
                if not compat.append_worker_request(self, rid, keep, tokens):
                    log.warning("evidence insertion failed on the worker for %s", rid)
            st.bans = payload.get("bans", {})
            st.ensure_proxy()
        st.in_step = True
        try:
            out = orig(self, *args, **kwargs)
        finally:
            st.in_step = False
        return st.finalize(out)

    return step


def patch_runner_class(cls) -> None:
    if getattr(cls, _PATCHED_FLAG, False):
        return
    cls.load_model = _wrap_load_model(cls.load_model)
    cls.get_model = _wrap_get_model(cls.get_model)
    cls.execute_model = _wrap_step(cls.execute_model, apply_directives=True)
    if hasattr(cls, "sample_tokens"):  # newer vLLM splits forward and sampling
        cls.sample_tokens = _wrap_step(cls.sample_tokens, apply_directives=False)
    setattr(cls, _PATCHED_FLAG, True)
    log.info("patched %s.%s", cls.__module__, cls.__name__)

"""Engine-core half: a vLLM V1 Scheduler subclass (selected with scheduler_cls=...).

update_from_output(), BEFORE vLLM appends this step's tokens:
    for every request with a fresh risk score -> policy.decide()
      ROLLBACK: truncate request tokens, evict stale prefix-cache hashes, set
                num_computed_tokens = num_tokens - 1, discard the token sampled this step,
                queue a worker truncation + a ban for the next step
      ABSTAIN : drop uncommitted tokens and replace the sampled token with EOS
      RETRIEVE: truncate the risky span (KV kept for the rest), discard this step's token,
                PAUSE the request (out of `running`, blocks still allocated) and start a
                retrieval in a worker thread
then super().update_from_output() (stop checks, outputs), then:
    commit horizon: only release tokens older than `horizon` to the client
    (so a rollback never has to retract text the user has already seen)

schedule(), BEFORE vLLM schedules:
    paused requests whose retrieval finished get the evidence turn appended as tokens
    (compat.insert_tokens) and go back to `running`; the next forward prefills only the
    evidence (the prompt + kept answer are already in the KV cache) and decoding continues.
    Other requests keep decoding while a retrieval is in flight.

Rollback cost on the host is O(span) list truncation + O(blocks in span) hash
evictions; on the GPU it is ONE re-forward of the last kept token. No blocks are freed
or re-allocated (see compat.rollback_kv).
"""

from __future__ import annotations

import hashlib
import random
import threading
import time
from collections import Counter, deque
from concurrent.futures import ThreadPoolExecutor, wait

from vllm.v1.core.sched.scheduler import Scheduler

from ..utils import append_jsonl_many, get_logger, prompt_hash
from . import channel, compat
from .config import ABSTAIN_STOP_REASON, load_runtime_config
from .heads import HeadBank
from .policy import Action, RequestTracker, AidosPolicy

log = get_logger("aidos.scheduler")
QUERY_KEY = "aidos_query"  # SamplingParams.extra_args key carrying the retrieval query
PROMPT_KEY = "aidos_prompt"  # long-form: the prompt the evidence turn restates (default: the query)
TELEMETRY_FLUSH = 512  # finished requests buffered per telemetry write
SENTENCE_END = (".", "!", "?", "\n", ".\"", ".'", ".)", "!\"", "?\"")


def sentence_boundary_ids(tok) -> frozenset[int]:
    """Token ids whose text ends a sentence (or contains a newline). Abbreviations ("Dr.",
    "U.S.") also end in "." and split a sentence early, which only shortens a rewind."""
    out = set()
    for i in range(len(tok)):
        s = tok.decode([i], skip_special_tokens=True)
        if s and ("\n" in s or s.rstrip(" ").endswith(SENTENCE_END)):
            out.add(i)
    return frozenset(out)


class AidosScheduler(Scheduler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        cfg = load_runtime_config()
        if cfg is None:
            raise RuntimeError("AidosScheduler needs AIDOS_CONFIG (use aidos.engine.factory.make_llm)")
        vc = self.vllm_config
        if getattr(vc.scheduler_config, "async_scheduling", False):
            raise RuntimeError("Aidos requires async_scheduling=False (rollback must see step t before scheduling t+1)")
        if getattr(vc, "speculative_config", None) is not None:
            raise RuntimeError("Aidos does not support speculative decoding yet")
        if vc.parallel_config.pipeline_parallel_size > 1:
            raise RuntimeError("Aidos does not support pipeline parallelism")
        taus = HeadBank.read_taus(cfg.head_dir, cfg.post_head)
        tau_post = cfg.tau_post if cfg.tau_post is not None else taus.get("post")
        tau_pre = cfg.tau_pre if cfg.tau_pre is not None else taus.get("pre")
        tau_gap = cfg.tau_gap
        if tau_gap is None:  # head_know.pt stores its tau on the gap score (1 - P(knows))
            tau_gap = taus["know"] if cfg.gap_signal == "know" and taus.get("know") is not None else tau_pre
        self.tw_cfg = cfg
        mondrian = HeadBank.read_mondrian(cfg.head_dir) if cfg.conformal == "mondrian" else None
        if cfg.conformal == "mondrian" and mondrian is None:
            raise RuntimeError("conformal=mondrian needs head_post.pt with Mondrian taus (run train-rag)")
        vc_m = vc.model_config
        self.tw_tok = None
        if cfg.retrieve_enabled or cfg.release == "sentence":
            from transformers import AutoTokenizer

            self.tw_tok = AutoTokenizer.from_pretrained(vc_m.tokenizer, trust_remote_code=vc_m.trust_remote_code)
        boundary = sentence_boundary_ids(self.tw_tok) if cfg.release == "sentence" else frozenset()
        self.tw_policy = AidosPolicy(cfg, tau_post, tau_pre, tau_gap, mondrian=mondrian, boundary=boundary)
        self.tw_trackers: dict[str, RequestTracker] = {}
        self.tw_truncate: dict[str, int] = {}
        self.tw_insert: dict[str, tuple[int, list[int]]] = {}
        self.tw_skip: set[str] = set()
        self.tw_stats: Counter = Counter()
        self.tw_tele: list[dict] = []  # finished-request telemetry, written in batches
        self.tw_status_t = 0.0  # live view: last snapshot time
        self.tw_recent: deque = deque(maxlen=64)  # live view: last finished requests
        hybrid = compat.is_hybrid(self)
        mode = cfg.rollback_mode
        if mode == "auto":
            mode = "recompute" if hybrid else "rewind"
        if mode == "rewind" and hybrid:
            raise RuntimeError("rewind rollback would corrupt recurrent (linear-attention) state; use rollback_mode=recompute")
        self.tw_rollback_mode = mode
        self.tw_recompute: list = []
        # ---- retrieval (paused requests) --------------------------------------------
        self.tw_parked: dict[str, dict] = {}
        self.tw_park_now: list = []
        self.tw_retriever = self.tw_pool = None
        if cfg.retrieve_enabled:
            from ..retrieval import load_retriever

            self.tw_retriever = load_retriever(cfg.retriever)
            self.tw_pool = ThreadPoolExecutor(max_workers=cfg.retrieval_workers, thread_name_prefix="aidos-retrieve")
            self.tw_delay_rng, self.tw_delay_lock = random.Random(0), threading.Lock()
            self.tw_max_len = vc_m.max_model_len
        log.info("aidos scheduler: policy=%s rollback=%s horizon=%d tau_post=%s tau_pre=%s tau_gap=%s gap=%s retriever=%s vllm=%s",
                 cfg.policy, mode, cfg.horizon, tau_post, tau_pre, tau_gap, cfg.gap_signal, cfg.retriever,
                 compat.vllm_version())

    # ------------------------------------------------------------------ intake
    def add_request(self, request) -> None:
        sp = request.sampling_params
        if sp is None:
            self.tw_skip.add(request.request_id)
        elif self.tw_cfg.intervenes and (sp.logprobs or sp.prompt_logprobs or compat.has_structured_output(sp)):
            # logprobs / grammars carry per-token state we do not roll back: leave untouched
            # (observe mode never changes tokens, so there they are fine)
            self.tw_skip.add(request.request_id)
        super().add_request(request)

    def finish_requests(self, request_ids, finished_status):
        if request_ids is None:  # vLLM: None = finish all (engine shutdown)
            ids = list(self.tw_trackers) + list(self.tw_parked)
        else:
            ids = [request_ids] if isinstance(request_ids, str) else list(request_ids)
        for rid in ids:
            parked = self.tw_parked.pop(rid, None)
            if parked is not None:
                parked["fut"].cancel()
            tr = self.tw_trackers.pop(rid, None)
            if tr is not None:
                self._tw_record(rid, tr, "aborted")
            self.tw_skip.discard(rid)
        return super().finish_requests(request_ids, finished_status)

    def get_num_unfinished_requests(self) -> int:
        # paused requests are unfinished: without this the engine loop would go idle
        # (and LLM.generate would hang) while the last requests wait for retrieval
        return super().get_num_unfinished_requests() + len(self.tw_parked)

    # ---------------------------------------------------------------- schedule
    def schedule(self):
        if self.tw_parked:
            self._tw_resume_parked()
        # a paused request keeps its batch slot: running + paused <= max_num_seqs, so a
        # resumed request always fits (vLLM admits waiting requests until running == max)
        cap = self.max_num_running_reqs
        self.max_num_running_reqs = max(0, cap - len(self.tw_parked))
        try:
            out = super().schedule()
        finally:
            self.max_num_running_reqs = cap
        bans = {}
        for rid in out.num_scheduled_tokens:
            tr, req = self.tw_trackers.get(rid), self.requests.get(rid)
            if tr is not None and req is not None:
                b = self.tw_policy.bans_for(tr, req.num_output_tokens)
                if b:
                    bans[rid] = sorted(b)
        channel.attach(out, {"truncate": self.tw_truncate, "bans": bans, "insert": self.tw_insert})
        self.tw_truncate = {}
        self.tw_insert = {}
        return out

    def _tw_resume_parked(self) -> None:
        if not self.running and (not self.waiting or len(self.tw_parked) >= self.max_num_running_reqs):
            # nothing else can run: block briefly on the first retrieval instead of spinning.
            # Short: the engine core reads new requests only between steps (50 ms here
            # delayed arrivals while every request was parked)
            wait([p["fut"] for p in self.tw_parked.values()], timeout=0.002, return_when="FIRST_COMPLETED")
        prev = getattr(self, "prev_step_scheduled_req_ids", ())
        for rid in [r for r, p in self.tw_parked.items() if p["fut"].done()]:
            if self.tw_rollback_mode == "recompute" and rid in prev:
                # a resumed (preempted) request must not have run in the previous step:
                # vLLM asserts this, since the worker only drops it from its persistent
                # batch after one unscheduled step. Resume on the next schedule() call.
                continue
            p = self.tw_parked.pop(rid)
            req, tr = p["req"], self.tw_trackers.get(rid)
            try:
                passages = p["fut"].result()
            except Exception as e:  # a failed retrieval must not kill the engine
                log.warning("retrieval failed for %s: %r", rid, e)
                passages = []
            tokens, used = self._tw_evidence_tokens(req, p["query"], passages, tr)
            keep = req.num_tokens
            if tokens:
                compat.insert_tokens(req, tokens)
                self.tw_insert[rid] = (keep, tokens)
            else:
                # nothing fits in the context: resume as is (truncate_request left
                # num_computed = num_tokens - 1, so the last kept token is re-read and a
                # fresh token sampled); being marked retrieved, a later trigger abstains
                self.tw_stats["retrieval_no_fit"] += 1
            if tr is not None:
                self.tw_policy.apply_retrieve_done(tr, len(tokens), used)
                tr.events[-1]["latency_ms"] = round(1000 * (time.perf_counter() - p["t0"]), 2)
            self.tw_stats["retrievals"] += 1
            if self.tw_rollback_mode == "recompute":
                # recurrent state cannot be rewound: re-prefill prompt + kept + evidence
                self.running.append(req)
                compat.preempt_for_recompute(self, req)
            else:
                self.running.append(req)

    def _tw_evidence_tokens(self, req, query: str, passages: list[dict],
                            tr: RequestTracker | None = None) -> tuple[list[int], int]:
        from ..data.qa import lf_insertion_ids, rag_insertion_ids

        lf = self.tw_cfg.longform
        if lf:
            # seeded: the new assistant turn re-opens with the answer the client has so far
            seed = None
            if self.tw_cfg.lf_insert == "seeded":
                seed = (tr.released_ids + tr.pending_tokens) if tr is not None else []
            prompt = self._tw_prompt(req)
            insert = lambda tok, _q, ps, chars: lf_insertion_ids(tok, prompt, ps, chars, seed)  # noqa: E731
        else:
            insert = rag_insertion_ids
        # long-form: room for the evidence turn and at least a sentence more, not the full
        # remaining max_tokens (a 512-token answer would leave no room for evidence)
        need = min(64, req.max_tokens - req.num_output_tokens) if lf else req.max_tokens - req.num_output_tokens
        budget = self.tw_max_len - req.num_tokens - max(1, need)
        for n in range(len(passages), 0, -1):
            toks = insert(self.tw_tok, query, passages[:n], self.tw_cfg.passage_chars)
            if len(toks) <= budget:
                return toks, n
        return [], 0

    def _tw_search(self, query: str, attempt: int = 0) -> list[dict]:
        """Runs in a retrieval worker thread, never on the scheduling path. Attempt a
        (0-based) inserts the passages ranked a*k+1 .. (a+1)*k: a second attempt reads the
        next-ranked evidence, the first evidence stays in context (and in the KV cache)."""
        if self.tw_cfg.retrieval_delay_ms:
            time.sleep(self.tw_cfg.retrieval_delay_ms / 1000)
        if self.tw_cfg.retrieval_delay_samples_ms:
            with self.tw_delay_lock:
                ms = self.tw_delay_rng.choice(self.tw_cfg.retrieval_delay_samples_ms)
            time.sleep(ms / 1000)
        k = self.tw_cfg.retrieve_k
        if self.tw_cfg.longform:  # every long-form retrieval has its own query: its top k
            attempt = 0
        return self.tw_retriever.search(query, k * (attempt + 1))[k * attempt:]

    def _tw_question(self, req) -> str:
        extra = getattr(req.sampling_params, "extra_args", None) or {}
        q = extra.get(QUERY_KEY)
        if q:
            return str(q)
        return self.tw_tok.decode(req.prompt_token_ids, skip_special_tokens=True)

    def _tw_prompt(self, req) -> str:
        extra = getattr(req.sampling_params, "extra_args", None) or {}
        return str(extra.get(PROMPT_KEY) or self._tw_question(req))

    def _tw_query(self, req, drop: int = 0, tr: RequestTracker | None = None) -> str:
        """Search query: the question; long-form adds the sentence being taken back, minus
        the tokens the head flagged (risk >= tau), as FLARE masks its low-probability tokens:
        a flagged token is usually a wrong entity, and searching for it fetches the wrong
        page (D84: "Who wrote X? ... by <wrong name>" retrieved the wrong name's page)."""
        q = self._tw_question(req)
        if self.tw_cfg.longform and drop:
            toks = list(req.output_token_ids[-drop:])
            if tr is not None and len(tr.pending_risks) >= drop and self.tw_policy.tau_post is not None:
                risks = tr.pending_risks[-drop:]
                toks = [t for t, r in zip(toks, risks) if r is None or r < self.tw_policy.tau_post]
            q = f"{q} {self.tw_tok.decode(toks, skip_special_tokens=True).strip()}".strip()
        return q

    # ------------------------------------------------------------------ update
    def update_from_output(self, scheduler_output, model_runner_output):
        payload = channel.take(model_runner_output) or {}
        risks = payload.get("risks", {})
        if risks:
            self._tw_decide(model_runner_output, risks)
        outputs = super().update_from_output(scheduler_output, model_runner_output)
        for req in self.tw_recompute:  # after super(): never preempt mid-update
            compat.preempt_for_recompute(self, req)
        self.tw_recompute = []
        for req in self.tw_park_now:  # after super(): pause requests waiting for retrieval
            if req in self.running:
                self.running.remove(req)
        self.tw_park_now = []
        if self.tw_trackers:
            self._tw_commit(outputs)
        if self.tw_cfg.status_path:
            self._tw_status()
        if self.tw_tele and (len(self.tw_tele) >= TELEMETRY_FLUSH
                             or (super().get_num_unfinished_requests() == 0 and not self.tw_parked)):
            # flushed before these outputs reach the client: when generate() returns, the
            # telemetry of every finished request is on disk
            self._tw_flush()
        return outputs

    def _tw_decide(self, mro, risks) -> None:
        sampled = list(mro.sampled_token_ids)
        changed = False
        for rid, vals in risks.items():
            if rid in self.tw_skip:
                continue
            r_post, r_pre, r_know, r_help, r_pre_rag, r_post_rag, r_gain, r_harm = (tuple(vals) + (None,) * 8)[:8]
            req = self.requests.get(rid)
            i = mro.req_id_to_index.get(rid)
            if req is None or i is None or req.is_finished():
                continue
            toks = sampled[i]
            if toks is None or len(toks) == 0:
                continue  # partial prefill chunk: nothing sampled, nothing to judge
            tr = self.tw_trackers.get(rid)
            if tr is None:
                tr = self.tw_trackers[rid] = RequestTracker(prompt_hash(req.prompt_token_ids), req.num_prompt_tokens)
            tr.decoded += len(toks)  # every sampled token, including ones later taken back
            d = self.tw_policy.decide(tr, req.num_output_tokens, r_post, r_pre, r_know, r_help, r_pre_rag, r_post_rag,
                                      r_gain, r_harm)
            self.tw_stats[d.action.value] += 1
            if d.action is Action.ROLLBACK:
                if self._tw_rollback(req, d.drop):
                    self.tw_policy.apply_rollback(tr, d)
                    sampled[i] = []
                    changed = True
                else:
                    self.tw_stats["rollback_refused"] += 1
            elif d.action is Action.RETRIEVE:
                if self._tw_start_retrieval(req, tr, d):
                    sampled[i] = []
                    changed = True
                else:
                    self.tw_stats["retrieve_refused"] += 1
            elif d.action is Action.ABSTAIN:
                eos = compat.eos_token_id(req)
                if eos is None or getattr(req.sampling_params, "ignore_eos", False):
                    self.tw_stats["abstain_impossible"] += 1
                    continue
                n_pending = len(tr.pending_tokens)
                if n_pending:
                    # the request ends this step: drop the tokens, no KV/state repair needed
                    # (nothing is written after them, so cached hashes stay truthful)
                    compat.truncate_request(req, n_pending, self.block_size)
                self.tw_policy.apply_abstain(tr, d.reason)
                sampled[i] = [eos]
                changed = True
        if changed:
            mro.sampled_token_ids = sampled

    def _tw_rollback(self, req, drop: int) -> bool:
        new_n = req.num_tokens - drop
        if new_n < req.num_prompt_tokens:
            return False
        if self.tw_rollback_mode == "rewind":
            if not compat.rollback_kv(self.kv_cache_manager, req.request_id, new_n, dry_run=True):
                return False
            compat.rollback_kv(self.kv_cache_manager, req.request_id, new_n, dry_run=False)
            compat.truncate_request(req, drop, self.block_size)
        else:  # recompute: truncate now, preempt after super().update_from_output()
            compat.truncate_request(req, drop, self.block_size)
            self.tw_recompute.append(req)
        self.tw_truncate[req.request_id] = new_n  # worker drops the same tokens + this step's sample
        return True

    def _tw_start_retrieval(self, req, tr: RequestTracker, d) -> bool:
        if self.tw_pool is None or tr.retrievals >= self.tw_cfg.max_retrievals:
            return False
        new_n = req.num_tokens - d.drop
        if new_n < req.num_prompt_tokens:
            return False
        if self.tw_rollback_mode == "rewind":
            if not compat.rollback_kv(self.kv_cache_manager, req.request_id, new_n, dry_run=True):
                return False
            compat.rollback_kv(self.kv_cache_manager, req.request_id, new_n, dry_run=False)
        query = self._tw_query(req, d.drop, tr)  # before the truncation: reads the dropped sentence
        compat.truncate_request(req, d.drop, self.block_size)
        self.tw_truncate[req.request_id] = new_n
        self.tw_policy.apply_retrieve_start(tr, d, req.num_output_tokens)
        if self.tw_cfg.longform and tr.events:
            tr.events[-1]["query"] = query
        fut = self.tw_pool.submit(self._tw_search, query, tr.retrievals - 1)
        self.tw_parked[req.request_id] = {"req": req, "fut": fut, "query": query, "t0": time.perf_counter()}
        self.tw_park_now.append(req)
        return True

    def _tw_commit(self, outputs) -> None:
        for eco in compat.iter_engine_core_outputs(outputs):
            kept = []
            for o in eco.outputs:
                tr = self.tw_trackers.get(o.request_id)
                if tr is None:
                    kept.append(o)
                    continue
                self.tw_policy.push(tr, list(o.new_token_ids or []))
                finished = o.finish_reason is not None
                o.new_token_ids = self.tw_policy.release(tr, finished)
                if finished:
                    if tr.abstained:
                        o.stop_reason = ABSTAIN_STOP_REASON
                    del self.tw_trackers[o.request_id]
                    self.tw_skip.discard(o.request_id)
                    self._tw_record(o.request_id, tr, str(o.finish_reason))
                if (o.new_token_ids or finished or getattr(o, "pooling_output", None) is not None
                        or getattr(o, "kv_transfer_params", None)):
                    kept.append(o)
            eco.outputs = kept

    def _tw_flush(self) -> None:
        """One open + one write per batch of finished requests. Appending per request
        (one open() on Lustre each) cost ~18% of bench throughput at 32B."""
        if self.tw_tele:
            append_jsonl_many(self.tw_cfg.telemetry_path, self.tw_tele)
            self.tw_tele = []

    def shutdown(self) -> None:
        self._tw_flush()
        parent = getattr(super(), "shutdown", None)
        if parent is not None:
            parent()

    def _tw_status(self, force: bool = False) -> None:
        """Live view: a small JSON snapshot of every tracked request (state, latest score,
        retrievals, rollbacks) plus the last finished ones. Rate-limited and written with an
        atomic replace; a failure is logged once and never affects serving."""
        now = time.time()
        if not force and now - self.tw_status_t < self.tw_cfg.status_interval_s:
            return
        self.tw_status_t = now
        try:
            import json
            import os

            def row(rid, tr, state):
                last = next((r for _, r in reversed(tr.trace) if r is not None), None)
                return {"id": rid, "state": state, "decoded": tr.decoded, "released": len(tr.released_ids),
                        "pre_risk": tr.pre_risk, "risk": None if last is None else round(last, 4),
                        "retrievals": tr.retrievals, "rollbacks": tr.rollbacks,
                        "trace": [None if r is None else round(r, 4) for _, r in tr.trace[-48:]]}
            active = [row(rid, tr, "paused" if rid in self.tw_parked else "running")
                      for rid, tr in self.tw_trackers.items()]
            snap = {"t": now, "policy": self.tw_cfg.policy, "lam": self.tw_cfg.eu_lambda,
                    "active": active, "finished": list(self.tw_recent), "stats": dict(self.tw_stats),
                    "waiting": len(self.waiting)}
            tmp = f"{self.tw_cfg.status_path}.tmp"
            with open(tmp, "w", encoding="utf-8") as f:
                json.dump(snap, f)
            os.replace(tmp, self.tw_cfg.status_path)
        except Exception as e:  # pragma: no cover - the live view must never break serving
            if not getattr(self, "tw_status_warned", False):
                log.warning("live status snapshot failed: %r", e)
                self.tw_status_warned = True

    def _tw_record(self, rid: str, tr: RequestTracker, finish: str) -> None:
        if self.tw_cfg.status_path:
            self.tw_recent.append({"id": rid, "state": "abstained" if tr.abstained else "finished",
                                   "finish": finish, "decoded": tr.decoded, "released": len(tr.released_ids),
                                   "pre_risk": tr.pre_risk, "retrievals": tr.retrievals, "rollbacks": tr.rollbacks,
                                   "trace": [None if r is None else round(r, 4) for _, r in tr.trace[-48:]]})
        if not self.tw_cfg.telemetry_path:
            return
        self.tw_tele.append({
            "request_id": rid,
            "prompt_hash": tr.prompt_hash,
            # joins telemetry to frontend outputs even when one prompt has many samples
            "out_hash": hashlib.sha1(",".join(map(str, tr.released_ids)).encode()).hexdigest()[:16],
            "finish": finish,
            "abstained": tr.abstained,
            "rollbacks": tr.rollbacks,
            "retrievals": tr.retrievals,
            "inserted": tr.inserted,
            "decoded": tr.decoded,
            "prompt_tokens": tr.n_prompt,
            "pre_risk": tr.pre_risk,
            "know": tr.know,
            "gap": tr.gap,
            "pre_risk_after": tr.pre_risk_after,
            "help": tr.help,
            "tau_post": tr.tau_post,
            "trace": [(i, None if r is None else round(r, 5)) for i, r in tr.trace],
            "events": tr.events,
            "released": tr.released,
        })

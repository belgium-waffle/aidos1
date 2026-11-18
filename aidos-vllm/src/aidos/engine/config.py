"""Runtime configuration shared by every vLLM process via the AIDOS_CONFIG env var.

vLLM V1 runs the scheduler (engine core) and the GPU workers in separate processes.
Environment variables are inherited by all of them, so a single JSON file path is the
simplest reliable way to configure both halves identically.
"""

from __future__ import annotations

import dataclasses
import json
import os
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

ENV_VAR = "AIDOS_CONFIG"
# What happens when a head fires (see engine/policy.py for the full table):
#   observe            score only
#   rollback           post trigger -> roll back the span, ban, resample
#   abstain            pre or post trigger -> stop and abstain
#   rollback+abstain   rollback; abstain when the rollback budget is spent
#   retrieve           gap at prefill or post trigger -> pause, retrieve, insert evidence, resume
#   retrieve+abstain   retrieve; abstain if still risky after retrieval
#   route              error-type routing: knowledge gap -> retrieve, drift -> rollback
#                      (budget spent -> retrieve), risky after retrieval -> abstain
#   route-noretrieve   same typing without a retriever: gap -> abstain, drift -> rollback
#   route-eu           expected-utility routing: no thresholds, only lam and the retrieval
#                      cost. At prefill: argmax of answer (1-(1+lam)*P_wrong, pre head),
#                      retrieve (EU(answer) + (1+lam)*(P_gain - P_harm) - cost, gain/harm
#                      heads), abstain (0). While answering: stop when continuing is worth
#                      less than retrieving / abstaining. After evidence: negative utility
#                      -> second attempt (next-ranked passages) while max_retrievals allows,
#                      then abstain.
#   lf-retrieve        long-form: the post head (post_head=post_lf, entity-level) fires inside
#                      a sentence -> rewind to the sentence start (earlier sentences keep their
#                      KV), retrieve with question + that sentence, insert the evidence with a
#                      "continue your answer" turn, resume. Text is released a sentence at a
#                      time (release=sentence), so a rewind never retracts shown text. Up to
#                      max_retrievals per answer; a trigger in the first sentence after an
#                      insertion is accepted (that sentence was written with the evidence).
POLICIES = ("observe", "rollback", "abstain", "rollback+abstain", "retrieve", "retrieve+abstain",
            "route", "route-noretrieve", "route-eu", "lf-retrieve")
ABSTAIN_STOP_REASON = "aidos_abstain"


@dataclass
class RuntimeConfig:
    head_dir: str
    policy: str = "observe"
    horizon: int = 8
    max_rollbacks: int = 3
    max_bans_per_position: int = 3
    low_ratio: float = 0.8
    on_budget_exhausted: str = "continue"  # continue | abstain ("rollback+abstain" forces abstain)
    tau_post: float | None = None
    tau_pre: float | None = None
    use_triton: bool = True
    force_rollback_every: int = 0
    telemetry_path: str | None = None
    dump_features_path: str | None = None
    aux_mode: str = "auto"  # auto | eagle3 | hooks
    rollback_mode: str = "auto"  # auto | rewind | recompute
    # ---- error-type routing / retrieval (route*, retrieve* policies) -----------------
    gap_signal: str = "pre"  # pre: gap score = pre-head risk | know: gap score = 1 - know-head
    tau_gap: float | None = None  # None -> tau of the gap head (pre: conformal tau_pre)
    drift_ratio: float = 0.5  # a post trigger is "drift" if gap score < drift_ratio * tau_gap
    # abstain thresholds AFTER evidence insertion. The heads are calibrated closed-book;
    # with evidence in context they over-estimate risk, so these are chosen separately on
    # val by the policy stage (1e9 = never abstain after retrieval). None -> tau_pre/tau_post.
    tau_pre_rag: float | None = None
    tau_post_rag: float | None = None
    retriever: str | None = None  # BM25 index dir (aidos.retrieval.bm25)
    retrieve_k: int = 3  # passages inserted per retrieval
    passage_chars: int = 600
    retrieval_workers: int = 4
    # what a retrieval triggered MID-answer takes back before inserting the evidence:
    #   answer: the whole answer, if none of it has reached the client yet (commit horizon);
    #           the model answers afresh from prompt + evidence, the same state as a
    #           retrieval at prefill (and as the offline RAG answers the policy is chosen on).
    #           Falls back to "span" once tokens have been released.
    #   span:   only the risky span; the model continues its partial answer after the
    #           evidence (the first 32B run: ~3 points less accurate than offline RAG)
    retrieve_rewind: str = "answer"
    # retrievals per request. When the answer WITH evidence is still judged risky (where a
    # single-retrieval policy abstains), attempt 2 rewinds that answer and inserts the
    # next-ranked passages (ranks k+1..2k) after the first evidence, which stays in the KV
    # cache; only after the last attempt does the request abstain. v4 (32B): the second attempt
    # was worth +0.2 utility points for ~40% more prefill, so 1 is the default, 2 an ablation.
    max_retrievals: int = 1
    # route-eu's value of retrieving: "gain" = EU(answer) + (1+lam)(P(gain) - P(harm)) - cost
    # (heads trained on whether retrieval flips the answer), "help" = 1 - (1+lam) P(evidence
    # answer wrong) - cost (the v3 head), "option" = E[max(utility after the evidence, 0) |
    # help] - cost (eu_option_table, fitted on val: the abstain option after retrieval is
    # valued). The policy stage picks one on val; gain/option fall back to help without data.
    eu_retrieve_signal: str = "help"
    eu_option_table: list | None = None
    # after an insertion, score with the heads trained WITH evidence in context
    # (head_pre_rag / head_post_rag, train-rag stage) when they exist
    rag_heads: bool = True
    # marginal: one conformal tau for the post head | mondrian: tau per pre-risk group
    # (head_post.pt "mondrian", train-rag stage)
    conformal: str = "marginal"
    # route-eu: utility weights and the answer-level calibration of the post heads'
    # running max ([a, c]: P(answer wrong) = sigmoid(a * logit(p) + c), fitted on val by
    # the policy stage; null = use the token probability as is)
    eu_lambda: float = 1.0
    eu_cost: float = 0.02
    eu_post_platt: list[float] | None = None
    eu_post_rag_platt: list[float] | None = None
    # testing / systems knobs: force one retrieval after n output tokens (0 = off), and add
    # artificial latency to every retrieval (emulates a remote retriever)
    force_retrieve_at: int = 0
    force_retry: bool = False  # testing: always take the second attempt right after the first insertion
    retrieval_delay_ms: float = 0.0
    # latency stage: every retrieval sleeps for a latency drawn from these measured live
    # BM25 + rerank service times (ms), so a cached lookup costs what a live one would
    retrieval_delay_samples_ms: list[float] | None = None
    # ---- long-form (lf-retrieve) -----------------------------------------------------
    post_head: str = "post"  # head file serving as the post head: post | post_lf | post_mix
    # horizon: hold back the newest `horizon` tokens | sentence: hold back the unfinished
    # sentence (at most lf_max_hold tokens), release each sentence when it ends
    release: str = "horizon"
    lf_max_hold: int = 96
    # evidence turn (D86): "seeded" = user turn with context + the original prompt, then the
    # assistant turn re-opened with the answer so far, so the model continues its own text
    # (FLARE's prompt shape; the earlier turns stay in the KV cache). "turn" = context +
    # "continue where you stopped" and an empty assistant turn: models restart or comment
    # on the context ("It appears there was a misunderstanding ...").
    lf_insert: str = "seeded"
    # live view (demo): every status_interval_s the scheduler writes a JSON snapshot of request
    # states and latest scores to status_path (atomic replace; off when None)
    status_path: str | None = None
    status_interval_s: float = 0.25

    def __post_init__(self) -> None:
        if self.policy not in POLICIES:
            raise ValueError(f"policy must be one of {POLICIES}, got {self.policy!r}")
        if self.gap_signal not in ("pre", "know"):
            raise ValueError("gap_signal must be 'pre' or 'know'")
        if self.retrieve_enabled and not self.retriever:
            raise ValueError(f"policy {self.policy!r} needs a retriever index (retriever=...)")
        if self.rollback_mode not in ("auto", "rewind", "recompute"):
            raise ValueError("rollback_mode must be auto, rewind or recompute")
        if self.retrieve_rewind not in ("answer", "span"):
            raise ValueError("retrieve_rewind must be 'answer' or 'span'")
        if self.max_retrievals < 1:
            raise ValueError("max_retrievals must be >= 1")
        if self.eu_retrieve_signal not in ("gain", "help", "option"):
            raise ValueError("eu_retrieve_signal must be 'gain', 'help' or 'option'")
        if self.conformal not in ("marginal", "mondrian"):
            raise ValueError("conformal must be 'marginal' or 'mondrian'")
        if self.aux_mode not in ("auto", "eagle3", "hooks"):
            raise ValueError("aux_mode must be auto, eagle3 or hooks")
        if self.horizon < 1:
            raise ValueError("horizon must be >= 1 (the flagged token must still be uncommitted)")
        if self.on_budget_exhausted not in ("continue", "abstain"):
            raise ValueError("on_budget_exhausted must be 'continue' or 'abstain'")
        if self.release not in ("horizon", "sentence"):
            raise ValueError("release must be 'horizon' or 'sentence'")
        if self.lf_insert not in ("seeded", "turn"):
            raise ValueError("lf_insert must be 'seeded' or 'turn'")
        if self.longform and self.release != "sentence":
            raise ValueError("lf-retrieve rewinds whole sentences: it needs release=sentence")

    @property
    def longform(self) -> bool:
        return self.policy == "lf-retrieve"

    @property
    def route_enabled(self) -> bool:  # error-type routing (threshold policies)
        return self.policy in ("route", "route-noretrieve")

    @property
    def eu_enabled(self) -> bool:  # expected-utility routing
        return self.policy == "route-eu"

    @property
    def rollback_enabled(self) -> bool:
        return "rollback" in self.policy or self.route_enabled

    @property
    def retrieve_enabled(self) -> bool:
        return self.policy in ("retrieve", "retrieve+abstain", "route", "route-eu", "lf-retrieve")

    @property
    def abstain_enabled(self) -> bool:
        return "abstain" in self.policy or self.route_enabled or self.eu_enabled

    @property
    def intervenes(self) -> bool:
        return self.policy != "observe" or bool(self.force_rollback_every) or bool(self.force_retrieve_at)

    @property
    def abstain_on_exhaust(self) -> bool:
        return self.policy == "rollback+abstain" or self.on_budget_exhausted == "abstain"

    def write(self, path: str | os.PathLike) -> Path:
        p = Path(path)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(dataclasses.asdict(self), indent=2), encoding="utf-8")
        return p


@lru_cache(maxsize=1)
def _load(path: str) -> RuntimeConfig:
    with open(path, encoding="utf-8") as f:
        return RuntimeConfig(**json.load(f))


def load_runtime_config() -> RuntimeConfig | None:
    path = os.environ.get(ENV_VAR)
    return _load(path) if path else None

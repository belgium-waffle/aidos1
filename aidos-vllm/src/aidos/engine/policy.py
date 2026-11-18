"""Decision logic: what to do with per-token risk scores. Pure Python, no vLLM.

Timeline of one request (P = prompt length):

  step 0 (prefill): row = last prompt token  -> risk_pre / risk_know  ("should I answer at all?")
  step s >= 1     : row = output token s-1   -> risk_post ("was token s-1 a confabulation?")
  after evidence insertion: the first scored row is the end of the inserted turn, i.e. a
  second "pre" decision ("now that I have context, can I answer?")

The risk computed at step s is attributed to the most recent output token. That token is
still *uncommitted* because of the commit horizon: the scheduler withholds the newest
`horizon` tokens from the client. So when a head fires we can still take the
whole risky span back, not just one token.

Rollback (the span):
  walk backwards from the flagged token while the risk stays above low_ratio * tau_post;
  drop that span (plus the token sampled this step), forbid the span's first token at
  that position, and resample from there. Because the score is computed AFTER the model
  has read the token, a different token gives a different hidden state and a different
  score, so a resample is a real second chance (not a loop on the same state).

Error-type routing (policies route / route-noretrieve), the Phase-B design:
  gap score g = pre-head risk (or 1 - know-head) at prefill
    g > tau_gap                    -> KNOWLEDGE GAP: retrieve (or abstain without retriever)
  later, the post head fires:
    already retrieved              -> abstain (evidence did not help)
    g < drift_ratio * tau_gap      -> DRIFT: the model should know this; roll back + resample
                                      (budget spent -> retrieve, or abstain)
    otherwise                      -> borderline knowledge: retrieve (or abstain)
  A rollback cannot create knowledge the model lacks (the first 32B run: rollback alone
  lowered accuracy on factoid QA), so only drift is sent to rollback.

Full table (prefill uses tau_pre for abstain*, tau_gap for retrieve*/route*):
  policy            prefill trigger   post trigger (before retrieval)        after retrieval
  rollback          -                 rollback (budget -> continue)          -
  abstain           abstain           abstain                                -
  rollback+abstain  abstain           rollback (budget -> abstain)           -
  retrieve          retrieve          retrieve                               continue
  retrieve+abstain  retrieve          retrieve                               abstain
  route             retrieve          drift: rollback(->retrieve) else retr. abstain
  route-noretrieve  abstain           drift: rollback(->abstain) else abst.  -
  route-eu          argmax EU of      continue while EU(answer) >= EU of     retry iff
                    answer/retrieve/  retrieve / abstain; else the better    EU(answer) < 0,
                    abstain           of the two                             then abstain

route-eu: EU(answer) = 1 - (1+lam) * P(wrong), EU(abstain) = 0, and
  EU(retrieve) = EU(answer) + (1+lam) * (P(gain) - P(harm)) - cost   (eu_retrieve_signal=gain)
               = 1 - (1+lam) * P(evidence answer wrong) - cost        (=help, the v3 head)
since P(evidence answer wrong) = P(wrong) - P(wrong -> right) + P(right -> wrong). The gain /
harm heads are trained on exactly the event that matters (does retrieval FLIP the answer),
so retrieval is chosen where it changes the outcome, which is what the oracle router does.
P(wrong) is the pre head at prefill, the calibrated running max of the post head while
answering, and the evidence-trained heads after an insertion.

Second attempt (max_retrievals >= 2, every policy that abstains after retrieval): where
"after retrieval" above says abstain, the request first retries - the evidence answer is
taken back (the whole answer while unreleased) and the next-ranked passages are inserted
after the first evidence (KV kept); the abstain decision applies after the last attempt.

After an insertion every policy reads the evidence-trained heads (pre_rag / post_rag)
when they are loaded (cfg.rag_heads); with conformal=mondrian the post tau of a request
is the one of its pre-risk group.
"""

from __future__ import annotations

import bisect
import math
from dataclasses import dataclass, field
from enum import Enum

from .config import RuntimeConfig


def option_value(table, x: float) -> float:
    """route-eu "option" signal: expected utility of the retrieval branch (the policy may
    still answer, retry or abstain after reading the evidence) as a function of the help
    head, table = [xs, values] fitted on val (pipeline/policy.py: fit_option_table).
    Linear interpolation, constant beyond the ends. Shared by the engine and the simulator."""
    xs, vs = table
    if x <= xs[0]:
        return float(vs[0])
    if x >= xs[-1]:
        return float(vs[-1])
    i = bisect.bisect_right(xs, x)
    a = (x - xs[i - 1]) / (xs[i] - xs[i - 1]) if xs[i] > xs[i - 1] else 0.0
    return float(vs[i - 1] + a * (vs[i] - vs[i - 1]))


class Action(Enum):
    NONE = "none"
    ROLLBACK = "rollback"
    ABSTAIN = "abstain"
    RETRIEVE = "retrieve"


@dataclass
class Decision:
    action: Action = Action.NONE
    drop: int = 0  # already-appended output tokens to remove (the token sampled this step is always discarded)
    ban_index: int | None = None  # output index whose next sample must avoid ban_token
    ban_token: int | None = None
    reason: str = ""


@dataclass
class RequestTracker:
    prompt_hash: str = ""
    n_prompt: int = 0
    pending_tokens: list[int] = field(default_factory=list)  # not yet released to the client
    pending_risks: list[float | None] = field(default_factory=list)
    released: int = 0
    released_ids: list[int] = field(default_factory=list)
    rollbacks: int = 0
    abstained: bool = False
    pre_risk: float | None = None
    know: float | None = None  # know-head P(knows) at prefill
    gap: float | None = None  # gap score at prefill
    retrieved: bool = False
    retrievals: int = 0
    inserted: int = 0  # evidence tokens inserted (engine-internal, never shown)
    decoded: int = 0  # tokens sampled (decode work), including discarded ones
    expect_pre: bool = False  # next scored row is the end of an inserted turn
    pre_risk_after: float | None = None
    bans: dict[int, set[int]] = field(default_factory=dict)
    trace: list[tuple[int, float | None]] = field(default_factory=list)  # (output index, risk)
    events: list[dict] = field(default_factory=list)
    steps: int = 0
    tau_post: float | None = None  # per-request post tau (Mondrian group), else the policy's
    help: float | None = None  # help head at prefill: P(the evidence answer is wrong)
    gain: float | None = None  # gain head at prefill: P(retrieval turns wrong into right)
    harm: float | None = None  # harm head at prefill: P(retrieval turns right into wrong)
    eu_retrieve: float | None = None  # route-eu: utility of retrieving, fixed at prefill
    lf_cooldown: bool = False  # lf-retrieve: inside the first sentence written with new evidence


class AidosPolicy:
    def __init__(self, cfg: RuntimeConfig, tau_post: float | None, tau_pre: float | None,
                 tau_gap: float | None = None, mondrian: dict | None = None,
                 boundary: frozenset[int] = frozenset()):
        self.cfg = cfg
        # token ids that end a sentence (".", "!", "?", newline; computed from the tokenizer by
        # the scheduler): sentence release and sentence rewind (lf-retrieve)
        self.boundary = boundary
        self.tau_post = tau_post
        self.tau_pre = tau_pre
        self.tau_gap = tau_gap if tau_gap is not None else tau_pre
        pre_rag, post_rag = getattr(cfg, "tau_pre_rag", None), getattr(cfg, "tau_post_rag", None)
        self.tau_pre_rag = pre_rag if pre_rag is not None else tau_pre
        self.tau_post_rag = post_rag if post_rag is not None else tau_post
        # {"edges": [...], "taus": [...]}: post tau by pre-risk group (Mondrian conformal)
        self.mondrian = mondrian if getattr(cfg, "conformal", "marginal") == "mondrian" else None

    # ------------------------------------------------------------------ helpers
    def gap_score(self, risk_pre: float | None, risk_know: float | None) -> float | None:
        if self.cfg.gap_signal == "know" and risk_know is not None:
            return 1.0 - risk_know
        return risk_pre

    def _is_drift(self, tr: RequestTracker) -> bool:
        return tr.gap is not None and self.tau_gap is not None and tr.gap < self.cfg.drift_ratio * self.tau_gap

    @staticmethod
    def _over(x: float | None, tau: float | None) -> bool:
        return x is not None and tau is not None and x > tau

    def _tau_post_now(self, tr: RequestTracker) -> float | None:
        if tr.retrieved:
            return self.tau_post_rag
        return tr.tau_post if tr.tau_post is not None else self.tau_post

    # ---- expected utility (route-eu) ------------------------------------------------
    def _eu(self, p_wrong: float) -> float:
        """Utility of answering when the answer is wrong with probability p: +1 correct,
        -lam wrong (abstaining is 0)."""
        return 1.0 - (1.0 + self.cfg.eu_lambda) * p_wrong

    @staticmethod
    def _answer_prob(p: float, platt) -> float:
        """Token probability -> P(answer wrong) for the running max of a post head."""
        if not platt:
            return p
        q = min(max(p, 1e-6), 1 - 1e-6)
        z = platt[0] * math.log(q / (1 - q)) + platt[1]
        return 1.0 / (1.0 + math.exp(-z))

    # ------------------------------------------------------------------ decide
    def decide(self, tr: RequestTracker, n_out: int, risk_post: float | None, risk_pre: float | None,
               risk_know: float | None = None, risk_help: float | None = None,
               risk_pre_rag: float | None = None, risk_post_rag: float | None = None,
               risk_gain: float | None = None, risk_harm: float | None = None) -> Decision:
        """n_out: number of output tokens BEFORE this step's sampled token is appended."""
        cfg = self.cfg
        tr.steps += 1
        if n_out == 0 and not tr.expect_pre:
            tr.gain, tr.harm = risk_gain, risk_harm
        if tr.retrieved and getattr(cfg, "rag_heads", True):
            # evidence in context: the heads trained with evidence (when present)
            risk_post = risk_post_rag if risk_post_rag is not None else risk_post
            risk_pre = risk_pre_rag if risk_pre_rag is not None else risk_pre
        if (cfg.force_retrieve_at and cfg.retrieve_enabled and n_out == cfg.force_retrieve_at
                and not tr.retrievals and not tr.expect_pre):
            if n_out > 0 and tr.pending_tokens:
                tr.pending_risks[-1] = risk_post
            return Decision(Action.RETRIEVE, self._retrieve_drop(tr, 0), reason="forced")
        if cfg.longform and (n_out == 0 or tr.expect_pre):
            # long-form: nothing to decide before writing; the first sentence after an
            # insertion was written with the evidence, so a trigger in it is accepted
            if tr.expect_pre:
                tr.expect_pre, tr.lf_cooldown = False, True
                tr.pre_risk_after = risk_pre
            else:
                tr.pre_risk = risk_pre
            return Decision()
        if n_out == 0 or tr.expect_pre:
            return self._decide_pre(tr, risk_pre, risk_know, risk_help)

        if tr.pending_tokens:
            tr.pending_risks[-1] = risk_post
        tr.trace.append((n_out - 1, risk_post))
        if cfg.longform:
            return self._decide_lf(tr, risk_post)
        if cfg.eu_enabled:
            return self._decide_eu_post(tr, risk_post)

        triggered = self._over(risk_post, self._tau_post_now(tr))
        forced = bool(cfg.force_rollback_every) and cfg.rollback_enabled and tr.steps % cfg.force_rollback_every == 0
        if not (triggered or forced) or not tr.pending_tokens:
            return Decision()
        span = self._span_start(tr) if triggered else len(tr.pending_tokens) - 1
        drop = len(tr.pending_tokens) - span
        if forced and not triggered:
            return self._rollback_or(tr, n_out, span, drop, "forced", fallback=Decision(reason="budget"))

        rdrop = self._retrieve_drop(tr, drop)
        if cfg.route_enabled:
            if tr.retrieved:
                return self._retry_or_abstain(tr, rdrop, "post-after-retrieval")
            fallback = (Decision(Action.RETRIEVE, rdrop, reason="drift-budget") if cfg.retrieve_enabled
                        else Decision(Action.ABSTAIN, reason="drift-budget"))
            if self._is_drift(tr):
                return self._rollback_or(tr, n_out, span, drop, "drift", fallback)
            return (Decision(Action.RETRIEVE, rdrop, reason="post-gap") if cfg.retrieve_enabled
                    else Decision(Action.ABSTAIN, reason="post-gap"))
        if cfg.retrieve_enabled:
            if not tr.retrieved:
                return Decision(Action.RETRIEVE, rdrop, reason="post")
            return self._retry_or_abstain(tr, rdrop, "post-after-retrieval") if cfg.abstain_enabled else Decision()
        if cfg.rollback_enabled:
            fallback = Decision(Action.ABSTAIN, reason="budget") if cfg.abstain_on_exhaust else Decision(reason="budget")
            return self._rollback_or(tr, n_out, span, drop, "post", fallback)
        if cfg.abstain_enabled:
            return Decision(Action.ABSTAIN, reason="post")
        return Decision()

    def _decide_lf(self, tr: RequestTracker, risk_post) -> Decision:
        """lf-retrieve: an unsupported-entity trigger inside the unreleased sentence ->
        take the sentence back and retrieve for it, while the budget lasts."""
        if not tr.pending_tokens or tr.lf_cooldown or not self._over(risk_post, self.tau_post):
            return Decision()
        if tr.retrievals >= self.cfg.max_retrievals:
            return Decision(reason="lf-budget")
        return Decision(Action.RETRIEVE, len(tr.pending_tokens) - self._sentence_start(tr), reason="lf-post")

    def _sentence_start(self, tr: RequestTracker) -> int:
        """Index in pending_tokens of the first token of the current sentence (the flagged,
        newest token never counts as the boundary that precedes it)."""
        for i in range(len(tr.pending_tokens) - 2, -1, -1):
            if tr.pending_tokens[i] in self.boundary:
                return i + 1
        return 0

    def _decide_eu_post(self, tr: RequestTracker, risk_post) -> Decision:
        """route-eu while answering: continue while continuing is worth more than the
        alternatives (retrieve once - its utility was fixed at prefill - or abstain)."""
        if risk_post is None or not tr.pending_tokens:
            return Decision()
        cfg = self.cfg
        platt = cfg.eu_post_rag_platt if tr.retrieved else cfg.eu_post_platt
        u = self._eu(self._answer_prob(risk_post, platt))
        alt = 0.0
        can_retrieve = not tr.retrievals and tr.eu_retrieve is not None
        if can_retrieve:
            alt = max(alt, tr.eu_retrieve)
        if u >= alt:
            return Decision()
        span = self._span_start(tr) if self.tau_post is not None else len(tr.pending_tokens) - 1
        rdrop = self._retrieve_drop(tr, len(tr.pending_tokens) - span)
        if can_retrieve and tr.eu_retrieve > 0.0:
            return Decision(Action.RETRIEVE, rdrop, reason="eu-post")
        if tr.retrieved:
            return self._retry_or_abstain(tr, rdrop, "eu-post-after-retrieval")
        return Decision(Action.ABSTAIN, reason="eu-post")

    def _decide_pre(self, tr: RequestTracker, risk_pre, risk_know, risk_help=None) -> Decision:
        cfg = self.cfg
        after = tr.expect_pre
        tr.expect_pre = False
        if after and getattr(cfg, "force_retry", False) and cfg.retrieve_enabled \
                and tr.retrievals < cfg.max_retrievals:
            return Decision(Action.RETRIEVE, 0, reason="forced-retry")
        if cfg.eu_enabled:
            return self._decide_eu_pre(tr, after, risk_pre, risk_know, risk_help)
        if not after:
            tr.pre_risk, tr.know = risk_pre, risk_know
            tr.gap = self.gap_score(risk_pre, risk_know)
            if self.mondrian is not None and risk_pre is not None:  # this request's post tau
                g = bisect.bisect_right(self.mondrian["edges"], risk_pre)
                tr.tau_post = self.mondrian["taus"][g]
            if cfg.retrieve_enabled and self._over(tr.gap, self.tau_gap):
                return Decision(Action.RETRIEVE, reason="gap")
            if cfg.route_enabled and self._over(tr.gap, self.tau_gap):  # route-noretrieve
                return Decision(Action.ABSTAIN, reason="gap")
            if cfg.abstain_enabled and not cfg.route_enabled and not cfg.retrieve_enabled \
                    and self._over(risk_pre, self.tau_pre):
                return Decision(Action.ABSTAIN, reason="pre")
            return Decision()
        # first row after an evidence insertion
        tr.pre_risk_after = risk_pre
        if cfg.abstain_enabled and self._over(risk_pre, self.tau_pre_rag):
            return self._retry_or_abstain(tr, 0, "pre-after-retrieval")
        return Decision()

    def _decide_eu_pre(self, tr: RequestTracker, after: bool, risk_pre, risk_know, risk_help) -> Decision:
        """route-eu at prefill: argmax over answer / retrieve / abstain of the expected
        utility (ties: answer, then retrieve). After an insertion: abstain iff answering
        with the evidence has negative utility. Missing scores never trigger anything."""
        if after:
            tr.pre_risk_after = risk_pre
            if risk_pre is not None and self._eu(risk_pre) < 0.0:
                return self._retry_or_abstain(tr, 0, "eu-pre-after-retrieval")
            return Decision()
        tr.pre_risk, tr.know, tr.help = risk_pre, risk_know, risk_help
        tr.gap = self.gap_score(risk_pre, risk_know)
        u_ans = self._eu(risk_pre) if risk_pre is not None else 1.0
        tr.eu_retrieve = self.eu_retrieve(u_ans, risk_help, tr.gain, tr.harm)
        u_ret = tr.eu_retrieve if tr.eu_retrieve is not None else float("-inf")
        if u_ans >= max(u_ret, 0.0):
            return Decision()
        if u_ret >= 0.0:
            return Decision(Action.RETRIEVE, reason="eu-retrieve")
        return Decision(Action.ABSTAIN, reason="eu-abstain")

    def eu_retrieve(self, u_ans: float, p_help: float | None, p_gain: float | None,
                    p_harm: float | None) -> float | None:
        """Utility of retrieving, known at prefill (None: no head to estimate it)."""
        cfg = self.cfg
        sig = getattr(cfg, "eu_retrieve_signal", "gain")
        if sig == "gain" and p_gain is not None:
            return u_ans + (1.0 + cfg.eu_lambda) * (p_gain - (p_harm or 0.0)) - cfg.eu_cost
        if sig == "option" and p_help is not None and getattr(cfg, "eu_option_table", None):
            return option_value(cfg.eu_option_table, p_help) - cfg.eu_cost
        if p_help is not None:
            return self._eu(p_help) - cfg.eu_cost
        return None

    def _retry_or_abstain(self, tr: RequestTracker, drop: int, reason: str) -> Decision:
        """The answer with evidence is still too risky: try the next-ranked evidence while
        the retrieval budget allows, abstain after the last attempt."""
        cfg = self.cfg
        used = max(tr.retrievals, int(tr.retrieved))  # evidence in context = at least one attempt used
        if cfg.retrieve_enabled and used < getattr(cfg, "max_retrievals", 1):
            return Decision(Action.RETRIEVE, drop, reason=f"retry:{reason}")
        return Decision(Action.ABSTAIN, reason=reason)

    def _rollback_or(self, tr, n_out, span, drop, reason, fallback: Decision) -> Decision:
        ban_index = n_out - drop
        ban_token = tr.pending_tokens[span]
        if tr.rollbacks < self.cfg.max_rollbacks and len(tr.bans.get(ban_index, ())) < self.cfg.max_bans_per_position:
            return Decision(Action.ROLLBACK, drop, ban_index, ban_token, reason)
        return fallback

    def _retrieve_drop(self, tr: RequestTracker, span_drop: int) -> int:
        """Tokens a retrieval takes back: the whole answer while none of it was released
        (retrieve_rewind="answer"), else the risky span."""
        if getattr(self.cfg, "retrieve_rewind", "answer") == "answer" and tr.released == 0:
            return len(tr.pending_tokens)
        return span_drop

    def _span_start(self, tr: RequestTracker) -> int:
        tau_low = self.cfg.low_ratio * self.tau_post
        s = len(tr.pending_tokens) - 1
        while s > 0:
            r = tr.pending_risks[s - 1]
            if r is None or r <= tau_low:
                break
            s -= 1
        return s

    # ----------------------------------------------------------------- mutate
    def _drop_pending(self, tr: RequestTracker, drop: int) -> None:
        if drop:
            del tr.pending_tokens[-drop:]
            del tr.pending_risks[-drop:]

    def apply_rollback(self, tr: RequestTracker, d: Decision) -> None:
        self._drop_pending(tr, d.drop)
        # bans deeper than the rollback point belonged to a prefix that no longer exists
        for idx in [i for i in tr.bans if i > d.ban_index]:
            del tr.bans[idx]
        tr.bans.setdefault(d.ban_index, set()).add(int(d.ban_token))
        tr.rollbacks += 1
        tr.events.append({"type": "rollback", "at": d.ban_index, "drop": d.drop, "ban": int(d.ban_token), "reason": d.reason})

    def apply_retrieve_start(self, tr: RequestTracker, d: Decision, n_out_kept: int) -> None:
        """The request is paused for retrieval; the risky span is gone."""
        self._drop_pending(tr, d.drop)
        tr.bans = {i: b for i, b in tr.bans.items() if i < n_out_kept}
        tr.retrievals += 1
        # at: engine output position (evidence turns included); pos: client-text position
        tr.events.append({"type": "retrieve", "at": n_out_kept, "pos": len(tr.released_ids) + len(tr.pending_tokens),
                          "drop": d.drop, "reason": d.reason})

    def apply_retrieve_done(self, tr: RequestTracker, n_inserted: int, n_passages: int) -> None:
        tr.retrieved = True
        tr.inserted += n_inserted
        tr.expect_pre = True
        tr.events.append({"type": "insert", "tokens": n_inserted, "passages": n_passages})

    def apply_abstain(self, tr: RequestTracker, reason: str) -> None:
        tr.pending_tokens.clear()
        tr.pending_risks.clear()
        tr.abstained = True
        tr.events.append({"type": "abstain", "reason": reason})

    def push(self, tr: RequestTracker, tokens: list[int]) -> None:
        for t in tokens:
            tr.pending_tokens.append(int(t))
            tr.pending_risks.append(None)
            if tr.lf_cooldown and int(t) in self.boundary:
                tr.lf_cooldown = False

    def release(self, tr: RequestTracker, finished: bool) -> list[int]:
        """Tokens that may now be shown to the client: older than the commit horizon, or
        (release=sentence) every finished sentence plus whatever exceeds lf_max_hold."""
        P = tr.pending_tokens
        if finished:
            n = len(P)
        elif self.cfg.release == "sentence":
            n = next((i + 1 for i in range(len(P) - 1, -1, -1) if P[i] in self.boundary), 0)
            n = max(n, len(P) - self.cfg.lf_max_hold)
        else:
            n = max(0, len(P) - self.cfg.horizon)
        out = tr.pending_tokens[:n]
        del tr.pending_tokens[:n]
        del tr.pending_risks[:n]
        tr.released += n
        tr.released_ids.extend(out)
        return out

    @staticmethod
    def bans_for(tr: RequestTracker, n_out: int) -> set[int] | None:
        return tr.bans.get(n_out)

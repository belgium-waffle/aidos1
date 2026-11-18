import pytest

from aidos.engine.config import RuntimeConfig
from aidos.engine.policy import Action, RequestTracker, AidosPolicy


def make(policy="rollback", tau_post=0.5, tau_pre=0.5, **kw):
    cfg = RuntimeConfig(head_dir="unused", policy=policy, **kw)
    return AidosPolicy(cfg, tau_post, tau_pre), RequestTracker()


def feed(pol, tr, tokens_and_risks):
    """Simulate steps: each item = (risk for previous token, token sampled this step)."""
    n_out = 0
    decisions = []
    for risk, tok in tokens_and_risks:
        d = pol.decide(tr, n_out, risk, None)
        decisions.append(d)
        if d.action is Action.NONE:
            pol.push(tr, [tok])
            n_out += 1
    return decisions, n_out


def test_horizon_release():
    pol, tr = make(policy="observe", horizon=3)
    pol.push(tr, [1, 2, 3, 4, 5])
    assert pol.release(tr, finished=False) == [1, 2]
    assert tr.pending_tokens == [3, 4, 5]
    assert pol.release(tr, finished=True) == [3, 4, 5]
    assert tr.released == 5


def test_observe_never_intervenes():
    pol, tr = make(policy="observe")
    decisions, n = feed(pol, tr, [(None, 10), (0.9, 11), (0.99, 12)])
    assert all(d.action is Action.NONE for d in decisions)
    assert n == 3
    assert tr.trace == [(0, 0.9), (1, 0.99)]


def test_rollback_span_and_ban():
    pol, tr = make(horizon=8, low_ratio=0.8)  # tau_low = 0.4
    # tokens 10 (risk .1), 11 (.45 > tau_low), 12 (.6 > tau) -> span starts at token 11
    pol.push(tr, [10])
    assert pol.decide(tr, 1, None, None).action is Action.NONE  # risk for token 10 unknown here
    tr.pending_risks[-1] = 0.1
    pol.push(tr, [11])
    assert pol.decide(tr, 2, 0.45, None).action is Action.NONE
    pol.push(tr, [12])
    d = pol.decide(tr, 3, 0.6, None)
    assert d.action is Action.ROLLBACK
    assert d.drop == 2 and d.ban_index == 1 and d.ban_token == 11
    pol.apply_rollback(tr, d)
    assert tr.pending_tokens == [10]
    assert tr.bans == {1: {11}}
    assert pol.bans_for(tr, 1) == {11}


def test_rollback_clears_deeper_bans():
    pol, tr = make()
    tr.bans = {3: {7}, 5: {9}}
    pol.push(tr, [1, 2, 3])
    tr.pending_risks[:] = [0.0, 0.0, None]
    d = pol.decide(tr, 3, 0.9, None)
    assert d.ban_index == 2
    pol.apply_rollback(tr, d)
    assert 3 not in tr.bans and 5 not in tr.bans and tr.bans[2] == {3}


def test_budget_exhaustion_continue_vs_abstain():
    pol, tr = make(max_rollbacks=1)
    tr.rollbacks = 1
    pol.push(tr, [5])
    assert pol.decide(tr, 1, 0.9, None).action is Action.NONE
    pol2, tr2 = make(policy="rollback+abstain", max_rollbacks=1)
    tr2.rollbacks = 1
    pol2.push(tr2, [5])
    assert pol2.decide(tr2, 1, 0.9, None).action is Action.ABSTAIN


def test_max_bans_per_position():
    pol, tr = make(max_bans_per_position=2)
    pol.push(tr, [5])
    tr.bans = {0: {1, 2}}
    d = pol.decide(tr, 1, 0.9, None)
    assert d.action is Action.NONE and d.reason == "budget"


def test_pre_abstain():
    pol, tr = make(policy="abstain", tau_pre=0.3)
    d = pol.decide(tr, 0, None, 0.31)
    assert d.action is Action.ABSTAIN and d.reason == "pre"
    pol.apply_abstain(tr, d.reason)
    assert tr.abstained and tr.pre_risk == 0.31


def test_pre_ignored_without_abstain_policy():
    pol, tr = make(policy="rollback", tau_pre=0.3)
    assert pol.decide(tr, 0, None, 0.99).action is Action.NONE


def test_forced_rollback_schedule():
    pol, tr = make(tau_post=float("inf"), force_rollback_every=2, max_rollbacks=100, max_bans_per_position=100)
    actions = []
    n_out = 0
    for step in range(6):
        d = pol.decide(tr, n_out, 0.1 if n_out else None, None)
        actions.append(d.action)
        if d.action is Action.ROLLBACK:
            assert d.drop == 1
            pol.apply_rollback(tr, d)
            n_out -= d.drop
        else:
            pol.push(tr, [step])
            n_out += 1
    assert actions.count(Action.ROLLBACK) >= 2


def test_invalid_config():
    with pytest.raises(ValueError):
        RuntimeConfig(head_dir="x", policy="nope")
    with pytest.raises(ValueError):
        RuntimeConfig(head_dir="x", horizon=0)
    with pytest.raises(ValueError):
        RuntimeConfig(head_dir="x", rollback_mode="teleport")
    with pytest.raises(ValueError):  # retrieval policies need an index
        RuntimeConfig(head_dir="x", policy="route")
    with pytest.raises(ValueError):
        RuntimeConfig(head_dir="x", gap_signal="vibes")


# ------------------------------------------------------------------ error-type routing
def route(policy="route", tau_post=0.5, tau_pre=0.5, tau_gap=0.6, **kw):
    kw.setdefault("retriever", "idx" if policy in ("route", "retrieve", "retrieve+abstain") else None)
    kw.setdefault("max_retrievals", 1)  # single-attempt semantics; retries: test_retry_* below
    cfg = RuntimeConfig(head_dir="unused", policy=policy, drift_ratio=0.5, **kw)
    return AidosPolicy(cfg, tau_post, tau_pre, tau_gap), RequestTracker()


def test_route_knowledge_gap_retrieves_at_prefill():
    pol, tr = route()
    d = pol.decide(tr, 0, None, 0.7)  # gap 0.7 > tau_gap 0.6
    assert d.action is Action.RETRIEVE and d.reason == "gap" and d.drop == 0
    pol2, tr2 = route("route-noretrieve")
    assert pol2.decide(tr2, 0, None, 0.7).action is Action.ABSTAIN


def test_route_drift_rolls_back_then_retrieves_when_budget_spent():
    pol, tr = route(max_rollbacks=1)
    assert pol.decide(tr, 0, None, 0.1).action is Action.NONE  # gap 0.1 < 0.5 * 0.6 -> drift zone
    pol.push(tr, [7])
    d = pol.decide(tr, 1, 0.9, None)
    assert d.action is Action.ROLLBACK and d.reason == "drift"
    pol.apply_rollback(tr, d)
    pol.push(tr, [8])
    d = pol.decide(tr, 1, 0.9, None)
    assert d.action is Action.RETRIEVE and d.reason == "drift-budget" and d.drop == 1


def test_route_borderline_post_trigger_retrieves_instead_of_resampling():
    pol, tr = route(retrieve_rewind="span")
    pol.decide(tr, 0, None, 0.4)  # 0.3 <= gap 0.4 <= 0.6: answer, but not "drift"
    pol.push(tr, [7, 8])
    tr.pending_risks[:] = [0.0, None]
    d = pol.decide(tr, 2, 0.9, None)
    assert d.action is Action.RETRIEVE and d.reason == "post-gap" and d.drop == 1  # the risky span only


def test_retrieval_rewinds_the_whole_unreleased_answer():
    pol, tr = route("retrieve+abstain")  # default retrieve_rewind="answer"
    pol.decide(tr, 0, None, 0.1)
    pol.push(tr, [7, 8, 9])
    tr.pending_risks[:] = [0.0, 0.0, None]
    d = pol.decide(tr, 3, 0.9, None)
    assert d.action is Action.RETRIEVE and d.drop == 3  # answer afresh from prompt + evidence
    pol.apply_retrieve_start(tr, d, n_out_kept=0)
    assert tr.pending_tokens == []
    # once tokens reached the client they cannot be taken back: the risky span only
    pol2, tr2 = route("retrieve+abstain", horizon=2)
    pol2.decide(tr2, 0, None, 0.1)
    pol2.push(tr2, [7, 8, 9])
    pol2.release(tr2, finished=False)  # releases 7
    tr2.pending_risks[:] = [0.0, None]
    d2 = pol2.decide(tr2, 3, 0.9, None)
    assert tr2.released == 1 and d2.drop == 1
    # forced retrievals (engine tests) follow the same rule
    pol3, tr3 = route("retrieve", force_retrieve_at=2)
    pol3.decide(tr3, 0, None, 0.1)
    pol3.push(tr3, [7, 8])
    assert pol3.decide(tr3, 2, 0.1, None).drop == 2
    pol4, tr4 = route("retrieve", force_retrieve_at=2, retrieve_rewind="span")
    pol4.decide(tr4, 0, None, 0.1)
    pol4.push(tr4, [7, 8])
    assert pol4.decide(tr4, 2, 0.1, None).drop == 0
    with pytest.raises(ValueError):
        RuntimeConfig(head_dir="x", retrieve_rewind="half")


def test_route_after_retrieval_abstains_and_checks_pre_again():
    pol, tr = route()
    d = pol.decide(tr, 0, None, 0.9)
    pol.apply_retrieve_start(tr, d, n_out_kept=0)
    pol.apply_retrieve_done(tr, n_inserted=120, n_passages=3)
    # the first scored row after insertion is a second pre decision
    d = pol.decide(tr, 120, None, 0.2)
    assert d.action is Action.NONE and tr.pre_risk_after == 0.2 and tr.pre_risk == 0.9
    pol.push(tr, [5])
    d = pol.decide(tr, 121, 0.9, None)
    assert d.action is Action.ABSTAIN and d.reason == "post-after-retrieval"
    pol2, tr2 = route()
    pol2.decide(tr2, 0, None, 0.9)
    tr2.retrieved, tr2.expect_pre = True, True
    assert pol2.decide(tr2, 100, None, 0.8).reason == "pre-after-retrieval"


def test_post_retrieval_thresholds_are_separate():
    # closed-book taus 0.5; after evidence: pre 0.85, post 0.95
    pol, tr = route(tau_pre_rag=0.85, tau_post_rag=0.95)
    pol.decide(tr, 0, None, 0.9)
    tr.retrieved, tr.expect_pre = True, True
    assert pol.decide(tr, 100, None, 0.8).action is Action.NONE  # 0.8 < 0.85
    pol.push(tr, [5])
    assert pol.decide(tr, 101, 0.9, None).action is Action.NONE  # 0.9 < 0.95
    pol.push(tr, [6])
    assert pol.decide(tr, 102, 0.97, None).reason == "post-after-retrieval"
    # before retrieval the closed-book taus still apply
    pol2, tr2 = route(tau_pre_rag=0.85, tau_post_rag=0.95)
    assert pol2.decide(tr2, 0, None, 0.7).action is Action.RETRIEVE  # gap 0.7 > 0.6


def test_gap_signal_know_head():
    pol, tr = route(gap_signal="know")
    d = pol.decide(tr, 0, None, 0.1, risk_know=0.2)  # pre says fine, know says gap 0.8
    assert d.action is Action.RETRIEVE and tr.gap == pytest.approx(0.8) and tr.know == 0.2


def test_retrieve_policy_retrieves_once_then_continues():
    pol, tr = route("retrieve")
    pol.decide(tr, 0, None, 0.1)
    pol.push(tr, [3])
    d = pol.decide(tr, 1, 0.9, None)
    assert d.action is Action.RETRIEVE and d.reason == "post"
    pol.apply_retrieve_start(tr, d, n_out_kept=0)
    pol.apply_retrieve_done(tr, 50, 3)
    pol.decide(tr, 50, None, 0.1)
    pol.push(tr, [4])
    assert pol.decide(tr, 51, 0.9, None).action is Action.NONE  # no abstain in plain retrieve
    pol2, tr2 = route("retrieve+abstain")
    tr2.retrieved = True
    pol2.push(tr2, [4])
    assert pol2.decide(tr2, 5, 0.9, None).action is Action.ABSTAIN


def test_released_ids_are_recorded():
    pol, tr = make(policy="observe", horizon=1)
    pol.push(tr, [1, 2, 3])
    pol.release(tr, finished=False)
    pol.release(tr, finished=True)
    assert tr.released_ids == [1, 2, 3]


# --------------------------------------------------------- evidence heads / Mondrian / EU
def test_after_insertion_the_evidence_trained_heads_decide():
    pol, tr = route("retrieve+abstain", tau_pre_rag=0.5, tau_post_rag=0.5)
    pol.decide(tr, 0, None, 0.9)  # gap -> retrieve
    tr.retrieved, tr.expect_pre = True, True
    # closed-book pre says 0.9 (abstain), the evidence-trained pre_rag says 0.2: answer
    assert pol.decide(tr, 100, None, 0.9, risk_pre_rag=0.2).action is Action.NONE
    assert tr.pre_risk_after == 0.2
    pol.push(tr, [5])
    assert pol.decide(tr, 101, 0.9, None, risk_post_rag=0.1).action is Action.NONE
    pol.push(tr, [6])
    assert pol.decide(tr, 102, 0.1, None, risk_post_rag=0.9).reason == "post-after-retrieval"
    # rag_heads=False: the closed-book heads as before
    pol2, tr2 = route("retrieve+abstain", tau_pre_rag=0.5, rag_heads=False)
    pol2.decide(tr2, 0, None, 0.9)
    tr2.retrieved, tr2.expect_pre = True, True
    assert pol2.decide(tr2, 100, None, 0.9, risk_pre_rag=0.2).reason == "pre-after-retrieval"


def test_mondrian_post_tau_follows_the_pre_risk_group():
    m = {"edges": [0.3, 0.6], "taus": [0.4, 0.6, 0.9]}
    cfg = RuntimeConfig(head_dir="unused", policy="abstain", conformal="mondrian")
    pol = AidosPolicy(cfg, 0.5, 0.95, mondrian=m)
    for pre, tau in ((0.1, 0.4), (0.45, 0.6), (0.8, 0.9)):
        tr = RequestTracker()
        assert pol.decide(tr, 0, None, pre).action is Action.NONE and tr.tau_post == tau
        pol.push(tr, [3])
        assert pol.decide(tr, 1, tau - 0.01, None).action is Action.NONE
        pol.push(tr, [4])
        assert pol.decide(tr, 2, tau + 0.01, None).action is Action.ABSTAIN
    # marginal config ignores the groups even if they are loaded
    pol2 = AidosPolicy(RuntimeConfig(head_dir="unused", policy="abstain"), 0.5, 0.95, mondrian=m)
    tr = RequestTracker()
    pol2.decide(tr, 0, None, 0.1)
    assert tr.tau_post is None
    with pytest.raises(ValueError):
        RuntimeConfig(head_dir="x", conformal="bonferroni")


def eu(lam=1.0, cost=0.02, **kw):
    kw.setdefault("max_retrievals", 1)
    cfg = RuntimeConfig(head_dir="unused", policy="route-eu", retriever="idx", eu_lambda=lam, eu_cost=cost, **kw)
    return AidosPolicy(cfg, 0.5, 0.5), RequestTracker()


def test_route_eu_prefill_is_an_argmax_of_expected_utility():
    # lam=1: EU(answer) = 1 - 2 p, EU(retrieve) = 1 - 2 help - 0.02, EU(abstain) = 0
    cases = [((0.1, 0.3), Action.NONE, ""),             # 0.80 vs 0.38: answer
             ((0.3, 0.1), Action.RETRIEVE, "eu-retrieve"),  # 0.40 vs 0.78: retrieve
             ((0.8, 0.7), Action.ABSTAIN, "eu-abstain"),    # -0.6 vs -0.42 vs 0: abstain
             ((0.2, 0.2), Action.NONE, "")]                 # 0.60 vs 0.58: the retrieval cost tips it
    for (pre, help_), action, reason in cases:
        pol, tr = eu()
        d = pol.decide(tr, 0, None, pre, risk_help=help_)
        assert d.action is action and d.reason == reason, (pre, help_, d)
    # lam=4 penalizes wrong answers harder: the same question is abstained on
    pol, tr = eu(lam=4.0)
    assert pol.decide(tr, 0, None, 0.3, risk_help=0.3).action is Action.ABSTAIN
    # no help head loaded: never retrieves at prefill, answers or abstains
    pol, tr = eu()
    assert pol.decide(tr, 0, None, 0.3).action is Action.NONE and tr.eu_retrieve is None


def test_route_eu_while_answering_and_after_evidence():
    pol, tr = eu(eu_post_platt=[1.0, 0.0])  # identity calibration
    pol.decide(tr, 0, None, 0.1, risk_help=0.2)  # answer; EU(retrieve) = 0.58
    pol.push(tr, [7])
    assert pol.decide(tr, 1, 0.15, None).action is Action.NONE  # EU 0.70 >= 0.58
    pol.push(tr, [8])
    d = pol.decide(tr, 2, 0.3, None)  # EU 0.40 < 0.58: retrieve, whole unreleased answer back
    assert d.action is Action.RETRIEVE and d.reason == "eu-post" and d.drop == 2
    pol.apply_retrieve_start(tr, d, n_out_kept=0)
    pol.apply_retrieve_done(tr, 50, 3)
    assert pol.decide(tr, 50, None, 0.9, risk_pre_rag=0.3).action is Action.NONE  # EU 0.4 >= 0
    pol.push(tr, [9])
    assert pol.decide(tr, 51, 0.1, None, risk_post_rag=0.6).reason == "eu-post-after-retrieval"
    # retrieval not worth it (help 0.6 -> EU -0.22): a risky answer is abstained on instead
    pol, tr = eu()
    pol.decide(tr, 0, None, 0.1, risk_help=0.6)
    pol.push(tr, [7])
    assert pol.decide(tr, 1, 0.7, None).reason == "eu-post"  # EU -0.4 < 0
    # calibration map: a token probability of 0.7 that the val data says means P(wrong)=0.25
    pol, tr = eu(eu_post_platt=[1.0, -1.9459])
    pol.decide(tr, 0, None, 0.1, risk_help=0.6)
    pol.push(tr, [7])
    assert pol.decide(tr, 1, 0.7, None).action is Action.NONE  # EU 0.5
    assert pol._answer_prob(0.7, [1.0, -1.9459]) == pytest.approx(0.25, abs=1e-3)


# ------------------------------------------------------------- second attempt / gain heads
def _retrieved(pol, tr, pre=0.9):
    """Prefill -> gap retrieval -> evidence inserted (first attempt)."""
    d = pol.decide(tr, 0, None, pre)
    assert d.action is Action.RETRIEVE
    pol.apply_retrieve_start(tr, d, n_out_kept=0)
    pol.apply_retrieve_done(tr, n_inserted=100, n_passages=3)


def test_retry_replaces_the_first_abstain_after_retrieval():
    for policy in ("route", "retrieve+abstain"):
        # risky right after the insertion: retry (nothing generated yet, drop 0), then abstain
        pol, tr = route(policy, max_retrievals=2)
        _retrieved(pol, tr)
        d = pol.decide(tr, 100, None, 0.8)
        assert d.action is Action.RETRIEVE and d.reason == "retry:pre-after-retrieval" and d.drop == 0
        pol.apply_retrieve_start(tr, d, n_out_kept=0)
        pol.apply_retrieve_done(tr, n_inserted=90, n_passages=3)
        assert tr.retrievals == 2 and tr.inserted == 190
        assert pol.decide(tr, 190, None, 0.8).reason == "pre-after-retrieval"  # budget spent
        # risky while answering with evidence: the whole unreleased evidence answer is taken back
        pol, tr = route(policy, max_retrievals=2)
        _retrieved(pol, tr)
        assert pol.decide(tr, 100, None, 0.1).action is Action.NONE
        pol.push(tr, [5, 6])
        tr.pending_risks[:] = [0.1, None]
        d = pol.decide(tr, 102, 0.9, None)
        assert d.action is Action.RETRIEVE and d.reason == "retry:post-after-retrieval" and d.drop == 2


def test_retry_needs_a_retriever_and_budget():
    pol, tr = route("route-noretrieve", max_retrievals=2)
    tr.retrieved, tr.expect_pre = True, True  # (cannot happen without a retriever; still abstains)
    assert pol.decide(tr, 10, None, 0.9).action is Action.ABSTAIN
    pol, tr = route("retrieve+abstain", max_retrievals=3)
    tr.retrievals, tr.retrieved, tr.expect_pre = 3, True, True
    assert pol.decide(tr, 10, None, 0.9).action is Action.ABSTAIN  # 3 of 3 used
    with pytest.raises(ValueError):
        RuntimeConfig(head_dir="x", max_retrievals=0)


def test_forced_retry_for_the_engine_test():
    pol, tr = route("retrieve", max_retrievals=2, force_retry=True, tau_gap=-1.0)
    _retrieved(pol, tr)
    d = pol.decide(tr, 100, None, 0.0)
    assert d.action is Action.RETRIEVE and d.reason == "forced-retry" and d.drop == 0
    pol.apply_retrieve_start(tr, d, 0)
    pol.apply_retrieve_done(tr, 90, 3)
    assert pol.decide(tr, 190, None, 0.0).action is Action.NONE  # budget spent: answer


def test_route_eu_retries_before_abstaining():
    pol, tr = eu(max_retrievals=2)
    assert pol.decide(tr, 0, None, 0.6, risk_help=0.1).action is Action.RETRIEVE
    tr.retrievals = 1
    pol.apply_retrieve_done(tr, 50, 3)
    d = pol.decide(tr, 50, None, 0.9, risk_pre_rag=0.7)  # EU(answer with evidence) = -0.4
    assert d.action is Action.RETRIEVE and d.reason == "retry:eu-pre-after-retrieval"
    tr.retrievals = 2
    pol.apply_retrieve_done(tr, 40, 3)
    assert pol.decide(tr, 90, None, 0.9, risk_pre_rag=0.7).reason == "eu-pre-after-retrieval"
    # while answering with evidence
    pol, tr = eu(max_retrievals=2)
    pol.decide(tr, 0, None, 0.6, risk_help=0.1)
    tr.retrievals = 1
    pol.apply_retrieve_done(tr, 50, 3)
    pol.decide(tr, 50, None, None, risk_pre_rag=0.1)
    pol.push(tr, [9])
    d = pol.decide(tr, 51, 0.1, None, risk_post_rag=0.8)
    assert d.action is Action.RETRIEVE and d.reason == "retry:eu-post-after-retrieval" and d.drop == 1


def test_route_eu_values_retrieval_by_the_flip_heads():
    # lam=1, cost 0.02: EU(answer) = 1 - 2 pre; EU(retrieve) = EU(answer) + 2 (gain - harm) - 0.02
    pol, tr = eu(eu_retrieve_signal="gain")
    d = pol.decide(tr, 0, None, 0.4, risk_help=0.9, risk_gain=0.3, risk_harm=0.05)
    assert tr.gain == 0.3 and tr.harm == 0.05
    assert tr.eu_retrieve == pytest.approx(0.2 + 2 * 0.25 - 0.02) and d.action is Action.RETRIEVE
    # retrieval rarely flips this answer: answer, although the help head alone would retrieve
    pol, tr = eu(eu_retrieve_signal="gain")
    d = pol.decide(tr, 0, None, 0.4, risk_help=0.05, risk_gain=0.02, risk_harm=0.02)
    assert d.action is Action.NONE and tr.eu_retrieve == pytest.approx(0.2 - 0.02)
    pol, tr = eu(eu_retrieve_signal="help")
    assert pol.decide(tr, 0, None, 0.4, risk_help=0.05, risk_gain=0.02, risk_harm=0.02).action is Action.RETRIEVE
    # gain heads missing: falls back to help
    pol, tr = eu(eu_retrieve_signal="gain")
    pol.decide(tr, 0, None, 0.4, risk_help=0.05)
    assert tr.eu_retrieve == pytest.approx(1 - 2 * 0.05 - 0.02)
    # option: a risky question (help 0.7: myopic EU(retrieve) < 0, so abstain) is still worth
    # trying when the post-retrieval checks make the retrieval branch's value positive
    pol, tr = eu(eu_retrieve_signal="help")
    assert pol.decide(tr, 0, None, 0.9, risk_help=0.7).action is Action.ABSTAIN
    pol, tr = eu(eu_retrieve_signal="option", eu_option_table=[[0.2, 0.8], [0.7, 0.1]])
    d = pol.decide(tr, 0, None, 0.9, risk_help=0.7)
    assert d.action is Action.RETRIEVE and tr.eu_retrieve == pytest.approx(0.2 - 0.02)
    with pytest.raises(ValueError):
        RuntimeConfig(head_dir="x", eu_retrieve_signal="vibes")

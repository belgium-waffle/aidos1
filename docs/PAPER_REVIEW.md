# Tripwire: soundness review before submission (2026-10-28)

This is a reviewer-style audit of every claim we intend to make. The source is the existing outputs only; no new runs were made.
- All numbers are read from `runs/<run>/policy/policy.json` (val-selected, test split), `bench/summary.md`, `latency/live.json`, `v7/report.json` and `lfgen/table.md` for the five final runs:
  - `v5_qwen2.5_7b`
  - `v5_llama3.1_8b`
  - `v5_mistral_7b`
  - `v4_qwen2.5_32b`
  - `v6_llama3.3_70b`
- In-domain test: 3166–3176 questions per model (TriviaQA + PopQA).
- OOD: 6992–6995 questions (NQ, HotpotQA, 2Wiki, SciQ).

Verdicts:
- **SOUND**: supported as stated.
- **REWORD**: true only in a narrower form.
- **DROP**: not supported.
- **OPEN**: needs evidence we do not have yet.

---

## 1. Claims and verdicts

| # | Claim | Evidence | Verdict | Wording to use |
|---|---|---|---|---|
| C1 | Tripwire beats published adaptive-retrieval baselines | λ=1 test utility, route-eu vs the best "+abstain" baseline: Qwen-7B 0.392 vs 0.213, Llama-8B 0.434 vs 0.336, Mistral 0.390 vs 0.278, Qwen-32B 0.504 vs 0.383, Llama-70B 0.545 vs 0.475 (+0.07 to +0.18). Route-eu has **higher accuracy than every +abstain baseline on all 5 models**, and lower or equal hallucination. | SOUND. Audit (2026-10-30): all 75 comparisons (5 models × 5 +abstain baselines × λ ∈ {1, 2, 4}) have paired-bootstrap CIs excluding 0, Holm p ≤ 0.0075. They also hold under LLM-judge labels on a 600-question subset (§6). | "At λ=1 Tripwire is more accurate than every baseline and hallucinates less, on 5 models from 7B to 70B." |
| C2 | "Half the hallucination of every baseline" | Against the *strongest* baseline (best utility) the ratio is 0.43–0.53 on all 5 models. But FLARE+abstain on Qwen-7B ties (0.069 vs 0.069, at acc 0.235), and SEP-RAG on Llama is 0.106 vs 0.065 (0.61×). | REWORD | "About half the hallucination rate of the strongest baseline (0.43–0.53×) at higher accuracy." Never say "every". |
| C3 | Baseline numbers are real, not just simulated | Every baseline was re-executed live in vLLM on ~3000 bench questions per model (`latency/live.json`). Live vs simulated agree within 0.005 in accuracy and hallucination at λ ∈ {1, 2, 4}, all 5 models. | SOUND | State it; it pre-empts the "you simulated the baselines" objection. |
| C4 | The engine reproduces the offline policy | route-eu engine vs simulation, λ=1: utility within 0.006 on all 5 models (e.g. 70B 0.553 vs 0.559). | SOUND | |
| C5 | The probe heads are what matters (vs token-level confidence) | Same router on token logprob instead of the heads: utility −0.090 to −0.207. On entropy: −0.089 to −0.205. All 5 models (table in section 2). | SOUND as a system ablation; REWORD the mechanism (std-metrics, 2026-10-30) | Main ablation of the paper. Raw closed-book detection is only modestly better, in-domain test AUROC:<br>• post head 0.888–0.925 vs the best output signal (token NLL / entropy / semantic entropy / SEP) 0.844–0.896, i.e. +0.016 to +0.046;<br>• pre head 0.866–0.908, on par with output signals (−0.022 on Llama-8B, up to +0.031 on 70B) but available before any draft.<br>OOD the probes are no better (pre 0.645–0.799, post 0.642–0.803 vs best output 0.732–0.807). Never say "probes detect errors much better than output confidence". Say "the probe *system* (decide before drafting, evidence-aware heads after retrieval, calibrated thresholds) is what matters". Open: a split ablation, probes closed-book + output signals after retrieval and vice versa, to locate the 0.09–0.21. |
| C6 | Evidence-trained heads after retrieval matter | Closed-book heads after retrieval cost −0.013 to −0.071, all 5 models. | SOUND | |
| C7 | The expected-utility (EU) rule beats a threshold policy | route-eu vs retrieve+abstain: −0.009, −0.001, 0.000, +0.002, +0.012. | DROP as a gain | "The EU rule matches tuned thresholds with one interpretable knob (λ) and trades accuracy for lower hallucination at equal utility." |
| C8 | Routing (retrieve only when needed) beats always-retrieve | vs rag+abstain (always retrieve, same heads): +0.010 to +0.019 utility on all 5 models, while retrieving for 69–72% instead of 100% of questions. | REWORD (audit done) | Positive on all 5 models, but Holm-significant only on Qwen-7B (+0.019, Holm p 0.022). Raw p: Llama 0.11, Mistral 0.053, 32B 0.012, 70B 0.054. Per dataset it is significant in none of the in-domain cells. Claim **equal utility with 28–31% fewer retrievals**, not a utility gain. The strong form of the routing claim is C9. |
| C9 | Routing pays off under a retrieval budget | Joint LTT, hallucination ≤ α **and** retrieval ≤ β, against 3-band baselines (fair: they can abstain without retrieving): Tripwire is more accurate in 29 of 30 (model, α, β) cells, by +0.01 to +0.11. At 70B it is certified at 12% retrieval with 0.586 accuracy. | SOUND, with caveats | Report the 3-band baselines only; the original +abstain baselines are a straw man under β. List the one loss (32B, α = 0.05, β = 0.2). |
| C10 | Certified hallucination budget (LTT) | D92: LTT violation rate ≤ δ in almost every cell. Exceptions: about 0.11 at α = 0.03 (Llama, Qwen-7B) and 0.145 at 70B (α = 0.05, β = 0.2). | REWORD | The guarantee is on the *population* risk. Our check uses a finite test half, so cells where the test risk sits on α can exceed δ through test noise alone. Say exactly this, and show the violation histogram, not a pass/fail claim. Guarantees hold under exchangeability only: none OOD (OOD hallucination 1.5–2× α). |
| C11 | Retrieval rescues knowledge gaps; rollback fixes drift ("error-type routing") | Rollback+abstain vs abstain: +0.004, −0.004, −0.008, −0.005, −0.007. route (with the drift/resample branch) vs retrieve+abstain: 0.000 to −0.002. Drift is about 4% of errors. | DROP | Rollback/resampling does not help short-form QA at any scale. Present it as a negative finding, and remove "rolls back the KV cache and resamples" from the title or abstract. |
| C12 | Exact in-engine evidence insertion and rollback | engine-test: 24/24 exact for every mode, including TP=2 at 70B. Parity cosine ≥ 0.9997. | SOUND (small n) | "Token-identical on all 24 test prompts per mode." Do not extrapolate to "provably exact". |
| C13 | Low overhead | Observe overhead per decode step: 2.2% / 1.8% (70B, batch 1 / 256), 2.9% (32B), 9–10% (7–8B). | SOUND, size-dependent | Always give it per model size; never "2–3%" across the board. |
| C14 | Latency competitive with baselines | c1 runs have only **100 requests**, so "p99" is the single slowest request. 70B p50: 446 ms vs 136–351 ms for the live baselines. | REWORD | Report p50/p90 for c1 and p99 only from the Poisson scenarios (600 requests). At 70B, Tripwire is slower at the median; the joint budget (C9) is the latency story. |
| C15 | Long-form: mid-answer retrieval beats FLARE and adds to RAG | 70B: +0.245 vs FLARE [0.214, 0.275]; RAG+lf vs RAG +0.019 [0.008, 0.032]; paired bootstrap, 242–266 people. Also replicated on 8B (D86). Second judge agrees on 90% of facts (κ 0.80). | SOUND, with caveats | Caveats to state: (i) the 32B run was judged by Qwen-32B, i.e. **self-judging**; quote the second-judge numbers for it. (ii) Retrieval and the judge both use Wikipedia, which favours retrieval methods (standard in FActScore work; say so). (iii) Fewer facts raise FActScore; report the length-penalised column next to it. |
| C16 | Detector transfers OOD | pre-head OOD AUROC 0.71–0.80, and OOD false-alarm rate 0.20–0.44. Recalibration with true labels recovers ≤ 0.012 utility (D95). | REWORD | "Transfers partially; OOD losses come from retrieval misses, not detector calibration." |
| C17 | OOD end-to-end advantage | λ=1 OOD acc − halluc: Tripwire is best on Qwen-7B, Mistral and 32B, and tied with rag+abstain (70B) or DRAGIN (Llama). Every method's OOD utility turns negative at λ ≥ 2. | REWORD (audit done) | Paired tests per OOD dataset, policy λ, Holm over 120 tests, route-eu vs the 5 published +abstain baselines across 5 models:<br>• NQ: significant in 19/25, positive in 25/25;<br>• HotpotQA: significant in 12/25, positive in 25/25;<br>• 2Wiki: significant in 12/25, positive in 16/25;<br>• SciQ: significant in 2/25, positive in 13/25.<br>So say "best or tied-best OOD at λ=1, significant on NQ, partly on multi-hop, **no advantage on SciQ**; no method, ours included, stays positive OOD at λ ≥ 2." |
| C18 | Steering along the detector direction reduces hallucination | Matched-abstention test on 2000 questions: steering is never better than head-threshold abstention and is worse on Qwen-7B and 32B. A 4-action router gains nothing. | DROP as a method | Keep it as a negative appendix: "the detector is readable but not a steering handle". |

## 2. Ablation table from the final pipeline (replaces the mixed-version table in the README)

The README's "Consolidated ablations" table mixes runs v2, v3, v4b and v5, i.e. different code versions. A reviewer will reject a table that mixes pipeline versions. This one is computed from the final `policy.json` of each model, with the same questions and validation-selected thresholds. Each cell is the test utility difference at λ=1 (utility = acc − halluc − 0.02·retrievals).

| Ablation (full → ablated) | Qwen-7B | Llama-8B | Mistral-7B | Qwen-32B | Llama-70B | Consistent? |
|---|---|---|---|---|---|---|
| probe heads → token logprob (same router) | +0.207 | +0.116 | +0.165 | +0.150 | +0.090 | yes, large |
| probe heads → top-k entropy | +0.205 | +0.094 | +0.141 | +0.148 | +0.089 | yes, large |
| evidence-trained heads → closed-book heads after retrieval | +0.071 | +0.033 | +0.031 | +0.048 | +0.013 | yes |
| retrieval → none (abstain only) | +0.169 | +0.135 | +0.092 | +0.174 | +0.071 | yes, large |
| routing → always retrieve (same heads) | +0.019 | +0.010 | +0.014 | +0.015 | +0.011 | yes, small (and −28–31% retrievals) |
| option-value signal → help head | +0.019 | +0.024 | +0.013 | +0.023 | +0.007 | yes, small |
| EU rule → tuned thresholds | −0.009 | −0.001 | 0.000 | +0.002 | +0.012 | **no effect** |
| rollback/resample → none (`rollback+abstain` vs `abstain`) | +0.004 | −0.004 | −0.008 | −0.005 | −0.007 | **no effect / harmful** |
| drift branch in `route` → none | 0.000 | −0.001 | +0.001 | −0.002 | −0.001 | **no effect** |
| second retrieval attempt → one | −0.005 | +0.004 | +0.002 | +0.002 | 0.000 | **no effect**, +25–30% retrievals |

Paired tests (audit, 2026-10-30; bootstrap CI + 10,000-flip permutation, Holm over all 50 ablation tests; `results/audit_all_models.md`). Number of models where the row is significant after Holm:
- heads → logprob: 5/5. heads → entropy: 5/5. Retrieval → none: 5/5.
- Evidence heads: 4/5 (70B raw p 0.052).
- Option value: 4/5 (70B raw p 0.09).
- Routing → always retrieve: 1/5 (Qwen-7B). All 5 are positive, raw p 0.0008–0.11 (see C8).
- EU rule, rollback, drift branch, second attempt: 0/5. Rollback is nominally *harmful* on Mistral (−0.009, raw p 0.019) and 70B (−0.007, raw p 0.033), but neither survives Holm.
- Detector seeds (3 per head): AUROC std ≤ 0.003 on every model.

## 3. Open risks a reviewer will raise

Ordered by severity. "Cost" means what closing the gap would take; nothing here has been run.

1. **Test-split reuse ("garden of forking paths").**
   - Thresholds are always selected on val. But ~100 design iterations (D1–D99) were *evaluated* on the same test split, so a reviewer can argue the test set has been overfitted through design choices.
   - What mitigates it: OOD datasets were never used for fitting, the live re-execution matches simulation, and the effects in rows 1–4 of section 2 are large.
   - What would close it: a sealed set of new TriviaQA/PopQA questions, never seen and evaluated once with everything frozen. Cost: a new GPU stage (frozen heads and policy, pre-reranked retrieval for the new questions, engine and live baselines), about 1 GPU-day across the 5 models.
   - Without it, the paper must state the protocol honestly in a limitations paragraph.
2. **Correctness labels come from alias substring matching only.**
   - What mitigates it: greedy answers are short (median 4 tokens) and closed-book abstention is under 0.1%, so the known failure modes (lists of candidates, hedges) are rare.
   - Even so, short-form QA has no LLM-judge validation. A reviewer will ask for agreement between alias matching and a judge on a sample (e.g. 300 answers × 5 methods × 2 models).
   - Cost: one GPU job with a cross-family judge.
3. **No paired significance tests or multiple-comparison correction for the short-form headline claims (C1, C8).**
   - Bench reports per-method CIs, and long-form has paired bootstrap. Short-form has neither paired tests against each baseline nor a correction across ~75 comparisons (5 models × 5 baselines × 3 λ).
   - Cost: CPU only, minutes, from existing per-question outcomes.
4. **Single training seed for the heads.**
   - CIs are over questions only; the head report has no seed spread (`probe.seeds` = one seed in these runs).
   - Linear probes vary little across seeds, but a reviewer may ask. Cost: CPU/GPU minutes per model (refit on stored features).
5. **Baseline naming and fidelity.** Each needs a precise description in the paper:
   - *Probing-RAG* uses **our** pre head as its gate, so it is closer to an ablation than an independent reimplementation. Call it "Probing-RAG-style (our probe as gate)".
   - *DRAGIN* is the attention-free RIND variant.
   - *SEP* is a probe we trained.
   - All baselines share our BM25 + cross-encoder retriever (fair, and say so).
   - "+abstain" and "+3band" are **our** extensions. Report the unmodified baselines too (they have 100% coverage, so their hallucination is 0.29–0.45).
6. **The strongest comparator is our own simple variant.** rag+abstain / retrieve+abstain are within 0.01–0.02 of route-eu. The paper must present this as the honest finding: the gain is from the trained heads, and routing pays off when retrieval is budgeted (C9).
7. **Mixed policy sources.**
   - D92/D94 (the guarantees) use `policy_d88_head` for 4 models and `policy` for 70B.
   - Engine and bench use `policy` everywhere.
   - Either recompute the guarantees from `policy` for all 5 models, or state per table which selection was used.
8. **Latency tails.** c1 has 100 requests (see C14).
9. **Long-form self-judging on the 32B run** (see C15).

## 4. What the paper can safely say (summary)

1. Linear probes on the residual stream, plugged into an exact in-engine router (≤ 3% overhead at ≥ 32B), give higher accuracy *and* about half the hallucination of the strongest adaptive-retrieval baseline at λ=1 on 5 models (7B–70B). The baselines were re-executed live and match within 0.005.
2. The gain comes from the heads: replacing them with token confidence costs 0.09–0.21 utility on every model. Evidence-trained heads after retrieval add 0.01–0.07.
3. Under a certified hallucination **and** retrieval budget, Tripwire is more accurate than fairly extended baselines in 29/30 settings. At 70B it certifies hallucination ≤ 10% while retrieving for only 12% of questions.
4. Mid-answer retrieval in long-form generation beats FLARE by +0.17 to +0.36 FActScore and adds +0.01 to +0.05 on top of RAG, on all 5 models and under two independent judges. On its own it does not beat retrieving up front.
5. Negative results that strengthen the paper:
   - rollback/resampling does not fix factoid hallucinations;
   - steering along the detector direction is no better than abstaining;
   - OOD losses are retrieval misses, not detector miscalibration.

## 6. Work on the open risks (2026-10-28; results 2026-10-30)

New outputs only go to new folders or files. Existing results are never overwritten: reruns move old output aside via `utils.fresh_dir`. The CLI now keeps each run's first `config.json` and appends every invocation to `config_history.jsonl`. Before this change, every CLI command rewrote `config.json`, so the copies in the 5 runs reflect their latest invocation; nothing reads them.

| Risk | What was done | Status |
|---|---|---|
| 1. Test-split reuse (stage A + C done; stage B queued) | **Sealed test set** (`pipeline/frozen.py`, `cache/sealed_*.sh`), one sealed run `sealed_<run>` per model:<br>• in domain: 2000 TriviaQA + 2000 PopQA questions no run has drawn (positions 8000–9999 of the same shuffled lists, and any qid a source run saw is dropped);<br>• OOD: 1000 each of NQ, HotpotQA and 2Wiki;<br>• the source run's heads and `policy.json` are copied and only applied: no fitting and no selection on these questions;<br>• check: the frozen scorer reproduces the stored predictions of all 7 heads on Qwen-7B within 1.8e-7 (`heads/frozen_verify.json`);<br>• SEP-RAG is excluded there, because its probe needs a train split.<br>Evaluated by the same `audit` stage. | Generation, features, frozen head scores and BM25 candidates are done for all 5 models: 6882 questions each, **0 qid overlap** with the source runs. Stage B (retrieval, evidence answers, baselines, audit, engine) is waiting for H200s: jobs 420410/1. |
| 2. Alias labels | **`judge-sf`**: a cross-family LLM judge (Mistral-Small-24B; Qwen2.5-32B for the Mistral run) re-labels every answer source on 600 test questions per model. Reports agreement, κ and every λ=1 policy under both labelings, plus route-eu − baseline under judge labels. | **done**, see results below |
| 3. Significance | **`audit`**: paired bootstrap CI + sign-flip permutation p (10,000) for route-eu vs every baseline at λ ∈ {1, 2, 4}, every ablation, and per dataset (in domain and OOD), with Holm correction per table. The re-simulation reproduces `policy.json` exactly (max deviation 0.0, all 5 models). | **done**, `results/audit_all_models.md` |
| 4. Seeds | Already in the data: the heads are fitted with `probe.seeds = [0, 1, 2]`. Example, Qwen-7B test AUROC: pre 0.8985 ± 0.0018, post 0.9240 ± 0.0005. The audit table reports this for every model. | done (reported by the audit) |
| 5. Baseline naming / unmodified baselines | The audit compares route-eu with the unmodified baselines too (`route-eu minus the unmodified baselines`). Naming is a writing task (§3 item 5). | done (data); text open |
| 7. Mixed policy sources | The audit recomputes D92 (LTT) and D94/D98 (joint budget) from `policy` for all 5 models into `paper_policy/` and `v7_policy/`. The `paper/` and `v7/` outputs are kept. | **done: identical.** Every LTT and joint-budget row is the same under both sources on all 5 models, because the route-eu parameters these stages read are the same in both selections. The mixed-source concern is void. |
| 9. Long-form self-judging | **`lf-judge2-full`**: the second judge on *every* test person (not 100), with paired bootstrap of lf-retrieve − FLARE, lf-retrieve − RAG and RAG+lf − RAG under both judges → `lfgen/judge2_full.json`. | **done**, see results below |
| D99 engine check | Certified budget configs run in the engine (70B). | **done**: the engine matches simulation in every config (acc within 0.007, halluc within 0.001, retrieval within 0.002) |

First audit result (Qwen-7B, test, Holm-corrected over all 30 baseline comparisons):
- route-eu beats every +abstain and unmodified baseline at λ ∈ {1, 2, 4}, all with adjusted p ≤ 0.0015. At λ=1 the gain is +0.18 to +0.24 utility.
- Ablations that hold: probe heads (+0.21), evidence heads (+0.07), retrieval (+0.17), routing vs always-retrieve (+0.019, Holm p 0.004) and option value (+0.019).
- Ablations that do not hold: EU rule (−0.010, p 0.29), rollback (p 0.69), drift branch (p 0.69) and the second attempt (p 0.25).
- Per dataset, the gain holds on both PopQA and TriviaQA. OOD it is significant on NQ and on most comparisons on HotpotQA and 2Wiki, but not on SciQ (1000 questions; no baseline differs significantly there except rag+abstain).
- Note for the λ=4 rows: several baselines' val-selected policy is "abstain on everything" (accuracy 0), which inflates the difference. Report λ=4 with that caveat.

### Results, all 5 models (2026-10-30)

**Audit** (`results/audit_all_models.md`, `runs/<run>/audit/`):
- *Headline.* route-eu beats every +abstain baseline, at every λ, on every model: 75/75 comparisons, Holm p ≤ 0.0075 (p = 1e-4 is the permutation floor). It also beats the unmodified baselines in all 75.
  - λ=1 gains: Qwen-7B +0.18 to +0.24, Llama-8B +0.10 to +0.15, Mistral +0.11 to +0.19, Qwen-32B +0.12 to +0.17, Llama-70B +0.07 to +0.13.
- *Ablations.* See §2.
- *Per in-domain dataset* (vs the published baselines):
  - PopQA: significant in 25/25.
  - TriviaQA: significant in 24/25; the exception is 70B vs SE-RAG (+0.030, Holm p 0.086).
  - vs rag+abstain: n.s. in 9/10 cells.
- *Per OOD dataset.* See C17. SciQ shows no advantage.

**Short-form judge** (`runs/<run>/judge_sf/table.md`; 600 test questions × 5 answer sources per model):
- Agreement between alias matching and the judge is 0.94–0.97, κ 0.87–0.92.
- Alias matching is slightly *conservative*: the judge's accuracy is +0.01 to +0.04 higher on the four Mistral-Small-judged models. On the Mistral run, judged by Qwen-32B, it is up to 0.03 lower.
- Under judge labels, route-eu − every +abstain baseline stays positive with a CI excluding 0 on all 5 models (25/25). Smallest: 70B vs probing-rag+abstain, +0.051 [+0.016, +0.087].
- **Risk 2 is closed:** the conclusions do not depend on the labeler.

**Long-form second judge on every test person** (`lfgen/judge2_full.json`; 277 people, 51k–68k facts per model):
- Overall agreement between Qwen-32B and Mistral-Small-24B is 0.90–0.93 per model, κ 0.79–0.86.
- Mistral-Small scores every arm 0.005–0.06 lower, but every paired difference below has the same sign under both judges.
- Paired results under **both** judges:
  - lf-retrieve − FLARE: +0.17 to +0.36 on all 5 models; all CIs exclude 0.
  - RAG+lf − RAG: +0.014 to +0.046 on all 5 models; all CIs exclude 0.
  - lf-retrieve − RAG: n.s. on 4/5; positive on Llama-8B (+0.031, both judges). Mid-answer retrieval on its own does **not** beat retrieving up front. Its value is beating FLARE and adding to RAG.
  - lf-resample − observe: n.s. under both judges on 4/5. On 70B it is +0.017 under judge 1 (p 0.034) but n.s. under judge 2. This is consistent with C11: resampling is not a method contribution.
- On the 32B run (the self-judging concern), the second judge gives the same conclusions: lf-retrieve − FLARE +0.278 [+0.244, +0.312]; RAG+lf − RAG +0.025 [+0.014, +0.037].
- **Risk 9 is closed.**

**D99** (`runs/v6_llama3.3_70b/v7/table.md`): five certified budget configs were run in the 70B engine, and simulation is confirmed live.
- Example, route-eu-cost0.5: sim acc 0.586, halluc 0.082, retrieval 0.115; engine acc 0.579, halluc 0.083 [0.073, 0.092], retrieval 0.113.

**Still open:**
- the sealed-set evaluation (stage B running: job 420410 for the four smaller models; 420411 for 70B waits on the memory QOS);
- the writing tasks in §3 item 5 and §5.

### Added 2026-10-30 (new outputs only)

| Gap a reviewer would raise | Stage | Output | Job |
|---|---|---|---|
| No standard QA metrics: EM / token F1; coverage and selective accuracy; risk–coverage along the λ sweep; AUPRC and AURC for every detector; ECE / Brier for the pre head | `std-metrics` (CPU, re-simulates the stored policy.json selections; `simulate` now records which answer was served in its trace, outcomes unchanged) | `runs/<run>/std_metrics/`, `results/std_metrics_all_models.md` | 423483 |
| No baseline independent of our probes | `text-router`: Adaptive-RAG-style RoBERTa-base classifier on the question text only, with the same gate + abstain structure as Probing-RAG and thresholds selected on val. It answers "why not just classify the question?" (which is also what a front-of-LLM decision model such as Jev can see) | `runs/<run>/text_router/`, `results/text_router_all_models.md` | 423481 |

### Partial results (2026-10-30, evening check)

**Sealed held-out set, stage B (frozen policies, 6882 fresh questions per model, test n ≈ 3880).** Done for Qwen-7B, Llama-8B, Mistral-7B (`runs/sealed_<run>/audit/table.md`); 32B is generating; 70B is queued (420411).
- Headline: route-eu beats every +abstain baseline at every λ on all three models: 36/36 comparisons, Holm p = 0.0012. λ=1 gains: Qwen-7B +0.18 to +0.24, Llama-8B +0.10 to +0.14, Mistral +0.14 to +0.19. These are the same ranges as the original test split, so the result was not a product of selecting policies on that split.
- Ablations reproduce the pattern:
  - probe heads → logprob/entropy: +0.10 to +0.20, significant on 3/3.
  - retrieval → none: significant on 3/3.
  - evidence heads: significant on 3/3.
  - option value: significant on 3/3.
  - EU rule and drift: n.s.
  - routing → always retrieve: Holm-significant only on Llama-8B (+0.019). On the original split only Qwen-7B was, so the C8 wording "equal utility with fewer retrievals" stands.
  - rollback → none: −0.010, Holm p = 0.02 on Mistral, so rollback slightly *hurts* there. Keep rollback out of the claims.
- Detector seeds on sealed: pre AUROC 0.868–0.899, post 0.889–0.924 (std ≤ 0.002), matching the original test split.
- Per-OOD caveat persists. On Qwen-7B, 2Wiki: route-eu vs FLARE+abstain −0.050 and vs Probing-RAG+abstain −0.051 (Holm p ≈ 0.05–0.06). HotpotQA vs Probing-RAG: n.s.

**Sealed 32B (job 420410 completed):**
- Headline: 12/12 comparisons, Holm p = 0.0012. λ=1: +0.11 to +0.16; λ=2: +0.16 to +0.20; λ=4: +0.16 to +0.24.
- Ablations:
  - probe heads → logprob +0.140, → entropy +0.136.
  - evidence heads +0.040.
  - retrieval → none +0.144.
  - routing → always retrieve +0.019 (Holm 0.001), significant here too.
  - option value +0.015.
  - EU rule: n.s.
  - drift → none −0.005 (Holm 0.017), so the drift branch slightly *hurts* on 32B, in the same way rollback did on Mistral. Keep both out of the claims.
- Detector seeds: pre 0.903, post 0.926.
- Per-OOD dataset: no significant losses; HotpotQA and NQ are wins or n.s.
- Sealed tally so far: 4 models, 48/48 headline comparisons significant. Routing → always retrieve is now significant on Llama-8B and 32B (2/4). 70B (420411) is running.

**Split ablation (job 423628, CPU, stage `split-ablation`):**
- A 2×2 of the threshold `route` policy: probe or output signal (logprob, entropy) *before* retrieval × probe or output signal *after* retrieval.
- Every cell is re-selected on val per λ, one attempt each.
- Paired tests isolate what each half of the probes is worth.
- Output: `runs/<run>/split_ablation/`, `results/split_ablation_all_models.md`.

**Text router (question only), done for Qwen-7B and Llama-8B; Mistral running.**

| Detector AUROC (test / OOD) | text router | pre head |
|---|---|---|
| Qwen-7B | 0.830 / 0.658 | 0.891 / 0.799 |
| Llama-8B | 0.803 / 0.606 | 0.866 / 0.743 |

- The pre head beats the question-only classifier by about 0.06 in domain and 0.14 OOD. So the probe reads something about the model, not just question difficulty. This is the cleanest support for C5.
- route-eu − text-router+abstain:
  - λ=1: +0.18 to +0.23 on test and +0.17 to +0.20 OOD.
  - λ=2: +0.21 to +0.31.
  - All Holm p < 0.001.
- Probing-RAG+abstain gated by our pre head also beats the text router by +0.05 to +0.16 at λ=1–2, so the gain is from the signal, not only from the policy.
- Exception at λ=4 OOD: route-eu − text router is −0.051 on Qwen-7B and +0.025 n.s. on Llama-8B. On Qwen-7B at λ=4 the val-selected text router abstains on everything (coverage 0, utility 0), and route-eu's OOD utility at λ=4 is below 0. This is the known λ=4 OOD weakness, not a detection win for the text router. Report it in the λ=4 caveat.


**Split ablation, all 5 models (job 423628, `results/split_ablation_all_models.md`).** lambda = 1, logprob variant; every cell is re-selected on val and retrieves at most once.

| Comparison | Utility diff | Holm-significant |
|---|---|---|
| Probes after retrieval, given probes before | +0.05 to +0.15 | 5/5 |
| Probes after retrieval, given output signal before | +0.09 to +0.18 | 5/5 |
| Probes before retrieval, given probes after | -0.01 to +0.03 | 1/5 (Qwen-7B only) |
| Probes before retrieval, given output signal after | +0.02 to +0.06 | 5/5 |
| Both halves | +0.09 to +0.21 | 5/5 |

The probe-vs-output gap therefore comes mostly from the **evidence-answer probes** (pre_rag / post_rag): judging whether retrieval fixed the answer. With those in place, the prefill probe adds no utility on 4/5 models. It mainly reduces retrievals: 0.75 vs 1.00 on Qwen-7B and 0.68 vs 1.00 on Qwen-32B; similar on the others.

Consequence for the claims: lead with the evidence-conditioned probes. Frame the prefill decision as the efficiency (fewer retrievals, a decision before any token) and latency story, not as the main source of utility. C5 and the pitch's "where the margin comes from" need this wording.

**Text router, all 5 models.**
- Pre-probe AUROC beats the question-only router on every model: test 0.87-0.91 vs 0.80-0.85; unseen datasets 0.65-0.80 vs 0.54-0.66.
- route-eu minus text-router+abstain at lambda = 1: test +0.09 to +0.23, unseen +0.09 to +0.32. All Holm p = 0.0006.

Repository renamed for the paper: **Aidos** (github.com/belgium-waffle/aidos, private). The package name stays `tripwire`.

## 5. Text to fix in the README (stale claims)

- The intro still sells "rolls back the KV cache, bans the bad branch and resamples" and error-type routing (C11). Rewrite it.
- The status line (2026-10-09, 32B v3 numbers) is stale.
- "Consolidated ablations" mixes code versions. Mark it historical and point to section 2 here.
- The D94 text "baselines certify nothing" is superseded by D98 (already marked in the README).

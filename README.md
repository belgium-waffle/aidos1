Aidos
=====

Deciding whether an LLM should answer, retrieve, or abstain, from its own hidden states.

Aidos puts small linear probes on the residual stream of
an open LLM. A probe scores the question at prefill, before any token is generated. If the
model retrieves, probes trained on evidence-conditioned answers judge whether the passage
actually helped. An expected-utility rule turns the calibrated scores into one of three
actions: answer, retrieve, or abstain. Everything runs inside vLLM.

Status: unpublished research. This repository holds the results and the review notes;
the implementation is kept private until publication. Please do not redistribute.


Key results
-----------

Five models (Qwen2.5-7B, Llama-3.1-8B, Mistral-7B, Qwen2.5-32B, Llama-3.3-70B), five published
adaptive-retrieval baselines (FLARE, DRAGIN, Probing-RAG, SEP-RAG, SE-RAG), each also given a
tuned abstain option. Same retriever, answers and tuning for every method; only the trigger
differs. Utility U = accuracy - lambda * hallucination - 0.02 * retrievals (higher is better;
an abstention is neither correct nor a hallucination).

1. Aidos has the highest utility on every model.

   Utility at lambda = 1, test split (~3,170 questions per model):

       Model           Aidos   Strongest baseline     Aidos - baseline,   Aidos - baseline,
                                                      test (5 baselines)  sealed set (4)
       Qwen2.5-7B      0.392   Probing-RAG  0.214     +0.18 to +0.24      +0.18 to +0.24
       Llama-3.1-8B    0.434   SE-RAG       0.335     +0.10 to +0.15      +0.10 to +0.14
       Mistral-7B      0.390   Probing-RAG  0.277     +0.11 to +0.19      +0.14 to +0.19
       Qwen2.5-32B     0.504   SE-RAG       0.383     +0.12 to +0.17      +0.11 to +0.16
       Llama-3.3-70B   0.545   Probing-RAG  0.475     +0.07 to +0.13      (running)

   - 75 / 75 comparisons significant on test (5 models x 5 baselines x lambda in {1, 2, 4};
     paired bootstrap, 10k sign-flip permutation, Holm p <= 0.0075).
   - 48 / 48 significant on a sealed held-out set (6,882 never-seen questions per model, all
     policies frozen beforehand; Holm p = 0.0012). The 70B sealed run is in progress.
   - Hallucination rate is 0.43-0.53x that of the strongest baseline, at higher accuracy.

2. The probes read the model, not the question.
   A RoBERTa router trained on the question text alone (Adaptive-RAG style) is clearly worse:

       pre-generation detection AUROC     question-only router   Aidos pre probe
       in domain (test)                   0.80 - 0.85            0.87 - 0.91
       unseen datasets                    0.54 - 0.66            0.65 - 0.80

   Aidos beats that router by +0.09 to +0.23 utility on test and +0.09 to +0.32 on unseen
   datasets (lambda = 1, all 5 models, Holm p < 0.001).

3. Most of the gain comes from probing the evidence answer.
   A 2x2 ablation swaps probes for token log-probabilities before and/or after retrieval
   (lambda = 1, all cells re-selected on validation):

       probes after retrieval, probes before kept        +0.05 to +0.15   (5/5 significant)
       probes before retrieval, probes after kept        -0.01 to +0.03   (1/5 significant)
       both halves swapped (the full ablation)           +0.09 to +0.21   (5/5 significant)

   Judging whether a retrieved passage actually fixed the answer is where the probes beat
   output confidence. The prefill probe mainly saves retrievals (25-32% fewer on the two Qwen
   models, at equal or slightly higher utility) and gives a decision before any token is generated.

4. It runs in a production engine at low cost.
   A custom vLLM V1 scheduler runs the probes and inserts evidence into the KV cache
   mid-request. Output is token-identical to re-prompting (24/24 test prompts per mode,
   including tensor parallelism at 70B). Probe overhead is 2-3% of decode time at 32B-70B
   (9-10% at 7-8B). Engine and offline simulation agree within 0.007 accuracy.

5. Supporting results.
   - Learn-then-Test guarantee (delta = 0.1) on hallucination, jointly with retrieval rate:
     at 70B, hallucination <= 10% and retrieval <= 12% at accuracy 0.586.
   - Standard QA metrics (Qwen-7B, lambda = 1): EM 0.795 / F1 0.862 on answered questions,
     coverage 0.54. Pre-probe calibration error (ECE) 0.02-0.03 in domain.
   - Long-form biographies (FActScore, two judges): +0.17 to +0.36 over FLARE.
   - Answer labels agree with an LLM judge 94-97% of the time (Cohen's kappa 0.87-0.92).
   - Probe AUROC varies by at most 0.003 across 3 seeds.


Limitations
-----------

- Raw detection is only modestly better than output signals: +0.02 to +0.05 AUROC in domain,
  and no better on unseen datasets (AUROC 0.64-0.80; pre-probe ECE rises to 0.09-0.18).
- Unseen datasets: significant wins in NQ 19/25, HotpotQA 12/25, 2Wiki 12/25 and SciQ 2/25
  comparisons.
- Against always-retrieve with the same probes, utility is equal or slightly better
  (+0.01 to +0.02) with 28-31% fewer retrievals; significant on 1/5 models (test) and 2/4
  (sealed).
- At lambda = 4 some tuned baselines abstain on everything, which inflates gains there.
- Median latency at 70B is 446 ms vs 136-351 ms for the baselines.
- KV-cache rollback and resampling, hidden-state steering and several extra decision rules
  gave no gain. They are kept in the code and reported as negative results.


What is new
-----------

Probing hidden states for correctness (P(IK), SAPLMA, semantic-entropy probes) and
probe-gated retrieval (Probing-RAG, SeaKR) already exist. To our knowledge, the new parts are:

- one decision over three actions (answer / retrieve / abstain) at prefill against an
  explicit utility, instead of a binary retrieve trigger;
- probes trained on evidence-conditioned answers, which judge whether retrieval helped
  (the largest single source of the gain, see result 3);
- an exact in-engine implementation (mid-request KV insertion in vLLM);
- distribution-free guarantees for adaptive RAG, jointly on hallucination and retrieval;
- a controlled comparison: shared retriever, abstain-augmented baselines, a probe-free
  question-only control, a sealed test set, and 5 models from 7B to 70B.


How it works
------------

    question --> prefill --> pre probe: P(wrong)
                                 |
            expected-utility rule (Platt-calibrated scores)
               /                 |                    \
          answer             retrieve                abstain
                                 |
             evidence inserted into the KV cache (in vLLM)
                                 |
             pre_rag / post_rag / help probes on the evidence answer
                         /                \
                     answer             abstain

- Probes: linear heads on z-scored residual activations, layer set chosen on validation,
  AdamW with weight decay and early stopping, Platt calibration, 3 seeds.
- Data: 16,000 TriviaQA + PopQA questions per model, split train / val / cal / test.
  NQ, HotpotQA, 2WikiMultihopQA and SciQ are held out and never fitted on.
- Retrieval: BM25 over DPR Wikipedia plus a cross-encoder reranker, shared by all methods.
- Selection: every threshold and choice is made on validation; test is scored once.


Contents
--------

    results/
        audit_all_models.md           headline tests, ablations, per-dataset tests
        sealed/                       the same on the sealed held-out set
        std_metrics_all_models.md     EM/F1, coverage, AURC, AUPRC, ECE, Brier
        text_router_all_models.md     question-only baseline
        split_ablation_all_models.md  before/after-retrieval probe ablation
        <run>/                        per-model tables, metrics and plots
                                      (v5_*, v4_qwen2.5_32b, v6_llama3.3_70b; v2/v3 and dev
                                      are earlier development runs)
    docs/
        PAPER_REVIEW.md               claims, verdicts, open risks and the evidence for each
        figures/                      summary plots

All numbers in this README come from the tables under results/. Every table reports paired
95% bootstrap intervals, permutation p-values and Holm-corrected p-values.


Open items
----------

- Sealed held-out evaluation for Llama-3.3-70B (running).
- Robustness on unseen datasets: mixed-domain probe training or an output-signal fallback.
- Paper draft.

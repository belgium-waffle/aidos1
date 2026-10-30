### test: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| tripwire_post | 0.888 [0.877, 0.899] | 0.122 [0.110, 0.134] | 0.429 [0.411, 0.450] |  | ~1-2% decode (in-engine) |
| tripwire_pre | 0.876 [0.862, 0.888] | 0.129 [0.117, 0.141] | 0.416 [0.396, 0.437] | 0.020 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_know | 0.875 [0.862, 0.887] | 0.128 [0.116, 0.140] | 0.417 [0.397, 0.438] | 0.013 | ~1-2% decode (in-engine, pre-answer) |
| p_true | 0.817 [0.802, 0.832] | 0.155 [0.141, 0.169] | 0.313 [0.294, 0.330] | 0.001 | +1 prefill |
| semantic_entropy_w | 0.813 [0.797, 0.829] | 0.182 [0.167, 0.198] | 0.385 [0.363, 0.405] | 0.001 | +N gen + NLI |
| semantic_entropy | 0.813 [0.797, 0.829] | 0.182 [0.167, 0.198] | 0.384 [0.363, 0.405] | 0.001 | +N gen + NLI |
| self_consistency | 0.809 [0.793, 0.824] | 0.183 [0.168, 0.199] | 0.377 [0.355, 0.397] | 0.001 | +N gen + NLI |
| entropy_max | 0.807 [0.790, 0.823] | 0.181 [0.164, 0.198] | 0.375 [0.355, 0.397] | 0.001 | none |
| entropy_mean | 0.800 [0.783, 0.818] | 0.183 [0.166, 0.200] | 0.368 [0.348, 0.388] | 0.001 | none |
| sep | 0.794 [0.775, 0.811] | 0.185 [0.168, 0.202] | 0.365 [0.346, 0.385] | 0.001 | ~free (probe, pre-answer) |
| neg_logprob_min | 0.788 [0.770, 0.805] | 0.188 [0.170, 0.204] | 0.358 [0.338, 0.379] | 0.001 | none |
| neg_logprob_mean | 0.786 [0.768, 0.803] | 0.189 [0.171, 0.206] | 0.355 [0.335, 0.375] | 0.001 | none |
| verbalized | 0.646 [0.631, 0.661] | 0.278 [0.261, 0.294] | 0.311 [0.294, 0.329] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.282

### ood: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| tripwire_post | 0.750 [0.738, 0.761] | 0.455 [0.440, 0.472] | 0.031 [0.015, 0.045] |  | ~1-2% decode (in-engine) |
| semantic_entropy_w | 0.734 [0.723, 0.744] | 0.496 [0.481, 0.510] | 0.017 [0.002, 0.032] | 0.005 | +N gen + NLI |
| semantic_entropy | 0.733 [0.722, 0.744] | 0.496 [0.481, 0.510] | 0.017 [0.002, 0.032] | 0.005 | +N gen + NLI |
| p_true | 0.733 [0.721, 0.744] | 0.467 [0.453, 0.484] | 0.014 [0.001, 0.026] | 0.004 | +1 prefill |
| entropy_mean | 0.732 [0.720, 0.743] | 0.479 [0.462, 0.495] | 0.021 [0.007, 0.035] | 0.010 | none |
| entropy_max | 0.730 [0.718, 0.741] | 0.483 [0.466, 0.499] | 0.025 [0.011, 0.039] | 0.001 | none |
| self_consistency | 0.730 [0.719, 0.740] | 0.497 [0.482, 0.512] | 0.015 [0.001, 0.030] | 0.003 | +N gen + NLI |
| tripwire_know | 0.722 [0.709, 0.734] | 0.478 [0.462, 0.494] | 0.011 [-0.004, 0.025] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_pre | 0.715 [0.702, 0.727] | 0.483 [0.467, 0.499] | 0.029 [0.015, 0.043] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| neg_logprob_mean | 0.713 [0.700, 0.724] | 0.489 [0.472, 0.505] | 0.013 [-0.001, 0.026] | 0.001 | none |
| neg_logprob_min | 0.707 [0.693, 0.719] | 0.493 [0.476, 0.509] | 0.016 [0.002, 0.030] | 0.001 | none |
| sep | 0.685 [0.672, 0.697] | 0.510 [0.493, 0.527] | -0.003 [-0.017, 0.010] | 0.001 | ~free (probe, pre-answer) |
| verbalized | 0.616 [0.606, 0.625] | 0.577 [0.564, 0.590] | 0.007 [-0.005, 0.019] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): -0.011

### error types (test, greedy)

| type | share | resample acc | best-of-N by risk | retrieval acc | any sample correct |
|---|---|---|---|---|---|
| correct | 0.650 | 0.970 | 0.968 | 0.934 | 0.999 |
| gap | 0.318 | 0.010 | 0.044 | 0.263 | 0.099 |
| drift | 0.032 | 0.337 | 0.631 | 0.583 | 1.000 |

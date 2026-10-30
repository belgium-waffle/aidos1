### test: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| tripwire_post | 0.925 [0.916, 0.933] | 0.212 [0.196, 0.228] | 0.299 [0.278, 0.321] |  | ~1-2% decode (in-engine) |
| tripwire_pre | 0.908 [0.897, 0.917] | 0.223 [0.206, 0.238] | 0.283 [0.263, 0.303] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_know | 0.905 [0.894, 0.915] | 0.224 [0.207, 0.239] | 0.281 [0.262, 0.301] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| entropy_mean | 0.897 [0.886, 0.907] | 0.229 [0.212, 0.245] | 0.263 [0.247, 0.281] | 0.001 | none |
| entropy_max | 0.896 [0.886, 0.906] | 0.229 [0.213, 0.245] | 0.267 [0.250, 0.285] | 0.001 | none |
| neg_logprob_mean | 0.889 [0.878, 0.899] | 0.232 [0.216, 0.249] | 0.247 [0.231, 0.265] | 0.001 | none |
| neg_logprob_min | 0.888 [0.877, 0.898] | 0.233 [0.217, 0.250] | 0.250 [0.234, 0.267] | 0.001 | none |
| semantic_entropy_w | 0.881 [0.869, 0.891] | 0.264 [0.245, 0.282] | 0.265 [0.247, 0.283] | 0.001 | +N gen + NLI |
| semantic_entropy | 0.880 [0.869, 0.891] | 0.264 [0.245, 0.282] | 0.265 [0.247, 0.282] | 0.001 | +N gen + NLI |
| self_consistency | 0.878 [0.866, 0.889] | 0.265 [0.246, 0.282] | 0.262 [0.244, 0.279] | 0.001 | +N gen + NLI |
| sep | 0.868 [0.856, 0.881] | 0.259 [0.240, 0.278] | 0.247 [0.230, 0.264] | 0.001 | ~free (probe, pre-answer) |
| p_true | 0.866 [0.853, 0.879] | 0.239 [0.222, 0.257] | 0.208 [0.193, 0.225] | 0.001 | +1 prefill |
| verbalized | 0.813 [0.799, 0.827] | 0.308 [0.287, 0.328] | 0.210 [0.196, 0.226] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.142

### ood: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| tripwire_post | 0.803 [0.792, 0.813] | 0.473 [0.457, 0.489] | 0.042 [0.029, 0.056] |  | ~1-2% decode (in-engine) |
| entropy_max | 0.787 [0.776, 0.797] | 0.498 [0.482, 0.514] | 0.029 [0.016, 0.041] | 0.003 | none |
| entropy_mean | 0.784 [0.773, 0.794] | 0.498 [0.483, 0.515] | 0.025 [0.012, 0.037] | 0.001 | none |
| semantic_entropy_w | 0.780 [0.770, 0.789] | 0.523 [0.509, 0.537] | 0.026 [0.013, 0.039] | 0.001 | +N gen + NLI |
| semantic_entropy | 0.779 [0.770, 0.789] | 0.523 [0.509, 0.537] | 0.026 [0.013, 0.039] | 0.001 | +N gen + NLI |
| self_consistency | 0.778 [0.769, 0.787] | 0.523 [0.509, 0.538] | 0.028 [0.015, 0.040] | 0.001 | +N gen + NLI |
| neg_logprob_mean | 0.772 [0.761, 0.782] | 0.503 [0.488, 0.520] | 0.027 [0.016, 0.038] | 0.001 | none |
| neg_logprob_min | 0.772 [0.761, 0.782] | 0.504 [0.488, 0.520] | 0.032 [0.021, 0.043] | 0.001 | none |
| sep | 0.752 [0.740, 0.763] | 0.526 [0.509, 0.541] | 0.022 [0.011, 0.035] | 0.001 | ~free (probe, pre-answer) |
| tripwire_know | 0.745 [0.733, 0.757] | 0.510 [0.494, 0.527] | 0.021 [0.008, 0.034] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_pre | 0.740 [0.728, 0.752] | 0.512 [0.496, 0.529] | 0.020 [0.007, 0.033] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| p_true | 0.736 [0.723, 0.749] | 0.503 [0.487, 0.519] | 0.044 [0.035, 0.054] | 0.001 | +1 prefill |
| verbalized | 0.701 [0.689, 0.713] | 0.557 [0.542, 0.572] | 0.048 [0.040, 0.057] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.035

### error types (test, greedy)

| type | share | resample acc | best-of-N by risk | retrieval acc | any sample correct |
|---|---|---|---|---|---|
| correct | 0.483 | 0.951 | 0.951 | 0.920 | 0.999 |
| gap | 0.480 | 0.005 | 0.016 | 0.377 | 0.051 |
| drift | 0.038 | 0.327 | 0.583 | 0.675 | 1.000 |

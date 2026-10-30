### test: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| tripwire_post | 0.904 [0.894, 0.914] | 0.223 [0.208, 0.238] | 0.283 [0.266, 0.303] |  | ~1-2% decode (in-engine) |
| entropy_max | 0.894 [0.883, 0.905] | 0.231 [0.216, 0.247] | 0.276 [0.259, 0.293] | 0.024 | none |
| entropy_mean | 0.891 [0.881, 0.903] | 0.230 [0.215, 0.245] | 0.275 [0.259, 0.292] | 0.012 | none |
| semantic_entropy_w | 0.891 [0.880, 0.902] | 0.239 [0.223, 0.255] | 0.273 [0.256, 0.290] | 0.006 | +N gen + NLI |
| semantic_entropy | 0.888 [0.877, 0.899] | 0.240 [0.224, 0.256] | 0.273 [0.256, 0.291] | 0.004 | +N gen + NLI |
| self_consistency | 0.883 [0.872, 0.894] | 0.242 [0.226, 0.258] | 0.269 [0.252, 0.286] | 0.001 | +N gen + NLI |
| neg_logprob_mean | 0.882 [0.871, 0.894] | 0.237 [0.221, 0.253] | 0.264 [0.247, 0.280] | 0.001 | none |
| neg_logprob_min | 0.876 [0.865, 0.888] | 0.244 [0.228, 0.261] | 0.258 [0.241, 0.273] | 0.001 | none |
| tripwire_pre | 0.874 [0.862, 0.885] | 0.243 [0.227, 0.259] | 0.259 [0.241, 0.275] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_know | 0.871 [0.860, 0.882] | 0.243 [0.227, 0.260] | 0.256 [0.239, 0.273] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| sep | 0.864 [0.851, 0.876] | 0.252 [0.235, 0.268] | 0.248 [0.231, 0.264] | 0.001 | ~free (probe, pre-answer) |
| p_true | 0.821 [0.805, 0.836] | 0.272 [0.254, 0.290] | 0.174 [0.162, 0.187] | 0.001 | +1 prefill |
| verbalized | 0.791 [0.777, 0.806] | 0.324 [0.305, 0.342] | 0.199 [0.186, 0.212] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.142

### ood: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| entropy_mean | 0.811 [0.800, 0.822] | 0.495 [0.481, 0.511] | 0.053 [0.042, 0.064] | 1.000 | none |
| neg_logprob_mean | 0.802 [0.791, 0.813] | 0.504 [0.489, 0.520] | 0.041 [0.030, 0.052] | 1.000 | none |
| entropy_max | 0.802 [0.790, 0.813] | 0.503 [0.488, 0.520] | 0.048 [0.036, 0.058] | 1.000 | none |
| semantic_entropy_w | 0.793 [0.780, 0.803] | 0.523 [0.508, 0.539] | 0.036 [0.024, 0.047] | 1.000 | +N gen + NLI |
| semantic_entropy | 0.791 [0.778, 0.801] | 0.524 [0.509, 0.540] | 0.035 [0.023, 0.047] | 1.000 | +N gen + NLI |
| self_consistency | 0.782 [0.770, 0.793] | 0.527 [0.512, 0.543] | 0.035 [0.024, 0.046] | 1.000 | +N gen + NLI |
| neg_logprob_min | 0.780 [0.768, 0.791] | 0.519 [0.504, 0.536] | 0.036 [0.024, 0.046] | 1.000 | none |
| tripwire_know | 0.735 [0.722, 0.748] | 0.552 [0.537, 0.569] | 0.005 [-0.007, 0.017] | 1.000 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_post | 0.709 [0.696, 0.722] | 0.548 [0.533, 0.565] | 0.018 [0.006, 0.029] |  | ~1-2% decode (in-engine) |
| sep | 0.706 [0.693, 0.720] | 0.568 [0.552, 0.584] | 0.014 [0.003, 0.023] | 0.287 | ~free (probe, pre-answer) |
| tripwire_pre | 0.688 [0.674, 0.703] | 0.569 [0.553, 0.586] | 0.012 [0.001, 0.023] | 0.002 | ~1-2% decode (in-engine, pre-answer) |
| verbalized | 0.663 [0.650, 0.675] | 0.613 [0.600, 0.628] | 0.018 [0.010, 0.026] | 0.001 | +1 generation |
| p_true | 0.649 [0.633, 0.662] | 0.585 [0.570, 0.602] | 0.022 [0.014, 0.028] | 0.001 | +1 prefill |

BAS of a constant confidence (val accuracy for every answer): 0.014

### error types (test, greedy)

| type | share | resample acc | best-of-N by risk | retrieval acc | any sample correct |
|---|---|---|---|---|---|
| correct | 0.484 | 0.866 | 0.911 | 0.846 | 0.991 |
| gap | 0.445 | 0.012 | 0.030 | 0.335 | 0.121 |
| drift | 0.071 | 0.322 | 0.540 | 0.615 | 1.000 |

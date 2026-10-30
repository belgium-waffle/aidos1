### test: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| tripwire_post | 0.890 [0.879, 0.900] | 0.232 [0.217, 0.250] | 0.262 [0.243, 0.280] |  | ~1-2% decode (in-engine) |
| tripwire_pre | 0.877 [0.865, 0.888] | 0.243 [0.227, 0.260] | 0.259 [0.242, 0.276] | 0.003 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_know | 0.875 [0.864, 0.886] | 0.240 [0.224, 0.258] | 0.259 [0.242, 0.276] | 0.002 | ~1-2% decode (in-engine, pre-answer) |
| sep | 0.844 [0.830, 0.856] | 0.264 [0.246, 0.283] | 0.235 [0.218, 0.251] | 0.001 | ~free (probe, pre-answer) |
| semantic_entropy | 0.832 [0.817, 0.846] | 0.276 [0.257, 0.294] | 0.231 [0.215, 0.247] | 0.001 | +N gen + NLI |
| semantic_entropy_w | 0.832 [0.818, 0.845] | 0.275 [0.257, 0.295] | 0.230 [0.215, 0.246] | 0.001 | +N gen + NLI |
| entropy_mean | 0.819 [0.805, 0.833] | 0.272 [0.254, 0.290] | 0.225 [0.210, 0.240] | 0.001 | none |
| entropy_max | 0.811 [0.797, 0.827] | 0.278 [0.260, 0.297] | 0.222 [0.207, 0.238] | 0.001 | none |
| self_consistency | 0.809 [0.793, 0.824] | 0.285 [0.267, 0.304] | 0.221 [0.205, 0.236] | 0.001 | +N gen + NLI |
| neg_logprob_mean | 0.800 [0.786, 0.816] | 0.282 [0.263, 0.301] | 0.213 [0.198, 0.227] | 0.001 | none |
| neg_logprob_min | 0.791 [0.776, 0.807] | 0.289 [0.270, 0.309] | 0.210 [0.194, 0.225] | 0.001 | none |
| p_true | 0.788 [0.772, 0.804] | 0.312 [0.292, 0.334] | 0.163 [0.151, 0.175] | 0.001 | +1 prefill |
| verbalized | 0.633 [0.621, 0.645] | 0.440 [0.421, 0.459] | 0.165 [0.153, 0.177] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.143

### ood: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| sep | 0.732 [0.720, 0.744] | 0.540 [0.523, 0.556] | 0.029 [0.018, 0.039] | 1.000 | ~free (probe, pre-answer) |
| entropy_mean | 0.694 [0.681, 0.707] | 0.561 [0.546, 0.578] | 0.038 [0.029, 0.046] | 1.000 | none |
| neg_logprob_mean | 0.673 [0.660, 0.687] | 0.572 [0.556, 0.588] | 0.038 [0.030, 0.046] | 1.000 | none |
| semantic_entropy | 0.658 [0.644, 0.670] | 0.574 [0.560, 0.591] | 0.036 [0.027, 0.045] | 0.993 | +N gen + NLI |
| semantic_entropy_w | 0.656 [0.642, 0.669] | 0.574 [0.559, 0.591] | 0.037 [0.028, 0.045] | 0.987 | +N gen + NLI |
| tripwire_post | 0.642 [0.627, 0.657] | 0.577 [0.560, 0.595] | 0.030 [0.019, 0.039] |  | ~1-2% decode (in-engine) |
| entropy_max | 0.642 [0.626, 0.655] | 0.579 [0.564, 0.596] | 0.036 [0.027, 0.044] | 0.447 | none |
| self_consistency | 0.641 [0.626, 0.655] | 0.581 [0.566, 0.598] | 0.037 [0.028, 0.045] | 0.382 | +N gen + NLI |
| tripwire_know | 0.635 [0.622, 0.648] | 0.598 [0.582, 0.614] | -0.011 [-0.021, 0.000] | 0.102 | ~1-2% decode (in-engine, pre-answer) |
| p_true | 0.629 [0.614, 0.642] | 0.614 [0.599, 0.632] | 0.033 [0.027, 0.040] | 0.024 | +1 prefill |
| neg_logprob_min | 0.623 [0.609, 0.637] | 0.589 [0.574, 0.606] | 0.033 [0.025, 0.041] | 0.004 | none |
| tripwire_pre | 0.601 [0.586, 0.614] | 0.609 [0.594, 0.625] | 0.008 [-0.001, 0.017] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| verbalized | 0.596 [0.587, 0.605] | 0.648 [0.637, 0.661] | 0.033 [0.025, 0.040] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.033

### error types (test, greedy)

| type | share | resample acc | best-of-N by risk | retrieval acc | any sample correct |
|---|---|---|---|---|---|
| correct | 0.486 | 0.930 | 0.924 | 0.833 | 0.995 |
| gap | 0.466 | 0.009 | 0.023 | 0.348 | 0.087 |
| drift | 0.048 | 0.346 | 0.399 | 0.523 | 1.000 |

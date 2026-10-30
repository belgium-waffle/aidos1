### test: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|
| tripwire_post | 0.926 [0.917, 0.934] | 0.210 [0.194, 0.225] |  | ~1-2% decode (in-engine) |
| tripwire_pre | 0.908 [0.897, 0.917] | 0.224 [0.206, 0.239] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_know | 0.907 [0.896, 0.916] | 0.222 [0.205, 0.237] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| entropy_mean | 0.896 [0.885, 0.906] | 0.228 [0.212, 0.244] | 0.001 | none |
| entropy_max | 0.895 [0.885, 0.905] | 0.228 [0.213, 0.244] | 0.001 | none |
| neg_logprob_mean | 0.887 [0.876, 0.898] | 0.232 [0.216, 0.248] | 0.001 | none |
| neg_logprob_min | 0.886 [0.875, 0.897] | 0.233 [0.217, 0.250] | 0.001 | none |
| semantic_entropy_w | 0.879 [0.868, 0.890] | 0.263 [0.244, 0.281] | 0.001 | +N gen + NLI |
| semantic_entropy | 0.879 [0.867, 0.889] | 0.264 [0.245, 0.282] | 0.001 | +N gen + NLI |
| self_consistency | 0.877 [0.865, 0.887] | 0.264 [0.245, 0.282] | 0.001 | +N gen + NLI |
| sep | 0.867 [0.854, 0.879] | 0.261 [0.241, 0.279] | 0.001 | ~free (probe, pre-answer) |
| p_true | 0.865 [0.852, 0.878] | 0.238 [0.221, 0.256] | 0.001 | +1 prefill |
| verbalized | 0.813 [0.799, 0.827] | 0.307 [0.287, 0.327] | 0.001 | +1 generation |

### ood: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|
| tripwire_post | 0.798 [0.785, 0.810] | 0.444 [0.425, 0.462] |  | ~1-2% decode (in-engine) |
| entropy_max | 0.772 [0.758, 0.784] | 0.479 [0.460, 0.499] | 0.001 | none |
| semantic_entropy_w | 0.769 [0.757, 0.781] | 0.499 [0.481, 0.516] | 0.001 | +N gen + NLI |
| semantic_entropy | 0.769 [0.757, 0.780] | 0.499 [0.481, 0.516] | 0.001 | +N gen + NLI |
| self_consistency | 0.767 [0.755, 0.779] | 0.499 [0.482, 0.516] | 0.001 | +N gen + NLI |
| entropy_mean | 0.767 [0.754, 0.779] | 0.482 [0.464, 0.502] | 0.001 | none |
| p_true | 0.765 [0.751, 0.777] | 0.458 [0.440, 0.477] | 0.001 | +1 prefill |
| tripwire_know | 0.764 [0.750, 0.777] | 0.474 [0.456, 0.493] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_pre | 0.761 [0.746, 0.774] | 0.476 [0.457, 0.495] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| neg_logprob_min | 0.757 [0.744, 0.770] | 0.485 [0.466, 0.505] | 0.001 | none |
| neg_logprob_mean | 0.754 [0.741, 0.767] | 0.486 [0.468, 0.506] | 0.001 | none |
| sep | 0.746 [0.732, 0.761] | 0.501 [0.481, 0.521] | 0.001 | ~free (probe, pre-answer) |
| verbalized | 0.732 [0.718, 0.745] | 0.513 [0.495, 0.530] | 0.001 | +1 generation |

### error types (test, greedy)

| type | share | resample acc | best-of-N by risk | retrieval acc | any sample correct |
|---|---|---|---|---|---|
| correct | 0.484 | 0.949 | 0.947 | 0.911 | 0.999 |
| gap | 0.480 | 0.005 | 0.017 | 0.266 | 0.051 |
| drift | 0.036 | 0.325 | 0.579 | 0.553 | 1.000 |

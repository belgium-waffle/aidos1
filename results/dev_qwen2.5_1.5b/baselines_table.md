### test: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| tripwire_post | 0.878 [0.848, 0.902] | 0.500 [0.452, 0.556] | 0.089 [0.065, 0.116] |  | ~1-2% decode (in-engine) |
| neg_logprob_mean | 0.874 [0.840, 0.897] | 0.513 [0.463, 0.569] | 0.079 [0.060, 0.097] | 0.398 | none |
| entropy_mean | 0.872 [0.834, 0.896] | 0.514 [0.464, 0.572] | 0.084 [0.060, 0.103] | 0.413 | none |
| self_consistency | 0.870 [0.831, 0.901] | 0.513 [0.467, 0.573] | 0.085 [0.062, 0.102] | 0.343 | +N gen + NLI |
| semantic_entropy_w | 0.861 [0.823, 0.894] | 0.517 [0.473, 0.574] | 0.083 [0.061, 0.101] | 0.184 | +N gen + NLI |
| semantic_entropy | 0.860 [0.822, 0.893] | 0.518 [0.474, 0.575] | 0.083 [0.061, 0.101] | 0.179 | +N gen + NLI |
| entropy_max | 0.856 [0.814, 0.885] | 0.523 [0.474, 0.583] | 0.079 [0.056, 0.097] | 0.139 | none |
| neg_logprob_min | 0.850 [0.808, 0.883] | 0.525 [0.476, 0.586] | 0.074 [0.054, 0.090] | 0.095 | none |
| tripwire_know | 0.841 [0.806, 0.875] | 0.525 [0.481, 0.588] | 0.079 [0.051, 0.098] | 0.015 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_pre | 0.840 [0.806, 0.875] | 0.525 [0.480, 0.587] | 0.079 [0.050, 0.098] | 0.015 | ~1-2% decode (in-engine, pre-answer) |
| p_true | 0.818 [0.776, 0.856] | 0.529 [0.478, 0.588] | 0.062 [0.045, 0.079] | 0.010 | +1 prefill |
| sep | 0.808 [0.771, 0.845] | 0.560 [0.509, 0.618] | 0.061 [0.039, 0.081] | 0.005 | ~free (probe, pre-answer) |
| verbalized | 0.603 [0.572, 0.632] | 0.715 [0.674, 0.751] | 0.037 [0.026, 0.049] | 0.005 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.032

### ood: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| self_consistency | 0.825 [0.801, 0.848] | 0.633 [0.594, 0.668] | 0.032 [0.017, 0.047] | 1.000 | +N gen + NLI |
| semantic_entropy | 0.822 [0.798, 0.843] | 0.633 [0.595, 0.668] | 0.030 [0.014, 0.046] | 1.000 | +N gen + NLI |
| semantic_entropy_w | 0.822 [0.798, 0.844] | 0.633 [0.595, 0.668] | 0.030 [0.014, 0.046] | 1.000 | +N gen + NLI |
| entropy_max | 0.803 [0.777, 0.830] | 0.639 [0.596, 0.673] | 0.034 [0.021, 0.051] | 1.000 | none |
| entropy_mean | 0.788 [0.759, 0.820] | 0.641 [0.601, 0.676] | 0.028 [0.012, 0.042] | 1.000 | none |
| neg_logprob_mean | 0.788 [0.761, 0.820] | 0.644 [0.602, 0.678] | 0.033 [0.021, 0.045] | 1.000 | none |
| neg_logprob_min | 0.788 [0.760, 0.819] | 0.649 [0.603, 0.685] | 0.034 [0.022, 0.047] | 1.000 | none |
| tripwire_know | 0.773 [0.742, 0.798] | 0.661 [0.627, 0.692] | -0.030 [-0.054, -0.006] | 1.000 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_pre | 0.772 [0.742, 0.798] | 0.660 [0.627, 0.692] | -0.023 [-0.046, -0.002] | 1.000 | ~1-2% decode (in-engine, pre-answer) |
| p_true | 0.709 [0.672, 0.747] | 0.672 [0.630, 0.706] | 0.021 [0.011, 0.033] | 0.736 | +1 prefill |
| tripwire_post | 0.698 [0.660, 0.733] | 0.663 [0.626, 0.700] | -0.002 [-0.022, 0.021] |  | ~1-2% decode (in-engine) |
| sep | 0.686 [0.655, 0.723] | 0.697 [0.662, 0.731] | -0.002 [-0.015, 0.013] | 0.214 | ~free (probe, pre-answer) |
| verbalized | 0.637 [0.609, 0.657] | 0.746 [0.715, 0.772] | 0.026 [0.019, 0.034] | 0.005 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.020

### error types (test, greedy)

| type | share | resample acc | best-of-N by risk | retrieval acc | any sample correct |
|---|---|---|---|---|---|
| correct | 0.243 | 0.760 | 0.834 | 0.834 | 0.993 |
| gap | 0.710 | 0.007 | 0.012 | 0.406 | 0.066 |
| drift | 0.047 | 0.261 | 0.464 | 0.643 | 1.000 |

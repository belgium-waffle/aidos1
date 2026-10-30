### test: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| tripwire_post | 0.920 [0.910, 0.929] | 0.321 [0.302, 0.341] | 0.196 [0.177, 0.213] |  | ~1-2% decode (in-engine) |
| tripwire_know | 0.898 [0.887, 0.908] | 0.339 [0.319, 0.361] | 0.178 [0.159, 0.194] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_pre | 0.896 [0.885, 0.907] | 0.341 [0.321, 0.364] | 0.179 [0.161, 0.196] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| entropy_mean | 0.890 [0.879, 0.901] | 0.346 [0.327, 0.368] | 0.171 [0.156, 0.185] | 0.001 | none |
| entropy_max | 0.888 [0.878, 0.900] | 0.348 [0.328, 0.369] | 0.171 [0.156, 0.185] | 0.001 | none |
| neg_logprob_mean | 0.885 [0.874, 0.897] | 0.349 [0.329, 0.371] | 0.163 [0.149, 0.176] | 0.001 | none |
| neg_logprob_min | 0.883 [0.872, 0.895] | 0.351 [0.331, 0.372] | 0.162 [0.149, 0.176] | 0.001 | none |
| self_consistency | 0.883 [0.871, 0.894] | 0.370 [0.350, 0.392] | 0.167 [0.153, 0.181] | 0.001 | +N gen + NLI |
| semantic_entropy_w | 0.881 [0.870, 0.893] | 0.371 [0.351, 0.392] | 0.168 [0.153, 0.182] | 0.001 | +N gen + NLI |
| semantic_entropy | 0.880 [0.869, 0.892] | 0.371 [0.351, 0.393] | 0.168 [0.153, 0.182] | 0.001 | +N gen + NLI |
| sep | 0.853 [0.840, 0.867] | 0.375 [0.353, 0.397] | 0.148 [0.134, 0.162] | 0.001 | ~free (probe, pre-answer) |
| p_true | 0.845 [0.830, 0.860] | 0.358 [0.337, 0.379] | 0.120 [0.107, 0.132] | 0.001 | +1 prefill |
| verbalized | 0.787 [0.770, 0.804] | 0.397 [0.376, 0.420] | 0.119 [0.108, 0.130] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.078

### ood: detecting wrong greedy answers

| detector | AUROC [95% CI] | AURC [95% CI] (lower=better) | BAS [95% CI] (higher=better) | p(tripwire_post better) | extra cost |
|---|---|---|---|---|---|
| semantic_entropy_w | 0.808 [0.798, 0.817] | 0.580 [0.564, 0.595] | 0.015 [0.005, 0.027] | 0.903 | +N gen + NLI |
| semantic_entropy | 0.807 [0.797, 0.816] | 0.581 [0.564, 0.595] | 0.015 [0.005, 0.027] | 0.884 | +N gen + NLI |
| self_consistency | 0.805 [0.796, 0.815] | 0.581 [0.565, 0.596] | 0.017 [0.007, 0.029] | 0.800 | +N gen + NLI |
| tripwire_post | 0.800 [0.788, 0.811] | 0.557 [0.540, 0.574] | 0.012 [0.000, 0.025] |  | ~1-2% decode (in-engine) |
| entropy_mean | 0.795 [0.784, 0.806] | 0.577 [0.559, 0.594] | 0.009 [-0.001, 0.020] | 0.263 | none |
| entropy_max | 0.794 [0.783, 0.804] | 0.579 [0.562, 0.595] | 0.012 [0.001, 0.023] | 0.188 | none |
| neg_logprob_mean | 0.788 [0.776, 0.798] | 0.580 [0.563, 0.597] | 0.017 [0.007, 0.027] | 0.035 | none |
| neg_logprob_min | 0.784 [0.773, 0.795] | 0.582 [0.565, 0.600] | 0.020 [0.010, 0.030] | 0.013 | none |
| tripwire_pre | 0.779 [0.766, 0.791] | 0.573 [0.555, 0.589] | 0.028 [0.017, 0.038] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| tripwire_know | 0.775 [0.762, 0.788] | 0.578 [0.561, 0.595] | 0.017 [0.006, 0.028] | 0.001 | ~1-2% decode (in-engine, pre-answer) |
| sep | 0.765 [0.752, 0.777] | 0.584 [0.566, 0.601] | 0.035 [0.027, 0.044] | 0.001 | ~free (probe, pre-answer) |
| p_true | 0.757 [0.744, 0.770] | 0.572 [0.554, 0.590] | 0.034 [0.027, 0.041] | 0.001 | +1 prefill |
| verbalized | 0.690 [0.676, 0.702] | 0.617 [0.601, 0.634] | 0.035 [0.028, 0.041] | 0.001 | +1 generation |

BAS of a constant confidence (val accuracy for every answer): 0.025

### error types (test, greedy)

| type | share | resample acc | best-of-N by risk | retrieval acc | any sample correct |
|---|---|---|---|---|---|
| correct | 0.367 | 0.898 | 0.925 | 0.826 | 0.996 |
| gap | 0.584 | 0.006 | 0.024 | 0.406 | 0.059 |
| drift | 0.049 | 0.335 | 0.652 | 0.594 | 1.000 |

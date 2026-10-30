### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.809 | 0.766 | tau = 0.6255 |
| FLARE (1 - min token probability) | 0.717 | 0.736 | theta = 0.2883 |

Sentences: {'val': 1300, 'test': 3585}; unsupported rate {'val': 0.9069230769230769, 'test': 0.9436541143654115}

### Bridge biographies ("Who directed F? ... bio of that person"), test questions (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | right person | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.196 | 0.187 | 0.080 | 29.5 | 6.0 | 23.5 | 0.175 | 0.181 | 0.230 | 0.00 | 0.00 | 46 | 271 | 54.84 |
| rag (always, up front) | 0.333 | 0.322 | 0.247 | 22.8 | 8.1 | 14.7 | 0.356 | 0.300 | 0.343 | 1.00 | 0.00 | 443 | 257 | 18.63 |
| flare | 0.321 | 0.290 | 0.275 | 23.8 | 7.9 | 15.9 | 0.285 | 0.302 | 0.376 | 2.90 | 0.00 | 1610 | 337 | 4.46 |
| tripwire lf-retrieve | 0.348 | 0.345 | 0.237 | 27.3 | 9.9 | 17.4 | 0.351 | 0.306 | 0.387 | 2.97 | 0.00 | 1587 | 338 | 1.27 |
| rag + tripwire lf-retrieve | 0.376 | 0.367 | 0.263 | 26.1 | 10.5 | 15.6 | 0.399 | 0.333 | 0.396 | 2.96 | 0.00 | 1495 | 329 | 1.76 |
| tripwire lf-resample | 0.194 | 0.182 | 0.085 | 26.9 | 5.6 | 21.3 | 0.163 | 0.176 | 0.243 | 0.00 | 2.93 | 2035 | 526 | 14.41 |
| flare-signal resample (SHARS-style) | 0.198 | 0.191 | 0.083 | 28.7 | 6.1 | 22.7 | 0.169 | 0.190 | 0.234 | 0.00 | 2.91 | 156 | 557 | 15.72 |
| tripwire lf-route (resample, then retrieve) | 0.295 | 0.266 | 0.230 | 23.9 | 7.6 | 16.3 | 0.309 | 0.233 | 0.341 | 2.31 | 2.94 | 3385 | 601 | 4.94 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 399 | +0.027 | [+0.003, +0.051] | 0.032 |
| tripwire lf-retrieve | flare | right person | 400 | -0.037 | [-0.072, -0.005] | 0.039 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 400 | +0.015 | [-0.006, +0.037] | 0.186 |
| tripwire lf-retrieve | rag (always, up front) | right person | 400 | -0.010 | [-0.040, +0.018] | 0.547 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 399 | +0.043 | [+0.022, +0.064] | 0.001 |
| rag + tripwire lf-retrieve | rag (always, up front) | right person | 400 | +0.015 | [-0.007, +0.035] | 0.213 |
| tripwire lf-resample | vanilla | FActScore | 399 | -0.001 | [-0.019, +0.016] | 0.888 |
| tripwire lf-resample | vanilla | right person | 400 | +0.005 | [-0.008, +0.020] | 0.600 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 399 | -0.003 | [-0.019, +0.012] | 0.678 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | right person | 400 | +0.003 | [-0.013, +0.018] | 0.844 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 398 | +0.100 | [+0.075, +0.127] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | right person | 400 | +0.145 | [+0.105, +0.185] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 399 | -0.054 | [-0.080, -0.030] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | right person | 400 | -0.007 | [-0.040, +0.025] | 0.732 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 398 | -0.027 | [-0.051, -0.003] | 0.030 |
| tripwire lf-route (resample, then retrieve) | flare | right person | 400 | -0.045 | [-0.077, -0.010] | 0.013 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.890, kappa 0.743

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 2968 | 0.898 | 0.729 | 0.217 | 0.280 |
| rag (always, up front) | 2273 | 0.885 | 0.738 | 0.277 | 0.353 |
| flare | 2393 | 0.878 | 0.725 | 0.290 | 0.365 |
| tripwire lf-retrieve | 2631 | 0.873 | 0.715 | 0.269 | 0.348 |
| rag + tripwire lf-retrieve | 2430 | 0.867 | 0.726 | 0.331 | 0.432 |
| tripwire lf-resample | 2716 | 0.907 | 0.764 | 0.225 | 0.276 |
| flare-signal resample (SHARS-style) | 2832 | 0.903 | 0.758 | 0.230 | 0.292 |
| tripwire lf-route (resample, then retrieve) | 2460 | 0.904 | 0.778 | 0.255 | 0.311 |

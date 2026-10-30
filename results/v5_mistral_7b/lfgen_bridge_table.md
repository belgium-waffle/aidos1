### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.677 | 0.718 | tau = 0.7094 |
| FLARE (1 - min token probability) | 0.679 | 0.676 | theta = 0.3380 |

Sentences: {'val': 1362, 'test': 3558}; unsupported rate {'val': 0.869309838472834, 'test': 0.886734120292299}

### Bridge biographies ("Who directed F? ... bio of that person"), test questions (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | right person | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.277 | 0.277 | 0.215 | 28.9 | 8.5 | 20.4 | 0.227 | 0.256 | 0.348 | 0.00 | 0.00 | 21 | 295 | 46.44 |
| rag (always, up front) | 0.314 | 0.309 | 0.258 | 22.5 | 7.5 | 15.1 | 0.321 | 0.286 | 0.336 | 1.00 | 0.00 | 479 | 265 | 17.20 |
| flare | 0.323 | 0.322 | 0.300 | 28.3 | 9.6 | 18.7 | 0.280 | 0.301 | 0.388 | 2.96 | 0.00 | 1871 | 382 | 3.95 |
| tripwire lf-retrieve | 0.388 | 0.373 | 0.282 | 18.5 | 7.6 | 10.9 | 0.381 | 0.353 | 0.429 | 2.86 | 0.00 | 1612 | 225 | 1.35 |
| rag + tripwire lf-retrieve | 0.371 | 0.332 | 0.250 | 16.9 | 6.6 | 10.2 | 0.370 | 0.342 | 0.401 | 2.95 | 0.00 | 1592 | 205 | 1.81 |
| tripwire lf-resample | 0.267 | 0.267 | 0.220 | 28.4 | 8.1 | 20.3 | 0.217 | 0.239 | 0.345 | 0.00 | 2.88 | 1943 | 604 | 13.91 |
| flare-signal resample (SHARS-style) | 0.274 | 0.274 | 0.223 | 29.0 | 8.3 | 20.8 | 0.223 | 0.260 | 0.339 | 0.00 | 2.96 | 194 | 627 | 15.25 |
| tripwire lf-route (resample, then retrieve) | 0.320 | 0.319 | 0.323 | 27.9 | 9.3 | 18.6 | 0.283 | 0.289 | 0.389 | 2.21 | 2.91 | 3378 | 684 | 4.35 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 400 | +0.065 | [+0.036, +0.093] | 0.000 |
| tripwire lf-retrieve | flare | right person | 400 | -0.018 | [-0.055, +0.022] | 0.381 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 400 | +0.073 | [+0.048, +0.098] | 0.000 |
| tripwire lf-retrieve | rag (always, up front) | right person | 400 | +0.025 | [-0.010, +0.060] | 0.186 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 396 | +0.056 | [+0.034, +0.079] | 0.000 |
| rag + tripwire lf-retrieve | rag (always, up front) | right person | 400 | -0.007 | [-0.028, +0.013] | 0.554 |
| tripwire lf-resample | vanilla | FActScore | 400 | -0.010 | [-0.026, +0.004] | 0.192 |
| tripwire lf-resample | vanilla | right person | 400 | +0.005 | [-0.015, +0.025] | 0.708 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 400 | -0.007 | [-0.025, +0.010] | 0.432 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | right person | 400 | -0.003 | [-0.022, +0.018] | 0.897 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 400 | +0.053 | [+0.033, +0.074] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | right person | 400 | +0.102 | [+0.068, +0.138] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 400 | -0.068 | [-0.093, -0.040] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | right person | 400 | +0.040 | [+0.003, +0.080] | 0.038 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 400 | -0.003 | [-0.021, +0.016] | 0.786 |
| tripwire lf-route (resample, then retrieve) | flare | right person | 400 | +0.022 | [-0.013, +0.058] | 0.227 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.885, kappa 0.750

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 2848 | 0.888 | 0.751 | 0.289 | 0.356 |
| rag (always, up front) | 2185 | 0.866 | 0.707 | 0.295 | 0.383 |
| flare | 2881 | 0.891 | 0.770 | 0.339 | 0.401 |
| tripwire lf-retrieve | 1769 | 0.863 | 0.723 | 0.355 | 0.468 |
| rag + tripwire lf-retrieve | 1700 | 0.869 | 0.730 | 0.312 | 0.428 |
| tripwire lf-resample | 2715 | 0.892 | 0.754 | 0.276 | 0.336 |
| flare-signal resample (SHARS-style) | 2774 | 0.896 | 0.763 | 0.283 | 0.345 |
| tripwire lf-route (resample, then retrieve) | 2813 | 0.894 | 0.771 | 0.326 | 0.383 |

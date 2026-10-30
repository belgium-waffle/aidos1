### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.694 | 0.698 | tau = 0.7026 |
| FLARE (1 - min token probability) | 0.696 | 0.672 | theta = 0.3152 |

Sentences: {'val': 1471, 'test': 4026}; unsupported rate {'val': 0.8436437797416724, 'test': 0.8700943864878291}

### Bridge biographies ("Who directed F? ... bio of that person"), test questions (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | right person | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.277 | 0.270 | 0.275 | 32.0 | 10.1 | 21.9 | 0.225 | 0.264 | 0.341 | 0.00 | 0.00 | 52 | 304 | 43.59 |
| rag (always, up front) | 0.332 | 0.310 | 0.302 | 25.5 | 9.3 | 16.2 | 0.338 | 0.290 | 0.369 | 1.00 | 0.00 | 435 | 284 | 16.84 |
| flare | 0.364 | 0.332 | 0.390 | 29.3 | 11.3 | 18.0 | 0.339 | 0.337 | 0.417 | 2.91 | 0.00 | 1591 | 357 | 3.85 |
| tripwire lf-retrieve | 0.396 | 0.382 | 0.367 | 19.7 | 8.6 | 11.1 | 0.373 | 0.373 | 0.442 | 2.84 | 0.00 | 1505 | 232 | 1.34 |
| rag + tripwire lf-retrieve | 0.402 | 0.372 | 0.333 | 21.3 | 9.4 | 11.9 | 0.410 | 0.365 | 0.431 | 2.94 | 0.00 | 1463 | 247 | 1.78 |
| tripwire lf-resample | 0.262 | 0.253 | 0.278 | 29.3 | 9.1 | 20.3 | 0.223 | 0.224 | 0.339 | 0.00 | 2.80 | 2733 | 526 | 12.85 |
| flare-signal resample (SHARS-style) | 0.273 | 0.261 | 0.287 | 30.5 | 9.6 | 20.9 | 0.226 | 0.250 | 0.341 | 0.00 | 2.84 | 154 | 556 | 13.44 |
| tripwire lf-route (resample, then retrieve) | 0.340 | 0.308 | 0.355 | 30.1 | 10.8 | 19.3 | 0.320 | 0.296 | 0.403 | 2.20 | 2.93 | 4048 | 601 | 4.76 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 397 | +0.033 | [+0.006, +0.061] | 0.017 |
| tripwire lf-retrieve | flare | right person | 400 | -0.022 | [-0.060, +0.015] | 0.253 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 395 | +0.065 | [+0.038, +0.092] | 0.000 |
| tripwire lf-retrieve | rag (always, up front) | right person | 400 | +0.065 | [+0.030, +0.100] | 0.000 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 395 | +0.070 | [+0.048, +0.092] | 0.000 |
| rag + tripwire lf-retrieve | rag (always, up front) | right person | 400 | +0.030 | [+0.010, +0.052] | 0.005 |
| tripwire lf-resample | vanilla | FActScore | 372 | -0.012 | [-0.030, +0.006] | 0.195 |
| tripwire lf-resample | vanilla | right person | 400 | +0.003 | [-0.020, +0.025] | 0.936 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 376 | -0.012 | [-0.030, +0.007] | 0.236 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | right person | 400 | -0.010 | [-0.030, +0.013] | 0.430 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 382 | +0.068 | [+0.049, +0.088] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | right person | 400 | +0.077 | [+0.045, +0.113] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 398 | -0.056 | [-0.082, -0.030] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | right person | 400 | -0.013 | [-0.045, +0.022] | 0.518 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 399 | -0.024 | [-0.048, -0.001] | 0.041 |
| tripwire lf-route (resample, then retrieve) | flare | right person | 400 | -0.035 | [-0.068, -0.003] | 0.043 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.889, kappa 0.762

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 3155 | 0.897 | 0.770 | 0.272 | 0.322 |
| rag (always, up front) | 2438 | 0.877 | 0.729 | 0.293 | 0.379 |
| flare | 2842 | 0.898 | 0.789 | 0.385 | 0.446 |
| tripwire lf-retrieve | 1902 | 0.875 | 0.750 | 0.366 | 0.466 |
| rag + tripwire lf-retrieve | 2171 | 0.855 | 0.708 | 0.355 | 0.456 |
| tripwire lf-resample | 3163 | 0.898 | 0.764 | 0.244 | 0.307 |
| flare-signal resample (SHARS-style) | 3123 | 0.900 | 0.778 | 0.276 | 0.314 |
| tripwire lf-route (resample, then retrieve) | 3033 | 0.895 | 0.765 | 0.315 | 0.380 |

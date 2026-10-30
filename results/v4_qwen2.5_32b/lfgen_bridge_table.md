### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.765 | 0.740 | tau = 0.6588 |
| FLARE (1 - min token probability) | 0.681 | 0.676 | theta = 0.2644 |

Sentences: {'val': 953, 'test': 2598}; unsupported rate {'val': 0.85099685204617, 'test': 0.8772132409545804}

### Bridge biographies ("Who directed F? ... bio of that person"), test questions (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | right person | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.301 | 0.281 | 0.170 | 22.5 | 7.2 | 15.3 | 0.259 | 0.272 | 0.371 | 0.00 | 0.00 | 46 | 197 | 19.02 |
| rag (always, up front) | 0.374 | 0.340 | 0.285 | 16.8 | 6.9 | 9.9 | 0.375 | 0.348 | 0.397 | 1.00 | 0.00 | 443 | 177 | 8.34 |
| flare | 0.402 | 0.342 | 0.290 | 18.6 | 8.0 | 10.6 | 0.359 | 0.376 | 0.470 | 2.37 | 0.00 | 1381 | 247 | 2.61 |
| tripwire lf-retrieve | 0.413 | 0.381 | 0.300 | 20.0 | 9.1 | 10.9 | 0.411 | 0.386 | 0.443 | 2.68 | 0.00 | 1437 | 226 | 1.12 |
| rag + tripwire lf-retrieve | 0.441 | 0.382 | 0.305 | 16.5 | 8.5 | 8.1 | 0.441 | 0.412 | 0.470 | 2.84 | 0.00 | 1427 | 193 | 1.41 |
| tripwire lf-resample | 0.277 | 0.255 | 0.163 | 21.1 | 6.3 | 14.8 | 0.227 | 0.255 | 0.348 | 0.00 | 2.72 | 1225 | 469 | 6.64 |
| flare-signal resample (SHARS-style) | 0.292 | 0.268 | 0.163 | 21.7 | 6.9 | 14.8 | 0.239 | 0.272 | 0.363 | 0.00 | 2.51 | 118 | 471 | 6.89 |
| tripwire lf-route (resample, then retrieve) | 0.356 | 0.320 | 0.263 | 19.3 | 7.5 | 11.8 | 0.322 | 0.327 | 0.417 | 2.02 | 2.77 | 2346 | 532 | 2.48 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 388 | +0.006 | [-0.025, +0.038] | 0.705 |
| tripwire lf-retrieve | flare | right person | 400 | +0.010 | [-0.022, +0.043] | 0.604 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 391 | +0.035 | [+0.009, +0.062] | 0.013 |
| tripwire lf-retrieve | rag (always, up front) | right person | 400 | +0.015 | [-0.015, +0.048] | 0.375 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 399 | +0.066 | [+0.044, +0.089] | 0.000 |
| rag + tripwire lf-retrieve | rag (always, up front) | right person | 400 | +0.020 | [-0.003, +0.045] | 0.121 |
| tripwire lf-resample | vanilla | FActScore | 398 | -0.024 | [-0.046, -0.002] | 0.036 |
| tripwire lf-resample | vanilla | right person | 400 | -0.007 | [-0.030, +0.013] | 0.558 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 398 | -0.014 | [-0.036, +0.006] | 0.171 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | right person | 400 | +0.000 | [-0.015, +0.015] | 1.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 395 | +0.080 | [+0.056, +0.107] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | right person | 400 | +0.100 | [+0.068, +0.135] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 389 | -0.055 | [-0.084, -0.026] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | right person | 400 | -0.037 | [-0.072, -0.003] | 0.038 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 394 | -0.046 | [-0.072, -0.020] | 0.002 |
| tripwire lf-route (resample, then retrieve) | flare | right person | 400 | -0.028 | [-0.062, +0.007] | 0.134 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.866, kappa 0.723

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 2237 | 0.877 | 0.734 | 0.300 | 0.389 |
| rag (always, up front) | 1620 | 0.855 | 0.704 | 0.330 | 0.421 |
| flare | 1793 | 0.847 | 0.692 | 0.375 | 0.484 |
| tripwire lf-retrieve | 1901 | 0.837 | 0.676 | 0.361 | 0.475 |
| rag + tripwire lf-retrieve | 1535 | 0.857 | 0.717 | 0.387 | 0.483 |
| tripwire lf-resample | 1981 | 0.890 | 0.750 | 0.274 | 0.357 |
| flare-signal resample (SHARS-style) | 2067 | 0.886 | 0.746 | 0.287 | 0.358 |
| tripwire lf-route (resample, then retrieve) | 1877 | 0.869 | 0.733 | 0.328 | 0.424 |

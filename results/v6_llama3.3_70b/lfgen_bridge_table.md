### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.675 | 0.694 | tau = 0.7984 |
| FLARE (1 - min token probability) | 0.630 | 0.637 | theta = 0.6224 |

Sentences: {'val': 1678, 'test': 4439}; unsupported rate {'val': 0.7854588796185935, 'test': 0.808740707366524}

### Bridge biographies ("Who directed F? ... bio of that person"), test questions (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | right person | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.390 | 0.388 | 0.532 | 39.8 | 16.6 | 23.2 | 0.340 | 0.376 | 0.455 | 0.00 | 0.00 | 52 | 353 | 8.70 |
| rag (always, up front) | 0.398 | 0.379 | 0.388 | 26.9 | 11.8 | 15.2 | 0.397 | 0.361 | 0.434 | 1.00 | 0.00 | 435 | 274 | 5.69 |
| flare | 0.460 | 0.453 | 0.590 | 36.8 | 17.6 | 19.1 | 0.432 | 0.447 | 0.500 | 3.00 | 0.00 | 1638 | 415 | 1.61 |
| tripwire lf-retrieve | 0.536 | 0.526 | 0.552 | 24.6 | 13.9 | 10.7 | 0.531 | 0.515 | 0.562 | 2.71 | 0.00 | 1501 | 247 | 1.41 |
| rag + tripwire lf-retrieve | 0.470 | 0.433 | 0.415 | 20.4 | 10.4 | 10.0 | 0.466 | 0.439 | 0.505 | 2.69 | 0.00 | 1412 | 227 | 1.84 |
| tripwire lf-resample | 0.393 | 0.392 | 0.527 | 40.2 | 16.8 | 23.4 | 0.339 | 0.371 | 0.467 | 0.00 | 2.86 | 3188 | 674 | 3.34 |
| flare-signal resample (SHARS-style) | 0.398 | 0.395 | 0.535 | 40.7 | 17.1 | 23.6 | 0.330 | 0.393 | 0.471 | 0.00 | 2.99 | 156 | 683 | 3.75 |
| tripwire lf-route (resample, then retrieve) | 0.445 | 0.435 | 0.573 | 37.0 | 17.3 | 19.8 | 0.417 | 0.421 | 0.498 | 2.33 | 2.85 | 4340 | 719 | 1.47 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 400 | +0.076 | [+0.055, +0.097] | 0.000 |
| tripwire lf-retrieve | flare | right person | 400 | -0.037 | [-0.068, -0.010] | 0.009 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 400 | +0.138 | [+0.110, +0.168] | 0.000 |
| tripwire lf-retrieve | rag (always, up front) | right person | 400 | +0.165 | [+0.122, +0.207] | 0.000 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 397 | +0.071 | [+0.050, +0.094] | 0.000 |
| rag + tripwire lf-retrieve | rag (always, up front) | right person | 400 | +0.028 | [+0.003, +0.052] | 0.040 |
| tripwire lf-resample | vanilla | FActScore | 398 | +0.001 | [-0.011, +0.014] | 0.810 |
| tripwire lf-resample | vanilla | right person | 400 | -0.005 | [-0.022, +0.013] | 0.714 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 398 | -0.006 | [-0.017, +0.006] | 0.331 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | right person | 400 | -0.007 | [-0.028, +0.010] | 0.533 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 396 | +0.048 | [+0.032, +0.065] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | right person | 400 | +0.045 | [+0.015, +0.075] | 0.001 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 398 | -0.092 | [-0.115, -0.070] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | right person | 400 | +0.020 | [-0.013, +0.052] | 0.261 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 398 | -0.016 | [-0.034, +0.001] | 0.061 |
| tripwire lf-route (resample, then retrieve) | flare | right person | 400 | -0.018 | [-0.045, +0.010] | 0.241 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.885, kappa 0.767

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 3859 | 0.890 | 0.775 | 0.384 | 0.405 |
| rag (always, up front) | 2556 | 0.866 | 0.722 | 0.334 | 0.423 |
| flare | 3585 | 0.883 | 0.767 | 0.457 | 0.488 |
| tripwire lf-retrieve | 2325 | 0.876 | 0.749 | 0.485 | 0.555 |
| rag + tripwire lf-retrieve | 1892 | 0.855 | 0.712 | 0.413 | 0.515 |
| tripwire lf-resample | 3994 | 0.894 | 0.779 | 0.360 | 0.389 |
| flare-signal resample (SHARS-style) | 3938 | 0.900 | 0.795 | 0.382 | 0.399 |
| tripwire lf-route (resample, then retrieve) | 3602 | 0.888 | 0.775 | 0.427 | 0.456 |

### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.759 | 0.802 | tau = 0.7312 |
| FLARE (1 - min token probability) | 0.715 | 0.668 | theta = 0.2841 |

Sentences: {'val': 1346, 'test': 2589}; unsupported rate {'val': 0.8395245170876672, 'test': 0.8420239474700657}

### Biographies, test people (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.319 | 0.276 | 27.4 | 8.7 | 18.7 | 0.152 | 0.276 | 0.478 | 0.00 | 0.00 | 39 | 303 | 44.52 |
| rag (always, up front) | 0.796 | 0.796 | 32.6 | 26.3 | 6.3 | 0.826 | 0.835 | 0.729 | 1.00 | 0.00 | 484 | 352 | 18.92 |
| flare | 0.484 | 0.461 | 31.0 | 15.4 | 15.6 | 0.435 | 0.418 | 0.587 | 2.70 | 0.00 | 1417 | 403 | 4.45 |
| tripwire lf-retrieve | 0.802 | 0.794 | 28.0 | 22.8 | 5.2 | 0.821 | 0.830 | 0.757 | 2.86 | 0.00 | 1616 | 329 | 1.35 |
| rag + tripwire lf-retrieve | 0.800 | 0.797 | 28.8 | 23.2 | 5.7 | 0.813 | 0.846 | 0.741 | 2.95 | 0.00 | 1617 | 334 | 1.82 |
| tripwire lf-resample | 0.302 | 0.269 | 25.9 | 8.3 | 17.6 | 0.147 | 0.217 | 0.480 | 0.00 | 2.58 | 3190 | 558 | 11.12 |
| flare-signal resample (SHARS-style) | 0.326 | 0.276 | 26.4 | 8.5 | 17.9 | 0.176 | 0.275 | 0.478 | 0.00 | 2.53 | 166 | 565 | 13.33 |
| tripwire lf-route (resample, then retrieve) | 0.458 | 0.432 | 31.8 | 15.0 | 16.7 | 0.405 | 0.432 | 0.530 | 1.79 | 2.77 | 4664 | 664 | 4.19 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 249 | +0.312 | [+0.278, +0.346] | 0.000 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 266 | +0.011 | [-0.012, +0.032] | 0.322 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 269 | +0.017 | [+0.006, +0.029] | 0.002 |
| tripwire lf-resample | vanilla | FActScore | 209 | -0.012 | [-0.034, +0.010] | 0.314 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 204 | -0.017 | [-0.043, +0.007] | 0.166 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 215 | +0.141 | [+0.111, +0.172] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 256 | -0.351 | [-0.384, -0.319] | 0.000 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 240 | -0.031 | [-0.058, -0.007] | 0.013 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.919, kappa 0.837

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 2267 | 0.924 | 0.825 | 0.328 | 0.296 |
| rag (always, up front) | 3143 | 0.918 | 0.761 | 0.778 | 0.761 |
| flare | 2776 | 0.921 | 0.840 | 0.446 | 0.400 |
| tripwire lf-retrieve | 2724 | 0.917 | 0.760 | 0.780 | 0.768 |
| rag + tripwire lf-retrieve | 2801 | 0.915 | 0.756 | 0.787 | 0.768 |
| tripwire lf-resample | 2286 | 0.930 | 0.837 | 0.306 | 0.282 |
| flare-signal resample (SHARS-style) | 2307 | 0.921 | 0.809 | 0.309 | 0.287 |
| tripwire lf-route (resample, then retrieve) | 2805 | 0.908 | 0.813 | 0.444 | 0.395 |

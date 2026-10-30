### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.702 | 0.683 | tau = 0.7874 |
| FLARE (1 - min token probability) | 0.688 | 0.676 | theta = 0.2836 |

Sentences: {'val': 1084, 'test': 1955}; unsupported rate {'val': 0.7804428044280443, 'test': 0.7503836317135549}

### Biographies, test people (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.436 | 0.408 | 20.8 | 10.1 | 10.8 | 0.278 | 0.377 | 0.539 | 0.00 | 0.00 | 45 | 205 | 50.44 |
| rag (always, up front) | 0.792 | 0.789 | 28.9 | 23.1 | 5.8 | 0.833 | 0.814 | 0.731 | 1.00 | 0.00 | 467 | 283 | 17.54 |
| flare | 0.646 | 0.434 | 22.1 | 12.9 | 9.2 | 0.719 | 0.616 | 0.608 | 2.37 | 0.00 | 1241 | 266 | 4.82 |
| tripwire lf-retrieve | 0.817 | 0.809 | 26.0 | 21.1 | 5.0 | 0.838 | 0.840 | 0.776 | 2.65 | 0.00 | 1452 | 270 | 1.44 |
| rag + tripwire lf-retrieve | 0.838 | 0.823 | 25.6 | 21.4 | 4.2 | 0.860 | 0.869 | 0.787 | 2.83 | 0.00 | 1511 | 268 | 1.90 |
| tripwire lf-resample | 0.445 | 0.408 | 19.2 | 9.4 | 9.8 | 0.312 | 0.407 | 0.530 | 0.00 | 2.22 | 2043 | 403 | 12.38 |
| flare-signal resample (SHARS-style) | 0.430 | 0.393 | 20.7 | 9.9 | 10.7 | 0.301 | 0.369 | 0.539 | 0.00 | 2.39 | 122 | 435 | 14.24 |
| tripwire lf-route (resample, then retrieve) | 0.607 | 0.411 | 21.0 | 11.6 | 9.4 | 0.666 | 0.580 | 0.584 | 1.29 | 2.25 | 2842 | 437 | 5.56 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 259 | +0.172 | [+0.141, +0.204] | 0.000 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 268 | +0.031 | [+0.007, +0.056] | 0.010 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 273 | +0.046 | [+0.028, +0.066] | 0.000 |
| tripwire lf-resample | vanilla | FActScore | 169 | +0.014 | [-0.011, +0.041] | 0.275 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 179 | +0.010 | [-0.012, +0.032] | 0.349 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 188 | +0.098 | [+0.061, +0.137] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 240 | -0.204 | [-0.236, -0.170] | 0.000 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 235 | -0.026 | [-0.055, +0.004] | 0.098 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.911, kappa 0.811

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 1998 | 0.895 | 0.790 | 0.419 | 0.375 |
| rag (always, up front) | 2828 | 0.915 | 0.752 | 0.772 | 0.756 |
| flare | 2119 | 0.906 | 0.809 | 0.640 | 0.610 |
| tripwire lf-retrieve | 2481 | 0.927 | 0.801 | 0.775 | 0.757 |
| rag + tripwire lf-retrieve | 2471 | 0.925 | 0.753 | 0.815 | 0.796 |
| tripwire lf-resample | 1767 | 0.899 | 0.797 | 0.442 | 0.387 |
| flare-signal resample (SHARS-style) | 1850 | 0.912 | 0.823 | 0.420 | 0.384 |
| tripwire lf-route (resample, then retrieve) | 1917 | 0.900 | 0.801 | 0.566 | 0.517 |

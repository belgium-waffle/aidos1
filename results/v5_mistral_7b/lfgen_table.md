### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.781 | 0.806 | tau = 0.8675 |
| FLARE (1 - min token probability) | 0.695 | 0.688 | theta = 0.2649 |

Sentences: {'val': 1689, 'test': 3118}; unsupported rate {'val': 0.8827708703374778, 'test': 0.8880692751763951}

### Biographies, test people (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.250 | 0.250 | 34.6 | 9.1 | 25.6 | 0.089 | 0.191 | 0.463 | 0.00 | 0.00 | 14 | 357 | 34.34 |
| rag (always, up front) | 0.766 | 0.761 | 28.6 | 22.3 | 6.3 | 0.793 | 0.781 | 0.725 | 1.00 | 0.00 | 517 | 330 | 16.38 |
| flare | 0.416 | 0.415 | 33.0 | 14.1 | 18.9 | 0.318 | 0.383 | 0.543 | 2.79 | 0.00 | 1735 | 441 | 3.48 |
| tripwire lf-retrieve | 0.757 | 0.745 | 24.3 | 17.7 | 6.6 | 0.800 | 0.804 | 0.669 | 2.37 | 0.00 | 1372 | 279 | 1.63 |
| rag + tripwire lf-retrieve | 0.811 | 0.799 | 23.4 | 19.0 | 4.4 | 0.849 | 0.842 | 0.745 | 2.61 | 0.00 | 1456 | 271 | 2.14 |
| tripwire lf-resample | 0.254 | 0.252 | 34.9 | 9.2 | 25.6 | 0.085 | 0.200 | 0.468 | 0.00 | 2.49 | 2780 | 670 | 10.13 |
| flare-signal resample (SHARS-style) | 0.248 | 0.246 | 34.0 | 8.9 | 25.2 | 0.088 | 0.193 | 0.453 | 0.00 | 2.78 | 221 | 709 | 11.26 |
| tripwire lf-route (resample, then retrieve) | 0.377 | 0.375 | 33.1 | 12.7 | 20.3 | 0.285 | 0.340 | 0.502 | 1.47 | 2.48 | 3596 | 703 | 4.39 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 268 | +0.338 | [+0.302, +0.373] | 0.000 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 271 | -0.013 | [-0.040, +0.015] | 0.350 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 270 | +0.035 | [+0.019, +0.051] | 0.000 |
| tripwire lf-resample | vanilla | FActScore | 269 | +0.003 | [-0.008, +0.014] | 0.553 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 270 | +0.006 | [-0.005, +0.018] | 0.292 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 270 | +0.124 | [+0.101, +0.147] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 268 | -0.378 | [-0.412, -0.344] | 0.000 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 269 | -0.040 | [-0.061, -0.021] | 0.001 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.929, kappa 0.855

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 3514 | 0.941 | 0.836 | 0.239 | 0.209 |
| rag (always, up front) | 2815 | 0.922 | 0.785 | 0.742 | 0.728 |
| flare | 3230 | 0.927 | 0.848 | 0.402 | 0.365 |
| tripwire lf-retrieve | 2379 | 0.911 | 0.799 | 0.706 | 0.697 |
| rag + tripwire lf-retrieve | 2276 | 0.924 | 0.786 | 0.778 | 0.772 |
| tripwire lf-resample | 3458 | 0.939 | 0.828 | 0.242 | 0.210 |
| flare-signal resample (SHARS-style) | 3397 | 0.935 | 0.814 | 0.232 | 0.197 |
| tripwire lf-route (resample, then retrieve) | 3307 | 0.924 | 0.827 | 0.340 | 0.299 |

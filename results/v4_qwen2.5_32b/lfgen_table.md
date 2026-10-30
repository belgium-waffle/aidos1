### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.777 | 0.765 | tau = 0.7785 |
| FLARE (1 - min token probability) | 0.659 | 0.669 | theta = 0.2296 |

Sentences: {'val': 1198, 'test': 2043}; unsupported rate {'val': 0.7445742904841403, 'test': 0.7601566324033284}

### Biographies, test people (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.413 | 0.355 | 23.9 | 10.8 | 13.1 | 0.256 | 0.331 | 0.610 | 0.00 | 0.00 | 39 | 250 | 13.73 |
| rag (always, up front) | 0.852 | 0.845 | 29.5 | 25.3 | 4.2 | 0.863 | 0.888 | 0.808 | 1.00 | 0.00 | 484 | 301 | 7.05 |
| flare | 0.588 | 0.542 | 26.8 | 16.7 | 10.1 | 0.509 | 0.543 | 0.694 | 2.33 | 0.00 | 1347 | 347 | 1.99 |
| tripwire lf-retrieve | 0.837 | 0.818 | 28.8 | 24.0 | 4.8 | 0.858 | 0.837 | 0.818 | 2.41 | 0.00 | 1352 | 321 | 1.21 |
| rag + tripwire lf-retrieve | 0.866 | 0.865 | 29.0 | 25.1 | 3.9 | 0.877 | 0.895 | 0.828 | 2.68 | 0.00 | 1472 | 315 | 1.42 |
| tripwire lf-resample | 0.421 | 0.374 | 24.0 | 10.9 | 13.0 | 0.223 | 0.358 | 0.613 | 0.00 | 2.21 | 2010 | 504 | 4.73 |
| flare-signal resample (SHARS-style) | 0.424 | 0.366 | 23.8 | 11.1 | 12.7 | 0.276 | 0.362 | 0.600 | 0.00 | 2.16 | 124 | 495 | 4.38 |
| tripwire lf-route (resample, then retrieve) | 0.583 | 0.559 | 29.4 | 17.6 | 11.8 | 0.501 | 0.566 | 0.676 | 1.47 | 2.39 | 3129 | 600 | 2.42 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 241 | +0.248 | [+0.216, +0.280] | 0.000 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 251 | -0.019 | [-0.042, +0.004] | 0.109 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 266 | +0.016 | [+0.002, +0.029] | 0.024 |
| tripwire lf-resample | vanilla | FActScore | 217 | -0.005 | [-0.030, +0.021] | 0.746 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 219 | -0.014 | [-0.041, +0.011] | 0.313 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 223 | +0.156 | [+0.125, +0.189] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 254 | -0.256 | [-0.284, -0.228] | 0.000 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 243 | -0.006 | [-0.034, +0.023] | 0.689 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.914, kappa 0.818

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 2262 | 0.923 | 0.841 | 0.404 | 0.369 |
| rag (always, up front) | 2897 | 0.914 | 0.714 | 0.817 | 0.776 |
| flare | 2553 | 0.914 | 0.825 | 0.547 | 0.508 |
| tripwire lf-retrieve | 2679 | 0.920 | 0.745 | 0.828 | 0.801 |
| rag + tripwire lf-retrieve | 2819 | 0.923 | 0.718 | 0.847 | 0.825 |
| tripwire lf-resample | 2298 | 0.909 | 0.813 | 0.414 | 0.361 |
| flare-signal resample (SHARS-style) | 2284 | 0.916 | 0.829 | 0.405 | 0.365 |
| tripwire lf-route (resample, then retrieve) | 2663 | 0.894 | 0.787 | 0.572 | 0.497 |

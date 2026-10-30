### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.659 | 0.678 | tau = 0.7842 |
| FLARE (1 - min token probability) | 0.601 | 0.636 | theta = 0.4424 |

Sentences: {'val': 1543, 'test': 2790}; unsupported rate {'val': 0.7303953337653921, 'test': 0.7279569892473118}

### Biographies, test people (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | resampled | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.469 | 0.455 | 32.6 | 16.1 | 16.5 | 0.311 | 0.454 | 0.591 | 0.00 | 0.00 | 45 | 306 | 8.93 |
| rag (always, up front) | 0.854 | 0.852 | 25.5 | 22.3 | 3.2 | 0.864 | 0.873 | 0.826 | 1.00 | 0.00 | 467 | 256 | 5.44 |
| flare | 0.598 | 0.576 | 30.8 | 18.7 | 12.1 | 0.514 | 0.590 | 0.666 | 2.48 | 0.00 | 1336 | 363 | 1.58 |
| tripwire lf-retrieve | 0.847 | 0.840 | 28.1 | 23.7 | 4.4 | 0.857 | 0.870 | 0.815 | 2.60 | 0.00 | 1452 | 286 | 1.46 |
| rag + tripwire lf-retrieve | 0.879 | 0.870 | 22.4 | 20.0 | 2.4 | 0.906 | 0.872 | 0.861 | 2.68 | 0.00 | 1430 | 244 | 1.83 |
| tripwire lf-resample | 0.495 | 0.487 | 31.6 | 16.3 | 15.3 | 0.336 | 0.481 | 0.607 | 0.00 | 2.60 | 2812 | 568 | 3.09 |
| flare-signal resample (SHARS-style) | 0.477 | 0.472 | 32.5 | 16.4 | 16.1 | 0.315 | 0.464 | 0.604 | 0.00 | 2.39 | 141 | 567 | 2.87 |
| tripwire lf-route (resample, then retrieve) | 0.589 | 0.562 | 33.0 | 19.4 | 13.6 | 0.516 | 0.609 | 0.637 | 2.00 | 2.62 | 4087 | 616 | 1.52 |

### Paired bootstrap over test items (A − B, 95% CI, two-sided p)

| A | B | metric | n | A − B | 95% CI | p |
|---|---|---|---|---|---|---|
| tripwire lf-retrieve | flare | FActScore | 242 | +0.245 | [+0.214, +0.275] | 0.000 |
| tripwire lf-retrieve | rag (always, up front) | FActScore | 264 | +0.001 | [-0.019, +0.022] | 0.975 |
| rag + tripwire lf-retrieve | rag (always, up front) | FActScore | 266 | +0.019 | [+0.008, +0.032] | 0.000 |
| tripwire lf-resample | vanilla | FActScore | 227 | +0.017 | [+0.002, +0.033] | 0.027 |
| tripwire lf-resample | flare-signal resample (SHARS-style) | FActScore | 225 | +0.006 | [-0.011, +0.022] | 0.495 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-resample | FActScore | 225 | +0.099 | [+0.074, +0.126] | 0.000 |
| tripwire lf-route (resample, then retrieve) | tripwire lf-retrieve | FActScore | 259 | -0.260 | [-0.286, -0.236] | 0.000 |
| tripwire lf-route (resample, then retrieve) | flare | FActScore | 235 | -0.002 | [-0.028, +0.024] | 0.836 |

### Second judge (unsloth/Mistral-Small-24B-Instruct-2501) on the same atomic facts of 100 test items (judge 1: Qwen/Qwen2.5-32B-Instruct); overall agreement 0.904, kappa 0.798

| method | facts | agreement | kappa | FActScore judge 1 | FActScore judge 2 |
|---|---|---|---|---|---|
| vanilla | 3074 | 0.895 | 0.789 | 0.459 | 0.408 |
| rag (always, up front) | 2507 | 0.917 | 0.692 | 0.831 | 0.815 |
| flare | 2840 | 0.899 | 0.796 | 0.578 | 0.521 |
| tripwire lf-retrieve | 2681 | 0.918 | 0.713 | 0.826 | 0.808 |
| rag + tripwire lf-retrieve | 2230 | 0.931 | 0.698 | 0.859 | 0.851 |
| tripwire lf-resample | 3020 | 0.891 | 0.781 | 0.464 | 0.400 |
| flare-signal resample (SHARS-style) | 3105 | 0.900 | 0.800 | 0.466 | 0.412 |
| tripwire lf-route (resample, then retrieve) | 3091 | 0.889 | 0.776 | 0.583 | 0.530 |

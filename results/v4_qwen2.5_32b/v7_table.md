### D94 Joint certified budget: hallucination <= alpha AND retrieval rate <= beta (LTT, delta = 0.1, 200 re-splits)

| method | alpha | beta | test acc | test halluc | test retrieval | violation rate | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.05 | 0.2 | 0.312 | 0.026 | 0.006 | 0.070 | lam=2.0,cost=0.8 |
| Tripwire route-eu | 0.05 | 0.35 | 0.447 | 0.034 | 0.243 | 0.000 | lam=2.0,cost=0.5 |
| Tripwire route-eu | 0.05 | 0.5 | 0.447 | 0.034 | 0.243 | 0.000 | lam=2.0,cost=0.5 |
| Tripwire route-eu | 0.1 | 0.2 | 0.436 | 0.077 | 0.036 | 0.000 | lam=0.5,cost=0.8 |
| Tripwire route-eu | 0.1 | 0.35 | 0.494 | 0.055 | 0.225 | 0.005 | lam=1.0,cost=0.5 |
| Tripwire route-eu | 0.1 | 0.5 | 0.549 | 0.060 | 0.389 | 0.000 | lam=1.0,cost=0.3 |
| always-retrieve+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| always-retrieve+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| always-retrieve+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| always-retrieve+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| always-retrieve+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| always-retrieve+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+3band | 0.05 | 0.2 | 0.244 | 0.024 | 0.173 | 0.010 | trig=0.0069,abstain>0.1162,after=0.0 |
| flare+3band | 0.05 | 0.35 | 0.244 | 0.024 | 0.173 | 0.135 | trig=0.0069,abstain>0.1162,after=0.0 |
| flare+3band | 0.05 | 0.5 | 0.246 | 0.024 | 0.364 | 0.135 | trig=0.0069,abstain>0.5245,after=0.0 |
| flare+3band | 0.1 | 0.2 | 0.366 | 0.073 | 0.173 | 0.005 | trig=0.0069,abstain>0.1162,after=1.143 |
| flare+3band | 0.1 | 0.35 | 0.366 | 0.073 | 0.173 | 0.000 | trig=0.0069,abstain>0.1162,after=1.143 |
| flare+3band | 0.1 | 0.5 | 0.366 | 0.073 | 0.173 | 0.045 | trig=0.0069,abstain>0.1162,after=1.143 |
| dragin+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+3band | 0.05 | 0.2 | 0.242 | 0.023 | 0.177 | 0.040 | trig=0.0392,abstain>0.39,after=0.0 |
| dragin+3band | 0.05 | 0.35 | 0.327 | 0.039 | 0.288 | 0.045 | trig=0.0034,abstain>0.39,after=0.0182 |
| dragin+3band | 0.05 | 0.5 | 0.327 | 0.039 | 0.288 | 0.045 | trig=0.0034,abstain>0.39,after=0.0182 |
| dragin+3band | 0.1 | 0.2 | 0.367 | 0.073 | 0.177 | 0.000 | trig=0.0392,abstain>0.39,after=1.2354 |
| dragin+3band | 0.1 | 0.35 | 0.367 | 0.073 | 0.177 | 0.140 | trig=0.0392,abstain>0.39,after=1.2354 |
| dragin+3band | 0.1 | 0.5 | 0.408 | 0.073 | 0.364 | 0.140 | trig=0.0392,abstain>1.0423,after=0.0182 |
| probing-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+3band | 0.05 | 0.2 | 0.349 | 0.032 | 0.188 | 0.005 | trig=0.1522,abstain>0.4342,after=0.0149 |
| probing-rag+3band | 0.05 | 0.35 | 0.349 | 0.032 | 0.188 | 0.005 | trig=0.1522,abstain>0.4342,after=0.0149 |
| probing-rag+3band | 0.05 | 0.5 | 0.349 | 0.032 | 0.188 | 0.005 | trig=0.1522,abstain>0.4342,after=0.0149 |
| probing-rag+3band | 0.1 | 0.2 | 0.386 | 0.059 | 0.077 | 0.005 | trig=0.3043,abstain>0.4342,after=1.1741 |
| probing-rag+3band | 0.1 | 0.35 | 0.448 | 0.072 | 0.247 | 0.000 | trig=0.3043,abstain>0.7604,after=0.0149 |
| probing-rag+3band | 0.1 | 0.5 | 0.448 | 0.072 | 0.247 | 0.000 | trig=0.3043,abstain>0.7604,after=0.0149 |
| sep-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+3band | 0.05 | 0.2 | 0.227 | 0.041 | 0.179 | 0.000 | trig=0.0579,abstain>0.1402,after=0.0 |
| sep-rag+3band | 0.05 | 0.35 | 0.313 | 0.042 | 0.294 | 0.000 | trig=0.0322,abstain>0.1402,after=0.0149 |
| sep-rag+3band | 0.05 | 0.5 | 0.313 | 0.042 | 0.294 | 0.000 | trig=0.0322,abstain>0.1402,after=0.0149 |
| sep-rag+3band | 0.1 | 0.2 | 0.365 | 0.078 | 0.179 | 0.000 | trig=0.0579,abstain>0.1402,after=1.1741 |
| sep-rag+3band | 0.1 | 0.35 | 0.366 | 0.077 | 0.294 | 0.050 | trig=0.0322,abstain>0.1402,after=1.1741 |
| sep-rag+3band | 0.1 | 0.5 | 0.417 | 0.081 | 0.350 | 0.050 | trig=0.0579,abstain>0.388,after=0.0149 |
| se-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.1 | 0.2 | 0.386 | 0.076 | 0.158 | 0.000 | trig=0.0,abstain>0.9404,after=0.0 |
| se-rag+3band | 0.1 | 0.35 | 0.386 | 0.076 | 0.158 | 0.000 | trig=0.0,abstain>0.9404,after=0.0 |
| se-rag+3band | 0.1 | 0.5 | 0.388 | 0.076 | 0.352 | 0.000 | trig=0.0,abstain>1.8344,after=0.0 |

### D95 Label-free online recalibration out of domain (explore eps = 0.1, evidence confidence P(wrong) < 0.3)

Pseudo-labels (closed-book draft vs confident evidence answer):

| split | labelled share | label accuracy | pseudo wrong rate | true wrong rate |
|---|---|---|---|---|
| val | 0.585 | 0.918 | 0.341 | 0.328 |
| test | 0.590 | 0.918 | 0.319 | 0.313 |
| ood | 0.378 | 0.766 | 0.398 | 0.531 |

| lam | dataset | utility: deployed | pseudo-label recal | oracle-label recal | halluc: deployed | pseudo | oracle | retrieval: deployed | pseudo |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 2wikimultihopqa | -0.010 | -0.010 | -0.009 | 0.118 | 0.118 | 0.116 | 0.988 | 0.990 |
| 1.0 | hotpotqa | 0.059 | 0.060 | 0.064 | 0.249 | 0.248 | 0.244 | 0.944 | 0.964 |
| 1.0 | nq | 0.152 | 0.149 | 0.159 | 0.164 | 0.167 | 0.148 | 0.880 | 0.896 |
| 1.0 | sciq | 0.290 | 0.281 | 0.279 | 0.189 | 0.235 | 0.188 | 0.694 | 0.605 |
| 1.0 | all OOD | 0.099 | 0.097 | 0.098 | 0.179 | 0.180 | 0.171 | 0.902 | 0.929 |
| 2.0 | 2wikimultihopqa | -0.059 | -0.059 | -0.059 | 0.056 | 0.056 | 0.056 | 0.993 | 0.994 |
| 2.0 | hotpotqa | -0.092 | -0.089 | -0.084 | 0.176 | 0.174 | 0.171 | 0.960 | 0.974 |
| 2.0 | nq | 0.034 | 0.034 | 0.045 | 0.103 | 0.103 | 0.094 | 0.920 | 0.931 |
| 2.0 | sciq | 0.168 | 0.118 | 0.158 | 0.120 | 0.171 | 0.116 | 0.783 | 0.677 |
| 2.0 | all OOD | -0.009 | -0.009 | -0.007 | 0.113 | 0.112 | 0.107 | 0.933 | 0.957 |
| 4.0 | 2wikimultihopqa | -0.080 | -0.080 | -0.080 | 0.025 | 0.025 | 0.025 | 0.986 | 0.988 |
| 4.0 | hotpotqa | -0.257 | -0.251 | -0.244 | 0.112 | 0.110 | 0.108 | 0.962 | 0.974 |
| 4.0 | nq | -0.069 | -0.076 | -0.064 | 0.054 | 0.055 | 0.050 | 0.913 | 0.925 |
| 4.0 | sciq | 0.004 | -0.050 | 0.009 | 0.070 | 0.096 | 0.065 | 0.842 | 0.777 |
| 4.0 | all OOD | -0.115 | -0.113 | -0.110 | 0.064 | 0.063 | 0.061 | 0.938 | 0.958 |

### D96 Steering as an action (1999 test questions)

(a) Matched abstention: steered answers vs abstaining on the pre head's riskiest unsteered answers

| direction | f | abstention | steer acc | steer halluc | head acc | head halluc | halluc diff [95% CI] |
|---|---|---|---|---|---|---|---|
| meandiff | 0.05 | 0.235 | 0.451 | 0.315 | 0.450 | 0.315 | -0.001 [-0.008, +0.007] |
| meandiff | 0.1 | 0.248 | 0.443 | 0.310 | 0.450 | 0.302 | +0.007 [-0.004, +0.019] |
| meandiff | 0.15 | 0.260 | 0.437 | 0.303 | 0.450 | 0.290 | +0.013 [-0.001, +0.026] |
| meandiff | 0.2 | 0.272 | 0.434 | 0.294 | 0.450 | 0.278 | +0.016 [+0.003, +0.030] |
| meandiff | 0.3 | 0.331 | 0.416 | 0.254 | 0.446 | 0.223 | +0.030 [+0.016, +0.046] |
| probe | 0.05 | 0.244 | 0.450 | 0.306 | 0.450 | 0.306 | -0.000 [-0.008, +0.009] |
| probe | 0.1 | 0.264 | 0.446 | 0.290 | 0.450 | 0.286 | +0.004 [-0.008, +0.015] |
| probe | 0.15 | 0.285 | 0.445 | 0.270 | 0.449 | 0.266 | +0.004 [-0.010, +0.017] |
| probe | 0.2 | 0.302 | 0.443 | 0.255 | 0.448 | 0.250 | +0.005 [-0.009, +0.019] |
| probe | 0.3 | 0.364 | 0.422 | 0.214 | 0.440 | 0.196 | +0.018 [+0.002, +0.033] |
| random0 | 0.05 | 0.239 | 0.448 | 0.314 | 0.450 | 0.311 | +0.003 [-0.004, +0.009] |
| random0 | 0.1 | 0.239 | 0.446 | 0.316 | 0.450 | 0.311 | +0.005 [-0.004, +0.013] |
| random0 | 0.15 | 0.242 | 0.446 | 0.313 | 0.450 | 0.308 | +0.005 [-0.006, +0.015] |
| random0 | 0.2 | 0.241 | 0.445 | 0.315 | 0.450 | 0.309 | +0.006 [-0.006, +0.017] |
| random0 | 0.3 | 0.247 | 0.440 | 0.313 | 0.450 | 0.303 | +0.010 [-0.003, +0.023] |
| random1 | 0.05 | 0.236 | 0.450 | 0.314 | 0.450 | 0.314 | +0.001 [-0.006, +0.007] |
| random1 | 0.1 | 0.243 | 0.447 | 0.310 | 0.450 | 0.307 | +0.003 [-0.005, +0.012] |
| random1 | 0.15 | 0.251 | 0.444 | 0.305 | 0.450 | 0.299 | +0.006 [-0.004, +0.017] |
| random1 | 0.2 | 0.259 | 0.442 | 0.299 | 0.450 | 0.291 | +0.008 [-0.003, +0.019] |
| random1 | 0.3 | 0.276 | 0.440 | 0.284 | 0.450 | 0.275 | +0.009 [-0.004, +0.022] |

(b) Router with a steer band vs without (50 random halves; thresholds on one half, utility on the other)

| lam | retrieval cost | utility 3-action | utility 4-action | diff [95%] | halves 4 better | retrieval 3 | retrieval 4 | steered share |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.02 | 0.481 | 0.480 | -0.0009 [-0.0090, +0.0049] | 0.320 | 0.748 | 0.741 | 0.214 |
| 1.0 | 0.1 | 0.426 | 0.426 | -0.0002 [-0.0040, +0.0034] | 0.340 | 0.676 | 0.676 | 0.280 |
| 1.0 | 0.2 | 0.363 | 0.361 | -0.0025 [-0.0125, +0.0049] | 0.280 | 0.495 | 0.473 | 0.259 |
| 2.0 | 0.02 | 0.403 | 0.404 | +0.0013 [-0.0086, +0.0096] | 0.440 | 0.773 | 0.760 | 0.213 |
| 2.0 | 0.1 | 0.343 | 0.342 | -0.0010 [-0.0212, +0.0062] | 0.280 | 0.628 | 0.630 | 0.249 |
| 2.0 | 0.2 | 0.291 | 0.288 | -0.0030 [-0.0311, +0.0061] | 0.260 | 0.471 | 0.466 | 0.244 |

### D99 Budgeted route-eu configs: simulation (test split) vs the real engine (bench questions)

| mode | sim acc | sim halluc | sim retrieval | engine acc | engine halluc [95% CI] | engine retrieval |
|---|---|---|---|---|---|---|
| route-eu-cost0.2 | 0.561 | 0.060 | 0.458 | - | - | - |
| route-eu-cost0.3 | 0.549 | 0.060 | 0.389 | - | - | - |
| route-eu-cost0.5 | 0.494 | 0.055 | 0.225 | - | - | - |
| route-eu-lam2-cost0.3 | 0.492 | 0.036 | 0.391 | - | - | - |
| route-eu-lam2-cost0.5 | 0.447 | 0.034 | 0.243 | - | - | - |

### D97 Speculative retrieval (search started at arrival; search 302 ms): latency bound, c1

| method | n | E2E p50 | p90 | p99 | speculative p50 | p90 | p99 | mean saving ms | wasted searches / q |
|---|---|---|---|---|---|---|---|---|---|
| route-eu | 100 | 427 | 490 | 566 | 376 | 441 | 490 | 34 | 0.250 |
| route-eu-2r | 100 | 451 | 744 | 833 | 406 | 704 | 793 | 35 | 0.240 |

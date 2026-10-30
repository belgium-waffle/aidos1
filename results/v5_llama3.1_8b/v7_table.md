### D94 Joint certified budget: hallucination <= alpha AND retrieval rate <= beta (LTT, delta = 0.1, 200 re-splits)

| method | alpha | beta | test acc | test halluc | test retrieval | violation rate | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.05 | 0.2 | 0.350 | 0.034 | 0.148 | 0.000 | lam=2.0,cost=0.5 |
| Tripwire route-eu | 0.05 | 0.35 | 0.380 | 0.036 | 0.272 | 0.000 | lam=2.0,cost=0.3 |
| Tripwire route-eu | 0.05 | 0.5 | 0.380 | 0.036 | 0.272 | 0.000 | lam=2.0,cost=0.3 |
| Tripwire route-eu | 0.1 | 0.2 | 0.428 | 0.063 | 0.160 | 0.000 | lam=1.0,cost=0.5 |
| Tripwire route-eu | 0.1 | 0.35 | 0.428 | 0.063 | 0.160 | 0.020 | lam=1.0,cost=0.5 |
| Tripwire route-eu | 0.1 | 0.5 | 0.499 | 0.065 | 0.465 | 0.000 | lam=1.0,cost=0.2 |
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
| flare+3band | 0.05 | 0.2 | 0.238 | 0.041 | 0.164 | 0.055 | trig=0.3136,abstain>0.544,after=0.0004 |
| flare+3band | 0.05 | 0.35 | 0.238 | 0.041 | 0.164 | 0.085 | trig=0.3136,abstain>0.544,after=0.0004 |
| flare+3band | 0.05 | 0.5 | 0.243 | 0.042 | 0.329 | 0.075 | trig=0.3136,abstain>0.8298,after=0.0004 |
| flare+3band | 0.1 | 0.2 | 0.354 | 0.077 | 0.164 | 0.010 | trig=0.3136,abstain>0.544,after=1.2662 |
| flare+3band | 0.1 | 0.35 | 0.363 | 0.087 | 0.225 | 0.035 | trig=0.461,abstain>0.8298,after=0.0254 |
| flare+3band | 0.1 | 0.5 | 0.372 | 0.090 | 0.443 | 0.030 | trig=0.1627,abstain>0.8298,after=0.3526 |
| dragin+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+3band | 0.05 | 0.2 | 0.215 | 0.032 | 0.098 | 0.115 | trig=0.4571,abstain>0.6191,after=1.2681 |
| dragin+3band | 0.05 | 0.35 | 0.290 | 0.044 | 0.162 | 0.030 | trig=0.6454,abstain>0.9252,after=0.0348 |
| dragin+3band | 0.05 | 0.5 | 0.290 | 0.044 | 0.162 | 0.035 | trig=0.6454,abstain>0.9252,after=0.0348 |
| dragin+3band | 0.1 | 0.2 | 0.381 | 0.083 | 0.148 | 0.010 | trig=1.0439,abstain>1.6063,after=0.0004 |
| dragin+3band | 0.1 | 0.35 | 0.381 | 0.083 | 0.148 | 0.100 | trig=1.0439,abstain>1.6063,after=0.0004 |
| dragin+3band | 0.1 | 0.5 | 0.402 | 0.087 | 0.434 | 0.100 | trig=0.7661,abstain>2.3588,after=0.0348 |
| probing-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+3band | 0.05 | 0.2 | 0.278 | 0.032 | 0.175 | 0.085 | trig=0.2103,abstain>0.4249,after=0.0389 |
| probing-rag+3band | 0.05 | 0.35 | 0.303 | 0.037 | 0.278 | 0.180 | trig=0.1099,abstain>0.4249,after=0.4014 |
| probing-rag+3band | 0.05 | 0.5 | 0.325 | 0.046 | 0.380 | 0.005 | trig=0.2103,abstain>0.6943,after=0.0389 |
| probing-rag+3band | 0.1 | 0.2 | 0.378 | 0.099 | 0.165 | 0.125 | trig=0.4805,abstain>0.6943,after=0.0004 |
| probing-rag+3band | 0.1 | 0.35 | 0.421 | 0.102 | 0.282 | 0.200 | trig=0.3276,abstain>0.6943,after=0.4014 |
| probing-rag+3band | 0.1 | 0.5 | 0.421 | 0.102 | 0.282 | 0.200 | trig=0.3276,abstain>0.6943,after=0.4014 |
| sep-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+3band | 0.05 | 0.2 | 0.278 | 0.037 | 0.181 | 0.010 | trig=0.1121,abstain>0.3258,after=0.0389 |
| sep-rag+3band | 0.05 | 0.35 | 0.278 | 0.037 | 0.181 | 0.050 | trig=0.1121,abstain>0.3258,after=0.0389 |
| sep-rag+3band | 0.05 | 0.5 | 0.278 | 0.037 | 0.181 | 0.050 | trig=0.1121,abstain>0.3258,after=0.0389 |
| sep-rag+3band | 0.1 | 0.2 | 0.353 | 0.077 | 0.181 | 0.005 | trig=0.1121,abstain>0.3258,after=1.2995 |
| sep-rag+3band | 0.1 | 0.35 | 0.371 | 0.074 | 0.247 | 0.000 | trig=0.2257,abstain>0.631,after=0.0389 |
| sep-rag+3band | 0.1 | 0.5 | 0.407 | 0.093 | 0.429 | 0.000 | trig=0.2257,abstain>0.8916,after=0.0389 |
| se-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.2 | 0.312 | 0.044 | 0.026 | 0.110 | trig=0.5004,abstain>0.639,after=0.0004 |
| se-rag+3band | 0.05 | 0.35 | 0.315 | 0.044 | 0.255 | 0.110 | trig=0.5004,abstain>1.4979,after=0.0004 |
| se-rag+3band | 0.05 | 0.5 | 0.304 | 0.037 | 0.120 | 0.095 | trig=-0.0,abstain>0.639,after=0.4014 |
| se-rag+3band | 0.1 | 0.2 | 0.406 | 0.085 | 0.161 | 0.000 | trig=0.8979,abstain>1.4979,after=0.0389 |
| se-rag+3band | 0.1 | 0.35 | 0.406 | 0.085 | 0.161 | 0.005 | trig=0.8979,abstain>1.4979,after=0.0389 |
| se-rag+3band | 0.1 | 0.5 | 0.406 | 0.085 | 0.161 | 0.010 | trig=0.8979,abstain>1.4979,after=0.0389 |

### D95 Label-free online recalibration out of domain (explore eps = 0.1, evidence confidence P(wrong) < 0.3)

Pseudo-labels (closed-book draft vs confident evidence answer):

| split | labelled share | label accuracy | pseudo wrong rate | true wrong rate |
|---|---|---|---|---|
| val | 0.535 | 0.892 | 0.305 | 0.282 |
| test | 0.525 | 0.897 | 0.315 | 0.298 |
| ood | 0.294 | 0.766 | 0.480 | 0.593 |

| lam | dataset | utility: deployed | pseudo-label recal | oracle-label recal | halluc: deployed | pseudo | oracle | retrieval: deployed | pseudo |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 2wikimultihopqa | -0.087 | -0.087 | -0.086 | 0.108 | 0.108 | 0.106 | 0.985 | 0.986 |
| 1.0 | hotpotqa | -0.002 | -0.001 | 0.004 | 0.220 | 0.220 | 0.213 | 0.957 | 0.965 |
| 1.0 | nq | 0.084 | 0.085 | 0.095 | 0.153 | 0.155 | 0.130 | 0.842 | 0.861 |
| 1.0 | sciq | 0.168 | 0.154 | 0.150 | 0.226 | 0.227 | 0.211 | 0.651 | 0.735 |
| 1.0 | all OOD | 0.023 | 0.023 | 0.022 | 0.170 | 0.164 | 0.156 | 0.888 | 0.931 |
| 2.0 | 2wikimultihopqa | -0.082 | -0.082 | -0.082 | 0.040 | 0.040 | 0.040 | 0.990 | 0.991 |
| 2.0 | hotpotqa | -0.098 | -0.098 | -0.091 | 0.122 | 0.123 | 0.118 | 0.973 | 0.977 |
| 2.0 | nq | -0.006 | -0.007 | 0.006 | 0.085 | 0.084 | 0.073 | 0.891 | 0.909 |
| 2.0 | sciq | 0.052 | 0.052 | 0.052 | 0.128 | 0.122 | 0.111 | 0.740 | 0.812 |
| 2.0 | all OOD | -0.046 | -0.044 | -0.044 | 0.089 | 0.084 | 0.081 | 0.921 | 0.955 |
| 4.0 | 2wikimultihopqa | -0.061 | -0.061 | -0.061 | 0.012 | 0.012 | 0.012 | 0.980 | 0.982 |
| 4.0 | hotpotqa | -0.178 | -0.179 | -0.171 | 0.066 | 0.066 | 0.063 | 0.962 | 0.968 |
| 4.0 | nq | -0.082 | -0.080 | -0.069 | 0.042 | 0.041 | 0.037 | 0.876 | 0.895 |
| 4.0 | sciq | -0.038 | -0.037 | -0.040 | 0.062 | 0.058 | 0.054 | 0.818 | 0.869 |
| 4.0 | all OOD | -0.097 | -0.096 | -0.095 | 0.043 | 0.041 | 0.039 | 0.922 | 0.947 |

### D96 Steering as an action (2000 test questions)

(a) Matched abstention: steered answers vs abstaining on the pre head's riskiest unsteered answers

| direction | f | abstention | steer acc | steer halluc | head acc | head halluc | halluc diff [95% CI] |
|---|---|---|---|---|---|---|---|
| meandiff | 0.05 | 0.178 | 0.467 | 0.355 | 0.464 | 0.357 | -0.003 [-0.012, +0.006] |
| meandiff | 0.1 | 0.200 | 0.467 | 0.333 | 0.463 | 0.337 | -0.004 [-0.017, +0.007] |
| meandiff | 0.15 | 0.236 | 0.461 | 0.302 | 0.458 | 0.306 | -0.004 [-0.019, +0.011] |
| meandiff | 0.2 | 0.267 | 0.459 | 0.275 | 0.450 | 0.283 | -0.009 [-0.024, +0.007] |
| meandiff | 0.3 | 0.365 | 0.432 | 0.202 | 0.429 | 0.205 | -0.003 [-0.019, +0.013] |
| probe | 0.05 | 0.147 | 0.469 | 0.383 | 0.466 | 0.380 | +0.003 [-0.004, +0.009] |
| probe | 0.1 | 0.140 | 0.473 | 0.387 | 0.466 | 0.380 | +0.006 [-0.002, +0.014] |
| probe | 0.15 | 0.133 | 0.472 | 0.395 | 0.466 | 0.380 | +0.015 [+0.005, +0.024] |
| probe | 0.2 | 0.128 | 0.472 | 0.400 | 0.466 | 0.380 | +0.020 [+0.010, +0.030] |
| probe | 0.3 | 0.117 | 0.469 | 0.413 | 0.466 | 0.380 | +0.033 [+0.020, +0.045] |
| random0 | 0.05 | 0.144 | 0.470 | 0.386 | 0.466 | 0.380 | +0.005 [-0.001, +0.012] |
| random0 | 0.1 | 0.133 | 0.475 | 0.392 | 0.466 | 0.380 | +0.011 [+0.003, +0.020] |
| random0 | 0.15 | 0.126 | 0.474 | 0.400 | 0.466 | 0.380 | +0.019 [+0.010, +0.029] |
| random0 | 0.2 | 0.121 | 0.477 | 0.402 | 0.466 | 0.380 | +0.022 [+0.011, +0.032] |
| random0 | 0.3 | 0.113 | 0.470 | 0.417 | 0.466 | 0.380 | +0.037 [+0.025, +0.049] |
| random1 | 0.05 | 0.150 | 0.468 | 0.382 | 0.466 | 0.380 | +0.002 [-0.004, +0.007] |
| random1 | 0.1 | 0.144 | 0.472 | 0.384 | 0.466 | 0.380 | +0.003 [-0.005, +0.011] |
| random1 | 0.15 | 0.141 | 0.474 | 0.386 | 0.466 | 0.380 | +0.005 [-0.004, +0.014] |
| random1 | 0.2 | 0.137 | 0.473 | 0.390 | 0.466 | 0.380 | +0.009 [-0.001, +0.019] |
| random1 | 0.3 | 0.138 | 0.473 | 0.390 | 0.466 | 0.380 | +0.009 [-0.001, +0.020] |

(b) Router with a steer band vs without (50 random halves; thresholds on one half, utility on the other)

| lam | retrieval cost | utility 3-action | utility 4-action | diff [95%] | halves 4 better | retrieval 3 | retrieval 4 | steered share |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.02 | 0.417 | 0.419 | +0.0021 [-0.0056, +0.0194] | 0.560 | 0.795 | 0.777 | 0.134 |
| 1.0 | 0.1 | 0.363 | 0.361 | -0.0028 [-0.0111, +0.0028] | 0.160 | 0.631 | 0.639 | 0.229 |
| 1.0 | 0.2 | 0.305 | 0.298 | -0.0065 [-0.0362, +0.0089] | 0.140 | 0.476 | 0.453 | 0.252 |
| 2.0 | 0.02 | 0.355 | 0.357 | +0.0020 [-0.0068, +0.0111] | 0.540 | 0.789 | 0.777 | 0.137 |
| 2.0 | 0.1 | 0.297 | 0.297 | +0.0001 [-0.0110, +0.0200] | 0.400 | 0.675 | 0.688 | 0.181 |
| 2.0 | 0.2 | 0.239 | 0.237 | -0.0023 [-0.0155, +0.0049] | 0.340 | 0.505 | 0.517 | 0.233 |

### D99 Budgeted route-eu configs: simulation (test split) vs the real engine (bench questions)

| mode | sim acc | sim halluc | sim retrieval | engine acc | engine halluc [95% CI] | engine retrieval |
|---|---|---|---|---|---|---|
| route-eu-cost0.2 | 0.499 | 0.065 | 0.465 | - | - | - |
| route-eu-cost0.3 | 0.479 | 0.064 | 0.342 | - | - | - |
| route-eu-cost0.5 | 0.428 | 0.063 | 0.160 | - | - | - |
| route-eu-lam2-cost0.3 | 0.380 | 0.036 | 0.272 | - | - | - |
| route-eu-lam2-cost0.5 | 0.350 | 0.034 | 0.148 | - | - | - |

### D97 Speculative retrieval (search started at arrival; search 302 ms): latency bound, c1

| method | n | E2E p50 | p90 | p99 | speculative p50 | p90 | p99 | mean saving ms | wasted searches / q |
|---|---|---|---|---|---|---|---|---|---|
| route-eu | 100 | 324 | 358 | 415 | 311 | 342 | 380 | 10 | 0.250 |
| route-eu-2r | 100 | 358 | 660 | 711 | 342 | 648 | 699 | 11 | 0.230 |

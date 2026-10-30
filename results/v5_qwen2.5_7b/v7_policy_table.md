### D94 Joint certified budget: hallucination <= alpha AND retrieval rate <= beta (LTT, delta = 0.1, 200 re-splits)

| method | alpha | beta | test acc | test halluc | test retrieval | violation rate | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.05 | 0.2 | 0.286 | 0.025 | 0.169 | 0.000 | lam=2.0,cost=0.5 |
| Tripwire route-eu | 0.05 | 0.35 | 0.286 | 0.025 | 0.169 | 0.070 | lam=2.0,cost=0.5 |
| Tripwire route-eu | 0.05 | 0.5 | 0.391 | 0.035 | 0.461 | 0.000 | lam=2.0,cost=0.2 |
| Tripwire route-eu | 0.1 | 0.2 | 0.339 | 0.076 | 0.069 | 0.000 | lam=0.5,cost=0.8 |
| Tripwire route-eu | 0.1 | 0.35 | 0.426 | 0.085 | 0.240 | 0.000 | lam=0.5,cost=0.5 |
| Tripwire route-eu | 0.1 | 0.5 | 0.442 | 0.059 | 0.416 | 0.050 | lam=1.0,cost=0.3 |
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
| flare+3band | 0.05 | 0.2 | 0.200 | 0.049 | 0.172 | 0.075 | trig=0.0657,abstain>0.3811,after=0.0 |
| flare+3band | 0.05 | 0.35 | 0.194 | 0.032 | 0.265 | 0.000 | trig=0.0131,abstain>0.3811,after=0.0002 |
| flare+3band | 0.05 | 0.5 | 0.200 | 0.049 | 0.357 | 0.070 | trig=0.0657,abstain>0.8615,after=0.0 |
| flare+3band | 0.1 | 0.2 | 0.276 | 0.074 | 0.172 | 0.070 | trig=0.0657,abstain>0.3811,after=0.0207 |
| flare+3band | 0.1 | 0.35 | 0.276 | 0.074 | 0.172 | 0.000 | trig=0.0657,abstain>0.3811,after=0.0207 |
| flare+3band | 0.1 | 0.5 | 0.276 | 0.074 | 0.172 | 0.065 | trig=0.0657,abstain>0.3811,after=0.0207 |
| dragin+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+3band | 0.05 | 0.2 | 0.199 | 0.045 | 0.176 | 0.010 | trig=0.2688,abstain>0.8638,after=0.0 |
| dragin+3band | 0.05 | 0.35 | 0.203 | 0.025 | 0.267 | 0.005 | trig=0.0726,abstain>0.8638,after=0.0003 |
| dragin+3band | 0.05 | 0.5 | 0.203 | 0.025 | 0.267 | 0.105 | trig=0.0726,abstain>0.8638,after=0.0003 |
| dragin+3band | 0.1 | 0.2 | 0.281 | 0.068 | 0.176 | 0.085 | trig=0.2688,abstain>0.8638,after=0.0301 |
| dragin+3band | 0.1 | 0.35 | 0.281 | 0.068 | 0.176 | 0.110 | trig=0.2688,abstain>0.8638,after=0.0301 |
| dragin+3band | 0.1 | 0.5 | 0.281 | 0.068 | 0.176 | 0.120 | trig=0.2688,abstain>0.8638,after=0.0301 |
| probing-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+3band | 0.05 | 0.2 | 0.218 | 0.045 | 0.183 | 0.025 | trig=0.3611,abstain>0.6832,after=0.0 |
| probing-rag+3band | 0.05 | 0.35 | 0.283 | 0.047 | 0.296 | 0.035 | trig=0.1616,abstain>0.6832,after=0.0302 |
| probing-rag+3band | 0.05 | 0.5 | 0.283 | 0.047 | 0.296 | 0.035 | trig=0.1616,abstain>0.6832,after=0.0302 |
| probing-rag+3band | 0.1 | 0.2 | 0.305 | 0.067 | 0.183 | 0.035 | trig=0.3611,abstain>0.6832,after=0.0302 |
| probing-rag+3band | 0.1 | 0.35 | 0.344 | 0.093 | 0.296 | 0.015 | trig=0.1616,abstain>0.6832,after=0.8003 |
| probing-rag+3band | 0.1 | 0.5 | 0.344 | 0.093 | 0.296 | 0.005 | trig=0.1616,abstain>0.6832,after=0.8003 |
| sep-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+3band | 0.05 | 0.2 | 0.172 | 0.041 | 0.087 | 0.030 | trig=0.053,abstain>0.1073,after=0.0302 |
| sep-rag+3band | 0.05 | 0.35 | 0.196 | 0.039 | 0.274 | 0.005 | trig=0.053,abstain>0.3257,after=0.0003 |
| sep-rag+3band | 0.05 | 0.5 | 0.196 | 0.039 | 0.274 | 0.010 | trig=0.053,abstain>0.3257,after=0.0003 |
| sep-rag+3band | 0.1 | 0.2 | 0.270 | 0.090 | 0.170 | 0.000 | trig=0.1227,abstain>0.3257,after=0.0302 |
| sep-rag+3band | 0.1 | 0.35 | 0.270 | 0.090 | 0.170 | 0.005 | trig=0.1227,abstain>0.3257,after=0.0302 |
| sep-rag+3band | 0.1 | 0.5 | 0.334 | 0.104 | 0.468 | 0.110 | trig=0.053,abstain>0.6361,after=0.0302 |
| se-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.1 | 0.2 | 0.304 | 0.095 | 0.100 | 0.025 | trig=0.0,abstain>0.639,after=0.8003 |
| se-rag+3band | 0.1 | 0.35 | 0.311 | 0.082 | 0.316 | 0.000 | trig=0.0,abstain>1.578,after=0.0003 |
| se-rag+3band | 0.1 | 0.5 | 0.311 | 0.082 | 0.316 | 0.000 | trig=0.0,abstain>1.578,after=0.0003 |

### D95 Label-free online recalibration out of domain (explore eps = 0.1, evidence confidence P(wrong) < 0.3)

Pseudo-labels (closed-book draft vs confident evidence answer):

| split | labelled share | label accuracy | pseudo wrong rate | true wrong rate |
|---|---|---|---|---|
| val | 0.488 | 0.914 | 0.462 | 0.425 |
| test | 0.485 | 0.902 | 0.454 | 0.420 |
| ood | 0.236 | 0.813 | 0.563 | 0.629 |

| lam | dataset | utility: deployed | pseudo-label recal | oracle-label recal | halluc: deployed | pseudo | oracle | retrieval: deployed | pseudo |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 2wikimultihopqa | -0.068 | -0.068 | -0.069 | 0.069 | 0.069 | 0.069 | 0.846 | 0.862 |
| 1.0 | hotpotqa | -0.004 | -0.005 | -0.003 | 0.208 | 0.209 | 0.206 | 0.945 | 0.953 |
| 1.0 | nq | 0.102 | 0.100 | 0.100 | 0.123 | 0.122 | 0.113 | 0.875 | 0.893 |
| 1.0 | sciq | 0.182 | 0.168 | 0.167 | 0.186 | 0.215 | 0.169 | 0.577 | 0.590 |
| 1.0 | all OOD | 0.035 | 0.032 | 0.026 | 0.141 | 0.140 | 0.132 | 0.844 | 0.872 |
| 2.0 | 2wikimultihopqa | -0.052 | -0.052 | -0.052 | 0.021 | 0.021 | 0.021 | 0.824 | 0.842 |
| 2.0 | hotpotqa | -0.099 | -0.099 | -0.099 | 0.118 | 0.118 | 0.117 | 0.936 | 0.946 |
| 2.0 | nq | 0.018 | 0.019 | 0.022 | 0.066 | 0.064 | 0.058 | 0.877 | 0.894 |
| 2.0 | sciq | 0.070 | 0.032 | 0.057 | 0.106 | 0.129 | 0.082 | 0.647 | 0.673 |
| 2.0 | all OOD | -0.028 | -0.028 | -0.030 | 0.074 | 0.071 | 0.066 | 0.846 | 0.875 |
| 4.0 | 2wikimultihopqa | -0.039 | -0.039 | -0.039 | 0.007 | 0.007 | 0.007 | 0.733 | 0.762 |
| 4.0 | hotpotqa | -0.159 | -0.160 | -0.159 | 0.061 | 0.061 | 0.060 | 0.884 | 0.899 |
| 4.0 | nq | -0.056 | -0.057 | -0.058 | 0.033 | 0.032 | 0.031 | 0.820 | 0.841 |
| 4.0 | sciq | 0.013 | -0.024 | -0.005 | 0.042 | 0.048 | 0.032 | 0.683 | 0.738 |
| 4.0 | all OOD | -0.071 | -0.076 | -0.076 | 0.034 | 0.034 | 0.032 | 0.794 | 0.824 |

### D96 Steering as an action (1995 test questions)

(a) Matched abstention: steered answers vs abstaining on the pre head's riskiest unsteered answers

| direction | f | abstention | steer acc | steer halluc | head acc | head halluc | halluc diff [95% CI] |
|---|---|---|---|---|---|---|---|
| meandiff | 0.05 | 0.402 | 0.335 | 0.264 | 0.341 | 0.257 | +0.007 [-0.005, +0.018] |
| meandiff | 0.1 | 0.458 | 0.313 | 0.229 | 0.330 | 0.212 | +0.017 [+0.003, +0.031] |
| meandiff | 0.15 | 0.519 | 0.294 | 0.187 | 0.316 | 0.165 | +0.022 [+0.007, +0.037] |
| meandiff | 0.2 | 0.593 | 0.265 | 0.142 | 0.293 | 0.114 | +0.027 [+0.012, +0.042] |
| meandiff | 0.3 | 0.758 | 0.181 | 0.061 | 0.203 | 0.040 | +0.022 [+0.010, +0.033] |
| probe | 0.05 | 0.384 | 0.338 | 0.278 | 0.343 | 0.273 | +0.005 [-0.006, +0.015] |
| probe | 0.1 | 0.427 | 0.325 | 0.248 | 0.336 | 0.237 | +0.011 [-0.001, +0.024] |
| probe | 0.15 | 0.465 | 0.309 | 0.226 | 0.328 | 0.207 | +0.019 [+0.005, +0.033] |
| probe | 0.2 | 0.500 | 0.295 | 0.205 | 0.321 | 0.178 | +0.026 [+0.010, +0.042] |
| probe | 0.3 | 0.557 | 0.276 | 0.167 | 0.306 | 0.137 | +0.029 [+0.015, +0.045] |
| random0 | 0.05 | 0.336 | 0.344 | 0.320 | 0.345 | 0.302 | +0.018 [+0.012, +0.025] |
| random0 | 0.1 | 0.319 | 0.347 | 0.333 | 0.345 | 0.302 | +0.032 [+0.023, +0.040] |
| random0 | 0.15 | 0.304 | 0.349 | 0.346 | 0.345 | 0.302 | +0.045 [+0.035, +0.055] |
| random0 | 0.2 | 0.289 | 0.349 | 0.362 | 0.345 | 0.302 | +0.060 [+0.047, +0.073] |
| random0 | 0.3 | 0.266 | 0.349 | 0.385 | 0.345 | 0.302 | +0.083 [+0.067, +0.098] |
| random1 | 0.05 | 0.371 | 0.340 | 0.288 | 0.345 | 0.284 | +0.004 [-0.003, +0.013] |
| random1 | 0.1 | 0.394 | 0.334 | 0.271 | 0.342 | 0.263 | +0.008 [-0.002, +0.018] |
| random1 | 0.15 | 0.421 | 0.325 | 0.254 | 0.337 | 0.242 | +0.012 [-0.001, +0.024] |
| random1 | 0.2 | 0.445 | 0.316 | 0.239 | 0.333 | 0.222 | +0.017 [+0.003, +0.031] |
| random1 | 0.3 | 0.490 | 0.296 | 0.214 | 0.323 | 0.187 | +0.026 [+0.011, +0.043] |

(b) Router with a steer band vs without (50 random halves; thresholds on one half, utility on the other)

| lam | retrieval cost | utility 3-action | utility 4-action | diff [95%] | halves 4 better | retrieval 3 | retrieval 4 | steered share |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.02 | 0.368 | 0.365 | -0.0033 [-0.0143, +0.0102] | 0.100 | 0.836 | 0.827 | 0.125 |
| 1.0 | 0.1 | 0.304 | 0.301 | -0.0025 [-0.0084, +0.0000] | 0.020 | 0.742 | 0.740 | 0.133 |
| 1.0 | 0.2 | 0.238 | 0.234 | -0.0037 [-0.0193, +0.0044] | 0.180 | 0.500 | 0.489 | 0.136 |
| 2.0 | 0.02 | 0.304 | 0.302 | -0.0014 [-0.0111, +0.0050] | 0.220 | 0.923 | 0.872 | 0.104 |
| 2.0 | 0.1 | 0.232 | 0.231 | -0.0009 [-0.0162, +0.0133] | 0.300 | 0.724 | 0.701 | 0.132 |
| 2.0 | 0.2 | 0.176 | 0.170 | -0.0062 [-0.0297, +0.0208] | 0.240 | 0.512 | 0.501 | 0.130 |

### D99 Budgeted route-eu configs: simulation (test split) vs the real engine (bench questions)

| mode | sim acc | sim halluc | sim retrieval | engine acc | engine halluc [95% CI] | engine retrieval |
|---|---|---|---|---|---|---|
| route-eu-cost0.2 | 0.463 | 0.065 | 0.514 | - | - | - |
| route-eu-cost0.3 | 0.442 | 0.059 | 0.416 | - | - | - |
| route-eu-cost0.5 | 0.392 | 0.052 | 0.261 | - | - | - |
| route-eu-lam2-cost0.3 | 0.358 | 0.031 | 0.340 | - | - | - |
| route-eu-lam2-cost0.5 | 0.286 | 0.025 | 0.169 | - | - | - |

### D97 Speculative retrieval (search started at arrival; search 299 ms): latency bound, c1

| method | n | E2E p50 | p90 | p99 | speculative p50 | p90 | p99 | mean saving ms | wasted searches / q |
|---|---|---|---|---|---|---|---|---|---|
| route-eu | 100 | 319 | 366 | 398 | 308 | 353 | 388 | 8 | 0.360 |
| route-eu-2r | 100 | 337 | 652 | 702 | 325 | 641 | 692 | 8 | 0.360 |

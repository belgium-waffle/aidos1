### D94 Joint certified budget: hallucination <= alpha AND retrieval rate <= beta (LTT, delta = 0.1, 200 re-splits)

| method | alpha | beta | test acc | test halluc | test retrieval | violation rate | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.05 | 0.2 | 0.307 | 0.030 | 0.109 | 0.000 | lam=2.0,cost=0.5 |
| Tripwire route-eu | 0.05 | 0.35 | 0.355 | 0.033 | 0.266 | 0.000 | lam=2.0,cost=0.3 |
| Tripwire route-eu | 0.05 | 0.5 | 0.355 | 0.033 | 0.266 | 0.010 | lam=2.0,cost=0.3 |
| Tripwire route-eu | 0.1 | 0.2 | 0.406 | 0.067 | 0.154 | 0.000 | lam=1.0,cost=0.5 |
| Tripwire route-eu | 0.1 | 0.35 | 0.406 | 0.067 | 0.154 | 0.000 | lam=1.0,cost=0.5 |
| Tripwire route-eu | 0.1 | 0.5 | 0.470 | 0.073 | 0.438 | 0.000 | lam=1.0,cost=0.2 |
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
| flare+3band | 0.05 | 0.2 | 0.205 | 0.037 | 0.089 | 0.010 | trig=0.0173,abstain>0.1269,after=1.3881 |
| flare+3band | 0.05 | 0.35 | 0.226 | 0.047 | 0.165 | 0.005 | trig=0.1646,abstain>0.4939,after=0.0042 |
| flare+3band | 0.05 | 0.5 | 0.226 | 0.047 | 0.165 | 0.060 | trig=0.1646,abstain>0.4939,after=0.0042 |
| flare+3band | 0.1 | 0.2 | 0.303 | 0.080 | 0.165 | 0.000 | trig=0.1646,abstain>0.4939,after=0.6327 |
| flare+3band | 0.1 | 0.35 | 0.303 | 0.080 | 0.165 | 0.035 | trig=0.1646,abstain>0.4939,after=0.6327 |
| flare+3band | 0.1 | 0.5 | 0.306 | 0.086 | 0.366 | 0.025 | trig=0.1646,abstain>0.7865,after=0.275 |
| dragin+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+3band | 0.05 | 0.2 | 0.230 | 0.044 | 0.188 | 0.000 | trig=0.5029,abstain>0.9719,after=0.0047 |
| dragin+3band | 0.05 | 0.35 | 0.230 | 0.044 | 0.188 | 0.015 | trig=0.5029,abstain>0.9719,after=0.0047 |
| dragin+3band | 0.05 | 0.5 | 0.230 | 0.044 | 0.188 | 0.015 | trig=0.5029,abstain>0.9719,after=0.0047 |
| dragin+3band | 0.1 | 0.2 | 0.321 | 0.080 | 0.188 | 0.080 | trig=0.5029,abstain>0.9719,after=0.6415 |
| dragin+3band | 0.1 | 0.35 | 0.321 | 0.080 | 0.188 | 0.110 | trig=0.5029,abstain>0.9719,after=0.6415 |
| dragin+3band | 0.1 | 0.5 | 0.321 | 0.080 | 0.188 | 0.110 | trig=0.5029,abstain>0.9719,after=0.6415 |
| probing-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+3band | 0.05 | 0.2 | 0.242 | 0.033 | 0.172 | 0.100 | trig=0.2352,abstain>0.4561,after=0.0052 |
| probing-rag+3band | 0.05 | 0.35 | 0.242 | 0.033 | 0.172 | 0.100 | trig=0.2352,abstain>0.4561,after=0.0052 |
| probing-rag+3band | 0.05 | 0.5 | 0.249 | 0.035 | 0.359 | 0.100 | trig=0.2352,abstain>0.7325,after=0.0052 |
| probing-rag+3band | 0.1 | 0.2 | 0.357 | 0.078 | 0.172 | 0.000 | trig=0.2352,abstain>0.4561,after=1.3632 |
| probing-rag+3band | 0.1 | 0.35 | 0.369 | 0.086 | 0.256 | 0.000 | trig=0.3644,abstain>0.7325,after=0.2707 |
| probing-rag+3band | 0.1 | 0.5 | 0.369 | 0.086 | 0.256 | 0.100 | trig=0.3644,abstain>0.7325,after=0.2707 |
| sep-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+3band | 0.05 | 0.2 | 0.198 | 0.034 | 0.087 | 0.000 | trig=0.1347,abstain>0.2069,after=1.3632 |
| sep-rag+3band | 0.05 | 0.35 | 0.223 | 0.034 | 0.291 | 0.000 | trig=0.1347,abstain>0.4375,after=0.2707 |
| sep-rag+3band | 0.05 | 0.5 | 0.223 | 0.034 | 0.291 | 0.005 | trig=0.1347,abstain>0.4375,after=0.2707 |
| sep-rag+3band | 0.1 | 0.2 | 0.319 | 0.083 | 0.053 | 0.010 | trig=0.3632,abstain>0.4375,after=0.2707 |
| sep-rag+3band | 0.1 | 0.35 | 0.319 | 0.083 | 0.053 | 0.000 | trig=0.3632,abstain>0.4375,after=0.2707 |
| sep-rag+3band | 0.1 | 0.5 | 0.319 | 0.083 | 0.053 | 0.010 | trig=0.3632,abstain>0.4375,after=0.2707 |
| se-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.2 | 0.218 | 0.038 | 0.099 | 0.110 | trig=-0.0,abstain>0.3251,after=0.6415 |
| se-rag+3band | 0.05 | 0.35 | 0.235 | 0.041 | 0.229 | 0.100 | trig=-0.0,abstain>0.9404,after=0.2707 |
| se-rag+3band | 0.05 | 0.5 | 0.235 | 0.041 | 0.229 | 0.100 | trig=-0.0,abstain>0.9404,after=0.2707 |
| se-rag+3band | 0.1 | 0.2 | 0.327 | 0.085 | 0.130 | 0.000 | trig=0.3251,abstain>0.9404,after=1.3632 |
| se-rag+3band | 0.1 | 0.35 | 0.317 | 0.079 | 0.328 | 0.125 | trig=0.3251,abstain>1.6094,after=0.2707 |
| se-rag+3band | 0.1 | 0.5 | 0.317 | 0.079 | 0.328 | 0.135 | trig=0.3251,abstain>1.6094,after=0.2707 |

### D95 Label-free online recalibration out of domain (explore eps = 0.1, evidence confidence P(wrong) < 0.3)

Pseudo-labels (closed-book draft vs confident evidence answer):

| split | labelled share | label accuracy | pseudo wrong rate | true wrong rate |
|---|---|---|---|---|
| val | 0.480 | 0.785 | 0.484 | 0.315 |
| test | 0.480 | 0.768 | 0.454 | 0.282 |
| ood | 0.218 | 0.727 | 0.621 | 0.581 |

| lam | dataset | utility: deployed | pseudo-label recal | oracle-label recal | halluc: deployed | pseudo | oracle | retrieval: deployed | pseudo |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 2wikimultihopqa | -0.081 | -0.081 | -0.081 | 0.091 | 0.091 | 0.090 | 0.992 | 0.993 |
| 1.0 | hotpotqa | -0.029 | -0.029 | -0.026 | 0.221 | 0.219 | 0.216 | 0.945 | 0.965 |
| 1.0 | nq | 0.065 | 0.067 | 0.074 | 0.162 | 0.156 | 0.133 | 0.833 | 0.865 |
| 1.0 | sciq | 0.106 | 0.098 | 0.079 | 0.240 | 0.236 | 0.234 | 0.658 | 0.733 |
| 1.0 | all OOD | 0.002 | -0.002 | -0.003 | 0.170 | 0.159 | 0.156 | 0.885 | 0.947 |
| 2.0 | 2wikimultihopqa | -0.050 | -0.051 | -0.051 | 0.024 | 0.024 | 0.024 | 0.832 | 0.850 |
| 2.0 | hotpotqa | -0.090 | -0.090 | -0.088 | 0.102 | 0.101 | 0.100 | 0.847 | 0.870 |
| 2.0 | nq | -0.037 | -0.035 | -0.025 | 0.078 | 0.074 | 0.063 | 0.723 | 0.763 |
| 2.0 | sciq | -0.009 | -0.014 | -0.019 | 0.125 | 0.120 | 0.110 | 0.547 | 0.624 |
| 2.0 | all OOD | -0.052 | -0.050 | -0.050 | 0.076 | 0.069 | 0.067 | 0.764 | 0.816 |
| 4.0 | 2wikimultihopqa | -0.037 | -0.037 | -0.037 | 0.006 | 0.006 | 0.006 | 0.885 | 0.897 |
| 4.0 | hotpotqa | -0.134 | -0.133 | -0.130 | 0.048 | 0.047 | 0.046 | 0.882 | 0.899 |
| 4.0 | nq | -0.070 | -0.066 | -0.057 | 0.031 | 0.028 | 0.024 | 0.782 | 0.813 |
| 4.0 | sciq | -0.088 | -0.091 | -0.099 | 0.056 | 0.055 | 0.053 | 0.683 | 0.730 |
| 4.0 | all OOD | -0.081 | -0.078 | -0.077 | 0.032 | 0.029 | 0.028 | 0.826 | 0.858 |

### D99 Budgeted route-eu configs: simulation (test split) vs the real engine (bench questions)

| mode | sim acc | sim halluc | sim retrieval | engine acc | engine halluc [95% CI] | engine retrieval |
|---|---|---|---|---|---|---|
| route-eu-cost0.2 | 0.470 | 0.073 | 0.438 | - | - | - |
| route-eu-cost0.3 | 0.467 | 0.073 | 0.355 | - | - | - |
| route-eu-cost0.5 | 0.406 | 0.067 | 0.154 | - | - | - |
| route-eu-lam2-cost0.3 | 0.355 | 0.033 | 0.266 | - | - | - |
| route-eu-lam2-cost0.5 | 0.307 | 0.030 | 0.109 | - | - | - |

### D97 Speculative retrieval (search started at arrival; search 296 ms): latency bound, c1

| method | n | E2E p50 | p90 | p99 | speculative p50 | p90 | p99 | mean saving ms | wasted searches / q |
|---|---|---|---|---|---|---|---|---|---|
| route-eu | 100 | 334 | 406 | 425 | 320 | 395 | 414 | 13 | 0.240 |
| route-eu-2r | 100 | 372 | 645 | 707 | 361 | 634 | 696 | 12 | 0.250 |

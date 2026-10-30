### D94 Joint certified budget: hallucination <= alpha AND retrieval rate <= beta (LTT, delta = 0.1, 200 re-splits)

| method | alpha | beta | test acc | test halluc | test retrieval | violation rate | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.05 | 0.2 | 0.522 | 0.051 | 0.139 | 0.145 | lam=2.0,cost=0.5 |
| Tripwire route-eu | 0.05 | 0.35 | 0.547 | 0.049 | 0.288 | 0.080 | lam=2.0,cost=0.3 |
| Tripwire route-eu | 0.05 | 0.5 | 0.547 | 0.049 | 0.288 | 0.065 | lam=2.0,cost=0.3 |
| Tripwire route-eu | 0.1 | 0.2 | 0.586 | 0.082 | 0.115 | 0.000 | lam=1.0,cost=0.5 |
| Tripwire route-eu | 0.1 | 0.35 | 0.596 | 0.078 | 0.221 | 0.000 | lam=1.0,cost=0.3 |
| Tripwire route-eu | 0.1 | 0.5 | 0.624 | 0.080 | 0.383 | 0.000 | lam=1.0,cost=0.2 |
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
| flare+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.010 | abstain on everything |
| flare+3band | 0.05 | 0.2 | 0.382 | 0.046 | 0.062 | 0.005 | trig=0.0019,abstain>0.0064,after=0.8017 |
| flare+3band | 0.05 | 0.35 | 0.382 | 0.046 | 0.062 | 0.005 | trig=0.0019,abstain>0.0064,after=0.8017 |
| flare+3band | 0.05 | 0.5 | 0.386 | 0.042 | 0.423 | 0.000 | trig=0.0,abstain>0.0064,after=0.8017 |
| flare+3band | 0.1 | 0.2 | 0.482 | 0.076 | 0.151 | 0.135 | trig=0.0143,abstain>0.1269,after=0.0078 |
| flare+3band | 0.1 | 0.35 | 0.482 | 0.076 | 0.151 | 0.080 | trig=0.0143,abstain>0.1269,after=0.0078 |
| flare+3band | 0.1 | 0.5 | 0.482 | 0.076 | 0.151 | 0.170 | trig=0.0143,abstain>0.1269,after=0.0078 |
| dragin+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.5 | 0.514 | 0.086 | 0.415 | 0.000 | trig=0.2475,after=-0.0 |
| dragin+3band | 0.05 | 0.2 | 0.388 | 0.045 | 0.065 | 0.015 | trig=0.0113,abstain>0.0347,after=0.9291 |
| dragin+3band | 0.05 | 0.35 | 0.388 | 0.045 | 0.065 | 0.005 | trig=0.0113,abstain>0.0347,after=0.9291 |
| dragin+3band | 0.05 | 0.5 | 0.388 | 0.045 | 0.065 | 0.005 | trig=0.0113,abstain>0.0347,after=0.9291 |
| dragin+3band | 0.1 | 0.2 | 0.516 | 0.090 | 0.040 | 0.150 | trig=0.2475,abstain>0.3669,after=0.0298 |
| dragin+3band | 0.1 | 0.35 | 0.516 | 0.090 | 0.040 | 0.150 | trig=0.2475,abstain>0.3669,after=0.0298 |
| dragin+3band | 0.1 | 0.5 | 0.516 | 0.090 | 0.040 | 0.055 | trig=0.2475,abstain>0.3669,after=0.0298 |
| probing-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.35 | 0.583 | 0.105 | 0.330 | 0.065 | trig=0.4393,after=-0.0 |
| probing-rag+abstain | 0.1 | 0.5 | 0.532 | 0.069 | 0.424 | 0.000 | trig=0.3058,after=-0.0 |
| probing-rag+3band | 0.05 | 0.2 | 0.445 | 0.042 | 0.131 | 0.000 | trig=0.2126,abstain>0.3536,after=-0.0 |
| probing-rag+3band | 0.05 | 0.35 | 0.455 | 0.043 | 0.313 | 0.000 | trig=0.2126,abstain>0.6787,after=-0.0 |
| probing-rag+3band | 0.05 | 0.5 | 0.479 | 0.038 | 0.357 | 0.000 | trig=0.1097,abstain>0.3536,after=0.0338 |
| probing-rag+3band | 0.1 | 0.2 | 0.540 | 0.071 | 0.131 | 0.080 | trig=0.2126,abstain>0.3536,after=0.9653 |
| probing-rag+3band | 0.1 | 0.35 | 0.546 | 0.065 | 0.242 | 0.000 | trig=0.1508,abstain>0.3536,after=0.9653 |
| probing-rag+3band | 0.1 | 0.5 | 0.581 | 0.093 | 0.313 | 0.000 | trig=0.2126,abstain>0.6787,after=0.0338 |
| sep-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.065 | abstain on everything |
| sep-rag+3band | 0.05 | 0.2 | 0.353 | 0.054 | 0.162 | 0.020 | trig=0.0573,abstain>0.089,after=0.0338 |
| sep-rag+3band | 0.05 | 0.35 | 0.353 | 0.054 | 0.162 | 0.050 | trig=0.0573,abstain>0.089,after=0.0338 |
| sep-rag+3band | 0.05 | 0.5 | 0.353 | 0.054 | 0.162 | 0.050 | trig=0.0573,abstain>0.089,after=0.0338 |
| sep-rag+3band | 0.1 | 0.2 | 0.496 | 0.093 | 0.148 | 0.015 | trig=0.1004,abstain>0.1607,after=0.0338 |
| sep-rag+3band | 0.1 | 0.35 | 0.496 | 0.093 | 0.148 | 0.000 | trig=0.1004,abstain>0.1607,after=0.0338 |
| sep-rag+3band | 0.1 | 0.5 | 0.496 | 0.093 | 0.148 | 0.095 | trig=0.1004,abstain>0.1607,after=0.0338 |
| se-rag+abstain | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.055 | abstain on everything |
| se-rag+3band | 0.05 | 0.2 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.35 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.05 | 0.5 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+3band | 0.1 | 0.2 | 0.000 | 0.000 | 0.000 | 0.120 | abstain on everything |
| se-rag+3band | 0.1 | 0.35 | 0.000 | 0.000 | 0.000 | 0.125 | abstain on everything |
| se-rag+3band | 0.1 | 0.5 | 0.000 | 0.000 | 0.000 | 0.125 | abstain on everything |

### D95 Label-free online recalibration out of domain (explore eps = 0.1, evidence confidence P(wrong) < 0.3)

Pseudo-labels (closed-book draft vs confident evidence answer):

| split | labelled share | label accuracy | pseudo wrong rate | true wrong rate |
|---|---|---|---|---|
| val | 0.652 | 0.893 | 0.165 | 0.180 |
| test | 0.648 | 0.900 | 0.158 | 0.170 |
| ood | 0.456 | 0.753 | 0.311 | 0.471 |

| lam | dataset | utility: deployed | pseudo-label recal | oracle-label recal | halluc: deployed | pseudo | oracle | retrieval: deployed | pseudo |
|---|---|---|---|---|---|---|---|---|---|
| 1.0 | 2wikimultihopqa | -0.043 | -0.043 | -0.041 | 0.188 | 0.187 | 0.184 | 0.984 | 0.988 |
| 1.0 | hotpotqa | 0.071 | 0.069 | 0.083 | 0.286 | 0.287 | 0.274 | 0.940 | 0.939 |
| 1.0 | nq | 0.153 | 0.142 | 0.172 | 0.222 | 0.240 | 0.192 | 0.797 | 0.809 |
| 1.0 | sciq | 0.296 | 0.296 | 0.301 | 0.249 | 0.258 | 0.242 | 0.878 | 0.811 |
| 1.0 | all OOD | 0.094 | 0.093 | 0.106 | 0.234 | 0.237 | 0.218 | 0.903 | 0.922 |
| 2.0 | 2wikimultihopqa | -0.097 | -0.096 | -0.095 | 0.095 | 0.094 | 0.093 | 0.991 | 0.993 |
| 2.0 | hotpotqa | -0.093 | -0.097 | -0.082 | 0.190 | 0.192 | 0.184 | 0.967 | 0.961 |
| 2.0 | nq | 0.033 | 0.026 | 0.038 | 0.131 | 0.132 | 0.120 | 0.874 | 0.914 |
| 2.0 | sciq | 0.146 | 0.144 | 0.152 | 0.166 | 0.173 | 0.162 | 0.938 | 0.871 |
| 2.0 | all OOD | -0.024 | -0.021 | -0.016 | 0.142 | 0.139 | 0.135 | 0.943 | 0.968 |
| 4.0 | 2wikimultihopqa | -0.088 | -0.088 | -0.088 | 0.034 | 0.034 | 0.034 | 0.975 | 0.978 |
| 4.0 | hotpotqa | -0.246 | -0.256 | -0.238 | 0.111 | 0.114 | 0.109 | 0.973 | 0.968 |
| 4.0 | nq | -0.084 | -0.089 | -0.093 | 0.065 | 0.064 | 0.065 | 0.900 | 0.926 |
| 4.0 | sciq | 0.030 | 0.015 | 0.031 | 0.087 | 0.093 | 0.086 | 0.959 | 0.910 |
| 4.0 | all OOD | -0.115 | -0.112 | -0.110 | 0.072 | 0.071 | 0.070 | 0.951 | 0.968 |

### D99 Budgeted route-eu configs: simulation (test split) vs the real engine (bench questions)

| mode | sim acc | sim halluc | sim retrieval | engine acc | engine halluc [95% CI] | engine retrieval |
|---|---|---|---|---|---|---|
| route-eu-cost0.2 | 0.624 | 0.080 | 0.383 | - | - | - |
| route-eu-cost0.3 | 0.596 | 0.078 | 0.221 | - | - | - |
| route-eu-cost0.5 | 0.586 | 0.082 | 0.115 | - | - | - |
| route-eu-lam2-cost0.3 | 0.547 | 0.049 | 0.288 | - | - | - |
| route-eu-lam2-cost0.5 | 0.522 | 0.051 | 0.139 | - | - | - |

### D97 Speculative retrieval (search started at arrival; search 288 ms): latency bound, c1

| method | n | E2E p50 | p90 | p99 | speculative p50 | p90 | p99 | mean saving ms | wasted searches / q |
|---|---|---|---|---|---|---|---|---|---|
| route-eu | 100 | 446 | 531 | 650 | 394 | 459 | 507 | 46 | 0.270 |
| route-eu-2r | 100 | 490 | 830 | 926 | 428 | 782 | 868 | 46 | 0.260 |

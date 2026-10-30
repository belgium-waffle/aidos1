### 1. Certified hallucination budget (Learn-then-Test, delta = 0.1; 500 re-splits)

| method | alpha | LTT: test acc | LTT: test halluc | LTT: violation rate | naive: violation rate | LTT: OOD halluc | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.03 | 0.227 | 0.011 | 0.018 | 0.330 | 0.015 | lam=6.0 |
| Tripwire route-eu | 0.05 | 0.341 | 0.027 | 0.020 | 0.020 | 0.047 | lam=3.0 |
| Tripwire route-eu | 0.1 | 0.483 | 0.079 | 0.004 | 0.196 | 0.170 | lam=1.0 |
| Tripwire route-eu | 0.15 | 0.540 | 0.131 | 0.000 | 0.000 | 0.284 | lam=0.5 |
| flare+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.05 | 0.000 | 0.000 | 0.000 | 0.004 | 0.000 | abstain on everything |
| flare+abstain | 0.1 | 0.245 | 0.061 | 0.000 | 0.000 | 0.080 | trig=0.2531,after=-0.9996 |
| flare+abstain | 0.15 | 0.343 | 0.126 | 0.016 | 0.362 | 0.157 | trig=0.2531,after=0.1803 |
| dragin+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.000 | 0.000 | 0.000 | 0.022 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.304 | 0.086 | 0.000 | 0.000 | 0.118 | trig=0.7969,after=-0.9996 |
| dragin+abstain | 0.15 | 0.352 | 0.116 | 0.038 | 0.098 | 0.157 | trig=0.6429,after=0.1808 |
| probing-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.000 | 0.000 | 0.140 | 0.146 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.311 | 0.062 | 0.000 | 0.022 | 0.132 | trig=0.3693,after=-0.9996 |
| probing-rag+abstain | 0.15 | 0.405 | 0.118 | 0.028 | 0.314 | 0.208 | trig=0.3693,after=0.1995 |
| sep-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.000 | 0.000 | 0.006 | 0.294 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.306 | 0.080 | 0.002 | 0.242 | 0.146 | trig=0.3654,after=-0.9996 |
| sep-rag+abstain | 0.15 | 0.374 | 0.129 | 0.010 | 0.138 | 0.246 | trig=0.5161,after=-0.9996 |
| se-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.000 | 0.000 | 0.000 | 0.008 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.290 | 0.072 | 0.000 | 0.000 | 0.101 | trig=0.673,after=-0.9996 |
| se-rag+abstain | 0.15 | 0.383 | 0.126 | 0.092 | 0.184 | 0.175 | trig=0.673,after=0.1995 |

### 2. Calibration error per decision stage and route-eu's regret (TEST)

| lam | pre (P wrong before answering) | post (closed-book answer, Platt) | post_rag (evidence answer, Platt) | pre_rag (evidence turn) | regret | bound (1+lam)·Σ |
|---|---|---|---|---|---|---|
| 1.0 | 0.030 | 0.037 | 0.021 | 0.027 | 0.009 | 0.230 |
| 2.0 | 0.030 | 0.037 | 0.021 | 0.027 | 0.007 | 0.344 |
| 4.0 | 0.030 | 0.037 | 0.021 | 0.027 | 0.009 | 0.574 |

### 3. Hallucination vs compute: 57% of baseline points are dominated by a Tripwire point (<= halluc, <= prefill, >= acc)

### 4. Error flow at lam=1 (TEST, share of questions)

| closed-book | Tripwire action | outcome | share |
|---|---|---|---|
| closed-book correct | retrieve: evidence has answer | correct | 0.238 |
| knowledge gap | abstain at once | abstain | 0.142 |
| closed-book correct | answer closed-book | correct | 0.135 |
| knowledge gap | retrieve: retrieval miss | abstain | 0.106 |
| knowledge gap | retrieve: evidence has answer | correct | 0.091 |
| knowledge gap | retrieve: evidence has answer | abstain | 0.075 |
| closed-book correct | retrieve: evidence has answer | abstain | 0.046 |
| closed-book correct | retrieve: retrieval miss | abstain | 0.031 |
| knowledge gap | retrieve: retrieval miss | wrong | 0.017 |
| knowledge gap | retrieve: evidence has answer | wrong | 0.016 |
| knowledge gap | answer closed-book | wrong | 0.015 |
| closed-book correct | retrieve: evidence has answer | wrong | 0.015 |
| drift | retrieve: evidence has answer | correct | 0.014 |
| drift | retrieve: evidence has answer | abstain | 0.011 |
| closed-book correct | abstain at once | abstain | 0.010 |
| drift | retrieve: retrieval miss | abstain | 0.008 |
| closed-book correct | retrieve: retrieval miss | wrong | 0.006 |
| drift | abstain at once | abstain | 0.006 |
| drift | retrieve: evidence has answer | wrong | 0.005 |
| drift | answer closed-book | wrong | 0.003 |
| closed-book correct | retrieve: retrieval miss | correct | 0.003 |
| knowledge gap | retrieve: retrieval miss | correct | 0.002 |
| knowledge gap | answer closed-book | abstain | 0.001 |
| drift | retrieve: retrieval miss | wrong | 0.001 |
| closed-book correct | answer closed-book | abstain | 0.001 |

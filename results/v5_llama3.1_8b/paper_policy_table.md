### 1. Certified hallucination budget (Learn-then-Test, delta = 0.1; 500 re-splits)

| method | alpha | LTT: test acc | LTT: test halluc | LTT: violation rate | naive: violation rate | LTT: OOD halluc | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.03 | 0.360 | 0.019 | 0.116 | 0.164 | 0.043 | lam=4.0 |
| Tripwire route-eu | 0.05 | 0.402 | 0.026 | 0.014 | 0.250 | 0.061 | lam=3.0 |
| Tripwire route-eu | 0.1 | 0.534 | 0.083 | 0.000 | 0.024 | 0.208 | lam=0.75 |
| Tripwire route-eu | 0.15 | 0.558 | 0.112 | 0.002 | 0.248 | 0.273 | lam=0.5 |
| flare+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.05 | 0.000 | 0.000 | 0.116 | 0.116 | 0.000 | abstain on everything |
| flare+abstain | 0.1 | 0.349 | 0.085 | 0.000 | 0.172 | 0.157 | trig=0.5473,after=-1.0 |
| flare+abstain | 0.15 | 0.432 | 0.138 | 0.044 | 0.192 | 0.182 | trig=0.5473,after=0.0124 |
| dragin+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.006 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.317 | 0.051 | 0.132 | 0.200 | 0.094 | trig=0.7701,after=-0.9999 |
| dragin+abstain | 0.1 | 0.387 | 0.084 | 0.002 | 0.020 | 0.106 | trig=0.6898,after=0.016 |
| dragin+abstain | 0.15 | 0.475 | 0.140 | 0.004 | 0.316 | 0.188 | trig=0.9284,after=0.0522 |
| probing-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.044 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.254 | 0.037 | 0.008 | 0.232 | 0.079 | trig=0.2529,after=-1.0 |
| probing-rag+abstain | 0.1 | 0.384 | 0.084 | 0.026 | 0.426 | 0.117 | trig=0.2529,after=0.0177 |
| probing-rag+abstain | 0.15 | 0.451 | 0.126 | 0.002 | 0.478 | 0.212 | trig=0.4298,after=0.0177 |
| sep-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.002 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.253 | 0.040 | 0.000 | 0.008 | 0.066 | trig=0.1479,after=-1.0 |
| sep-rag+abstain | 0.1 | 0.387 | 0.087 | 0.000 | 0.142 | 0.106 | trig=0.1479,after=0.0177 |
| sep-rag+abstain | 0.15 | 0.452 | 0.140 | 0.000 | 0.374 | 0.171 | trig=0.2274,after=0.0575 |
| se-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.311 | 0.044 | 0.000 | 0.312 | 0.080 | trig=0.3251,after=-1.0 |
| se-rag+abstain | 0.1 | 0.419 | 0.088 | 0.070 | 0.086 | 0.116 | trig=0.3251,after=0.0177 |
| se-rag+abstain | 0.15 | 0.468 | 0.122 | 0.006 | 0.452 | 0.181 | trig=0.9404,after=0.0177 |

### 2. Calibration error per decision stage and route-eu's regret (TEST)

| lam | pre (P wrong before answering) | post (closed-book answer, Platt) | post_rag (evidence answer, Platt) | pre_rag (evidence turn) | regret | bound (1+lam)·Σ |
|---|---|---|---|---|---|---|
| 1.0 | 0.021 | 0.017 | 0.018 | 0.023 | -0.009 | 0.156 |
| 2.0 | 0.021 | 0.017 | 0.018 | 0.023 | 0.004 | 0.235 |
| 4.0 | 0.021 | 0.017 | 0.018 | 0.023 | -0.017 | 0.391 |

### 3. Hallucination vs compute: 50% of baseline points are dominated by a Tripwire point (<= halluc, <= prefill, >= acc)

### 4. Error flow at lam=1 (TEST, share of questions)

| closed-book | Tripwire action | outcome | share |
|---|---|---|---|
| closed-book correct | retrieve: evidence has answer | correct | 0.233 |
| closed-book correct | answer closed-book | correct | 0.144 |
| knowledge gap | abstain at once | abstain | 0.117 |
| knowledge gap | retrieve: retrieval miss | abstain | 0.116 |
| knowledge gap | retrieve: evidence has answer | correct | 0.097 |
| knowledge gap | retrieve: evidence has answer | abstain | 0.071 |
| closed-book correct | retrieve: evidence has answer | abstain | 0.041 |
| closed-book correct | retrieve: retrieval miss | abstain | 0.035 |
| drift | retrieve: evidence has answer | correct | 0.032 |
| knowledge gap | retrieve: retrieval miss | wrong | 0.019 |
| drift | retrieve: evidence has answer | abstain | 0.013 |
| drift | retrieve: retrieval miss | abstain | 0.013 |
| knowledge gap | answer closed-book | wrong | 0.012 |
| knowledge gap | retrieve: evidence has answer | wrong | 0.011 |
| closed-book correct | retrieve: evidence has answer | wrong | 0.010 |
| closed-book correct | abstain at once | abstain | 0.009 |
| closed-book correct | retrieve: retrieval miss | correct | 0.005 |
| closed-book correct | retrieve: retrieval miss | wrong | 0.005 |
| drift | abstain at once | abstain | 0.004 |
| drift | retrieve: evidence has answer | wrong | 0.003 |
| drift | answer closed-book | wrong | 0.003 |
| drift | retrieve: retrieval miss | wrong | 0.002 |
| knowledge gap | retrieve: retrieval miss | correct | 0.002 |
| knowledge gap | answer closed-book | abstain | 0.001 |
| drift | retrieve: retrieval miss | correct | 0.001 |
| drift | answer closed-book | abstain | 0.000 |
| closed-book correct | answer closed-book | abstain | 0.000 |

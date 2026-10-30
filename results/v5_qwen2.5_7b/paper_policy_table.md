### 1. Certified hallucination budget (Learn-then-Test, delta = 0.1; 500 re-splits)

| method | alpha | LTT: test acc | LTT: test halluc | LTT: violation rate | naive: violation rate | LTT: OOD halluc | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.03 | 0.321 | 0.017 | 0.108 | 0.108 | 0.034 | lam=4.0 |
| Tripwire route-eu | 0.05 | 0.411 | 0.038 | 0.004 | 0.192 | 0.074 | lam=2.0 |
| Tripwire route-eu | 0.1 | 0.499 | 0.084 | 0.000 | 0.004 | 0.176 | lam=0.75 |
| Tripwire route-eu | 0.15 | 0.524 | 0.116 | 0.000 | 0.016 | 0.236 | lam=0.5 |
| flare+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| flare+abstain | 0.05 | 0.000 | 0.000 | 0.000 | 0.002 | 0.000 | abstain on everything |
| flare+abstain | 0.1 | 0.266 | 0.093 | 0.010 | 0.010 | 0.202 | trig=0.2306,after=-1.0 |
| flare+abstain | 0.15 | 0.295 | 0.126 | 0.036 | 0.402 | 0.263 | trig=0.3856,after=-1.0 |
| dragin+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| dragin+abstain | 0.05 | 0.000 | 0.000 | 0.000 | 0.002 | 0.000 | abstain on everything |
| dragin+abstain | 0.1 | 0.232 | 0.066 | 0.002 | 0.004 | 0.155 | trig=0.426,after=-1.0 |
| dragin+abstain | 0.15 | 0.301 | 0.122 | 0.002 | 0.138 | 0.273 | trig=0.8693,after=-1.0 |
| probing-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.05 | 0.000 | 0.000 | 0.000 | 0.002 | 0.000 | abstain on everything |
| probing-rag+abstain | 0.1 | 0.284 | 0.094 | 0.014 | 0.014 | 0.182 | trig=0.5731,after=-1.0 |
| probing-rag+abstain | 0.15 | 0.310 | 0.138 | 0.000 | 0.044 | 0.240 | trig=0.6849,after=-1.0 |
| sep-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.05 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| sep-rag+abstain | 0.1 | 0.219 | 0.084 | 0.002 | 0.152 | 0.104 | trig=0.1632,after=-1.0 |
| sep-rag+abstain | 0.15 | 0.287 | 0.130 | 0.028 | 0.034 | 0.131 | trig=-0.9994,after=0.0005 |
| se-rag+abstain | 0.03 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.05 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | abstain on everything |
| se-rag+abstain | 0.1 | 0.278 | 0.096 | 0.016 | 0.088 | 0.213 | trig=0.3251,after=-1.0 |
| se-rag+abstain | 0.15 | 0.291 | 0.111 | 0.028 | 0.410 | 0.242 | trig=0.639,after=-1.0 |

### 2. Calibration error per decision stage and route-eu's regret (TEST)

| lam | pre (P wrong before answering) | post (closed-book answer, Platt) | post_rag (evidence answer, Platt) | pre_rag (evidence turn) | regret | bound (1+lam)·Σ |
|---|---|---|---|---|---|---|
| 1.0 | 0.022 | 0.019 | 0.019 | 0.020 | 0.000 | 0.159 |
| 2.0 | 0.022 | 0.019 | 0.019 | 0.020 | -0.010 | 0.239 |
| 4.0 | 0.022 | 0.019 | 0.019 | 0.020 | 0.003 | 0.399 |

### 3. Hallucination vs compute: 78% of baseline points are dominated by a Tripwire point (<= halluc, <= prefill, >= acc)

### 4. Error flow at lam=1 (TEST, share of questions)

| closed-book | Tripwire action | outcome | share |
|---|---|---|---|
| closed-book correct | retrieve: evidence has answer | correct | 0.184 |
| knowledge gap | abstain at once | abstain | 0.180 |
| knowledge gap | retrieve: evidence has answer | correct | 0.161 |
| closed-book correct | answer closed-book | correct | 0.104 |
| knowledge gap | retrieve: retrieval miss | abstain | 0.102 |
| knowledge gap | retrieve: evidence has answer | abstain | 0.095 |
| closed-book correct | retrieve: evidence has answer | abstain | 0.037 |
| drift | retrieve: evidence has answer | correct | 0.023 |
| knowledge gap | retrieve: retrieval miss | wrong | 0.021 |
| knowledge gap | retrieve: evidence has answer | wrong | 0.018 |
| closed-book correct | retrieve: retrieval miss | abstain | 0.016 |
| closed-book correct | retrieve: evidence has answer | wrong | 0.012 |
| closed-book correct | abstain at once | abstain | 0.008 |
| drift | retrieve: evidence has answer | abstain | 0.008 |
| drift | retrieve: retrieval miss | abstain | 0.007 |
| knowledge gap | answer closed-book | wrong | 0.005 |
| closed-book correct | retrieve: retrieval miss | wrong | 0.004 |
| drift | abstain at once | abstain | 0.003 |
| drift | answer closed-book | wrong | 0.003 |
| drift | retrieve: evidence has answer | wrong | 0.003 |
| drift | retrieve: retrieval miss | wrong | 0.002 |
| closed-book correct | retrieve: retrieval miss | correct | 0.002 |
| closed-book correct | answer closed-book | abstain | 0.000 |
| knowledge gap | answer closed-book | abstain | 0.000 |
| knowledge gap | retrieve: retrieval miss | correct | 0.000 |

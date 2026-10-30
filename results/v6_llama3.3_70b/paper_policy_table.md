### 1. Certified hallucination budget (Learn-then-Test, delta = 0.1; 500 re-splits)

| method | alpha | LTT: test acc | LTT: test halluc | LTT: violation rate | naive: violation rate | LTT: OOD halluc | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.03 | 0.411 | 0.012 | 0.056 | 0.302 | 0.043 | lam=6.0 |
| Tripwire route-eu | 0.05 | 0.579 | 0.046 | 0.010 | 0.080 | 0.142 | lam=2.0 |
| Tripwire route-eu | 0.1 | 0.647 | 0.089 | 0.000 | 0.044 | 0.271 | lam=0.75 |
| Tripwire route-eu | 0.15 | 0.688 | 0.147 | 0.034 | 0.034 | 0.404 | lam=0.25 |
| flare+abstain | 0.03 | 0.275 | 0.020 | 0.070 | 0.184 | 0.032 | trig=0.0005,after=-1.0 |
| flare+abstain | 0.05 | 0.384 | 0.045 | 0.112 | 0.228 | 0.076 | trig=0.0067,after=-1.0 |
| flare+abstain | 0.1 | 0.494 | 0.079 | 0.020 | 0.204 | 0.152 | trig=0.051,after=0.0 |
| flare+abstain | 0.15 | 0.572 | 0.140 | 0.084 | 0.130 | 0.238 | trig=0.1269,after=0.0002 |
| dragin+abstain | 0.03 | 0.282 | 0.021 | 0.008 | 0.218 | 0.038 | trig=0.0039,after=-1.0 |
| dragin+abstain | 0.05 | 0.408 | 0.048 | 0.036 | 0.042 | 0.083 | trig=0.0354,after=0.0 |
| dragin+abstain | 0.1 | 0.500 | 0.079 | 0.008 | 0.480 | 0.157 | trig=0.1989,after=0.0 |
| dragin+abstain | 0.15 | 0.594 | 0.136 | 0.132 | 0.588 | 0.231 | trig=0.1989,after=0.0069 |
| probing-rag+abstain | 0.03 | 0.379 | 0.028 | 0.022 | 0.122 | 0.044 | trig=0.152,after=0.0 |
| probing-rag+abstain | 0.05 | 0.430 | 0.038 | 0.058 | 0.180 | 0.063 | trig=0.1829,after=0.0 |
| probing-rag+abstain | 0.1 | 0.551 | 0.084 | 0.046 | 0.510 | 0.182 | trig=0.3563,after=0.0 |
| probing-rag+abstain | 0.15 | 0.625 | 0.144 | 0.012 | 0.472 | 0.277 | trig=0.443,after=0.0009 |
| sep-rag+abstain | 0.03 | 0.073 | 0.003 | 0.000 | 0.000 | 0.004 | trig=-0.9945,after=0.0 |
| sep-rag+abstain | 0.05 | 0.319 | 0.050 | 0.000 | 0.070 | 0.089 | trig=0.0636,after=0.0 |
| sep-rag+abstain | 0.1 | 0.497 | 0.087 | 0.054 | 0.304 | 0.147 | trig=0.0759,after=0.0001 |
| sep-rag+abstain | 0.15 | 0.603 | 0.147 | 0.040 | 0.522 | 0.251 | trig=0.1083,after=0.0073 |
| se-rag+abstain | 0.03 | 0.073 | 0.003 | 0.000 | 0.000 | 0.004 | trig=-1.0,after=0.0 |
| se-rag+abstain | 0.05 | 0.073 | 0.003 | 0.004 | 0.006 | 0.004 | trig=-1.0,after=0.0 |
| se-rag+abstain | 0.1 | 0.431 | 0.058 | 0.066 | 0.398 | 0.086 | trig=-1.0,after=0.0009 |
| se-rag+abstain | 0.15 | 0.595 | 0.116 | 0.024 | 0.536 | 0.231 | trig=0.0,after=0.0001 |

### 2. Calibration error per decision stage and route-eu's regret (TEST)

| lam | pre (P wrong before answering) | post (closed-book answer, Platt) | post_rag (evidence answer, Platt) | pre_rag (evidence turn) | regret | bound (1+lam)·Σ |
|---|---|---|---|---|---|---|
| 1.0 | 0.014 | 0.015 | 0.016 | 0.027 | -0.004 | 0.145 |
| 2.0 | 0.014 | 0.015 | 0.016 | 0.027 | 0.004 | 0.217 |
| 4.0 | 0.014 | 0.015 | 0.016 | 0.027 | -0.011 | 0.362 |

### 3. Hallucination vs compute: 12% of baseline points are dominated by a Tripwire point (<= halluc, <= prefill, >= acc)

### 4. Error flow at lam=1 (TEST, share of questions)

| closed-book | Tripwire action | outcome | share |
|---|---|---|---|
| closed-book correct | retrieve: evidence has answer | correct | 0.360 |
| closed-book correct | answer closed-book | correct | 0.165 |
| knowledge gap | retrieve: retrieval miss | abstain | 0.093 |
| knowledge gap | abstain at once | abstain | 0.082 |
| knowledge gap | retrieve: evidence has answer | correct | 0.054 |
| closed-book correct | retrieve: retrieval miss | abstain | 0.043 |
| closed-book correct | retrieve: retrieval miss | correct | 0.037 |
| knowledge gap | retrieve: evidence has answer | abstain | 0.032 |
| knowledge gap | retrieve: retrieval miss | wrong | 0.024 |
| closed-book correct | retrieve: evidence has answer | abstain | 0.023 |
| knowledge gap | answer closed-book | wrong | 0.020 |
| drift | retrieve: evidence has answer | correct | 0.014 |
| knowledge gap | retrieve: evidence has answer | wrong | 0.012 |
| closed-book correct | abstain at once | abstain | 0.008 |
| closed-book correct | retrieve: evidence has answer | wrong | 0.007 |
| closed-book correct | retrieve: retrieval miss | wrong | 0.006 |
| drift | retrieve: retrieval miss | abstain | 0.005 |
| drift | abstain at once | abstain | 0.004 |
| drift | retrieve: evidence has answer | abstain | 0.003 |
| drift | retrieve: retrieval miss | wrong | 0.002 |
| drift | retrieve: evidence has answer | wrong | 0.002 |
| knowledge gap | retrieve: retrieval miss | correct | 0.002 |
| drift | answer closed-book | wrong | 0.002 |
| knowledge gap | answer closed-book | abstain | 0.001 |
| drift | retrieve: retrieval miss | correct | 0.001 |

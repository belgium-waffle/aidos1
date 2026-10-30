### 1. Certified hallucination budget (Learn-then-Test, delta = 0.1; 500 re-splits)

| method | alpha | LTT: test acc | LTT: test halluc | LTT: violation rate | naive: violation rate | LTT: OOD halluc | policy |
|---|---|---|---|---|---|---|---|
| Tripwire route-eu | 0.03 | 0.388 | 0.015 | 0.014 | 0.306 | 0.044 | lam=6.0 |
| Tripwire route-eu | 0.05 | 0.487 | 0.029 | 0.022 | 0.074 | 0.083 | lam=3.0 |
| Tripwire route-eu | 0.1 | 0.584 | 0.067 | 0.002 | 0.152 | 0.179 | lam=1.0 |
| Tripwire route-eu | 0.15 | 0.617 | 0.097 | 0.004 | 0.004 | 0.255 | lam=0.5 |
| flare+abstain | 0.03 | 0.018 | 0.001 | 0.000 | 0.052 | 0.004 | trig=-1.0,after=0.0 |
| flare+abstain | 0.05 | 0.283 | 0.033 | 0.000 | 0.122 | 0.097 | trig=0.016,after=0.0 |
| flare+abstain | 0.1 | 0.328 | 0.052 | 0.000 | 0.058 | 0.135 | trig=0.0481,after=0.0 |
| flare+abstain | 0.15 | 0.470 | 0.119 | 0.002 | 0.420 | 0.218 | trig=0.0481,after=0.0002 |
| dragin+abstain | 0.03 | 0.017 | 0.000 | 0.000 | 0.024 | 0.004 | trig=-1.0,after=0.0 |
| dragin+abstain | 0.05 | 0.283 | 0.033 | 0.000 | 0.056 | 0.105 | trig=0.0822,after=0.0 |
| dragin+abstain | 0.1 | 0.401 | 0.088 | 0.000 | 0.002 | 0.112 | trig=-1.0,after=0.0002 |
| dragin+abstain | 0.15 | 0.495 | 0.126 | 0.010 | 0.124 | 0.216 | trig=0.2069,after=0.0002 |
| probing-rag+abstain | 0.03 | 0.016 | 0.000 | 0.014 | 0.258 | 0.004 | trig=-0.9989,after=0.0 |
| probing-rag+abstain | 0.05 | 0.289 | 0.027 | 0.108 | 0.324 | 0.056 | trig=0.2076,after=0.0 |
| probing-rag+abstain | 0.1 | 0.383 | 0.071 | 0.000 | 0.080 | 0.153 | trig=0.4387,after=0.0 |
| probing-rag+abstain | 0.15 | 0.514 | 0.123 | 0.012 | 0.354 | 0.178 | trig=0.3098,after=0.0002 |
| sep-rag+abstain | 0.03 | 0.016 | 0.000 | 0.000 | 0.000 | 0.004 | trig=-0.9974,after=0.0 |
| sep-rag+abstain | 0.05 | 0.016 | 0.000 | 0.040 | 0.490 | 0.004 | trig=-0.9974,after=0.0 |
| sep-rag+abstain | 0.1 | 0.356 | 0.089 | 0.000 | 0.004 | 0.188 | trig=0.1413,after=-1.0 |
| sep-rag+abstain | 0.15 | 0.496 | 0.129 | 0.134 | 0.136 | 0.187 | trig=0.0715,after=0.0002 |
| se-rag+abstain | 0.03 | 0.016 | 0.000 | 0.000 | 0.000 | 0.004 | trig=-1.0,after=0.0 |
| se-rag+abstain | 0.05 | 0.016 | 0.000 | 0.000 | 0.000 | 0.004 | trig=-1.0,after=0.0 |
| se-rag+abstain | 0.1 | 0.390 | 0.076 | 0.000 | 0.008 | 0.208 | trig=-0.0,after=0.0 |
| se-rag+abstain | 0.15 | 0.478 | 0.123 | 0.008 | 0.276 | 0.171 | trig=-1.0,after=0.0026 |

### 2. Calibration error per decision stage and route-eu's regret (TEST)

| lam | pre (P wrong before answering) | post (closed-book answer, Platt) | post_rag (evidence answer, Platt) | pre_rag (evidence turn) | regret | bound (1+lam)·Σ |
|---|---|---|---|---|---|---|
| 1.0 | 0.019 | 0.017 | 0.011 | 0.020 | -0.006 | 0.135 |
| 2.0 | 0.019 | 0.017 | 0.011 | 0.020 | -0.007 | 0.202 |
| 4.0 | 0.019 | 0.017 | 0.011 | 0.020 | -0.000 | 0.337 |

### 3. Hallucination vs compute: 58% of baseline points are dominated by a Tripwire point (<= halluc, <= prefill, >= acc)

### 4. Error flow at lam=1 (TEST, share of questions)

| closed-book | Tripwire action | outcome | share |
|---|---|---|---|
| closed-book correct | retrieve: evidence has answer | correct | 0.239 |
| closed-book correct | answer closed-book | correct | 0.167 |
| knowledge gap | retrieve: retrieval miss | abstain | 0.145 |
| knowledge gap | retrieve: evidence has answer | correct | 0.137 |
| knowledge gap | abstain at once | abstain | 0.088 |
| knowledge gap | retrieve: evidence has answer | abstain | 0.056 |
| knowledge gap | retrieve: retrieval miss | wrong | 0.025 |
| closed-book correct | retrieve: retrieval miss | abstain | 0.022 |
| closed-book correct | retrieve: evidence has answer | abstain | 0.020 |
| drift | retrieve: evidence has answer | correct | 0.019 |
| closed-book correct | retrieve: retrieval miss | correct | 0.017 |
| knowledge gap | retrieve: evidence has answer | wrong | 0.013 |
| knowledge gap | answer closed-book | wrong | 0.010 |
| closed-book correct | retrieve: evidence has answer | wrong | 0.007 |
| closed-book correct | abstain at once | abstain | 0.007 |
| drift | retrieve: retrieval miss | abstain | 0.006 |
| drift | retrieve: evidence has answer | abstain | 0.004 |
| drift | answer closed-book | wrong | 0.003 |
| closed-book correct | retrieve: retrieval miss | wrong | 0.003 |
| knowledge gap | retrieve: retrieval miss | correct | 0.003 |
| drift | retrieve: evidence has answer | wrong | 0.003 |
| drift | retrieve: retrieval miss | correct | 0.002 |
| drift | retrieve: retrieval miss | wrong | 0.002 |
| knowledge gap | answer closed-book | abstain | 0.001 |
| drift | abstain at once | abstain | 0.000 |

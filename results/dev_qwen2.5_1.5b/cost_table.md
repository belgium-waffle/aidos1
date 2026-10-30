### Cost per test question at lam=1.0 (thresholds from val)

| family | acc | halluc | prefill tok | decode tok | LLM prefills | samples | retrievals | ms / q (batched) | x vanilla |
|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.243 | 0.757 | 52 | 4.2 | 1.00 | 0.00 | 0.00 | 0.35 | 1.00 |
| oracle-route | 0.543 | 0.447 | 400 | 8.0 | 1.00 | 0.09 | 0.71 | 2.68 | 7.65 |
| rag-always | 0.521 | 0.479 | 592 | 4.6 | 2.00 | 0.00 | 1.00 | 3.09 | 8.84 |
| abstain | 0.144 | 0.060 | 52 | 1.1 | 1.00 | 0.00 | 0.00 | 0.35 | 1.01 |
| rollback+abstain | 0.159 | 0.070 | 52 | 2.5 | 1.00 | 0.28 | 0.00 | 0.39 | 1.10 |
| route-noretrieve | 0.146 | 0.060 | 52 | 1.2 | 1.00 | 0.00 | 0.00 | 0.35 | 1.01 |
| route | 0.441 | 0.157 | 540 | 4.6 | 1.00 | 0.00 | 1.00 | 3.46 | 9.89 |
| retrieve+abstain | 0.441 | 0.157 | 540 | 4.6 | 1.00 | 0.00 | 1.00 | 3.46 | 9.89 |
| abstain@logprob | 0.136 | 0.101 | 52 | 1.1 | 1.00 | 0.00 | 0.00 | 0.29 | 0.82 |
| route-noretrieve@logprob | 0.139 | 0.111 | 52 | 1.2 | 1.00 | 0.01 | 0.00 | 0.29 | 0.82 |
| route@logprob | 0.409 | 0.300 | 540 | 4.6 | 1.00 | 0.00 | 1.00 | 2.83 | 8.08 |
| abstain@entropy | 0.146 | 0.102 | 52 | 1.1 | 1.00 | 0.00 | 0.00 | 0.29 | 0.82 |
| route-noretrieve@entropy | 0.149 | 0.104 | 52 | 1.2 | 1.00 | 0.01 | 0.00 | 0.29 | 0.82 |
| route@entropy | 0.362 | 0.211 | 540 | 4.6 | 1.00 | 0.00 | 1.00 | 2.83 | 8.08 |
| route@cbrag | 0.350 | 0.132 | 540 | 4.6 | 1.00 | 0.00 | 1.00 | 3.46 | 9.89 |
| retrieve+abstain@cbrag | 0.350 | 0.132 | 540 | 4.6 | 1.00 | 0.00 | 1.00 | 3.46 | 9.89 |
| retrieve+abstain-2r | 0.442 | 0.178 | 734 | 6.5 | 1.00 | 0.00 | 1.40 | 4.71 | 13.46 |
| retrieve+abstain-conf | 0.444 | 0.171 | 1251 | 6.6 | 1.00 | 0.00 | 1.40 | 7.91 | 22.61 |
| route-eu | 0.365 | 0.082 | 384 | 3.4 | 1.00 | 0.00 | 0.68 | 2.47 | 7.04 |
| route-eu-2r | 0.363 | 0.079 | 486 | 4.6 | 1.00 | 0.00 | 0.88 | 3.13 | 8.94 |
| route-eu-conf | 0.372 | 0.084 | 818 | 4.6 | 1.00 | 0.00 | 0.88 | 5.18 | 14.80 |
| route-eu-help | 0.347 | 0.067 | 311 | 2.7 | 1.00 | 0.00 | 0.52 | 1.99 | 5.69 |
| route-eu-gain | 0.293 | 0.047 | 287 | 2.1 | 1.00 | 0.00 | 0.48 | 1.83 | 5.23 |
| route-eu-option | 0.365 | 0.082 | 384 | 3.4 | 1.00 | 0.00 | 0.68 | 2.47 | 7.04 |
| flare | 0.496 | 0.504 | 592 | 8.8 | 2.00 | 0.00 | 1.00 | 3.18 | 9.08 |
| flare+abstain | 0.193 | 0.112 | 592 | 8.8 | 2.00 | 0.00 | 1.00 | 3.18 | 9.08 |
| dragin | 0.516 | 0.484 | 592 | 8.8 | 2.00 | 0.00 | 1.00 | 3.18 | 9.08 |
| dragin+abstain | 0.303 | 0.162 | 592 | 8.8 | 2.00 | 0.00 | 1.00 | 3.18 | 9.08 |
| probing-rag | 0.521 | 0.479 | 592 | 4.6 | 2.00 | 0.00 | 1.00 | 3.09 | 8.84 |
| probing-rag+abstain | 0.241 | 0.116 | 592 | 4.6 | 2.00 | 0.00 | 1.00 | 3.09 | 8.84 |
| sep-rag | 0.521 | 0.479 | 592 | 4.6 | 2.00 | 0.00 | 1.00 | 3.09 | 8.84 |
| sep-rag+abstain | 0.241 | 0.116 | 592 | 4.6 | 2.00 | 0.00 | 1.00 | 3.09 | 8.84 |
| se-rag (+NLI) | 0.521 | 0.479 | 592 | 53.3 | 2.00 | 10.00 | 1.00 | 4.09 | 11.70 |
| se-rag+abstain (+NLI) | 0.241 | 0.116 | 592 | 53.3 | 2.00 | 10.00 | 1.00 | 4.09 | 11.70 |

Time model: 5.06 us / prefill token, 20.54 us / decode token (batched, fitted on vanilla + rag); Tripwire head overhead 22.4%.

| bench mode | measured s | predicted s | error |
|---|---|---|---|
| abstain-mondrian | 0.4 | 0.2 | -48.4% |
| abstain | 0.1 | 0.2 | +52.3% |
| observe | 0.2 | 0.2 | +6.6% |
| rag | 1.4 | 1.4 | +0.0% |
| retrieve+abstain-1r | 1.8 | 1.7 | -3.4% |
| retrieve+abstain-2r | 2.4 | 2.3 | -5.5% |
| retrieve+abstain-lam2 | 1.8 | 1.7 | -3.7% |
| retrieve+abstain-lam4 | 1.7 | 1.7 | -1.8% |
| retrieve+abstain | 1.8 | 1.7 | -3.6% |
| rollback | 0.2 | 0.2 | -8.1% |
| rollback+abstain | 0.2 | 0.2 | +11.8% |
| route-eu-1r | 0.8 | 0.8 | -0.3% |
| route-eu-2r | 1.5 | 1.5 | -2.7% |
| route-eu-gain | 0.9 | 0.9 | -1.5% |
| route-eu-help | 1.0 | 1.0 | -2.4% |
| route-eu-lam2 | 1.1 | 1.1 | -1.5% |
| route-eu-lam4 | 1.0 | 1.0 | +1.0% |
| route-eu-option | 1.2 | 1.2 | -2.8% |
| route-eu | 1.3 | 1.2 | -4.1% |
| route-noretrieve | 0.1 | 0.2 | +50.1% |
| route | 1.8 | 1.7 | -4.2% |
| vanilla | 0.2 | 0.2 | +0.0% |

Token model vs measured (per question; bench = 3k engine questions, latency = replay subset)

| family | source | prefill model / measured | decode model / measured |
|---|---|---|---|
| vanilla | bench | 52 / 52 | 4.2 / 4.1 |
| abstain | bench | 52 / 52 | 1.1 / 2.2 |
| rollback+abstain | bench | 52 / 52 | 2.5 / 3.0 |
| route-noretrieve | bench | 52 / 52 | 1.2 / 1.7 |
| route | bench | 540 / 540 | 4.6 / 4.2 |
| retrieve+abstain | bench | 540 / 540 | 4.6 / 4.2 |
| retrieve+abstain-2r | bench | 734 / 732 | 6.5 / 4.7 |
| route-eu | bench | 384 / 377 | 3.4 / 3.3 |
| route-eu-2r | bench | 486 / 472 | 4.6 / 3.4 |
| route-eu-help | bench | 311 / 298 | 2.7 / 2.9 |
| route-eu-gain | bench | 287 / 276 | 2.1 / 2.6 |
| route-eu-option | bench | 384 / 377 | 3.4 / 3.2 |
| flare+abstain | latency | 592 / 601 | 8.8 / 8.8 |
| dragin+abstain | latency | 592 / 601 | 8.8 / 8.8 |
| probing-rag+abstain | latency | 592 / 601 | 4.6 / 4.7 |
| sep-rag+abstain | latency | 592 / 601 | 4.6 / 4.7 |
| se-rag+abstain | latency | 592 / 653 | 53.3 / 52.0 |

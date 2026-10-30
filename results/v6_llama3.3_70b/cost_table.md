### Cost per test question at lam=1.0 (thresholds from val)

| family | acc | halluc | prefill tok | decode tok | LLM prefills | samples | retrievals | ms / q (batched) | x vanilla |
|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.650 | 0.350 | 73 | 4.3 | 1.00 | 0.00 | 0.00 | - | - |
| oracle-route | 0.744 | 0.244 | 223 | 6.1 | 1.00 | 0.06 | 0.32 | - | - |
| rag-always | 0.709 | 0.291 | 616 | 4.4 | 2.00 | 0.00 | 1.00 | - | - |
| abstain | 0.582 | 0.104 | 73 | 3.7 | 1.00 | 0.00 | 0.00 | - | - |
| rollback+abstain | 0.594 | 0.124 | 73 | 8.5 | 1.00 | 0.84 | 0.00 | - | - |
| route-noretrieve | 0.581 | 0.108 | 73 | 4.7 | 1.00 | 0.22 | 0.00 | - | - |
| route | 0.625 | 0.079 | 408 | 8.2 | 1.00 | 0.58 | 0.71 | - | - |
| retrieve+abstain | 0.626 | 0.077 | 435 | 5.0 | 1.00 | 0.00 | 0.77 | - | - |
| abstain@logprob | 0.559 | 0.146 | 73 | 3.4 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@logprob | 0.586 | 0.170 | 73 | 3.6 | 1.00 | 0.06 | 0.00 | - | - |
| route@logprob | 0.612 | 0.160 | 293 | 4.6 | 1.00 | 0.05 | 0.47 | - | - |
| abstain@entropy | 0.609 | 0.164 | 73 | 3.4 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@entropy | 0.588 | 0.158 | 73 | 3.5 | 1.00 | 0.04 | 0.00 | - | - |
| route@entropy | 0.652 | 0.199 | 300 | 4.8 | 1.00 | 0.07 | 0.48 | - | - |
| route@cbrag | 0.619 | 0.087 | 370 | 7.0 | 1.00 | 0.39 | 0.63 | - | - |
| retrieve+abstain@cbrag | 0.617 | 0.085 | 411 | 4.8 | 1.00 | 0.00 | 0.72 | - | - |
| rag+abstain | 0.628 | 0.073 | 543 | 4.4 | 1.00 | 0.00 | 1.00 | - | - |
| retrieve+abstain-2r | 0.643 | 0.091 | 573 | 6.4 | 1.00 | 0.00 | 1.07 | - | - |
| retrieve+abstain-conf | 0.648 | 0.092 | 946 | 6.4 | 1.00 | 0.00 | 1.07 | - | - |
| route-eu | 0.633 | 0.073 | 412 | 4.4 | 1.00 | 0.00 | 0.72 | - | - |
| route-eu-2r | 0.645 | 0.082 | 509 | 5.4 | 1.00 | 0.00 | 0.93 | - | - |
| route-eu-conf | 0.647 | 0.084 | 761 | 5.4 | 1.00 | 0.00 | 0.93 | - | - |
| route-eu-help | 0.618 | 0.069 | 337 | 3.9 | 1.00 | 0.00 | 0.56 | - | - |
| route-eu-gain | 0.601 | 0.059 | 362 | 3.7 | 1.00 | 0.00 | 0.61 | - | - |
| route-eu-option | 0.633 | 0.073 | 412 | 4.4 | 1.00 | 0.00 | 0.72 | - | - |
| flare | 0.707 | 0.293 | 456 | 7.5 | 1.70 | 0.00 | 0.70 | - | - |
| flare+abstain | 0.592 | 0.168 | 241 | 5.7 | 1.31 | 0.00 | 0.31 | - | - |
| dragin | 0.710 | 0.289 | 340 | 6.5 | 1.49 | 0.00 | 0.49 | - | - |
| dragin+abstain | 0.628 | 0.163 | 310 | 6.3 | 1.44 | 0.00 | 0.44 | - | - |
| probing-rag | 0.709 | 0.291 | 616 | 4.4 | 2.00 | 0.00 | 1.00 | - | - |
| probing-rag+abstain | 0.625 | 0.144 | 249 | 4.3 | 1.33 | 0.00 | 0.33 | - | - |
| sep-rag | 0.709 | 0.291 | 616 | 4.4 | 2.00 | 0.00 | 1.00 | - | - |
| sep-rag+abstain | 0.616 | 0.156 | 304 | 4.3 | 1.42 | 0.00 | 0.42 | - | - |
| se-rag (+NLI) | 0.709 | 0.291 | 272 | 49.3 | 1.37 | 10.00 | 0.37 | - | - |
| se-rag+abstain (+NLI) | 0.630 | 0.150 | 272 | 49.3 | 1.37 | 10.00 | 0.37 | - | - |

Token model vs measured (per question; bench = 3k engine questions, latency = replay subset)

| family | source | prefill model / measured | decode model / measured |
|---|---|---|---|
| vanilla | bench | 73 / 73 | 4.3 / 4.3 |
| abstain | bench | 73 / 73 | 3.7 / 3.0 |
| rollback+abstain | bench | 73 / 73 | 8.5 / 3.5 |
| route-noretrieve | bench | 73 / 73 | 4.7 / 3.8 |
| route | bench | 408 / 399 | 8.2 / 5.5 |
| retrieve+abstain | bench | 435 / 436 | 5.0 / 4.3 |
| retrieve+abstain-2r | bench | 573 / 574 | 6.4 / 4.8 |
| route-eu | bench | 412 / 413 | 4.4 / 4.2 |
| route-eu-2r | bench | 509 / 510 | 5.4 / 4.6 |
| route-eu-help | bench | 337 / 337 | 3.9 / 4.0 |
| route-eu-gain | bench | 362 / 362 | 3.7 / 3.9 |
| route-eu-option | bench | 412 / 412 | 4.4 / 4.2 |
| flare+abstain | latency | 241 / 271 | 5.7 / 5.5 |
| dragin+abstain | latency | 310 / 342 | 6.3 / 6.0 |
| probing-rag+abstain | latency | 249 / 249 | 4.3 / 4.1 |
| sep-rag+abstain | latency | 304 / 313 | 4.3 / 4.0 |
| se-rag+abstain | latency | 272 / 351 | 49.3 / 46.5 |

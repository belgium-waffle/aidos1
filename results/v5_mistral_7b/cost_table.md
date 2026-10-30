### Cost per test question at lam=1.0 (thresholds from val)

| family | acc | halluc | prefill tok | decode tok | LLM prefills | samples | retrievals | ms / q (batched) | x vanilla |
|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.486 | 0.514 | 46 | 10.2 | 1.00 | 0.00 | 0.00 | - | - |
| oracle-route | 0.660 | 0.323 | 305 | 16.6 | 1.00 | 0.09 | 0.47 | - | - |
| rag-always | 0.592 | 0.408 | 645 | 10.1 | 2.00 | 0.00 | 1.00 | - | - |
| abstain | 0.389 | 0.096 | 46 | 5.4 | 1.00 | 0.00 | 0.00 | - | - |
| rollback+abstain | 0.404 | 0.119 | 46 | 9.8 | 1.00 | 0.32 | 0.00 | - | - |
| route-noretrieve | 0.401 | 0.103 | 46 | 6.4 | 1.00 | 0.06 | 0.00 | - | - |
| route | 0.539 | 0.134 | 443 | 13.4 | 1.00 | 0.21 | 0.72 | - | - |
| retrieve+abstain | 0.540 | 0.135 | 448 | 10.2 | 1.00 | 0.00 | 0.73 | - | - |
| abstain@logprob | 0.343 | 0.108 | 46 | 4.2 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@logprob | 0.350 | 0.104 | 46 | 6.9 | 1.00 | 0.15 | 0.00 | - | - |
| route@logprob | 0.475 | 0.235 | 436 | 10.0 | 1.00 | 0.01 | 0.71 | - | - |
| abstain@entropy | 0.336 | 0.093 | 46 | 4.2 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@entropy | 0.353 | 0.101 | 46 | 6.4 | 1.00 | 0.12 | 0.00 | - | - |
| route@entropy | 0.507 | 0.242 | 443 | 10.4 | 1.00 | 0.02 | 0.72 | - | - |
| route@cbrag | 0.484 | 0.110 | 443 | 13.4 | 1.00 | 0.21 | 0.72 | - | - |
| retrieve+abstain@cbrag | 0.489 | 0.115 | 423 | 10.5 | 1.00 | 0.00 | 0.68 | - | - |
| rag+abstain | 0.528 | 0.132 | 599 | 10.1 | 1.00 | 0.00 | 1.00 | - | - |
| retrieve+abstain-2r | 0.545 | 0.145 | 626 | 14.2 | 1.00 | 0.00 | 1.05 | - | - |
| retrieve+abstain-conf | 0.513 | 0.103 | 1308 | 15.2 | 1.00 | 0.00 | 1.13 | - | - |
| route-eu | 0.483 | 0.079 | 428 | 8.8 | 1.00 | 0.00 | 0.69 | - | - |
| route-eu-2r | 0.496 | 0.084 | 577 | 12.1 | 1.00 | 0.00 | 0.96 | - | - |
| route-eu-conf | 0.495 | 0.086 | 1010 | 12.1 | 1.00 | 0.00 | 0.96 | - | - |
| route-eu-help | 0.458 | 0.071 | 320 | 6.6 | 1.00 | 0.00 | 0.49 | - | - |
| route-eu-gain | 0.431 | 0.065 | 335 | 6.1 | 1.00 | 0.00 | 0.52 | - | - |
| route-eu-option | 0.483 | 0.079 | 428 | 8.8 | 1.00 | 0.00 | 0.69 | - | - |
| flare | 0.585 | 0.415 | 645 | 20.2 | 2.00 | 0.00 | 1.00 | - | - |
| flare+abstain | 0.365 | 0.148 | 422 | 17.1 | 1.63 | 0.00 | 0.63 | - | - |
| dragin | 0.590 | 0.410 | 458 | 17.7 | 1.69 | 0.00 | 0.69 | - | - |
| dragin+abstain | 0.415 | 0.162 | 411 | 17.0 | 1.61 | 0.00 | 0.61 | - | - |
| probing-rag | 0.598 | 0.402 | 459 | 9.8 | 1.69 | 0.00 | 0.69 | - | - |
| probing-rag+abstain | 0.447 | 0.158 | 381 | 9.8 | 1.56 | 0.00 | 0.56 | - | - |
| sep-rag | 0.597 | 0.403 | 460 | 9.7 | 1.69 | 0.00 | 0.69 | - | - |
| sep-rag+abstain | 0.431 | 0.176 | 382 | 9.5 | 1.56 | 0.00 | 0.56 | - | - |
| se-rag (+NLI) | 0.596 | 0.404 | 453 | 129.2 | 1.68 | 10.00 | 0.68 | - | - |
| se-rag+abstain (+NLI) | 0.409 | 0.152 | 428 | 128.8 | 1.64 | 10.00 | 0.64 | - | - |

Token model vs measured (per question; bench = 3k engine questions, latency = replay subset)

| family | source | prefill model / measured | decode model / measured |
|---|---|---|---|
| vanilla | bench | 46 / 46 | 10.2 / 10.2 |
| abstain | bench | 46 / 46 | 5.4 / 5.2 |
| rollback+abstain | bench | 46 / 46 | 9.8 / 6.1 |
| route-noretrieve | bench | 46 / 46 | 6.4 / 5.2 |
| route | bench | 443 / 440 | 13.4 / 7.6 |
| retrieve+abstain | bench | 448 / 447 | 10.2 / 7.0 |
| retrieve+abstain-2r | bench | 626 / 627 | 14.2 / 7.5 |
| route-eu | bench | 428 / 429 | 8.8 / 6.2 |
| route-eu-2r | bench | 577 / 581 | 12.1 / 6.7 |
| route-eu-help | bench | 320 / 319 | 6.6 / 5.7 |
| route-eu-gain | bench | 335 / 333 | 6.1 / 5.4 |
| route-eu-option | bench | 428 / 429 | 8.8 / 6.2 |
| flare+abstain | latency | 422 / 325 | 17.1 / 14.7 |
| dragin+abstain | latency | 411 / 327 | 17.0 / 14.7 |
| probing-rag+abstain | latency | 381 / 329 | 9.8 / 8.8 |
| sep-rag+abstain | latency | 382 / 347 | 9.5 / 8.5 |
| se-rag+abstain | latency | 428 / 440 | 128.8 / 113.3 |

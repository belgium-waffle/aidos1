### Cost per test question at lam=1.0 (thresholds from val)

| family | acc | halluc | prefill tok | decode tok | LLM prefills | samples | retrievals | ms / q (batched) | x vanilla |
|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.483 | 0.517 | 52 | 4.3 | 1.00 | 0.00 | 0.00 | - | - |
| oracle-route | 0.677 | 0.311 | 285 | 7.1 | 1.00 | 0.07 | 0.48 | - | - |
| rag-always | 0.651 | 0.349 | 589 | 4.5 | 2.00 | 0.00 | 1.00 | - | - |
| abstain | 0.411 | 0.076 | 52 | 2.5 | 1.00 | 0.00 | 0.00 | - | - |
| rollback+abstain | 0.416 | 0.087 | 52 | 4.4 | 1.00 | 0.35 | 0.00 | - | - |
| route-noretrieve | 0.415 | 0.085 | 52 | 3.0 | 1.00 | 0.03 | 0.00 | - | - |
| route | 0.596 | 0.082 | 382 | 8.6 | 1.00 | 0.46 | 0.68 | - | - |
| retrieve+abstain | 0.596 | 0.081 | 386 | 5.9 | 1.00 | 0.00 | 0.69 | - | - |
| abstain@logprob | 0.398 | 0.124 | 52 | 2.5 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@logprob | 0.363 | 0.090 | 52 | 2.0 | 1.00 | 0.02 | 0.00 | - | - |
| route@logprob | 0.506 | 0.143 | 369 | 5.0 | 1.00 | 0.05 | 0.65 | - | - |
| abstain@entropy | 0.437 | 0.147 | 52 | 2.5 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@entropy | 0.418 | 0.130 | 52 | 2.8 | 1.00 | 0.03 | 0.00 | - | - |
| route@entropy | 0.507 | 0.141 | 371 | 4.9 | 1.00 | 0.04 | 0.66 | - | - |
| route@cbrag | 0.585 | 0.119 | 382 | 8.6 | 1.00 | 0.46 | 0.68 | - | - |
| retrieve+abstain@cbrag | 0.584 | 0.116 | 385 | 6.1 | 1.00 | 0.00 | 0.68 | - | - |
| rag+abstain | 0.604 | 0.094 | 537 | 4.5 | 1.00 | 0.00 | 1.00 | - | - |
| retrieve+abstain-2r | 0.610 | 0.092 | 541 | 7.5 | 1.00 | 0.00 | 1.01 | - | - |
| retrieve+abstain-conf | 0.614 | 0.093 | 957 | 7.4 | 1.00 | 0.00 | 1.01 | - | - |
| route-eu | 0.584 | 0.067 | 404 | 4.3 | 1.00 | 0.00 | 0.72 | - | - |
| route-eu-2r | 0.600 | 0.075 | 532 | 5.6 | 1.00 | 0.00 | 0.99 | - | - |
| route-eu-conf | 0.602 | 0.078 | 862 | 5.6 | 1.00 | 0.00 | 0.99 | - | - |
| route-eu-help | 0.551 | 0.059 | 315 | 3.4 | 1.00 | 0.00 | 0.54 | - | - |
| route-eu-gain | 0.515 | 0.053 | 334 | 3.0 | 1.00 | 0.00 | 0.58 | - | - |
| route-eu-option | 0.584 | 0.067 | 404 | 4.3 | 1.00 | 0.00 | 0.72 | - | - |
| flare | 0.618 | 0.381 | 423 | 7.6 | 1.69 | 0.00 | 0.69 | - | - |
| flare+abstain | 0.452 | 0.106 | 423 | 7.6 | 1.69 | 0.00 | 0.69 | - | - |
| dragin | 0.645 | 0.354 | 422 | 7.6 | 1.69 | 0.00 | 0.69 | - | - |
| dragin+abstain | 0.495 | 0.126 | 385 | 7.3 | 1.62 | 0.00 | 0.62 | - | - |
| probing-rag | 0.651 | 0.349 | 589 | 4.5 | 2.00 | 0.00 | 1.00 | - | - |
| probing-rag+abstain | 0.514 | 0.123 | 388 | 4.5 | 1.63 | 0.00 | 0.63 | - | - |
| sep-rag | 0.651 | 0.349 | 589 | 4.5 | 2.00 | 0.00 | 1.00 | - | - |
| sep-rag+abstain | 0.535 | 0.164 | 350 | 4.5 | 1.55 | 0.00 | 0.55 | - | - |
| se-rag (+NLI) | 0.651 | 0.349 | 589 | 53.2 | 2.00 | 10.00 | 1.00 | - | - |
| se-rag+abstain (+NLI) | 0.544 | 0.150 | 341 | 51.4 | 1.54 | 10.00 | 0.54 | - | - |

Token model vs measured (per question; bench = 3k engine questions, latency = replay subset)

| family | source | prefill model / measured | decode model / measured |
|---|---|---|---|
| vanilla | bench | 52 / 52 | 4.3 / 4.3 |
| abstain | bench | 52 / 52 | 2.5 / 2.6 |
| rollback+abstain | bench | 52 / 52 | 4.4 / 3.2 |
| route-noretrieve | bench | 52 / 52 | 3.0 / 2.8 |
| route | bench | 382 / 375 | 8.6 / 5.5 |
| retrieve+abstain | bench | 386 / 388 | 5.9 / 4.4 |
| retrieve+abstain-2r | bench | 541 / 544 | 7.5 / 4.9 |
| route-eu | bench | 404 / 405 | 4.3 / 4.0 |
| route-eu-2r | bench | 532 / 533 | 5.6 / 4.5 |
| route-eu-help | bench | 315 / 315 | 3.4 / 3.7 |
| route-eu-gain | bench | 334 / 331 | 3.0 / 3.5 |
| route-eu-option | bench | 404 / 405 | 4.3 / 4.0 |
| flare+abstain | latency | 423 / 367 | 7.6 / 6.8 |
| dragin+abstain | latency | 385 / 323 | 7.3 / 6.4 |
| probing-rag+abstain | latency | 388 / 372 | 4.5 / 4.1 |
| sep-rag+abstain | latency | 350 / 341 | 4.5 / 4.1 |
| se-rag+abstain | latency | 341 / 352 | 51.4 / 50.4 |

### Cost per test question at lam=1.0 (thresholds from val)

| family | acc | halluc | prefill tok | decode tok | LLM prefills | samples | retrievals | ms / q (batched) | x vanilla |
|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.484 | 0.516 | 73 | 5.1 | 1.00 | 0.00 | 0.00 | - | - |
| oracle-route | 0.652 | 0.322 | 283 | 8.2 | 1.00 | 0.14 | 0.45 | - | - |
| rag-always | 0.602 | 0.398 | 616 | 4.5 | 2.00 | 0.00 | 1.00 | - | - |
| abstain | 0.430 | 0.134 | 73 | 4.0 | 1.00 | 0.00 | 0.00 | - | - |
| rollback+abstain | 0.420 | 0.128 | 73 | 5.0 | 1.00 | 0.27 | 0.00 | - | - |
| route-noretrieve | 0.439 | 0.140 | 73 | 4.8 | 1.00 | 0.08 | 0.00 | - | - |
| route | 0.560 | 0.111 | 417 | 5.0 | 1.00 | 0.02 | 0.73 | - | - |
| retrieve+abstain | 0.560 | 0.111 | 418 | 4.8 | 1.00 | 0.00 | 0.73 | - | - |
| abstain@logprob | 0.413 | 0.129 | 73 | 3.0 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@logprob | 0.386 | 0.108 | 73 | 2.7 | 1.00 | 0.02 | 0.00 | - | - |
| route@logprob | 0.501 | 0.173 | 311 | 5.1 | 1.00 | 0.02 | 0.51 | - | - |
| abstain@entropy | 0.396 | 0.096 | 73 | 2.9 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@entropy | 0.389 | 0.091 | 73 | 2.7 | 1.00 | 0.01 | 0.00 | - | - |
| route@entropy | 0.508 | 0.158 | 318 | 5.1 | 1.00 | 0.01 | 0.52 | - | - |
| route@cbrag | 0.536 | 0.122 | 375 | 5.3 | 1.00 | 0.02 | 0.64 | - | - |
| retrieve+abstain@cbrag | 0.536 | 0.122 | 376 | 5.2 | 1.00 | 0.00 | 0.64 | - | - |
| rag+abstain | 0.552 | 0.108 | 543 | 4.5 | 1.00 | 0.00 | 1.00 | - | - |
| retrieve+abstain-2r | 0.532 | 0.083 | 613 | 6.7 | 1.00 | 0.00 | 1.15 | - | - |
| retrieve+abstain-conf | 0.573 | 0.122 | 986 | 6.3 | 1.00 | 0.00 | 1.06 | - | - |
| route-eu | 0.514 | 0.065 | 408 | 4.3 | 1.00 | 0.00 | 0.71 | - | - |
| route-eu-2r | 0.532 | 0.074 | 558 | 5.7 | 1.00 | 0.00 | 1.03 | - | - |
| route-eu-conf | 0.531 | 0.076 | 937 | 5.7 | 1.00 | 0.00 | 1.03 | - | - |
| route-eu-help | 0.480 | 0.061 | 307 | 3.4 | 1.00 | 0.00 | 0.49 | - | - |
| route-eu-gain | 0.447 | 0.055 | 344 | 3.0 | 1.00 | 0.00 | 0.57 | - | - |
| route-eu-option | 0.514 | 0.065 | 408 | 4.3 | 1.00 | 0.00 | 0.71 | - | - |
| flare | 0.597 | 0.402 | 448 | 8.3 | 1.69 | 0.00 | 0.69 | - | - |
| flare+abstain | 0.454 | 0.158 | 348 | 7.4 | 1.51 | 0.00 | 0.51 | - | - |
| dragin | 0.616 | 0.384 | 383 | 7.8 | 1.57 | 0.00 | 0.57 | - | - |
| dragin+abstain | 0.469 | 0.126 | 357 | 7.5 | 1.52 | 0.00 | 0.52 | - | - |
| probing-rag | 0.598 | 0.402 | 458 | 4.6 | 1.71 | 0.00 | 0.71 | - | - |
| probing-rag+abstain | 0.451 | 0.126 | 380 | 4.7 | 1.57 | 0.00 | 0.57 | - | - |
| sep-rag | 0.604 | 0.396 | 458 | 4.6 | 1.71 | 0.00 | 0.71 | - | - |
| sep-rag+abstain | 0.421 | 0.106 | 415 | 4.7 | 1.63 | 0.00 | 0.63 | - | - |
| se-rag (+NLI) | 0.617 | 0.383 | 424 | 65.7 | 1.65 | 10.00 | 0.65 | - | - |
| se-rag+abstain (+NLI) | 0.468 | 0.122 | 367 | 65.3 | 1.54 | 10.00 | 0.54 | - | - |

Token model vs measured (per question; bench = 3k engine questions, latency = replay subset)

| family | source | prefill model / measured | decode model / measured |
|---|---|---|---|
| vanilla | bench | 73 / 73 | 5.1 / 5.1 |
| abstain | bench | 73 / 73 | 4.0 / 3.2 |
| rollback+abstain | bench | 73 / 73 | 5.0 / 3.8 |
| route-noretrieve | bench | 73 / 73 | 4.8 / 3.8 |
| route | bench | 417 / 418 | 5.0 / 4.4 |
| retrieve+abstain | bench | 418 / 419 | 4.8 / 4.4 |
| retrieve+abstain-2r | bench | 613 / 614 | 6.7 / 5.4 |
| route-eu | bench | 408 / 407 | 4.3 / 4.0 |
| route-eu-2r | bench | 558 / 555 | 5.7 / 4.4 |
| route-eu-help | bench | 307 / 305 | 3.4 / 3.6 |
| route-eu-gain | bench | 344 / 342 | 3.0 / 3.4 |
| route-eu-option | bench | 408 / 405 | 4.3 / 3.9 |
| flare+abstain | latency | 348 / 356 | 7.4 / 7.0 |
| dragin+abstain | latency | 357 / 372 | 7.5 / 7.2 |
| probing-rag+abstain | latency | 380 / 344 | 4.7 / 4.4 |
| sep-rag+abstain | latency | 415 / 408 | 4.7 / 4.3 |
| se-rag+abstain | latency | 367 / 433 | 65.3 / 61.8 |

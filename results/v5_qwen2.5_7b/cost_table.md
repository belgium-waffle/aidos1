### Cost per test question at lam=1.0 (thresholds from val)

| family | acc | halluc | prefill tok | decode tok | LLM prefills | samples | retrievals | ms / q (batched) | x vanilla |
|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.367 | 0.633 | 52 | 4.1 | 1.00 | 0.00 | 0.00 | - | - |
| oracle-route | 0.621 | 0.362 | 336 | 7.4 | 1.00 | 0.10 | 0.58 | - | - |
| rag-always | 0.569 | 0.431 | 589 | 4.5 | 2.00 | 0.00 | 1.00 | - | - |
| abstain | 0.305 | 0.089 | 52 | 2.4 | 1.00 | 0.00 | 0.00 | - | - |
| rollback+abstain | 0.310 | 0.090 | 52 | 3.8 | 1.00 | 0.39 | 0.00 | - | - |
| route-noretrieve | 0.307 | 0.085 | 52 | 2.4 | 1.00 | 0.07 | 0.00 | - | - |
| route | 0.502 | 0.086 | 419 | 5.0 | 1.00 | 0.07 | 0.75 | - | - |
| retrieve+abstain | 0.502 | 0.085 | 421 | 4.8 | 1.00 | 0.00 | 0.76 | - | - |
| abstain@logprob | 0.259 | 0.084 | 52 | 1.5 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@logprob | 0.247 | 0.086 | 52 | 1.6 | 1.00 | 0.03 | 0.00 | - | - |
| route@logprob | 0.451 | 0.243 | 403 | 4.6 | 1.00 | 0.02 | 0.72 | - | - |
| abstain@entropy | 0.268 | 0.085 | 52 | 1.5 | 1.00 | 0.00 | 0.00 | - | - |
| route-noretrieve@entropy | 0.262 | 0.087 | 52 | 1.4 | 1.00 | 0.01 | 0.00 | - | - |
| route@entropy | 0.446 | 0.235 | 403 | 4.6 | 1.00 | 0.02 | 0.72 | - | - |
| route@cbrag | 0.476 | 0.131 | 393 | 5.6 | 1.00 | 0.04 | 0.70 | - | - |
| retrieve+abstain@cbrag | 0.475 | 0.131 | 394 | 5.5 | 1.00 | 0.00 | 0.70 | - | - |
| rag+abstain | 0.478 | 0.085 | 537 | 4.5 | 1.00 | 0.00 | 1.00 | - | - |
| retrieve+abstain-2r | 0.512 | 0.094 | 619 | 6.8 | 1.00 | 0.00 | 1.17 | - | - |
| retrieve+abstain-conf | 0.514 | 0.107 | 1098 | 7.4 | 1.00 | 0.00 | 1.10 | - | - |
| route-eu | 0.474 | 0.069 | 391 | 3.7 | 1.00 | 0.00 | 0.70 | - | - |
| route-eu-2r | 0.484 | 0.077 | 521 | 5.0 | 1.00 | 0.00 | 0.96 | - | - |
| route-eu-conf | 0.485 | 0.081 | 865 | 5.0 | 1.00 | 0.00 | 0.96 | - | - |
| route-eu-help | 0.443 | 0.060 | 300 | 2.9 | 1.00 | 0.00 | 0.51 | - | - |
| route-eu-gain | 0.410 | 0.049 | 299 | 2.6 | 1.00 | 0.00 | 0.51 | - | - |
| route-eu-option | 0.474 | 0.069 | 391 | 3.7 | 1.00 | 0.00 | 0.70 | - | - |
| flare | 0.548 | 0.452 | 589 | 8.7 | 2.00 | 0.00 | 1.00 | - | - |
| flare+abstain | 0.235 | 0.069 | 426 | 7.5 | 1.70 | 0.00 | 0.70 | - | - |
| dragin | 0.569 | 0.431 | 428 | 7.5 | 1.70 | 0.00 | 0.70 | - | - |
| dragin+abstain | 0.428 | 0.219 | 428 | 7.5 | 1.70 | 0.00 | 0.70 | - | - |
| probing-rag | 0.569 | 0.431 | 589 | 4.5 | 2.00 | 0.00 | 1.00 | - | - |
| probing-rag+abstain | 0.389 | 0.162 | 419 | 4.4 | 1.68 | 0.00 | 0.68 | - | - |
| sep-rag | 0.563 | 0.437 | 427 | 4.4 | 1.70 | 0.00 | 0.70 | - | - |
| sep-rag+abstain | 0.412 | 0.207 | 427 | 4.4 | 1.70 | 0.00 | 0.70 | - | - |
| se-rag (+NLI) | 0.570 | 0.430 | 388 | 49.9 | 1.63 | 10.00 | 0.63 | - | - |
| se-rag+abstain (+NLI) | 0.461 | 0.245 | 388 | 49.9 | 1.63 | 10.00 | 0.63 | - | - |

Token model vs measured (per question; bench = 3k engine questions, latency = replay subset)

| family | source | prefill model / measured | decode model / measured |
|---|---|---|---|
| vanilla | bench | 52 / 52 | 4.1 / 4.1 |
| abstain | bench | 52 / 52 | 2.4 / 2.3 |
| rollback+abstain | bench | 52 / 52 | 3.8 / 2.9 |
| route-noretrieve | bench | 52 / 52 | 2.4 / 2.4 |
| route | bench | 419 / 419 | 5.0 / 4.0 |
| retrieve+abstain | bench | 421 / 422 | 4.8 / 3.9 |
| retrieve+abstain-2r | bench | 619 / 622 | 6.8 / 4.5 |
| route-eu | bench | 391 / 390 | 3.7 / 3.6 |
| route-eu-2r | bench | 521 / 519 | 5.0 / 3.9 |
| route-eu-help | bench | 300 / 297 | 2.9 / 3.2 |
| route-eu-gain | bench | 299 / 297 | 2.6 / 3.1 |
| route-eu-option | bench | 391 / 390 | 3.7 / 3.6 |
| flare+abstain | latency | 426 / 372 | 7.5 / 7.0 |
| dragin+abstain | latency | 428 / 372 | 7.5 / 7.0 |
| probing-rag+abstain | latency | 419 / 369 | 4.4 / 4.4 |
| sep-rag+abstain | latency | 427 / 381 | 4.4 / 4.4 |
| se-rag+abstain | latency | 388 / 376 | 49.9 / 48.4 |

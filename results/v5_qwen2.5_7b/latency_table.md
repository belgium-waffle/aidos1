Retrieval service (live BM25 top-50 + BAAI/bge-reranker-v2-m3, one query at a time): p50 299.4 ms (BM25 261.8 + rerank 33.9), p99 376.6 ms

### Tokens per question (c1 questions; measured)

| method | prefill | decode | total | x vanilla | LLM requests | retrievals | acc | halluc |
|---|---|---|---|---|---|---|---|---|
| vanilla | 52 | 4.0 | 56 | 1.00 | 1.00 | 0.00 | 0.460 | 0.540 |
| rag | 541 | 4.5 | 546 | 9.74 | 1.00 | 1.00 | 0.510 | 0.490 |
| replay:flare+abstain | 372 | 7.0 | 379 | 6.76 | 1.60 | 0.60 | 0.235 | 0.069 |
| replay:dragin+abstain | 372 | 7.0 | 379 | 6.76 | 1.60 | 0.60 | 0.428 | 0.219 |
| replay:probing-rag+abstain | 369 | 4.4 | 373 | 6.67 | 1.59 | 0.59 | 0.389 | 0.162 |
| replay:sep-rag+abstain | 381 | 4.4 | 385 | 6.88 | 1.61 | 0.61 | 0.412 | 0.207 |
| replay:se-rag+abstain | 376 | 48.4 | 424 | 7.58 | 2.51 | 0.51 | 0.461 | 0.245 |
| observe | 52 | 4.0 | 56 | 1.00 | 1.00 | 0.00 | 0.460 | 0.540 |
| retrieve+abstain | 374 | 3.8 | 377 | 6.74 | 1.00 | 0.66 | 0.530 | 0.060 |
| route-eu | 365 | 3.6 | 368 | 6.57 | 1.00 | 0.64 | 0.480 | 0.060 |
| route-eu-2r | 480 | 3.9 | 484 | 8.64 | 1.00 | 0.88 | 0.480 | 0.070 |
| live:flare+abstain | 379 | 7.0 | 386 | 6.88 | 1.61 | 0.61 | 0.320 | 0.070 |
| live:dragin+abstain | 374 | 6.9 | 381 | 6.80 | 1.60 | 0.60 | 0.470 | 0.250 |
| live:probing-rag+abstain | 369 | 4.4 | 373 | 6.67 | 1.59 | 0.59 | 0.500 | 0.180 |
| live:sep-rag+abstain | 381 | 4.4 | 385 | 6.88 | 1.61 | 0.61 | 0.480 | 0.240 |
| live:se-rag+abstain | 376 | 47.8 | 424 | 7.57 | 2.51 | 0.51 | 0.520 | 0.300 |

(acc / halluc: measured for real generations; simulated on the full test split for replays)

### Latency, one request at a time (c1)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 11 | 11 | 25 | 36 | 55 | - | - | 25 | 0.00 | 38.80 | 61% |
| rag | 315 | 383 | 334 | 365 | 408 | 334 | 408 | - | 1.00 | 2.95 | 7% |
| replay:flare+abstain | 341 | 418 | 341 | 385 | 418 | 361 | 436 | 16 | 0.60 | 4.42 | 16% |
| replay:dragin+abstain | 341 | 419 | 341 | 385 | 419 | 361 | 436 | 16 | 0.60 | 4.42 | 16% |
| replay:probing-rag+abstain | 323 | 429 | 323 | 369 | 429 | 342 | 431 | 21 | 0.59 | 4.69 | 16% |
| replay:sep-rag+abstain | 325 | 428 | 325 | 369 | 428 | 345 | 430 | 16 | 0.61 | 4.56 | 16% |
| replay:se-rag+abstain | 322 | 454 | 322 | 391 | 454 | 369 | 493 | 23 | 0.51 | 4.90 | 29% |
| observe | 23 | 50 | 23 | 34 | 55 | - | - | 23 | 0.00 | 43.66 | 0% |
| retrieve+abstain | 318 | 410 | 318 | 362 | 410 | 337 | 415 | 18 | 0.66 | 4.33 | 2% |
| route-eu | 319 | 398 | 319 | 366 | 398 | 345 | 413 | 7 | 0.64 | 4.47 | 4% |
| route-eu-2r | 337 | 702 | 337 | 652 | 702 | 367 | 739 | 6 | 0.64 | 3.34 | 3% |
| live:flare+abstain | 346 | 470 | 346 | 392 | 470 | 370 | 1141 | 21 | 0.61 | 3.95 | 16% |
| live:dragin+abstain | 348 | 425 | 348 | 388 | 425 | 366 | 442 | 21 | 0.60 | 4.31 | 16% |
| live:probing-rag+abstain | 328 | 433 | 328 | 374 | 433 | 347 | 435 | 26 | 0.59 | 4.59 | 16% |
| live:sep-rag+abstain | 330 | 433 | 330 | 373 | 433 | 350 | 435 | 21 | 0.61 | 4.46 | 16% |
| live:se-rag+abstain | 331 | 467 | 331 | 404 | 467 | 381 | 517 | 28 | 0.51 | 4.74 | 29% |

### Latency, Poisson arrivals at 25% of the sustainable always-RAG throughput (26.0 q/s: GPU bench rate capped by the retrieval pool) (p25)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 7 | 15 | 22 | 32 | 47 | - | - | 22 | 0.00 | 6.11 | 62% |
| rag | 319 | 415 | 339 | 370 | 421 | 339 | 421 | - | 1.00 | 6.09 | 6% |
| replay:flare+abstain | 351 | 429 | 351 | 397 | 429 | 364 | 442 | 18 | 0.72 | 6.09 | 14% |
| replay:dragin+abstain | 352 | 435 | 352 | 393 | 435 | 366 | 452 | 20 | 0.72 | 6.09 | 14% |
| replay:probing-rag+abstain | 333 | 419 | 333 | 372 | 419 | 345 | 435 | 21 | 0.68 | 6.09 | 15% |
| replay:sep-rag+abstain | 334 | 443 | 334 | 369 | 443 | 347 | 449 | 21 | 0.70 | 6.09 | 15% |
| replay:se-rag+abstain | 357 | 454 | 357 | 403 | 454 | 372 | 481 | 25 | 0.63 | 6.08 | 25% |
| observe | 23 | 50 | 23 | 34 | 51 | - | - | 23 | 0.00 | 6.11 | 0% |
| retrieve+abstain | 329 | 420 | 329 | 369 | 420 | 339 | 429 | 20 | 0.76 | 6.08 | 2% |
| route-eu | 327 | 416 | 327 | 368 | 416 | 341 | 439 | 9 | 0.70 | 6.09 | 3% |
| route-eu-2r | 348 | 734 | 348 | 669 | 734 | 375 | 756 | 9 | 0.70 | 6.07 | 2% |
| live:flare+abstain | 360 | 604 | 360 | 427 | 604 | 375 | 619 | 22 | 0.72 | 6.09 | 14% |
| live:dragin+abstain | 356 | 468 | 356 | 404 | 468 | 372 | 495 | 22 | 0.72 | 6.09 | 14% |
| live:probing-rag+abstain | 333 | 423 | 333 | 373 | 423 | 346 | 435 | 22 | 0.68 | 6.09 | 15% |
| live:sep-rag+abstain | 334 | 444 | 334 | 370 | 444 | 348 | 449 | 22 | 0.70 | 6.09 | 15% |
| live:se-rag+abstain | 367 | 526 | 367 | 427 | 526 | 387 | 535 | 29 | 0.63 | 6.08 | 25% |

### Latency, Poisson arrivals at 75% of the sustainable always-RAG throughput (26.0 q/s: GPU bench rate capped by the retrieval pool) (p75)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 7 | 15 | 22 | 35 | 49 | - | - | 22 | 0.00 | 19.72 | 62% |
| rag | 332 | 608 | 353 | 444 | 632 | 353 | 632 | - | 1.00 | 19.49 | 6% |
| replay:flare+abstain | 363 | 485 | 363 | 415 | 485 | 379 | 506 | 25 | 0.72 | 19.46 | 14% |
| replay:dragin+abstain | 364 | 487 | 364 | 416 | 487 | 377 | 511 | 25 | 0.72 | 19.49 | 14% |
| replay:probing-rag+abstain | 340 | 457 | 340 | 390 | 457 | 355 | 476 | 24 | 0.68 | 19.51 | 15% |
| replay:sep-rag+abstain | 341 | 464 | 341 | 388 | 464 | 356 | 469 | 24 | 0.70 | 19.50 | 15% |
| replay:se-rag+abstain | 367 | 480 | 367 | 421 | 480 | 386 | 522 | 29 | 0.63 | 19.48 | 25% |
| observe | 23 | 51 | 23 | 35 | 51 | - | - | 23 | 0.00 | 19.72 | 0% |
| retrieve+abstain | 336 | 506 | 336 | 387 | 506 | 347 | 510 | 24 | 0.76 | 19.25 | 2% |
| route-eu | 334 | 463 | 334 | 377 | 463 | 348 | 483 | 12 | 0.70 | 19.49 | 3% |
| route-eu-2r | 367 | 1045 | 367 | 694 | 1045 | 425 | 1066 | 15 | 0.70 | 19.30 | 2% |
| live:flare+abstain | 369 | 515 | 369 | 430 | 515 | 384 | 521 | 27 | 0.72 | 19.48 | 14% |
| live:dragin+abstain | 368 | 540 | 368 | 430 | 540 | 382 | 546 | 27 | 0.72 | 19.47 | 14% |
| live:probing-rag+abstain | 342 | 465 | 342 | 392 | 465 | 357 | 482 | 25 | 0.68 | 19.50 | 15% |
| live:sep-rag+abstain | 343 | 468 | 343 | 389 | 468 | 357 | 470 | 24 | 0.70 | 19.49 | 15% |
| live:se-rag+abstain | 380 | 564 | 380 | 456 | 564 | 405 | 566 | 33 | 0.63 | 19.47 | 25% |

(ms; TTFT = first answer token the client receives; E2E = arrival to last token or abstention; the prefix cache is emptied before every scenario (bench.latency_cold_cache), so hits are only shared prompt prefixes within a scenario)

### Baselines executed live (2991 bench questions, all arriving at once; thresholds chosen on val)

Each method runs as a controller on the real outputs: draft -> trigger -> its own query -> retrieval -> evidence answer -> abstain rule. `sim` = the policy stage's composition of measured parts on the full test split. Retrieval cache: 16129 hits, 115 queries searched live (drafts that differ from the generate stage's).

| lam | method | acc | halluc | coverage | retrieved | utility | sim acc | sim halluc | q/s |
|---|---|---|---|---|---|---|---|---|---|
| 1 | flare+abstain | 0.234 | 0.068 | 0.302 | 0.70 | 0.152 | 0.235 | 0.069 | 36.7 |
| 1 | dragin+abstain | 0.430 | 0.216 | 0.647 | 0.71 | 0.200 | 0.428 | 0.219 | 36.3 |
| 1 | probing-rag+abstain | 0.388 | 0.163 | 0.551 | 0.69 | 0.211 | 0.389 | 0.162 | 37.6 |
| 1 | sep-rag+abstain | 0.411 | 0.205 | 0.616 | 0.70 | 0.192 | 0.412 | 0.207 | 36.8 |
| 1 | se-rag+abstain | 0.459 | 0.246 | 0.705 | 0.63 | 0.201 | 0.461 | 0.245 | 40.5 |
| 2 | flare+abstain | 0.234 | 0.068 | 0.302 | 0.70 | 0.084 | 0.235 | 0.069 | 36.6 |
| 2 | dragin+abstain | 0.231 | 0.063 | 0.294 | 0.71 | 0.091 | 0.232 | 0.066 | 36.2 |
| 2 | probing-rag+abstain | 0.249 | 0.066 | 0.315 | 0.69 | 0.104 | 0.251 | 0.065 | 37.6 |
| 2 | sep-rag+abstain | 0.218 | 0.083 | 0.301 | 0.70 | 0.039 | 0.219 | 0.084 | 36.9 |
| 2 | se-rag+abstain | 0.278 | 0.095 | 0.372 | 0.63 | 0.076 | 0.278 | 0.096 | 40.8 |
| 4 | flare+abstain | 0.000 | 0.000 | 0.000 | 1.00 | -0.020 | 0.000 | 0.000 | 25.8 |
| 4 | dragin+abstain | 0.000 | 0.000 | 0.000 | 1.00 | -0.020 | 0.000 | 0.000 | 25.8 |
| 4 | probing-rag+abstain | 0.249 | 0.066 | 0.315 | 0.69 | -0.027 | 0.251 | 0.065 | 37.6 |
| 4 | sep-rag+abstain | 0.000 | 0.000 | 0.000 | 1.00 | -0.020 | 0.000 | 0.000 | 25.9 |
| 4 | se-rag+abstain | 0.000 | 0.000 | 0.000 | 1.00 | -0.020 | 0.000 | 0.000 | 25.6 |

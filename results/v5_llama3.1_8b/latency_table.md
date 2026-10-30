Retrieval service (live BM25 top-50 + BAAI/bge-reranker-v2-m3, one query at a time): p50 302.4 ms (BM25 265.2 + rerank 33.7), p99 366.8 ms

### Tokens per question (c1 questions; measured)

| method | prefill | decode | total | x vanilla | LLM requests | retrievals | acc | halluc |
|---|---|---|---|---|---|---|---|---|
| vanilla | 73 | 4.8 | 78 | 1.00 | 1.00 | 0.00 | 0.540 | 0.460 |
| rag | 545 | 4.1 | 549 | 7.02 | 1.00 | 1.00 | 0.640 | 0.360 |
| replay:flare+abstain | 356 | 7.0 | 363 | 4.64 | 1.52 | 0.52 | 0.454 | 0.158 |
| replay:dragin+abstain | 372 | 7.2 | 379 | 4.84 | 1.55 | 0.55 | 0.469 | 0.126 |
| replay:probing-rag+abstain | 344 | 4.4 | 348 | 4.45 | 1.50 | 0.50 | 0.451 | 0.126 |
| replay:sep-rag+abstain | 408 | 4.3 | 413 | 5.27 | 1.62 | 0.62 | 0.421 | 0.106 |
| replay:se-rag+abstain | 433 | 61.8 | 495 | 6.32 | 2.53 | 0.53 | 0.468 | 0.122 |
| observe | 73 | 4.8 | 78 | 1.00 | 1.00 | 0.00 | 0.540 | 0.460 |
| retrieve+abstain | 418 | 4.1 | 423 | 5.40 | 1.00 | 0.73 | 0.560 | 0.080 |
| route-eu | 428 | 3.6 | 432 | 5.52 | 1.00 | 0.75 | 0.510 | 0.040 |
| route-eu-2r | 607 | 4.2 | 611 | 7.80 | 1.00 | 1.13 | 0.520 | 0.070 |
| live:flare+abstain | 357 | 7.2 | 364 | 4.65 | 1.52 | 0.52 | 0.500 | 0.110 |
| live:dragin+abstain | 366 | 7.2 | 373 | 4.76 | 1.54 | 0.54 | 0.500 | 0.090 |
| live:probing-rag+abstain | 344 | 4.4 | 348 | 4.45 | 1.50 | 0.50 | 0.500 | 0.150 |
| live:sep-rag+abstain | 408 | 4.3 | 412 | 5.27 | 1.62 | 0.62 | 0.440 | 0.100 |
| live:se-rag+abstain | 433 | 62.2 | 495 | 6.33 | 2.53 | 0.53 | 0.460 | 0.130 |

(acc / halluc: measured for real generations; simulated on the full test split for replays)

### Latency, one request at a time (c1)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 11 | 13 | 30 | 39 | 70 | - | - | 30 | 0.00 | 31.28 | 65% |
| rag | 317 | 374 | 332 | 366 | 395 | 332 | 395 | - | 1.00 | 2.95 | 9% |
| replay:flare+abstain | 336 | 414 | 336 | 389 | 414 | 355 | 421 | 25 | 0.52 | 4.95 | 23% |
| replay:dragin+abstain | 338 | 413 | 338 | 386 | 413 | 360 | 414 | 28 | 0.55 | 4.72 | 23% |
| replay:probing-rag+abstain | 179 | 397 | 179 | 354 | 397 | 338 | 401 | 23 | 0.50 | 5.42 | 24% |
| replay:sep-rag+abstain | 328 | 390 | 328 | 356 | 390 | 339 | 394 | 28 | 0.62 | 4.50 | 22% |
| replay:se-rag+abstain | 345 | 434 | 345 | 403 | 434 | 373 | 435 | 34 | 0.53 | 4.62 | 39% |
| observe | 27 | 53 | 27 | 36 | 70 | - | - | 27 | 0.00 | 34.67 | 0% |
| retrieve+abstain | 325 | 391 | 325 | 362 | 391 | 334 | 391 | 25 | 0.73 | 3.94 | 3% |
| route-eu | 324 | 415 | 324 | 358 | 415 | 331 | 417 | 19 | 0.75 | 3.87 | 5% |
| route-eu-2r | 358 | 711 | 358 | 660 | 711 | 389 | 712 | 19 | 0.77 | 2.61 | 3% |
| live:flare+abstain | 343 | 441 | 343 | 396 | 441 | 371 | 454 | 31 | 0.52 | 4.73 | 23% |
| live:dragin+abstain | 346 | 423 | 346 | 392 | 423 | 365 | 425 | 33 | 0.54 | 4.64 | 23% |
| live:probing-rag+abstain | 182 | 402 | 182 | 359 | 402 | 343 | 407 | 28 | 0.50 | 5.27 | 24% |
| live:sep-rag+abstain | 332 | 395 | 332 | 361 | 395 | 344 | 398 | 33 | 0.62 | 4.40 | 22% |
| live:se-rag+abstain | 353 | 527 | 353 | 445 | 527 | 400 | 528 | 35 | 0.53 | 4.19 | 39% |

### Latency, Poisson arrivals at 25% of the sustainable always-RAG throughput (25.8 q/s: GPU bench rate capped by the retrieval pool) (p25)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 7 | 16 | 28 | 44 | 109 | - | - | 28 | 0.00 | 6.07 | 65% |
| rag | 320 | 377 | 341 | 375 | 403 | 341 | 403 | - | 1.00 | 6.05 | 9% |
| replay:flare+abstain | 54 | 466 | 54 | 399 | 466 | 375 | 497 | 28 | 0.50 | 6.07 | 24% |
| replay:dragin+abstain | 340 | 457 | 340 | 400 | 457 | 375 | 482 | 28 | 0.53 | 6.07 | 23% |
| replay:probing-rag+abstain | 328 | 403 | 328 | 371 | 403 | 347 | 414 | 28 | 0.55 | 6.05 | 23% |
| replay:sep-rag+abstain | 333 | 401 | 333 | 370 | 401 | 348 | 404 | 28 | 0.61 | 6.05 | 22% |
| replay:se-rag+abstain | 354 | 481 | 354 | 418 | 481 | 388 | 501 | 36 | 0.53 | 6.06 | 39% |
| observe | 30 | 55 | 30 | 44 | 118 | - | - | 30 | 0.00 | 6.07 | 0% |
| retrieve+abstain | 336 | 411 | 336 | 375 | 412 | 344 | 414 | 29 | 0.75 | 6.05 | 3% |
| route-eu | 336 | 3204 | 336 | 385 | 3204 | 347 | 3236 | 21 | 0.73 | 6.04 | 4% |
| route-eu-2r | 361 | 733 | 362 | 678 | 733 | 386 | 734 | 22 | 0.76 | 6.03 | 3% |
| live:flare+abstain | 102 | 511 | 102 | 425 | 511 | 382 | 533 | 30 | 0.49 | 6.07 | 23% |
| live:dragin+abstain | 340 | 494 | 340 | 408 | 494 | 378 | 514 | 29 | 0.52 | 6.07 | 23% |
| live:probing-rag+abstain | 329 | 404 | 329 | 372 | 404 | 348 | 415 | 29 | 0.55 | 6.05 | 23% |
| live:sep-rag+abstain | 334 | 404 | 334 | 371 | 404 | 349 | 406 | 29 | 0.61 | 6.05 | 22% |
| live:se-rag+abstain | 363 | 558 | 363 | 492 | 558 | 417 | 570 | 41 | 0.53 | 6.06 | 39% |

### Latency, Poisson arrivals at 75% of the sustainable always-RAG throughput (25.8 q/s: GPU bench rate capped by the retrieval pool) (p75)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 8 | 17 | 30 | 45 | 109 | - | - | 30 | 0.00 | 19.57 | 65% |
| rag | 335 | 573 | 358 | 450 | 602 | 358 | 602 | - | 1.00 | 19.36 | 9% |
| replay:flare+abstain | 74 | 482 | 74 | 410 | 482 | 386 | 518 | 31 | 0.50 | 19.52 | 24% |
| replay:dragin+abstain | 347 | 483 | 347 | 413 | 483 | 383 | 509 | 32 | 0.53 | 19.45 | 23% |
| replay:probing-rag+abstain | 334 | 438 | 334 | 378 | 438 | 356 | 441 | 29 | 0.55 | 19.39 | 23% |
| replay:sep-rag+abstain | 339 | 424 | 339 | 383 | 424 | 357 | 451 | 30 | 0.61 | 19.39 | 22% |
| replay:se-rag+abstain | 362 | 501 | 362 | 436 | 501 | 401 | 523 | 40 | 0.53 | 19.47 | 39% |
| observe | 30 | 57 | 30 | 46 | 119 | - | - | 30 | 0.00 | 19.57 | 0% |
| retrieve+abstain | 342 | 497 | 342 | 393 | 497 | 353 | 512 | 34 | 0.75 | 19.37 | 3% |
| route-eu | 342 | 466 | 342 | 393 | 466 | 353 | 468 | 23 | 0.73 | 19.33 | 4% |
| route-eu-2r | 404 | 1023 | 404 | 784 | 1023 | 523 | 1058 | 26 | 0.76 | 19.14 | 3% |
| live:flare+abstain | 225 | 671 | 225 | 447 | 671 | 397 | 689 | 35 | 0.50 | 19.50 | 23% |
| live:dragin+abstain | 351 | 509 | 351 | 416 | 509 | 388 | 520 | 34 | 0.52 | 19.42 | 23% |
| live:probing-rag+abstain | 335 | 439 | 335 | 380 | 439 | 359 | 444 | 32 | 0.55 | 19.39 | 23% |
| live:sep-rag+abstain | 340 | 426 | 340 | 384 | 426 | 360 | 454 | 33 | 0.61 | 19.38 | 22% |
| live:se-rag+abstain | 377 | 598 | 377 | 523 | 598 | 432 | 611 | 45 | 0.53 | 19.41 | 39% |

(ms; TTFT = first answer token the client receives; E2E = arrival to last token or abstention; the prefix cache is emptied before every scenario (bench.latency_cold_cache), so hits are only shared prompt prefixes within a scenario)

### Baselines executed live (3000 bench questions, all arriving at once; thresholds chosen on val)

Each method runs as a controller on the real outputs: draft -> trigger -> its own query -> retrieval -> evidence answer -> abstain rule. `sim` = the policy stage's composition of measured parts on the full test split. Retrieval cache: 12112 hits, 89 queries searched live (drafts that differ from the generate stage's).

| lam | method | acc | halluc | coverage | retrieved | utility | sim acc | sim halluc | q/s |
|---|---|---|---|---|---|---|---|---|---|
| 1 | flare+abstain | 0.450 | 0.157 | 0.607 | 0.51 | 0.282 | 0.454 | 0.158 | 49.8 |
| 1 | dragin+abstain | 0.467 | 0.127 | 0.594 | 0.52 | 0.329 | 0.469 | 0.126 | 47.9 |
| 1 | probing-rag+abstain | 0.448 | 0.127 | 0.575 | 0.57 | 0.309 | 0.451 | 0.126 | 45.2 |
| 1 | sep-rag+abstain | 0.416 | 0.107 | 0.523 | 0.63 | 0.296 | 0.421 | 0.106 | 40.3 |
| 1 | se-rag+abstain | 0.466 | 0.122 | 0.588 | 0.54 | 0.333 | 0.468 | 0.122 | 46.7 |
| 2 | flare+abstain | 0.305 | 0.064 | 0.369 | 0.63 | 0.164 | 0.308 | 0.064 | 40.2 |
| 2 | dragin+abstain | 0.415 | 0.093 | 0.509 | 0.64 | 0.216 | 0.418 | 0.093 | 39.9 |
| 2 | probing-rag+abstain | 0.385 | 0.085 | 0.470 | 0.71 | 0.201 | 0.384 | 0.084 | 36.0 |
| 2 | sep-rag+abstain | 0.385 | 0.088 | 0.473 | 0.71 | 0.195 | 0.387 | 0.087 | 36.0 |
| 2 | se-rag+abstain | 0.430 | 0.095 | 0.525 | 0.62 | 0.227 | 0.433 | 0.095 | 40.6 |
| 4 | flare+abstain | 0.259 | 0.049 | 0.308 | 0.69 | 0.049 | 0.262 | 0.049 | 36.6 |
| 4 | dragin+abstain | 0.315 | 0.052 | 0.366 | 0.63 | 0.095 | 0.317 | 0.051 | 40.1 |
| 4 | probing-rag+abstain | 0.253 | 0.036 | 0.289 | 0.71 | 0.095 | 0.254 | 0.037 | 36.0 |
| 4 | sep-rag+abstain | 0.250 | 0.039 | 0.289 | 0.71 | 0.079 | 0.253 | 0.040 | 36.0 |
| 4 | se-rag+abstain | 0.307 | 0.044 | 0.351 | 0.65 | 0.120 | 0.311 | 0.044 | 39.0 |

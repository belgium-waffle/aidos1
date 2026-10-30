Retrieval service (live BM25 top-50 + BAAI/bge-reranker-v2-m3, one query at a time): p50 295.7 ms (BM25 258.3 + rerank 33.5), p99 365.1 ms

### Tokens per question (c1 questions; measured)

| method | prefill | decode | total | x vanilla | LLM requests | retrievals | acc | halluc |
|---|---|---|---|---|---|---|---|---|
| vanilla | 48 | 9.2 | 57 | 1.00 | 1.00 | 0.00 | 0.630 | 0.370 |
| rag | 603 | 9.3 | 612 | 10.73 | 1.00 | 1.00 | 0.650 | 0.350 |
| replay:flare+abstain | 325 | 14.7 | 340 | 5.96 | 1.46 | 0.46 | 0.365 | 0.148 |
| replay:dragin+abstain | 327 | 14.7 | 342 | 6.00 | 1.46 | 0.46 | 0.415 | 0.162 |
| replay:probing-rag+abstain | 329 | 8.8 | 338 | 5.93 | 1.46 | 0.46 | 0.447 | 0.158 |
| replay:sep-rag+abstain | 347 | 8.5 | 355 | 6.23 | 1.49 | 0.49 | 0.431 | 0.176 |
| replay:se-rag+abstain | 440 | 113.3 | 554 | 9.71 | 2.57 | 0.57 | 0.409 | 0.152 |
| observe | 48 | 9.2 | 57 | 1.00 | 1.00 | 0.00 | 0.630 | 0.370 |
| retrieve+abstain | 406 | 7.5 | 413 | 7.25 | 1.00 | 0.64 | 0.620 | 0.140 |
| route-eu | 474 | 6.9 | 481 | 8.43 | 1.00 | 0.76 | 0.570 | 0.100 |
| route-eu-2r | 619 | 7.2 | 627 | 10.99 | 1.00 | 1.02 | 0.570 | 0.110 |
| live:flare+abstain | 320 | 14.7 | 335 | 5.87 | 1.45 | 0.45 | 0.480 | 0.150 |
| live:dragin+abstain | 322 | 14.1 | 336 | 5.89 | 1.45 | 0.45 | 0.500 | 0.190 |
| live:probing-rag+abstain | 329 | 9.0 | 338 | 5.94 | 1.46 | 0.46 | 0.550 | 0.160 |
| live:sep-rag+abstain | 347 | 8.6 | 355 | 6.23 | 1.49 | 0.49 | 0.540 | 0.180 |
| live:se-rag+abstain | 440 | 114.9 | 555 | 9.74 | 2.57 | 0.57 | 0.520 | 0.170 |

(acc / halluc: measured for real generations; simulated on the full test split for replays)

### Latency, one request at a time (c1)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 11 | 12 | 43 | 96 | 175 | - | - | 43 | 0.00 | 18.44 | 51% |
| rag | 312 | 370 | 356 | 415 | 461 | 356 | 461 | - | 1.00 | 2.76 | 4% |
| replay:flare+abstain | 67 | 563 | 67 | 478 | 563 | 440 | 568 | 22 | 0.46 | 4.51 | 13% |
| replay:dragin+abstain | 67 | 576 | 67 | 478 | 576 | 445 | 576 | 22 | 0.46 | 4.51 | 13% |
| replay:probing-rag+abstain | 75 | 468 | 75 | 396 | 468 | 372 | 471 | 25 | 0.46 | 5.16 | 12% |
| replay:sep-rag+abstain | 75 | 466 | 75 | 402 | 466 | 373 | 470 | 22 | 0.49 | 4.98 | 12% |
| replay:se-rag+abstain | 397 | 583 | 397 | 497 | 583 | 446 | 583 | 39 | 0.57 | 3.62 | 22% |
| observe | 41 | 53 | 41 | 99 | 184 | - | - | 41 | 0.00 | 18.67 | 0% |
| retrieve+abstain | 323 | 412 | 323 | 398 | 453 | 352 | 457 | 24 | 0.64 | 4.12 | 1% |
| route-eu | 334 | 412 | 334 | 406 | 425 | 354 | 425 | 18 | 0.76 | 3.61 | 2% |
| route-eu-2r | 358 | 693 | 372 | 645 | 707 | 402 | 709 | 18 | 0.75 | 2.78 | 1% |
| live:flare+abstain | 69 | 611 | 69 | 505 | 611 | 441 | 1472 | 26 | 0.45 | 4.16 | 13% |
| live:dragin+abstain | 64 | 525 | 64 | 472 | 525 | 447 | 552 | 26 | 0.45 | 4.57 | 13% |
| live:probing-rag+abstain | 76 | 472 | 76 | 405 | 472 | 381 | 474 | 31 | 0.46 | 5.05 | 12% |
| live:sep-rag+abstain | 76 | 469 | 76 | 410 | 469 | 377 | 473 | 26 | 0.49 | 4.87 | 12% |
| live:se-rag+abstain | 423 | 598 | 423 | 552 | 598 | 504 | 620 | 33 | 0.57 | 3.25 | 22% |

### Latency, Poisson arrivals at 25% of the sustainable always-RAG throughput (26.5 q/s: GPU bench rate capped by the retrieval pool) (p25)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 7 | 16 | 49 | 96 | 170 | - | - | 49 | 0.00 | 6.22 | 58% |
| rag | 315 | 381 | 367 | 425 | 490 | 367 | 490 | - | 1.00 | 6.20 | 5% |
| replay:flare+abstain | 397 | 581 | 397 | 502 | 581 | 442 | 591 | 30 | 0.59 | 6.20 | 13% |
| replay:dragin+abstain | 391 | 582 | 391 | 500 | 582 | 443 | 592 | 31 | 0.59 | 6.21 | 13% |
| replay:probing-rag+abstain | 335 | 494 | 335 | 410 | 494 | 377 | 496 | 38 | 0.53 | 6.20 | 13% |
| replay:sep-rag+abstain | 336 | 476 | 336 | 415 | 476 | 377 | 485 | 34 | 0.54 | 6.20 | 13% |
| replay:se-rag+abstain | 416 | 605 | 416 | 521 | 605 | 463 | 611 | 45 | 0.62 | 6.20 | 21% |
| observe | 52 | 57 | 52 | 104 | 184 | - | - | 52 | 0.00 | 6.22 | 0% |
| retrieve+abstain | 332 | 424 | 334 | 413 | 494 | 355 | 502 | 31 | 0.73 | 6.20 | 2% |
| route-eu | 332 | 422 | 333 | 405 | 468 | 356 | 476 | 13 | 0.71 | 6.20 | 2% |
| route-eu-2r | 364 | 731 | 373 | 665 | 754 | 411 | 758 | 14 | 0.70 | 6.20 | 2% |
| live:flare+abstain | 400 | 672 | 400 | 534 | 672 | 449 | 712 | 33 | 0.59 | 6.20 | 13% |
| live:dragin+abstain | 399 | 609 | 399 | 509 | 609 | 445 | 617 | 30 | 0.59 | 6.21 | 13% |
| live:probing-rag+abstain | 335 | 489 | 335 | 411 | 489 | 378 | 498 | 38 | 0.53 | 6.20 | 13% |
| live:sep-rag+abstain | 337 | 481 | 337 | 414 | 481 | 378 | 486 | 35 | 0.54 | 6.20 | 13% |
| live:se-rag+abstain | 445 | 639 | 445 | 574 | 639 | 514 | 657 | 55 | 0.62 | 6.20 | 21% |

### Latency, Poisson arrivals at 75% of the sustainable always-RAG throughput (26.5 q/s: GPU bench rate capped by the retrieval pool) (p75)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 12 | 16 | 52 | 97 | 176 | - | - | 52 | 0.00 | 20.07 | 58% |
| rag | 331 | 567 | 392 | 500 | 677 | 392 | 677 | - | 1.00 | 19.84 | 5% |
| replay:flare+abstain | 410 | 620 | 410 | 527 | 620 | 466 | 625 | 38 | 0.59 | 19.82 | 13% |
| replay:dragin+abstain | 411 | 623 | 411 | 530 | 623 | 465 | 634 | 38 | 0.59 | 19.84 | 13% |
| replay:probing-rag+abstain | 347 | 511 | 347 | 428 | 511 | 389 | 518 | 47 | 0.53 | 19.86 | 13% |
| replay:sep-rag+abstain | 346 | 506 | 346 | 431 | 506 | 394 | 522 | 42 | 0.54 | 19.86 | 13% |
| replay:se-rag+abstain | 446 | 699 | 446 | 574 | 699 | 496 | 721 | 56 | 0.62 | 19.82 | 21% |
| observe | 52 | 58 | 53 | 104 | 187 | - | - | 53 | 0.00 | 20.07 | 0% |
| retrieve+abstain | 340 | 460 | 342 | 434 | 529 | 363 | 539 | 39 | 0.73 | 19.84 | 2% |
| route-eu | 339 | 444 | 339 | 422 | 481 | 364 | 484 | 18 | 0.71 | 19.85 | 2% |
| route-eu-2r | 385 | 826 | 399 | 704 | 841 | 446 | 848 | 20 | 0.71 | 19.72 | 2% |
| live:flare+abstain | 418 | 970 | 418 | 603 | 970 | 491 | 1076 | 46 | 0.58 | 19.80 | 13% |
| live:dragin+abstain | 419 | 722 | 419 | 558 | 722 | 479 | 763 | 40 | 0.58 | 19.83 | 13% |
| live:probing-rag+abstain | 346 | 506 | 346 | 429 | 506 | 391 | 508 | 47 | 0.53 | 19.86 | 13% |
| live:sep-rag+abstain | 346 | 507 | 346 | 433 | 507 | 394 | 523 | 42 | 0.54 | 19.86 | 13% |
| live:se-rag+abstain | 481 | 754 | 481 | 643 | 754 | 559 | 770 | 71 | 0.62 | 19.81 | 21% |

(ms; TTFT = first answer token the client receives; E2E = arrival to last token or abstention; the prefix cache is emptied before every scenario (bench.latency_cold_cache), so hits are only shared prompt prefixes within a scenario)

### Baselines executed live (2996 bench questions, all arriving at once; thresholds chosen on val)

Each method runs as a controller on the real outputs: draft -> trigger -> its own query -> retrieval -> evidence answer -> abstain rule. `sim` = the policy stage's composition of measured parts on the full test split. Retrieval cache: 14156 hits, 292 queries searched live (drafts that differ from the generate stage's).

| lam | method | acc | halluc | coverage | retrieved | utility | sim acc | sim halluc | q/s |
|---|---|---|---|---|---|---|---|---|---|
| 1 | flare+abstain | 0.363 | 0.150 | 0.513 | 0.63 | 0.201 | 0.365 | 0.148 | 41.2 |
| 1 | dragin+abstain | 0.412 | 0.167 | 0.578 | 0.61 | 0.233 | 0.415 | 0.162 | 42.8 |
| 1 | probing-rag+abstain | 0.447 | 0.162 | 0.609 | 0.56 | 0.274 | 0.447 | 0.158 | 46.6 |
| 1 | sep-rag+abstain | 0.432 | 0.176 | 0.607 | 0.57 | 0.244 | 0.431 | 0.176 | 46.6 |
| 1 | se-rag+abstain | 0.407 | 0.152 | 0.559 | 0.64 | 0.242 | 0.409 | 0.152 | 40.2 |
| 2 | flare+abstain | 0.241 | 0.062 | 0.303 | 0.70 | 0.104 | 0.245 | 0.061 | 37.6 |
| 2 | dragin+abstain | 0.251 | 0.060 | 0.311 | 0.69 | 0.116 | 0.251 | 0.060 | 38.1 |
| 2 | probing-rag+abstain | 0.265 | 0.044 | 0.309 | 0.69 | 0.162 | 0.267 | 0.044 | 38.0 |
| 2 | sep-rag+abstain | 0.257 | 0.051 | 0.308 | 0.69 | 0.141 | 0.258 | 0.051 | 38.1 |
| 2 | se-rag+abstain | 0.260 | 0.055 | 0.315 | 0.68 | 0.135 | 0.264 | 0.056 | 37.7 |
| 4 | flare+abstain | 0.000 | 0.000 | 0.000 | 1.00 | -0.020 | 0.000 | 0.000 | 26.4 |
| 4 | dragin+abstain | 0.251 | 0.059 | 0.309 | 0.69 | 0.002 | 0.251 | 0.060 | 38.0 |
| 4 | probing-rag+abstain | 0.265 | 0.044 | 0.309 | 0.69 | 0.073 | 0.267 | 0.044 | 37.9 |
| 4 | sep-rag+abstain | 0.257 | 0.051 | 0.308 | 0.69 | 0.039 | 0.258 | 0.051 | 38.1 |
| 4 | se-rag+abstain | 0.260 | 0.055 | 0.315 | 0.68 | 0.024 | 0.264 | 0.056 | 37.7 |

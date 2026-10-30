Retrieval service (live BM25 top-50 + BAAI/bge-reranker-v2-m3, one query at a time): p50 302.4 ms (BM25 263.2 + rerank 33.9), p99 375.3 ms

### Tokens per question (c1 questions; measured)

| method | prefill | decode | total | x vanilla | LLM requests | retrievals | acc | halluc |
|---|---|---|---|---|---|---|---|---|
| vanilla | 52 | 4.2 | 56 | 1.00 | 1.00 | 0.00 | 0.550 | 0.450 |
| rag | 541 | 4.2 | 545 | 9.68 | 1.00 | 1.00 | 0.760 | 0.240 |
| replay:flare+abstain | 367 | 6.8 | 374 | 6.63 | 1.58 | 0.58 | 0.452 | 0.106 |
| replay:dragin+abstain | 323 | 6.4 | 329 | 5.84 | 1.50 | 0.50 | 0.495 | 0.126 |
| replay:probing-rag+abstain | 372 | 4.1 | 376 | 6.67 | 1.59 | 0.59 | 0.514 | 0.123 |
| replay:sep-rag+abstain | 341 | 4.1 | 345 | 6.12 | 1.53 | 0.53 | 0.535 | 0.164 |
| replay:se-rag+abstain | 352 | 50.4 | 402 | 7.14 | 2.46 | 0.46 | 0.544 | 0.150 |
| observe | 52 | 4.2 | 56 | 1.00 | 1.00 | 0.00 | 0.550 | 0.450 |
| retrieve+abstain | 371 | 4.7 | 375 | 6.66 | 1.00 | 0.65 | 0.710 | 0.070 |
| route-eu | 422 | 4.4 | 427 | 7.57 | 1.00 | 0.75 | 0.700 | 0.060 |
| route-eu-2r | 504 | 4.7 | 509 | 9.03 | 1.00 | 0.92 | 0.710 | 0.060 |
| live:flare+abstain | 363 | 6.9 | 370 | 6.56 | 1.57 | 0.57 | 0.580 | 0.110 |
| live:dragin+abstain | 324 | 6.6 | 330 | 5.86 | 1.50 | 0.50 | 0.660 | 0.090 |
| live:probing-rag+abstain | 372 | 4.2 | 376 | 6.67 | 1.59 | 0.59 | 0.620 | 0.090 |
| live:sep-rag+abstain | 341 | 4.3 | 345 | 6.12 | 1.53 | 0.53 | 0.660 | 0.100 |
| live:se-rag+abstain | 352 | 49.9 | 402 | 7.13 | 2.46 | 0.46 | 0.690 | 0.100 |

(acc / halluc: measured for real generations; simulated on the full test split for replays)

### Latency, one request at a time (c1)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 40 | 41 | 97 | 136 | 193 | - | - | 97 | 0.00 | 9.85 | 61% |
| rag | 365 | 427 | 427 | 483 | 517 | 427 | 517 | - | 1.00 | 2.32 | 6% |
| replay:flare+abstain | 458 | 620 | 458 | 579 | 620 | 521 | 628 | 78 | 0.58 | 2.99 | 15% |
| replay:dragin+abstain | 291 | 642 | 291 | 563 | 642 | 511 | 646 | 78 | 0.50 | 3.34 | 16% |
| replay:probing-rag+abstain | 420 | 528 | 420 | 477 | 528 | 450 | 531 | 78 | 0.59 | 3.36 | 15% |
| replay:sep-rag+abstain | 408 | 536 | 408 | 480 | 536 | 451 | 540 | 78 | 0.53 | 3.63 | 16% |
| replay:se-rag+abstain | 143 | 669 | 143 | 600 | 669 | 557 | 681 | 100 | 0.46 | 3.22 | 29% |
| observe | 80 | 177 | 80 | 119 | 178 | - | - | 80 | 0.00 | 11.83 | 0% |
| retrieve+abstain | 408 | 538 | 408 | 500 | 538 | 448 | 559 | 80 | 0.65 | 3.13 | 1% |
| route-eu | 427 | 566 | 427 | 490 | 566 | 448 | 584 | 61 | 0.75 | 2.86 | 2% |
| route-eu-2r | 451 | 833 | 451 | 744 | 833 | 473 | 876 | 60 | 0.76 | 2.42 | 1% |
| live:flare+abstain | 470 | 680 | 470 | 605 | 680 | 535 | 685 | 96 | 0.57 | 2.83 | 15% |
| live:dragin+abstain | 311 | 756 | 311 | 574 | 756 | 532 | 794 | 96 | 0.50 | 3.10 | 16% |
| live:probing-rag+abstain | 441 | 561 | 441 | 497 | 561 | 470 | 643 | 97 | 0.59 | 3.13 | 15% |
| live:sep-rag+abstain | 427 | 566 | 427 | 507 | 566 | 471 | 636 | 96 | 0.53 | 3.36 | 16% |
| live:se-rag+abstain | 152 | 1067 | 152 | 634 | 1067 | 588 | 1069 | 100 | 0.46 | 2.92 | 29% |

### Latency, Poisson arrivals at 25% of the sustainable always-RAG throughput (18.1 q/s: GPU bench rate capped by the retrieval pool) (p25)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 23 | 58 | 81 | 137 | 201 | - | - | 81 | 0.00 | 4.25 | 62% |
| rag | 381 | 544 | 457 | 567 | 699 | 457 | 699 | - | 1.00 | 4.24 | 6% |
| replay:flare+abstain | 518 | 881 | 518 | 687 | 881 | 564 | 895 | 93 | 0.68 | 4.24 | 15% |
| replay:dragin+abstain | 494 | 859 | 494 | 659 | 859 | 563 | 979 | 92 | 0.59 | 4.24 | 16% |
| replay:probing-rag+abstain | 440 | 672 | 440 | 550 | 672 | 483 | 694 | 94 | 0.61 | 4.24 | 16% |
| replay:sep-rag+abstain | 427 | 675 | 427 | 554 | 675 | 486 | 689 | 81 | 0.55 | 4.24 | 16% |
| replay:se-rag+abstain | 488 | 893 | 488 | 697 | 893 | 599 | 1022 | 105 | 0.53 | 4.24 | 27% |
| observe | 80 | 179 | 80 | 136 | 199 | - | - | 80 | 0.00 | 4.25 | 0% |
| retrieve+abstain | 415 | 641 | 415 | 559 | 648 | 466 | 659 | 81 | 0.68 | 4.24 | 2% |
| route-eu | 424 | 660 | 424 | 552 | 660 | 455 | 689 | 61 | 0.70 | 4.24 | 2% |
| route-eu-2r | 478 | 969 | 478 | 799 | 980 | 532 | 1000 | 62 | 0.71 | 4.24 | 2% |
| live:flare+abstain | 528 | 1022 | 528 | 705 | 1022 | 581 | 1066 | 102 | 0.68 | 4.24 | 15% |
| live:dragin+abstain | 499 | 922 | 499 | 676 | 922 | 570 | 1095 | 98 | 0.60 | 4.24 | 16% |
| live:probing-rag+abstain | 445 | 677 | 445 | 560 | 677 | 489 | 719 | 95 | 0.61 | 4.24 | 16% |
| live:sep-rag+abstain | 432 | 687 | 432 | 559 | 687 | 492 | 710 | 85 | 0.55 | 4.24 | 16% |
| live:se-rag+abstain | 512 | 1334 | 512 | 836 | 1334 | 662 | 1388 | 114 | 0.53 | 4.24 | 27% |

### Latency, Poisson arrivals at 75% of the sustainable always-RAG throughput (18.1 q/s: GPU bench rate capped by the retrieval pool) (p75)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 47 | 59 | 98 | 149 | 225 | - | - | 98 | 0.00 | 13.70 | 62% |
| rag | 512 | 1320 | 708 | 1203 | 2135 | 708 | 2135 | - | 1.00 | 13.53 | 6% |
| replay:flare+abstain | 687 | 1400 | 687 | 1066 | 1400 | 800 | 1596 | 169 | 0.68 | 13.50 | 15% |
| replay:dragin+abstain | 616 | 1299 | 616 | 906 | 1299 | 753 | 1411 | 157 | 0.59 | 13.51 | 16% |
| replay:probing-rag+abstain | 534 | 975 | 534 | 749 | 975 | 619 | 1034 | 156 | 0.61 | 13.54 | 16% |
| replay:sep-rag+abstain | 490 | 982 | 490 | 722 | 982 | 605 | 1007 | 144 | 0.55 | 13.54 | 16% |
| replay:se-rag+abstain | 665 | 1726 | 665 | 1180 | 1726 | 916 | 1835 | 201 | 0.53 | 13.48 | 27% |
| observe | 83 | 195 | 83 | 139 | 219 | - | - | 83 | 0.00 | 13.71 | 0% |
| retrieve+abstain | 503 | 1128 | 503 | 824 | 1136 | 602 | 1171 | 144 | 0.68 | 13.57 | 2% |
| route-eu | 524 | 1085 | 524 | 819 | 1085 | 592 | 1103 | 118 | 0.71 | 13.58 | 2% |
| route-eu-2r | 741 | 1691 | 741 | 1209 | 1700 | 864 | 1731 | 173 | 0.71 | 13.50 | 2% |
| live:flare+abstain | 728 | 1667 | 728 | 1108 | 1667 | 844 | 1782 | 194 | 0.68 | 13.53 | 15% |
| live:dragin+abstain | 630 | 1500 | 630 | 995 | 1500 | 794 | 1708 | 158 | 0.60 | 13.48 | 16% |
| live:probing-rag+abstain | 536 | 959 | 536 | 770 | 959 | 628 | 1022 | 158 | 0.61 | 13.54 | 16% |
| live:sep-rag+abstain | 503 | 900 | 503 | 735 | 900 | 615 | 916 | 148 | 0.55 | 13.53 | 16% |
| live:se-rag+abstain | 694 | 2247 | 694 | 1360 | 2247 | 1006 | 2297 | 198 | 0.53 | 13.36 | 27% |

(ms; TTFT = first answer token the client receives; E2E = arrival to last token or abstention; the prefix cache is emptied before every scenario (bench.latency_cold_cache), so hits are only shared prompt prefixes within a scenario)

### Baselines executed live (2997 bench questions, all arriving at once; thresholds chosen on val)

Each method runs as a controller on the real outputs: draft -> trigger -> its own query -> retrieval -> evidence answer -> abstain rule. `sim` = the policy stage's composition of measured parts on the full test split. Retrieval cache: 13840 hits, 46 queries searched live (drafts that differ from the generate stage's).

| lam | method | acc | halluc | coverage | retrieved | utility | sim acc | sim halluc | q/s |
|---|---|---|---|---|---|---|---|---|---|
| 1 | flare+abstain | 0.448 | 0.105 | 0.553 | 0.69 | 0.329 | 0.452 | 0.106 | 24.2 |
| 1 | dragin+abstain | 0.492 | 0.126 | 0.618 | 0.62 | 0.354 | 0.495 | 0.126 | 27.0 |
| 1 | probing-rag+abstain | 0.511 | 0.121 | 0.632 | 0.63 | 0.377 | 0.514 | 0.123 | 27.0 |
| 1 | sep-rag+abstain | 0.533 | 0.162 | 0.695 | 0.56 | 0.360 | 0.535 | 0.164 | 30.2 |
| 1 | se-rag+abstain | 0.540 | 0.150 | 0.690 | 0.54 | 0.379 | 0.544 | 0.150 | 20.1 |
| 2 | flare+abstain | 0.448 | 0.105 | 0.553 | 0.69 | 0.224 | 0.452 | 0.106 | 24.1 |
| 2 | dragin+abstain | 0.467 | 0.108 | 0.576 | 0.69 | 0.237 | 0.470 | 0.109 | 24.3 |
| 2 | probing-rag+abstain | 0.491 | 0.105 | 0.597 | 0.69 | 0.266 | 0.494 | 0.108 | 24.6 |
| 2 | sep-rag+abstain | 0.493 | 0.127 | 0.620 | 0.70 | 0.225 | 0.496 | 0.129 | 24.4 |
| 2 | se-rag+abstain | 0.540 | 0.150 | 0.690 | 0.54 | 0.229 | 0.544 | 0.150 | 20.1 |
| 4 | flare+abstain | 0.274 | 0.033 | 0.307 | 0.69 | 0.130 | 0.276 | 0.032 | 24.2 |
| 4 | dragin+abstain | 0.282 | 0.033 | 0.315 | 0.69 | 0.134 | 0.283 | 0.033 | 24.3 |
| 4 | probing-rag+abstain | 0.289 | 0.027 | 0.316 | 0.69 | 0.167 | 0.289 | 0.027 | 24.6 |
| 4 | sep-rag+abstain | 0.260 | 0.048 | 0.308 | 0.70 | 0.052 | 0.261 | 0.049 | 24.3 |
| 4 | se-rag+abstain | 0.389 | 0.077 | 0.465 | 0.54 | 0.071 | 0.390 | 0.076 | 20.0 |

Retrieval service (live BM25 top-50 + BAAI/bge-reranker-v2-m3, one query at a time): p50 288.3 ms (BM25 252.1 + rerank 33.4), p99 357.2 ms

### Tokens per question (c1 questions; measured)

| method | prefill | decode | total | x vanilla | LLM requests | retrievals | acc | halluc |
|---|---|---|---|---|---|---|---|---|
| vanilla | 74 | 4.0 | 78 | 1.00 | 1.00 | 0.00 | 0.630 | 0.370 |
| rag | 548 | 4.1 | 552 | 7.06 | 1.00 | 1.00 | 0.700 | 0.300 |
| replay:flare+abstain | 271 | 5.5 | 277 | 3.54 | 1.36 | 0.36 | 0.592 | 0.168 |
| replay:dragin+abstain | 342 | 6.0 | 348 | 4.45 | 1.49 | 0.49 | 0.628 | 0.163 |
| replay:probing-rag+abstain | 249 | 4.1 | 253 | 3.24 | 1.32 | 0.32 | 0.625 | 0.144 |
| replay:sep-rag+abstain | 313 | 4.0 | 317 | 4.05 | 1.44 | 0.44 | 0.616 | 0.156 |
| replay:se-rag+abstain | 351 | 46.5 | 398 | 5.08 | 2.37 | 0.37 | 0.630 | 0.150 |
| observe | 74 | 4.0 | 78 | 1.00 | 1.00 | 0.00 | 0.630 | 0.370 |
| retrieve+abstain | 455 | 4.3 | 459 | 5.87 | 1.00 | 0.80 | 0.610 | 0.110 |
| route-eu | 422 | 4.2 | 426 | 5.45 | 1.00 | 0.73 | 0.590 | 0.100 |
| route-eu-2r | 535 | 4.6 | 540 | 6.90 | 1.00 | 0.97 | 0.600 | 0.110 |
| live:flare+abstain | 288 | 5.7 | 293 | 3.75 | 1.39 | 0.39 | 0.530 | 0.160 |
| live:dragin+abstain | 348 | 6.0 | 354 | 4.52 | 1.50 | 0.50 | 0.580 | 0.150 |
| live:probing-rag+abstain | 249 | 4.1 | 253 | 3.24 | 1.32 | 0.32 | 0.610 | 0.180 |
| live:sep-rag+abstain | 313 | 4.1 | 317 | 4.05 | 1.44 | 0.44 | 0.550 | 0.150 |
| live:se-rag+abstain | 351 | 47.0 | 398 | 5.09 | 2.37 | 0.37 | 0.600 | 0.170 |

(acc / halluc: measured for real generations; simulated on the full test split for replays)

### Latency, one request at a time (c1)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 48 | 51 | 114 | 158 | 183 | - | - | 114 | 0.00 | 8.72 | 64% |
| rag | 393 | 448 | 456 | 510 | 575 | 456 | 575 | - | 1.00 | 2.16 | 9% |
| replay:flare+abstain | 115 | 639 | 115 | 557 | 639 | 531 | 698 | 92 | 0.36 | 3.90 | 26% |
| replay:dragin+abstain | 171 | 647 | 171 | 575 | 647 | 540 | 675 | 92 | 0.49 | 3.17 | 23% |
| replay:probing-rag+abstain | 114 | 542 | 114 | 488 | 542 | 483 | 591 | 92 | 0.32 | 4.56 | 27% |
| replay:sep-rag+abstain | 137 | 551 | 137 | 493 | 551 | 468 | 574 | 92 | 0.44 | 3.78 | 25% |
| replay:se-rag+abstain | 180 | 727 | 180 | 625 | 727 | 596 | 750 | 150 | 0.37 | 3.11 | 45% |
| observe | 94 | 166 | 94 | 140 | 166 | - | - | 94 | 0.00 | 10.43 | 0% |
| retrieve+abstain | 448 | 639 | 448 | 532 | 662 | 455 | 674 | 74 | 0.80 | 2.52 | 3% |
| route-eu | 446 | 637 | 446 | 531 | 650 | 476 | 653 | 72 | 0.73 | 2.72 | 3% |
| route-eu-2r | 490 | 926 | 490 | 830 | 926 | 526 | 933 | 72 | 0.74 | 2.15 | 2% |
| live:flare+abstain | 138 | 869 | 138 | 608 | 869 | 570 | 8079 | 114 | 0.39 | 2.41 | 25% |
| live:dragin+abstain | 351 | 664 | 351 | 608 | 664 | 552 | 670 | 115 | 0.50 | 2.92 | 23% |
| live:probing-rag+abstain | 136 | 564 | 136 | 511 | 564 | 505 | 614 | 115 | 0.32 | 4.14 | 27% |
| live:sep-rag+abstain | 160 | 574 | 160 | 516 | 574 | 491 | 597 | 115 | 0.44 | 3.49 | 25% |
| live:se-rag+abstain | 168 | 756 | 168 | 622 | 756 | 604 | 791 | 131 | 0.37 | 3.16 | 45% |

### Latency, Poisson arrivals at 25% of the sustainable always-RAG throughput (11.2 q/s: GPU bench rate capped by the retrieval pool) (p25)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 27 | 71 | 99 | 158 | 202 | - | - | 99 | 0.00 | 2.63 | 65% |
| rag | 407 | 613 | 505 | 645 | 783 | 505 | 783 | - | 1.00 | 2.63 | 9% |
| replay:flare+abstain | 131 | 842 | 131 | 634 | 842 | 600 | 905 | 102 | 0.31 | 2.63 | 28% |
| replay:dragin+abstain | 175 | 817 | 175 | 664 | 817 | 599 | 901 | 107 | 0.43 | 2.63 | 25% |
| replay:probing-rag+abstain | 127 | 681 | 127 | 563 | 681 | 523 | 734 | 96 | 0.32 | 2.63 | 28% |
| replay:sep-rag+abstain | 177 | 680 | 177 | 577 | 680 | 519 | 722 | 114 | 0.42 | 2.63 | 25% |
| replay:se-rag+abstain | 195 | 922 | 195 | 726 | 922 | 670 | 968 | 155 | 0.36 | 2.63 | 46% |
| observe | 96 | 202 | 96 | 145 | 202 | - | - | 96 | 0.00 | 2.63 | 0% |
| retrieve+abstain | 480 | 771 | 480 | 632 | 796 | 509 | 808 | 98 | 0.79 | 2.63 | 3% |
| route-eu | 477 | 795 | 477 | 614 | 815 | 505 | 842 | 95 | 0.75 | 2.63 | 3% |
| route-eu-2r | 530 | 1182 | 530 | 902 | 1189 | 593 | 1227 | 87 | 0.76 | 2.63 | 2% |
| live:flare+abstain | 137 | 870 | 137 | 652 | 870 | 613 | 938 | 113 | 0.32 | 2.63 | 28% |
| live:dragin+abstain | 173 | 813 | 173 | 678 | 813 | 607 | 882 | 115 | 0.43 | 2.63 | 25% |
| live:probing-rag+abstain | 136 | 728 | 136 | 576 | 728 | 527 | 1076 | 106 | 0.32 | 2.63 | 28% |
| live:sep-rag+abstain | 181 | 693 | 181 | 576 | 693 | 527 | 722 | 115 | 0.42 | 2.63 | 25% |
| live:se-rag+abstain | 202 | 1008 | 202 | 773 | 1008 | 703 | 1334 | 160 | 0.36 | 2.63 | 45% |

### Latency, Poisson arrivals at 75% of the sustainable always-RAG throughput (11.2 q/s: GPU bench rate capped by the retrieval pool) (p75)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s | prefill from prefix cache |
|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 53 | 74 | 118 | 165 | 234 | - | - | 118 | 0.00 | 8.49 | 65% |
| rag | 586 | 1379 | 850 | 1506 | 2887 | 850 | 2887 | - | 1.00 | 8.42 | 9% |
| replay:flare+abstain | 191 | 1017 | 191 | 778 | 1017 | 711 | 1218 | 144 | 0.31 | 8.46 | 28% |
| replay:dragin+abstain | 300 | 1163 | 300 | 873 | 1163 | 740 | 1297 | 164 | 0.43 | 8.43 | 25% |
| replay:probing-rag+abstain | 186 | 891 | 186 | 654 | 891 | 591 | 919 | 138 | 0.32 | 8.49 | 28% |
| replay:sep-rag+abstain | 272 | 1019 | 272 | 722 | 1019 | 637 | 1206 | 151 | 0.42 | 8.42 | 25% |
| replay:se-rag+abstain | 320 | 1472 | 320 | 981 | 1472 | 850 | 1544 | 208 | 0.36 | 8.45 | 46% |
| observe | 106 | 416 | 106 | 153 | 416 | - | - | 106 | 0.00 | 8.49 | 0% |
| retrieve+abstain | 718 | 1442 | 718 | 1130 | 1557 | 787 | 1585 | 174 | 0.79 | 8.41 | 3% |
| route-eu | 666 | 1551 | 666 | 1058 | 1551 | 748 | 1585 | 171 | 0.75 | 8.41 | 3% |
| route-eu-2r | 982 | 2755 | 982 | 1816 | 2808 | 1109 | 2828 | 265 | 0.76 | 8.38 | 2% |
| live:flare+abstain | 200 | 1038 | 200 | 799 | 1038 | 729 | 1285 | 148 | 0.32 | 8.46 | 28% |
| live:dragin+abstain | 305 | 1148 | 305 | 867 | 1148 | 762 | 1294 | 170 | 0.43 | 8.43 | 25% |
| live:probing-rag+abstain | 189 | 896 | 189 | 662 | 896 | 596 | 935 | 144 | 0.32 | 8.49 | 28% |
| live:sep-rag+abstain | 275 | 953 | 275 | 738 | 953 | 651 | 1161 | 158 | 0.42 | 8.42 | 25% |
| live:se-rag+abstain | 344 | 1674 | 344 | 1087 | 1674 | 927 | 1962 | 226 | 0.36 | 8.44 | 45% |

(ms; TTFT = first answer token the client receives; E2E = arrival to last token or abstention; the prefix cache is emptied before every scenario (bench.latency_cold_cache), so hits are only shared prompt prefixes within a scenario)

### Baselines executed live (2999 bench questions, all arriving at once; thresholds chosen on val)

Each method runs as a controller on the real outputs: draft -> trigger -> its own query -> retrieval -> evidence answer -> abstain rule. `sim` = the policy stage's composition of measured parts on the full test split. Retrieval cache: 9523 hits, 175 queries searched live (drafts that differ from the generate stage's).

| lam | method | acc | halluc | coverage | retrieved | utility | sim acc | sim halluc | q/s |
|---|---|---|---|---|---|---|---|---|---|
| 1 | flare+abstain | 0.593 | 0.165 | 0.758 | 0.31 | 0.421 | 0.592 | 0.168 | 30.0 |
| 1 | dragin+abstain | 0.623 | 0.165 | 0.788 | 0.44 | 0.449 | 0.628 | 0.163 | 22.7 |
| 1 | probing-rag+abstain | 0.622 | 0.146 | 0.768 | 0.33 | 0.470 | 0.625 | 0.144 | 30.2 |
| 1 | sep-rag+abstain | 0.614 | 0.156 | 0.771 | 0.43 | 0.449 | 0.616 | 0.156 | 23.6 |
| 1 | se-rag+abstain | 0.625 | 0.151 | 0.776 | 0.37 | 0.467 | 0.630 | 0.150 | 16.9 |
| 2 | flare+abstain | 0.477 | 0.077 | 0.554 | 0.45 | 0.314 | 0.482 | 0.076 | 22.3 |
| 2 | dragin+abstain | 0.548 | 0.120 | 0.668 | 0.57 | 0.296 | 0.552 | 0.117 | 17.9 |
| 2 | probing-rag+abstain | 0.513 | 0.065 | 0.579 | 0.45 | 0.374 | 0.517 | 0.064 | 22.7 |
| 2 | sep-rag+abstain | 0.517 | 0.095 | 0.612 | 0.68 | 0.312 | 0.518 | 0.094 | 15.3 |
| 2 | se-rag+abstain | 0.591 | 0.118 | 0.709 | 0.37 | 0.346 | 0.595 | 0.116 | 17.0 |
| 4 | flare+abstain | 0.382 | 0.047 | 0.429 | 0.57 | 0.184 | 0.384 | 0.045 | 17.7 |
| 4 | dragin+abstain | 0.405 | 0.050 | 0.455 | 0.57 | 0.194 | 0.408 | 0.048 | 18.1 |
| 4 | probing-rag+abstain | 0.375 | 0.028 | 0.403 | 0.63 | 0.249 | 0.379 | 0.028 | 16.5 |
| 4 | sep-rag+abstain | 0.430 | 0.058 | 0.488 | 1.00 | 0.176 | 0.431 | 0.058 | 10.7 |
| 4 | se-rag+abstain | 0.430 | 0.058 | 0.488 | 1.00 | 0.176 | 0.431 | 0.058 | 8.6 |

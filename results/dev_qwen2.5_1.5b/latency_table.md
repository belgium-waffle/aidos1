Retrieval service (live BM25 top-50 + BAAI/bge-reranker-v2-m3, one query at a time): p50 299.6 ms (BM25 261.0 + rerank 33.3), p99 355.0 ms

### Tokens per question (c1 questions; measured)

| method | prefill | decode | total | x vanilla | LLM requests | retrievals | acc | halluc |
|---|---|---|---|---|---|---|---|---|
| vanilla | 52 | 4.1 | 56 | 1.00 | 1.00 | 0.00 | 0.240 | 0.760 |
| rag | 549 | 4.7 | 553 | 9.81 | 1.00 | 1.00 | 0.510 | 0.490 |
| replay:flare+abstain | 601 | 8.8 | 610 | 10.81 | 2.00 | 1.00 | 0.193 | 0.112 |
| replay:dragin+abstain | 601 | 8.8 | 610 | 10.81 | 2.00 | 1.00 | 0.303 | 0.162 |
| replay:probing-rag+abstain | 601 | 4.7 | 605 | 10.74 | 2.00 | 1.00 | 0.241 | 0.116 |
| replay:sep-rag+abstain | 601 | 4.7 | 605 | 10.74 | 2.00 | 1.00 | 0.241 | 0.116 |
| replay:se-rag+abstain | 653 | 52.0 | 705 | 12.51 | 3.00 | 1.00 | 0.241 | 0.116 |
| observe | 52 | 4.1 | 56 | 1.00 | 1.00 | 0.00 | 0.240 | 0.760 |
| retrieve+abstain | 549 | 4.4 | 553 | 9.81 | 1.00 | 1.00 | 0.420 | 0.250 |
| route-eu | 375 | 3.4 | 379 | 6.72 | 1.00 | 0.64 | 0.360 | 0.130 |
| route-eu-2r | 479 | 3.6 | 483 | 8.56 | 1.00 | 0.85 | 0.360 | 0.130 |

(acc / halluc: measured for real generations; simulated on the full test split for replays)

### Latency, one request at a time (c1)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s |
|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 5 | 5 | 11 | 16 | 31 | - | - | 11 | 0.00 | 84.76 |
| rag | 307 | 362 | 315 | 345 | 370 | 315 | 370 | - | 1.00 | 3.14 |
| replay:flare+abstain | 325 | 375 | 325 | 353 | 375 | 325 | 375 | - | 1.00 | 3.06 |
| replay:dragin+abstain | 326 | 375 | 326 | 353 | 375 | 326 | 375 | - | 1.00 | 3.06 |
| replay:probing-rag+abstain | 315 | 371 | 315 | 346 | 371 | 315 | 371 | - | 1.00 | 3.13 |
| replay:sep-rag+abstain | 315 | 371 | 315 | 346 | 371 | 315 | 371 | - | 1.00 | 3.13 |
| replay:se-rag+abstain | 330 | 379 | 330 | 357 | 379 | 330 | 379 | - | 1.00 | 3.02 |
| observe | 11 | 24 | 11 | 16 | 34 | - | - | 11 | 0.00 | 87.41 |
| retrieve+abstain | 317 | 376 | 317 | 344 | 376 | 317 | 376 | - | 1.00 | 3.12 |
| route-eu | 305 | 379 | 305 | 339 | 379 | 316 | 384 | 4 | 0.64 | 4.82 |
| route-eu-2r | 311 | 662 | 311 | 631 | 662 | 342 | 666 | 4 | 0.62 | 3.65 |

### Latency, Poisson arrivals at 25% of always-RAG throughput (p25)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s |
|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 7 | 11 | 12 | 19 | 30 | - | - | 12 | 0.00 | 80.52 |
| rag | 6500 | 12889 | 6509 | 11629 | 12893 | 6509 | 12893 | - | 1.00 | 26.04 |
| replay:flare+abstain | 6521 | 12898 | 6521 | 11638 | 12898 | 6521 | 12898 | - | 1.00 | 26.03 |
| replay:dragin+abstain | 6521 | 12898 | 6521 | 11638 | 12898 | 6521 | 12898 | - | 1.00 | 26.03 |
| replay:probing-rag+abstain | 6511 | 12890 | 6511 | 11630 | 12890 | 6511 | 12890 | - | 1.00 | 26.04 |
| replay:sep-rag+abstain | 6511 | 12890 | 6511 | 11630 | 12890 | 6511 | 12890 | - | 1.00 | 26.04 |
| replay:se-rag+abstain | 6527 | 12906 | 6527 | 11646 | 12906 | 6527 | 12906 | - | 1.00 | 26.02 |
| observe | 13 | 28 | 13 | 20 | 35 | - | - | 13 | 0.00 | 80.52 |
| retrieve+abstain | 6826 | 13111 | 6826 | 11983 | 13111 | 6826 | 13111 | - | 1.00 | 25.62 |
| route-eu | 2015 | 6793 | 2015 | 5769 | 6793 | 3535 | 6820 | 55 | 0.66 | 38.33 |
| route-eu-2r | 2444 | 11543 | 2444 | 10587 | 11543 | 5607 | 11658 | 55 | 0.62 | 30.09 |

### Latency, Poisson arrivals at 75% of always-RAG throughput (p75)

| method | TTFT p50 | TTFT p99 | E2E p50 | E2E p90 | E2E p99 | E2E p50 retrieved | E2E p99 retrieved | E2E p50 not retrieved | retrieved | achieved q/s |
|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 8 | 10 | 13 | 20 | 32 | - | - | 13 | 0.00 | 277.77 |
| rag | 8778 | 17265 | 8787 | 15596 | 17267 | 8787 | 17267 | - | 1.00 | 26.07 |
| replay:flare+abstain | 8802 | 17279 | 8802 | 15607 | 17279 | 8802 | 17279 | - | 1.00 | 26.05 |
| replay:dragin+abstain | 8802 | 17278 | 8802 | 15607 | 17278 | 8802 | 17278 | - | 1.00 | 26.05 |
| replay:probing-rag+abstain | 8793 | 17270 | 8793 | 15603 | 17270 | 8793 | 17270 | - | 1.00 | 26.06 |
| replay:sep-rag+abstain | 8793 | 17271 | 8793 | 15603 | 17271 | 8793 | 17271 | - | 1.00 | 26.07 |
| replay:se-rag+abstain | 8815 | 17310 | 8815 | 15626 | 17310 | 8815 | 17310 | - | 1.00 | 26.03 |
| observe | 15 | 30 | 15 | 22 | 42 | - | - | 15 | 0.00 | 277.64 |
| retrieve+abstain | 9084 | 17416 | 9084 | 15860 | 17416 | 9084 | 17416 | - | 1.00 | 25.71 |
| route-eu | 3163 | 11076 | 3163 | 9569 | 11076 | 5828 | 11158 | 119 | 0.66 | 38.36 |
| route-eu-2r | 3539 | 14739 | 3543 | 13822 | 14739 | 8467 | 14856 | 112 | 0.62 | 30.11 |

(ms; TTFT = first answer token the client receives; E2E = arrival to last token or abstention)

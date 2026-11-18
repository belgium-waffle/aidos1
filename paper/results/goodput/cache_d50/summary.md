| retriever | delay ms | condition | load | req/s | out tok/s | accuracy | abstain | hallucination | goodput (correct/s) | safe goodput |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval.jsonl | 50 | vanilla | 32 | 326.1 | 1334 | 0.481 | 0.000 | 0.519 | 156.9 | 156.9 |
| retrieval.jsonl | 50 | always_rag | 32 | 50.6 | 223 | 0.670 | 0.000 | 0.330 | 33.9 | 33.9 |
| retrieval.jsonl | 50 | aidos_observe | 32 | 425.6 | 1740 | 0.482 | 0.000 | 0.518 | 205.1 | 205.1 |
| retrieval.jsonl | 50 | aidos | 32 | 92.7 | 285 | 0.591 | 0.329 | 0.081 | 54.7 | 85.2 |
| retrieval.jsonl | 50 | vanilla | 128 | 903.4 | 3704 | 0.479 | 0.000 | 0.521 | 432.7 | 432.7 |
| retrieval.jsonl | 50 | always_rag | 128 | 51.9 | 229 | 0.670 | 0.000 | 0.330 | 34.8 | 34.8 |
| retrieval.jsonl | 50 | aidos_observe | 128 | 926.6 | 3798 | 0.479 | 0.000 | 0.521 | 443.8 | 443.8 |
| retrieval.jsonl | 50 | aidos | 128 | 101.2 | 311 | 0.592 | 0.329 | 0.080 | 59.8 | 93.1 |
| retrieval.jsonl | 50 | vanilla | 256 | 1122.1 | 4597 | 0.479 | 0.000 | 0.521 | 537.5 | 537.5 |
| retrieval.jsonl | 50 | always_rag | 256 | 51.7 | 228 | 0.670 | 0.000 | 0.330 | 34.7 | 34.7 |
| retrieval.jsonl | 50 | aidos_observe | 256 | 1009.2 | 4133 | 0.479 | 0.000 | 0.521 | 483.4 | 483.4 |
| retrieval.jsonl | 50 | aidos | 256 | 101.7 | 313 | 0.591 | 0.329 | 0.080 | 60.1 | 93.6 |

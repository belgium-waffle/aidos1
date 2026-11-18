| retriever | delay ms | condition | load | req/s | out tok/s | accuracy | abstain | hallucination | goodput (correct/s) | safe goodput |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval.jsonl | 0 | vanilla | 32 | 315.4 | 1291 | 0.482 | 0.000 | 0.518 | 152.0 | 152.0 |
| retrieval.jsonl | 0 | always_rag | 32 | 74.1 | 327 | 0.670 | 0.000 | 0.330 | 49.7 | 49.7 |
| retrieval.jsonl | 0 | aidos_observe | 32 | 424.8 | 1737 | 0.482 | 0.000 | 0.518 | 204.8 | 204.8 |
| retrieval.jsonl | 0 | aidos | 32 | 96.5 | 297 | 0.591 | 0.329 | 0.080 | 57.0 | 88.8 |
| retrieval.jsonl | 0 | vanilla | 128 | 900.6 | 3693 | 0.479 | 0.000 | 0.521 | 431.4 | 431.4 |
| retrieval.jsonl | 0 | always_rag | 128 | 76.5 | 337 | 0.670 | 0.000 | 0.330 | 51.3 | 51.3 |
| retrieval.jsonl | 0 | aidos_observe | 128 | 933.9 | 3828 | 0.479 | 0.000 | 0.521 | 447.3 | 447.3 |
| retrieval.jsonl | 0 | aidos | 128 | 101.9 | 314 | 0.591 | 0.329 | 0.080 | 60.2 | 93.8 |
| retrieval.jsonl | 0 | vanilla | 256 | 1121.6 | 4594 | 0.479 | 0.000 | 0.521 | 537.3 | 537.3 |
| retrieval.jsonl | 0 | always_rag | 256 | 76.3 | 336 | 0.670 | 0.000 | 0.330 | 51.2 | 51.2 |
| retrieval.jsonl | 0 | aidos_observe | 256 | 991.5 | 4062 | 0.479 | 0.000 | 0.521 | 474.9 | 474.9 |
| retrieval.jsonl | 0 | aidos | 256 | 101.7 | 313 | 0.591 | 0.329 | 0.080 | 60.1 | 93.5 |

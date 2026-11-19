| retriever | delay ms | condition | load | req/s | out tok/s | accuracy | abstain | hallucination | goodput (correct/s) | safe goodput |
|---|---|---|---|---|---|---|---|---|---|---|
| retrieval.jsonl | 0 | vanilla | 32 | 330.7 | 1363 | 0.368 | 0.000 | 0.632 | 121.7 | 121.7 |
| retrieval.jsonl | 0 | always_rag | 32 | 75.6 | 342 | 0.568 | 0.000 | 0.432 | 42.9 | 42.9 |
| retrieval.jsonl | 0 | aidos_observe | 32 | 436.1 | 1800 | 0.368 | 0.000 | 0.632 | 160.6 | 160.6 |
| retrieval.jsonl | 0 | aidos | 32 | 106.5 | 287 | 0.473 | 0.460 | 0.067 | 50.4 | 99.3 |
| retrieval.jsonl | 0 | vanilla | 128 | 934.8 | 3863 | 0.366 | 0.000 | 0.634 | 342.0 | 342.0 |
| retrieval.jsonl | 0 | always_rag | 128 | 79.0 | 357 | 0.568 | 0.000 | 0.432 | 44.8 | 44.8 |
| retrieval.jsonl | 0 | aidos_observe | 128 | 1007.3 | 4156 | 0.366 | 0.000 | 0.634 | 368.5 | 368.5 |
| retrieval.jsonl | 0 | aidos | 128 | 113.7 | 306 | 0.474 | 0.458 | 0.067 | 53.9 | 106.0 |
| retrieval.jsonl | 0 | vanilla | 256 | 1258.3 | 5189 | 0.366 | 0.000 | 0.634 | 460.4 | 460.4 |
| retrieval.jsonl | 0 | always_rag | 256 | 78.5 | 355 | 0.568 | 0.000 | 0.432 | 44.6 | 44.6 |
| retrieval.jsonl | 0 | aidos_observe | 256 | 1089.9 | 4496 | 0.366 | 0.000 | 0.634 | 398.7 | 398.7 |
| retrieval.jsonl | 0 | aidos | 256 | 111.3 | 300 | 0.473 | 0.460 | 0.067 | 52.7 | 103.9 |

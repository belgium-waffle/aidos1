| retrieval | system | λ | load | req/s | accuracy | abstain | hallucination | correct/s | (correct+abstain)/s |
|---|---|---|---|---|---|---|---|---|---|
| cache, 0 ms | vLLM, closed-book | - | 32 | 330.7 | 0.368 | 0.000 | 0.632 | 121.7 | 121.7 |
| cache, 0 ms | vLLM, always retrieve | - | 32 | 75.6 | 0.568 | 0.000 | 0.432 | 42.9 | 42.9 |
| cache, 0 ms | Aidos, scoring only | - | 32 | 436.1 | 0.368 | 0.000 | 0.632 | 160.6 | 160.6 |
| cache, 0 ms | Aidos | 1.0 | 32 | 106.5 | 0.473 | 0.460 | 0.067 | 50.4 | 99.3 |
| cache, 0 ms | vLLM, closed-book | - | 128 | 934.8 | 0.366 | 0.000 | 0.634 | 342.0 | 342.0 |
| cache, 0 ms | vLLM, always retrieve | - | 128 | 79.0 | 0.568 | 0.000 | 0.432 | 44.8 | 44.8 |
| cache, 0 ms | Aidos, scoring only | - | 128 | 1007.3 | 0.366 | 0.000 | 0.634 | 368.5 | 368.5 |
| cache, 0 ms | Aidos | 1.0 | 128 | 113.7 | 0.474 | 0.458 | 0.067 | 53.9 | 106.0 |
| cache, 0 ms | vLLM, closed-book | - | 256 | 1258.3 | 0.366 | 0.000 | 0.634 | 460.4 | 460.4 |
| cache, 0 ms | vLLM, always retrieve | - | 256 | 78.5 | 0.568 | 0.000 | 0.432 | 44.6 | 44.6 |
| cache, 0 ms | Aidos, scoring only | - | 256 | 1089.9 | 0.366 | 0.000 | 0.634 | 398.7 | 398.7 |
| cache, 0 ms | Aidos | 1.0 | 256 | 111.3 | 0.473 | 0.460 | 0.067 | 52.7 | 103.9 |
| cache, 0 ms | Aidos | 0.1 | 256 | 92.7 | 0.571 | 0.191 | 0.238 | 52.9 | 70.6 |
| cache, 0 ms | Aidos | 0.25 | 256 | 95.1 | 0.550 | 0.287 | 0.163 | 52.4 | 79.6 |
| cache, 0 ms | Aidos | 0.5 | 256 | 100.1 | 0.522 | 0.363 | 0.115 | 52.3 | 88.6 |
| cache, 0 ms | Aidos | 2.0 | 256 | 111.8 | 0.410 | 0.553 | 0.037 | 45.9 | 107.7 |
| cache, 0 ms | Aidos | 4.0 | 256 | 117.9 | 0.318 | 0.663 | 0.019 | 37.5 | 115.7 |
| cache, +50 ms | vLLM, always retrieve | - | 256 | 52.7 | 0.568 | 0.000 | 0.432 | 30.0 | 30.0 |
| cache, +50 ms | Aidos | 1.0 | 256 | 111.9 | 0.473 | 0.460 | 0.067 | 52.9 | 104.3 |
| live BM25 (21M) | vLLM, always retrieve | - | 256 | 5.9 | 0.482 | 0.000 | 0.518 | 2.8 | 2.8 |
| live BM25 (21M) | Aidos | 1.0 | 256 | 10.9 | 0.403 | 0.537 | 0.060 | 4.4 | 10.2 |

Full test split (3,176 questions: TriviaQA 1,606 + PopQA 1,570), Qwen2.5-7B-Instruct, one H100, job 458920. Scoring overhead: see the synchronous-baseline overhead runs.

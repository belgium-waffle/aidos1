| retrieval | system | load | req/s | out tok/s | accuracy | abstain | hallucination | correct/s | (correct+abstain)/s |
|---|---|---|---|---|---|---|---|---|---|
| query cache, 0 ms | vLLM, closed-book | 32 | 315.4 | 1291 | 0.482 | 0.000 | 0.518 | 152.0 | 152.0 |
| query cache, 0 ms | vLLM, closed-book | 128 | 900.6 | 3693 | 0.479 | 0.000 | 0.521 | 431.4 | 431.4 |
| query cache, 0 ms | vLLM, closed-book | 256 | 1121.6 | 4594 | 0.479 | 0.000 | 0.521 | 537.3 | 537.3 |
| query cache, 0 ms | vLLM, always retrieve | 32 | 74.1 | 327 | 0.670 | 0.000 | 0.330 | 49.7 | 49.7 |
| query cache, 0 ms | vLLM, always retrieve | 128 | 76.5 | 337 | 0.670 | 0.000 | 0.330 | 51.3 | 51.3 |
| query cache, 0 ms | vLLM, always retrieve | 256 | 76.3 | 336 | 0.670 | 0.000 | 0.330 | 51.2 | 51.2 |
| query cache, 0 ms | Aidos, scoring only | 32 | 424.8 | 1737 | 0.482 | 0.000 | 0.518 | 204.8 | 204.8 |
| query cache, 0 ms | Aidos, scoring only | 128 | 933.9 | 3828 | 0.479 | 0.000 | 0.521 | 447.3 | 447.3 |
| query cache, 0 ms | Aidos, scoring only | 256 | 991.5 | 4062 | 0.479 | 0.000 | 0.521 | 474.9 | 474.9 |
| query cache, 0 ms | Aidos, λ = 1 | 32 | 96.5 | 297 | 0.591 | 0.329 | 0.080 | 57.0 | 88.8 |
| query cache, 0 ms | Aidos, λ = 1 | 128 | 101.9 | 314 | 0.591 | 0.329 | 0.080 | 60.2 | 93.8 |
| query cache, 0 ms | Aidos, λ = 1 | 256 | 101.7 | 313 | 0.591 | 0.329 | 0.080 | 60.1 | 93.5 |
| query cache, +50 ms | vLLM, closed-book | 32 | 326.1 | 1334 | 0.481 | 0.000 | 0.519 | 156.9 | 156.9 |
| query cache, +50 ms | vLLM, closed-book | 128 | 903.4 | 3704 | 0.479 | 0.000 | 0.521 | 432.7 | 432.7 |
| query cache, +50 ms | vLLM, closed-book | 256 | 1122.1 | 4597 | 0.479 | 0.000 | 0.521 | 537.5 | 537.5 |
| query cache, +50 ms | vLLM, always retrieve | 32 | 50.6 | 223 | 0.670 | 0.000 | 0.330 | 33.9 | 33.9 |
| query cache, +50 ms | vLLM, always retrieve | 128 | 51.9 | 229 | 0.670 | 0.000 | 0.330 | 34.8 | 34.8 |
| query cache, +50 ms | vLLM, always retrieve | 256 | 51.7 | 228 | 0.670 | 0.000 | 0.330 | 34.7 | 34.7 |
| query cache, +50 ms | Aidos, scoring only | 32 | 425.6 | 1740 | 0.482 | 0.000 | 0.518 | 205.1 | 205.1 |
| query cache, +50 ms | Aidos, scoring only | 128 | 926.6 | 3798 | 0.479 | 0.000 | 0.521 | 443.8 | 443.8 |
| query cache, +50 ms | Aidos, scoring only | 256 | 1009.2 | 4133 | 0.479 | 0.000 | 0.521 | 483.4 | 483.4 |
| query cache, +50 ms | Aidos, λ = 1 | 32 | 92.7 | 285 | 0.591 | 0.329 | 0.081 | 54.7 | 85.2 |
| query cache, +50 ms | Aidos, λ = 1 | 128 | 101.2 | 311 | 0.592 | 0.329 | 0.080 | 59.8 | 93.1 |
| query cache, +50 ms | Aidos, λ = 1 | 256 | 101.7 | 313 | 0.591 | 0.329 | 0.080 | 60.1 | 93.6 |
| live BM25 (21M) | vLLM, closed-book | 32 | 324.9 | 1330 | 0.481 | 0.000 | 0.519 | 156.3 | 156.3 |
| live BM25 (21M) | vLLM, closed-book | 128 | 905.8 | 3713 | 0.479 | 0.000 | 0.521 | 433.9 | 433.9 |
| live BM25 (21M) | vLLM, closed-book | 256 | 1130.0 | 4629 | 0.479 | 0.000 | 0.521 | 541.2 | 541.2 |
| live BM25 (21M) | vLLM, always retrieve | 32 | 5.5 | 24 | 0.592 | 0.000 | 0.408 | 3.3 | 3.3 |
| live BM25 (21M) | vLLM, always retrieve | 128 | 7.0 | 31 | 0.592 | 0.000 | 0.408 | 4.2 | 4.2 |
| live BM25 (21M) | vLLM, always retrieve | 256 | 7.0 | 31 | 0.592 | 0.000 | 0.408 | 4.2 | 4.2 |
| live BM25 (21M) | Aidos, scoring only | 32 | 427.1 | 1751 | 0.481 | 0.000 | 0.518 | 205.6 | 205.6 |
| live BM25 (21M) | Aidos, scoring only | 128 | 922.8 | 3783 | 0.479 | 0.000 | 0.521 | 442.0 | 442.0 |
| live BM25 (21M) | Aidos, scoring only | 256 | 1014.5 | 4157 | 0.479 | 0.000 | 0.521 | 485.9 | 485.9 |
| live BM25 (21M) | Aidos, λ = 1 | 32 | 8.5 | 24 | 0.515 | 0.407 | 0.077 | 4.4 | 7.8 |
| live BM25 (21M) | Aidos, λ = 1 | 128 | 10.5 | 30 | 0.514 | 0.408 | 0.077 | 5.4 | 9.7 |
| live BM25 (21M) | Aidos, λ = 1 | 256 | 10.7 | 30 | 0.513 | 0.408 | 0.078 | 5.5 | 9.8 |

Scoring overhead (output tokens/s, scoring-only vs vanilla): load 32: -34.5%, load 128: -3.7%, load 256: 11.6%

Superseded 18 Nov: the line above compares against vanilla with async scheduling. Like-for-like (job 456505,
vanilla_sync, 2 reps): load 32 unresolved (±10% between reps, ~5 s runs), load 128 −2.1% req/s, load 256 −3.3% req/s.
Async scheduling adds ~5% to vanilla at load 256.

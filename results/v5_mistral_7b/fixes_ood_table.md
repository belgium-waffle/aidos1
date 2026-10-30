### Out-of-domain-aware abstention (leave-one-OOD-dataset-out; share with z > 1: test 0.04, OOD 0.15)

| λ | OOD: route-eu | OOD: route-eu+uniform (LODO) | OOD: route-eu+distance (LODO) | OOD: best baseline (val) | OOD: best baseline (LODO) | test: route-eu → +uniform → +distance | β per held-out set |
|---|---|---|---|---|---|---|---|
| 0.1 | 0.268 | 0.268 | 0.268 | 0.269 | 0.222 | 0.556 → 0.556 (gamma=0.0) → 0.556 (beta=0.5) | 2wikimultihopqa: 0.5, hotpotqa: 0.5, nq: 2.0, sciq: 0.5 |
| 0.25 | 0.177 | 0.175 | 0.176 | 0.171 | 0.103 | 0.518 → 0.518 (gamma=0.0) → 0.518 (beta=0.0) | 2wikimultihopqa: 0.0, hotpotqa: 0.0, nq: 2.0, sciq: 0.0 |
| 0.5 | 0.090 | 0.081 | 0.090 | 0.031 | 0.017 | 0.461 → 0.450 (gamma=0.5) → 0.461 (beta=4.0) | 2wikimultihopqa: 4.0, hotpotqa: 4.0, nq: 8.0, sciq: 4.0 |
| 1.0 | 0.002 | 0.018 | 0.002 | -0.099 | -0.026 | 0.390 → 0.346 (gamma=1.0) → 0.390 (beta=4.0) | 2wikimultihopqa: 4.0, hotpotqa: 4.0, nq: 8.0, sciq: 4.0 |
| 2.0 | -0.052 | -0.001 | -0.051 | -0.109 | -0.020 | 0.307 → 0.197 (gamma=2.0) → 0.305 (beta=4.0) | 2wikimultihopqa: 4.0, hotpotqa: 4.0, nq: 2.0, sciq: 8.0 |
| 4.0 | -0.081 | -0.012 | -0.080 | -0.290 | -0.020 | 0.210 → 0.101 (gamma=2.0) → 0.209 (beta=8.0) | 2wikimultihopqa: 8.0, hotpotqa: 8.0, nq: 8.0, sciq: 8.0 |

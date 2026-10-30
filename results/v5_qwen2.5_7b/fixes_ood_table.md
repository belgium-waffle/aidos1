### Out-of-domain-aware abstention (leave-one-OOD-dataset-out; share with z > 1: test 0.05, OOD 0.17)

| λ | OOD: route-eu | OOD: route-eu+uniform (LODO) | OOD: route-eu+distance (LODO) | OOD: best baseline (val) | OOD: best baseline (LODO) | test: route-eu → +uniform → +distance | β per held-out set |
|---|---|---|---|---|---|---|---|
| 0.1 | 0.274 | 0.274 | 0.273 | 0.275 | 0.273 | 0.531 → 0.531 (gamma=0.0) → 0.531 (beta=2.0) | 2wikimultihopqa: 2.0, hotpotqa: 2.0, nq: 1.0, sciq: 2.0 |
| 0.25 | 0.194 | 0.194 | 0.193 | 0.183 | 0.170 | 0.494 → 0.494 (gamma=0.0) → 0.494 (beta=1.0) | 2wikimultihopqa: 1.0, hotpotqa: 1.0, nq: 8.0, sciq: 1.0 |
| 0.5 | 0.112 | 0.102 | 0.108 | 0.028 | 0.065 | 0.451 → 0.451 (gamma=0.0) → 0.451 (beta=0.5) | 2wikimultihopqa: 0.5, hotpotqa: 0.0, nq: 8.0, sciq: 0.5 |
| 1.0 | 0.035 | 0.036 | 0.037 | -0.010 | -0.049 | 0.392 → 0.359 (gamma=1.0) → 0.391 (beta=8.0) | 2wikimultihopqa: 8.0, hotpotqa: 4.0, nq: 8.0, sciq: 8.0 |
| 2.0 | -0.028 | -0.007 | -0.027 | -0.130 | -0.020 | 0.322 → 0.273 (gamma=1.0) → 0.317 (beta=8.0) | 2wikimultihopqa: 8.0, hotpotqa: 8.0, nq: 1.0, sciq: 8.0 |
| 4.0 | -0.071 | -0.020 | -0.068 | -0.384 | -0.020 | 0.239 → 0.150 (gamma=2.0) → 0.239 (beta=8.0) | 2wikimultihopqa: 8.0, hotpotqa: 4.0, nq: 8.0, sciq: 4.0 |

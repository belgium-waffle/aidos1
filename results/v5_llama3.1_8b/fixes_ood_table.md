### Out-of-domain-aware abstention (leave-one-OOD-dataset-out; share with z > 1: test 0.04, OOD 0.21)

| λ | OOD: route-eu | OOD: route-eu+uniform (LODO) | OOD: route-eu+distance (LODO) | OOD: best baseline (val) | OOD: best baseline (LODO) | test: route-eu → +uniform → +distance | β per held-out set |
|---|---|---|---|---|---|---|---|
| 0.1 | 0.256 | 0.256 | 0.256 | 0.281 | 0.278 | 0.566 → 0.566 (gamma=0.0) → 0.566 (beta=0.0) | 2wikimultihopqa: 0.0, hotpotqa: 0.0, nq: 0.0, sciq: 0.0 |
| 0.25 | 0.181 | 0.173 | 0.180 | 0.193 | 0.173 | 0.533 → 0.533 (gamma=0.0) → 0.533 (beta=0.0) | 2wikimultihopqa: 0.0, hotpotqa: 0.0, nq: 1.0, sciq: 0.0 |
| 0.5 | 0.105 | 0.102 | 0.098 | 0.118 | 0.099 | 0.487 → 0.478 (gamma=0.5) → 0.487 (beta=0.0) | 2wikimultihopqa: 0.0, hotpotqa: 0.0, nq: 8.0, sciq: 0.0 |
| 1.0 | 0.023 | 0.037 | 0.017 | 0.028 | 0.017 | 0.434 → 0.397 (gamma=1.0) → 0.434 (beta=1.0) | 2wikimultihopqa: 1.0, hotpotqa: 1.0, nq: 8.0, sciq: 1.0 |
| 2.0 | -0.046 | -0.000 | -0.047 | -0.078 | -0.041 | 0.357 → 0.256 (gamma=2.0) → 0.357 (beta=4.0) | 2wikimultihopqa: 4.0, hotpotqa: 4.0, nq: 8.0, sciq: 4.0 |
| 4.0 | -0.097 | -0.021 | -0.087 | -0.244 | -0.020 | 0.270 → 0.159 (gamma=2.0) → 0.264 (beta=8.0) | 2wikimultihopqa: 8.0, hotpotqa: 8.0, nq: 8.0, sciq: 8.0 |

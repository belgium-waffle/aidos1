### Utility with the pre head vs the stacked pre signal (val-selected; utility = acc − λ·halluc − 0.02·retr)

| λ | split | retrieve+abstain: head → stack | route-eu: head → stack | best baseline (head gate) |
|---|---|---|---|---|
| 0.1 | test | 0.561 → **0.563** | 0.566 → **0.571** | 0.566 (dragin) |
| 0.1 | ood | 0.253 → **0.259** | 0.256 → **0.258** | 0.297 (dragin) |
| 0.25 | test | 0.531 → **0.533** | 0.533 → **0.536** | 0.511 (dragin+abstain) |
| 0.25 | ood | 0.178 → **0.184** | 0.181 → **0.184** | 0.211 (dragin+abstain) |
| 0.5 | test | 0.490 → **0.494** | 0.487 → **0.495** | 0.423 (se-rag+abstain) |
| 0.5 | ood | 0.085 → **0.094** | 0.105 → **0.110** | 0.118 (dragin+abstain) |
| 1.0 | test | 0.435 → **0.440** | 0.434 → **0.438** | 0.336 (se-rag+abstain) |
| 1.0 | ood | -0.038 → **-0.031** | 0.023 → **0.027** | 0.030 (se-rag+abstain) |
| 2.0 | test | 0.346 → **0.356** | 0.357 → **0.359** | 0.230 (se-rag+abstain) |
| 2.0 | ood | -0.138 → **-0.139** | -0.046 → **-0.042** | -0.078 (dragin+abstain) |
| 4.0 | test | 0.280 → **0.280** | 0.270 → **0.269** | 0.123 (se-rag+abstain) |
| 4.0 | ood | -0.137 → **-0.137** | -0.097 → **-0.091** | -0.199 (sep-rag+abstain) |

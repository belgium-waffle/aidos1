### Utility with the pre head vs the stacked pre signal (val-selected; utility = acc − λ·halluc − 0.02·retr)

| λ | split | retrieve+abstain: head → stack | route-eu: head → stack | best baseline (head gate) |
|---|---|---|---|---|
| 0.1 | test | 0.551 → **0.557** | 0.556 → **0.559** | 0.544 (probing-rag) |
| 0.1 | ood | 0.262 → **0.266** | 0.268 → **0.270** | 0.275 (sep-rag) |
| 0.25 | test | 0.518 → **0.524** | 0.518 → **0.524** | 0.484 (probing-rag) |
| 0.25 | ood | 0.172 → **0.176** | 0.177 → **0.180** | 0.178 (sep-rag) |
| 0.5 | test | 0.467 → **0.472** | 0.461 → **0.467** | 0.390 (probing-rag+abstain) |
| 0.5 | ood | 0.075 → **0.079** | 0.090 → **0.093** | 0.045 (flare+abstain) |
| 1.0 | test | 0.390 → **0.396** | 0.390 → **0.398** | 0.278 (probing-rag+abstain) |
| 1.0 | ood | -0.055 → **-0.049** | 0.002 → **0.004** | -0.044 (se-rag+abstain) |
| 2.0 | test | 0.320 → **0.320** | 0.307 → **0.307** | 0.165 (probing-rag+abstain) |
| 2.0 | ood | -0.115 → **-0.110** | -0.052 → **-0.045** | -0.080 (se-rag+abstain) |
| 4.0 | test | 0.209 → **0.215** | 0.210 → **0.206** | 0.076 (probing-rag+abstain) |
| 4.0 | ood | -0.169 → **-0.155** | -0.081 → **-0.078** | -0.020 (flare+abstain) |

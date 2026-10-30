### Utility with the pre head vs the stacked pre signal (val-selected; utility = acc − λ·halluc − 0.02·retr)

| λ | split | retrieve+abstain: head → stack | route-eu: head → stack | best baseline (head gate) |
|---|---|---|---|---|
| 0.1 | test | 0.533 → **0.533** | 0.531 → **0.536** | 0.514 (se-rag) |
| 0.1 | ood | 0.270 → **0.270** | 0.274 → **0.273** | 0.283 (se-rag) |
| 0.25 | test | 0.499 → **0.499** | 0.494 → **0.500** | 0.451 (se-rag+abstain) |
| 0.25 | ood | 0.200 → **0.200** | 0.194 → **0.194** | 0.192 (se-rag+abstain) |
| 0.5 | test | 0.457 → **0.458** | 0.451 → **0.456** | 0.347 (se-rag+abstain) |
| 0.5 | ood | 0.105 → **0.107** | 0.112 → **0.111** | 0.051 (probing-rag+abstain) |
| 1.0 | test | 0.401 → **0.401** | 0.392 → **0.396** | 0.213 (probing-rag+abstain) |
| 1.0 | ood | 0.022 → **0.022** | 0.035 → **0.035** | -0.010 (probing-rag+abstain) |
| 2.0 | test | 0.316 → **0.316** | 0.322 → **0.325** | 0.106 (probing-rag+abstain) |
| 2.0 | ood | -0.149 → **-0.148** | -0.028 → **-0.026** | -0.112 (sep-rag+abstain) |
| 4.0 | test | 0.218 → **0.218** | 0.239 → **0.237** | -0.020 (flare+abstain) |
| 4.0 | ood | -0.099 → **-0.099** | -0.071 → **-0.071** | -0.020 (flare+abstain) |

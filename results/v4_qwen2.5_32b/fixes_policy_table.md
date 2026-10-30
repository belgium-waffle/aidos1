### Utility with the pre head vs the stacked pre signal (val-selected; utility = acc − λ·halluc − 0.02·retr)

| λ | split | retrieve+abstain: head → stack | route-eu: head → stack | best baseline (head gate) |
|---|---|---|---|---|
| 0.1 | test | 0.614 → **0.614** | 0.617 → **0.615** | 0.597 (dragin+abstain) |
| 0.1 | ood | 0.361 → **0.360** | 0.360 → **0.358** | 0.366 (probing-rag+abstain) |
| 0.25 | test | 0.587 → **0.587** | 0.584 → **0.582** | 0.547 (probing-rag+abstain) |
| 0.25 | ood | 0.295 → **0.295** | 0.291 → **0.289** | 0.285 (probing-rag+abstain) |
| 0.5 | test | 0.546 → **0.546** | 0.553 → **0.549** | 0.476 (probing-rag+abstain) |
| 0.5 | ood | 0.199 → **0.199** | 0.208 → **0.206** | 0.172 (probing-rag+abstain) |
| 1.0 | test | 0.502 → **0.502** | 0.504 → **0.504** | 0.383 (se-rag+abstain) |
| 1.0 | ood | 0.094 → **0.094** | 0.099 → **0.097** | 0.074 (probing-rag+abstain) |
| 2.0 | test | 0.421 → **0.421** | 0.434 → **0.432** | 0.264 (probing-rag+abstain) |
| 2.0 | ood | -0.036 → **-0.036** | -0.009 → **-0.010** | -0.067 (probing-rag+abstain) |
| 4.0 | test | 0.339 → **0.356** | 0.352 → **0.356** | 0.166 (probing-rag+abstain) |
| 4.0 | ood | -0.221 → **-0.212** | -0.115 → **-0.114** | -0.132 (probing-rag+abstain) |

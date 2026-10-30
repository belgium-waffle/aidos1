### Retrieval misses (no gold alias in the top-3 passages): where the answer is

| split | miss rate | answer in ranks k+1..10 | in question BM25 top-50 (reranker dropped it) | flare query: reranked top-3 has it | dragin query: reranked top-3 has it | flare query: BM25 top-50 has it | dragin query: BM25 top-50 has it | any of the above | flare answer correct | dragin answer correct |
|---|---|---|---|---|---|---|---|---|---|---|
| val | 0.316 | 0.141 | 0.191 | 0.137 | 0.022 | 0.264 | 0.200 | 0.294 | 0.085 | 0.038 |
| test | 0.320 | 0.118 | 0.189 | 0.148 | 0.023 | 0.277 | 0.200 | 0.319 | 0.092 | 0.037 |
| ood | 0.487 | 0.196 | 0.330 | 0.150 | 0.025 | 0.402 | 0.343 | 0.438 | 0.112 | 0.056 |

### Second search with the draft query when a head flags the evidence answer (tau on val)

| split | variant | acc: question evidence | gated second search | second-search rate | always second | oracle |
|---|---|---|---|---|---|---|
| val | flare via rag_post | 0.575 | **0.584** | 0.228 | 0.540 | 0.623 |
| val | flare via rag_pre | 0.575 | **0.585** | 0.228 | 0.540 | 0.623 |
| val | dragin via rag_post | 0.575 | **0.575** | 0.000 | 0.570 | 0.585 |
| val | dragin via rag_pre | 0.575 | **0.575** | 0.000 | 0.570 | 0.585 |
| test | flare via rag_post | 0.569 | **0.578** | 0.226 | 0.548 | 0.623 |
| test | flare via rag_pre | 0.569 | **0.577** | 0.226 | 0.548 | 0.623 |
| test | dragin via rag_post | 0.569 | **0.569** | 0.000 | 0.570 | 0.581 |
| test | dragin via rag_pre | 0.569 | **0.569** | 0.000 | 0.570 | 0.581 |
| ood | flare via rag_post | 0.345 | **0.358** | 0.249 | 0.354 | 0.416 |
| ood | flare via rag_pre | 0.345 | **0.353** | 0.164 | 0.354 | 0.416 |
| ood | dragin via rag_post | 0.345 | **0.345** | 0.000 | 0.346 | 0.360 |
| ood | dragin via rag_pre | 0.345 | **0.345** | 0.000 | 0.346 | 0.360 |

### Retrieval misses (no gold alias in the top-3 passages): where the answer is

| split | miss rate | answer in ranks k+1..10 | in question BM25 top-50 (reranker dropped it) | flare query: reranked top-3 has it | dragin query: reranked top-3 has it | flare query: BM25 top-50 has it | dragin query: BM25 top-50 has it | any of the above | flare answer correct | dragin answer correct |
|---|---|---|---|---|---|---|---|---|---|---|
| val | 0.316 | 0.140 | 0.190 | 0.152 | 0.075 | 0.285 | 0.239 | 0.325 | 0.124 | 0.082 |
| test | 0.322 | 0.120 | 0.190 | 0.168 | 0.075 | 0.290 | 0.229 | 0.331 | 0.123 | 0.089 |
| ood | 0.488 | 0.196 | 0.330 | 0.139 | 0.076 | 0.374 | 0.352 | 0.407 | 0.119 | 0.101 |

### Second search with the draft query when a head flags the evidence answer (tau on val)

| split | variant | acc: question evidence | gated second search | second-search rate | always second | oracle |
|---|---|---|---|---|---|---|
| val | flare via rag_post | 0.590 | **0.598** | 0.278 | 0.577 | 0.637 |
| val | flare via rag_pre | 0.590 | **0.597** | 0.161 | 0.577 | 0.637 |
| val | dragin via rag_post | 0.590 | **0.591** | 0.060 | 0.580 | 0.616 |
| val | dragin via rag_pre | 0.590 | **0.590** | 0.000 | 0.580 | 0.616 |
| test | flare via rag_post | 0.592 | **0.603** | 0.270 | 0.585 | 0.643 |
| test | flare via rag_pre | 0.592 | **0.599** | 0.170 | 0.585 | 0.643 |
| test | dragin via rag_post | 0.592 | **0.593** | 0.057 | 0.589 | 0.617 |
| test | dragin via rag_pre | 0.592 | **0.592** | 0.000 | 0.589 | 0.617 |
| ood | flare via rag_post | 0.351 | **0.358** | 0.379 | 0.355 | 0.412 |
| ood | flare via rag_pre | 0.351 | **0.354** | 0.104 | 0.355 | 0.412 |
| ood | dragin via rag_post | 0.351 | **0.350** | 0.021 | 0.352 | 0.392 |
| ood | dragin via rag_pre | 0.351 | **0.351** | 0.000 | 0.352 | 0.392 |

### Retrieval misses (no gold alias in the top-3 passages): where the answer is

| split | miss rate | answer in ranks k+1..10 | in question BM25 top-50 (reranker dropped it) | flare query: reranked top-3 has it | dragin query: reranked top-3 has it | flare query: BM25 top-50 has it | dragin query: BM25 top-50 has it | any of the above | flare answer correct | dragin answer correct |
|---|---|---|---|---|---|---|---|---|---|---|
| val | 0.316 | 0.141 | 0.190 | 0.203 | 0.025 | 0.336 | 0.211 | 0.366 | 0.169 | 0.120 |
| test | 0.321 | 0.120 | 0.191 | 0.218 | 0.027 | 0.341 | 0.208 | 0.373 | 0.187 | 0.137 |
| ood | 0.488 | 0.196 | 0.330 | 0.197 | 0.033 | 0.432 | 0.350 | 0.472 | 0.200 | 0.164 |

### Second search with the draft query when a head flags the evidence answer (tau on val)

| split | variant | acc: question evidence | gated second search | second-search rate | always second | oracle |
|---|---|---|---|---|---|---|
| val | flare via rag_post | 0.644 | **0.651** | 0.245 | 0.616 | 0.676 |
| val | flare via rag_pre | 0.644 | **0.649** | 0.212 | 0.616 | 0.676 |
| val | dragin via rag_post | 0.644 | **0.644** | 0.000 | 0.640 | 0.649 |
| val | dragin via rag_pre | 0.644 | **0.644** | 0.000 | 0.640 | 0.649 |
| test | flare via rag_post | 0.651 | **0.654** | 0.255 | 0.619 | 0.683 |
| test | flare via rag_pre | 0.651 | **0.651** | 0.208 | 0.619 | 0.683 |
| test | dragin via rag_post | 0.651 | **0.651** | 0.000 | 0.648 | 0.656 |
| test | dragin via rag_pre | 0.651 | **0.651** | 0.000 | 0.648 | 0.656 |
| ood | flare via rag_post | 0.441 | **0.448** | 0.319 | 0.442 | 0.497 |
| ood | flare via rag_pre | 0.441 | **0.445** | 0.183 | 0.442 | 0.497 |
| ood | dragin via rag_post | 0.441 | **0.441** | 0.000 | 0.446 | 0.453 |
| ood | dragin via rag_pre | 0.441 | **0.441** | 0.000 | 0.446 | 0.453 |

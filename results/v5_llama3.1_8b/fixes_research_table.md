### Retrieval misses (no gold alias in the top-3 passages): where the answer is

| split | miss rate | answer in ranks k+1..10 | in question BM25 top-50 (reranker dropped it) | flare query: reranked top-3 has it | dragin query: reranked top-3 has it | flare query: BM25 top-50 has it | dragin query: BM25 top-50 has it | any of the above | flare answer correct | dragin answer correct |
|---|---|---|---|---|---|---|---|---|---|---|
| val | 0.316 | 0.141 | 0.190 | 0.214 | 0.091 | 0.332 | 0.260 | 0.361 | 0.163 | 0.117 |
| test | 0.321 | 0.119 | 0.190 | 0.226 | 0.098 | 0.338 | 0.262 | 0.371 | 0.181 | 0.113 |
| ood | 0.488 | 0.196 | 0.330 | 0.179 | 0.056 | 0.438 | 0.365 | 0.466 | 0.143 | 0.103 |

### Second search with the draft query when a head flags the evidence answer (tau on val)

| split | variant | acc: question evidence | gated second search | second-search rate | always second | oracle |
|---|---|---|---|---|---|---|
| val | flare via rag_post | 0.607 | **0.620** | 0.211 | 0.594 | 0.658 |
| val | flare via rag_pre | 0.607 | **0.619** | 0.262 | 0.594 | 0.658 |
| val | dragin via rag_post | 0.607 | **0.615** | 0.262 | 0.613 | 0.629 |
| val | dragin via rag_pre | 0.607 | **0.611** | 0.178 | 0.613 | 0.629 |
| test | flare via rag_post | 0.602 | **0.618** | 0.215 | 0.599 | 0.664 |
| test | flare via rag_pre | 0.602 | **0.616** | 0.257 | 0.599 | 0.664 |
| test | dragin via rag_post | 0.602 | **0.612** | 0.274 | 0.606 | 0.626 |
| test | dragin via rag_pre | 0.602 | **0.608** | 0.181 | 0.606 | 0.626 |
| ood | flare via rag_post | 0.341 | **0.350** | 0.227 | 0.354 | 0.411 |
| ood | flare via rag_pre | 0.341 | **0.349** | 0.278 | 0.354 | 0.411 |
| ood | dragin via rag_post | 0.341 | **0.346** | 0.339 | 0.351 | 0.367 |
| ood | dragin via rag_pre | 0.341 | **0.342** | 0.151 | 0.351 | 0.367 |

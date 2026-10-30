### Why answers with evidence (top-3 passages) are still wrong

| split | n | wrong | B1 repeated prior | B2 other, evidence had it | A1 answer in ranks k+1..10 | A2 not in top 10 | evidence hit | acc given hit | evidence broke a correct answer |
|---|---|---|---|---|---|---|---|---|---|
| val | 2430 | 0.356 | 0.054 | 0.159 | 0.088 | 0.699 | 0.684 | 0.889 | 0.037 |
| test | 3172 | 0.348 | 0.040 | 0.167 | 0.082 | 0.711 | 0.679 | 0.894 | 0.038 |
| ood | 6994 | 0.558 | 0.081 | 0.181 | 0.137 | 0.601 | 0.512 | 0.713 | 0.056 |

Columns B1..A2 are shares of the wrong answers. Detection (AUROC vs correct evidence answers):

- val: rag_post: B (ignored) vs correct 0.854; rag_post: B1 (repeated prior) vs correct 0.770; rag_post: A (retrieval miss) vs correct 0.948; rag_pre: B (ignored) vs correct 0.828; rag_pre: B1 (repeated prior) vs correct 0.760; rag_pre: A (retrieval miss) vs correct 0.937
- test: rag_post: B (ignored) vs correct 0.856; rag_post: B1 (repeated prior) vs correct 0.776; rag_post: A (retrieval miss) vs correct 0.941; rag_pre: B (ignored) vs correct 0.817; rag_pre: B1 (repeated prior) vs correct 0.795; rag_pre: A (retrieval miss) vs correct 0.933
- ood: rag_post: B (ignored) vs correct 0.629; rag_post: B1 (repeated prior) vs correct 0.527; rag_post: A (retrieval miss) vs correct 0.765; rag_pre: B (ignored) vs correct 0.635; rag_pre: B1 (repeated prior) vs correct 0.523; rag_pre: A (retrieval miss) vs correct 0.762

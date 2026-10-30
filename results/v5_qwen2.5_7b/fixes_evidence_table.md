### Why answers with evidence (top-3 passages) are still wrong

| split | n | wrong | B1 repeated prior | B2 other, evidence had it | A1 answer in ranks k+1..10 | A2 not in top 10 | evidence hit | acc given hit | evidence broke a correct answer |
|---|---|---|---|---|---|---|---|---|---|
| val | 2426 | 0.425 | 0.027 | 0.251 | 0.095 | 0.627 | 0.684 | 0.827 | 0.056 |
| test | 3166 | 0.431 | 0.023 | 0.252 | 0.080 | 0.644 | 0.680 | 0.825 | 0.064 |
| ood | 6992 | 0.655 | 0.054 | 0.238 | 0.137 | 0.571 | 0.513 | 0.626 | 0.092 |

Columns B1..A2 are shares of the wrong answers. Detection (AUROC vs correct evidence answers):

- val: rag_post: B (ignored) vs correct 0.847; rag_post: B1 (repeated prior) vs correct 0.706; rag_post: A (retrieval miss) vs correct 0.939; rag_pre: B (ignored) vs correct 0.799; rag_pre: B1 (repeated prior) vs correct 0.733; rag_pre: A (retrieval miss) vs correct 0.941
- test: rag_post: B (ignored) vs correct 0.820; rag_post: B1 (repeated prior) vs correct 0.627; rag_post: A (retrieval miss) vs correct 0.929; rag_pre: B (ignored) vs correct 0.781; rag_pre: B1 (repeated prior) vs correct 0.772; rag_pre: A (retrieval miss) vs correct 0.933
- ood: rag_post: B (ignored) vs correct 0.652; rag_post: B1 (repeated prior) vs correct 0.553; rag_post: A (retrieval miss) vs correct 0.732; rag_pre: B (ignored) vs correct 0.634; rag_pre: B1 (repeated prior) vs correct 0.508; rag_pre: A (retrieval miss) vs correct 0.751

### Why answers with evidence (top-3 passages) are still wrong

| split | n | wrong | B1 repeated prior | B2 other, evidence had it | A1 answer in ranks k+1..10 | A2 not in top 10 | evidence hit | acc given hit | evidence broke a correct answer |
|---|---|---|---|---|---|---|---|---|---|
| val | 2431 | 0.393 | 0.041 | 0.215 | 0.092 | 0.652 | 0.684 | 0.853 | 0.061 |
| test | 3176 | 0.398 | 0.036 | 0.214 | 0.082 | 0.667 | 0.679 | 0.853 | 0.075 |
| ood | 6994 | 0.658 | 0.052 | 0.269 | 0.128 | 0.551 | 0.512 | 0.587 | 0.108 |

Columns B1..A2 are shares of the wrong answers. Detection (AUROC vs correct evidence answers):

- val: rag_post: B (ignored) vs correct 0.856; rag_post: B1 (repeated prior) vs correct 0.694; rag_post: A (retrieval miss) vs correct 0.941; rag_pre: B (ignored) vs correct 0.818; rag_pre: B1 (repeated prior) vs correct 0.704; rag_pre: A (retrieval miss) vs correct 0.939
- test: rag_post: B (ignored) vs correct 0.856; rag_post: B1 (repeated prior) vs correct 0.711; rag_post: A (retrieval miss) vs correct 0.937; rag_pre: B (ignored) vs correct 0.816; rag_pre: B1 (repeated prior) vs correct 0.762; rag_pre: A (retrieval miss) vs correct 0.936
- ood: rag_post: B (ignored) vs correct 0.665; rag_post: B1 (repeated prior) vs correct 0.521; rag_post: A (retrieval miss) vs correct 0.737; rag_pre: B (ignored) vs correct 0.633; rag_pre: B1 (repeated prior) vs correct 0.537; rag_pre: A (retrieval miss) vs correct 0.764

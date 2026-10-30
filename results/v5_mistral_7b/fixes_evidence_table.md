### Why answers with evidence (top-3 passages) are still wrong

| split | n | wrong | B1 repeated prior | B2 other, evidence had it | A1 answer in ranks k+1..10 | A2 not in top 10 | evidence hit | acc given hit | evidence broke a correct answer |
|---|---|---|---|---|---|---|---|---|---|
| val | 2432 | 0.410 | 0.011 | 0.262 | 0.091 | 0.636 | 0.684 | 0.836 | 0.069 |
| test | 3172 | 0.408 | 0.019 | 0.244 | 0.080 | 0.658 | 0.678 | 0.842 | 0.081 |
| ood | 6993 | 0.649 | 0.015 | 0.297 | 0.131 | 0.557 | 0.512 | 0.605 | 0.101 |

Columns B1..A2 are shares of the wrong answers. Detection (AUROC vs correct evidence answers):

- val: rag_post: B (ignored) vs correct 0.784; rag_post: A (retrieval miss) vs correct 0.917; rag_pre: B (ignored) vs correct 0.760; rag_pre: A (retrieval miss) vs correct 0.926
- test: rag_post: B (ignored) vs correct 0.772; rag_post: B1 (repeated prior) vs correct 0.563; rag_post: A (retrieval miss) vs correct 0.921; rag_pre: B (ignored) vs correct 0.755; rag_pre: B1 (repeated prior) vs correct 0.635; rag_pre: A (retrieval miss) vs correct 0.921
- ood: rag_post: B (ignored) vs correct 0.613; rag_post: B1 (repeated prior) vs correct 0.371; rag_post: A (retrieval miss) vs correct 0.690; rag_pre: B (ignored) vs correct 0.592; rag_pre: B1 (repeated prior) vs correct 0.409; rag_pre: A (retrieval miss) vs correct 0.696

### Pre-answer decision out of domain (greedy answers; mean answer 11.4 tokens)

| signal | decided after | val AUROC | test AUROC | OOD AUROC | OOD AURC | 2wikimultihopqa | hotpotqa | nq | sciq |
|---|---|---|---|---|---|---|---|---|---|
| pre (deployed) | prefill | 0.877 [0.863, 0.890] | 0.868 [0.855, 0.878] | 0.645 [0.629, 0.660] | 0.592 | 0.689 | 0.689 | 0.639 | 0.636 |
| entropy@1 | prefill | 0.839 [0.823, 0.853] | 0.838 [0.825, 0.851] | 0.722 [0.708, 0.733] | 0.546 | 0.799 | 0.733 | 0.661 | 0.667 |
| pre+entropy@1 (stack) | prefill | 0.897 [0.885, 0.909] | 0.889 [0.877, 0.899] | 0.709 [0.696, 0.723] | 0.555 | 0.782 | 0.749 | 0.679 | 0.693 |
| late@1 | 1 token(s) | 0.839 [0.824, 0.855] | 0.834 [0.819, 0.848] | 0.579 [0.563, 0.593] | 0.658 | 0.585 | 0.587 | 0.564 | 0.587 |
| late@2 | 2 token(s) | 0.877 [0.864, 0.890] | 0.870 [0.857, 0.882] | 0.607 [0.592, 0.623] | 0.613 | 0.537 | 0.652 | 0.630 | 0.622 |
| late@4 | 4 token(s) | 0.891 [0.879, 0.903] | 0.883 [0.871, 0.895] | 0.631 [0.617, 0.646] | 0.594 | 0.559 | 0.678 | 0.652 | 0.674 |
| pre+late@2+entropy@1 (stack) | 2 token(s) | 0.903 [0.892, 0.914] | 0.897 [0.885, 0.906] | 0.696 [0.682, 0.710] | 0.561 | 0.755 | 0.742 | 0.681 | 0.689 |

Chosen on val: no delay = **pre+entropy@1 (stack)**; within 2 tokens = **pre+late@2+entropy@1 (stack)**.

### Conformal false alarms per dataset (post head, alpha = 0.1; 300 re-splits)

| grouping | test FAR | FAR popqa | FAR triviaqa | gap | recall | OOD FAR | OOD recall | re-split gap | re-split recall | cluster purity |
|---|---|---|---|---|---|---|---|---|---|---|
| marginal | 0.118 | 0.264 | 0.063 | 0.201 | 0.730 | 0.440 | 0.667 | 0.186 | 0.704 | 0.51 |
| pre-risk bins (D51) | 0.108 | 0.143 | 0.095 | 0.048 | 0.443 | 0.365 | 0.462 | 0.058 | 0.447 | 0.76 |
| hidden-state clusters k=4 | 0.111 | 0.133 | 0.103 | 0.031 | 0.600 | 0.406 | 0.610 | 0.022 | 0.588 | 0.96 |
| hidden-state clusters k=8 | 0.099 | 0.124 | 0.090 | 0.034 | 0.525 | 0.434 | 0.625 | 0.033 | 0.558 | 0.90 |

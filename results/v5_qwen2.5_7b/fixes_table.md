### Pre-answer decision out of domain (greedy answers; mean answer 4.3 tokens)

| signal | decided after | val AUROC | test AUROC | OOD AUROC | OOD AURC | 2wikimultihopqa | hotpotqa | nq | sciq |
|---|---|---|---|---|---|---|---|---|---|
| pre (deployed) | prefill | 0.897 [0.885, 0.910] | 0.891 [0.879, 0.903] | 0.799 [0.789, 0.811] | 0.561 | 0.824 | 0.779 | 0.746 | 0.659 |
| entropy@1 | prefill | 0.865 [0.852, 0.879] | 0.868 [0.857, 0.880] | 0.743 [0.732, 0.755] | 0.623 | 0.807 | 0.765 | 0.710 | 0.677 |
| pre+entropy@1 (stack) | prefill | 0.912 [0.902, 0.924] | 0.912 [0.901, 0.922] | 0.819 [0.809, 0.830] | 0.548 | 0.834 | 0.810 | 0.775 | 0.708 |
| late@1 | 1 token(s) | 0.894 [0.881, 0.905] | 0.883 [0.870, 0.894] | 0.746 [0.735, 0.758] | 0.606 | 0.742 | 0.720 | 0.712 | 0.676 |
| late@2 | 2 token(s) | 0.924 [0.915, 0.934] | 0.906 [0.896, 0.917] | 0.778 [0.767, 0.789] | 0.576 | 0.762 | 0.753 | 0.758 | 0.719 |
| late@4 | 4 token(s) | 0.931 [0.922, 0.941] | 0.919 [0.910, 0.929] | 0.802 [0.791, 0.813] | 0.556 | 0.781 | 0.781 | 0.787 | 0.749 |
| pre+late@2+entropy@1 (stack) | 2 token(s) | 0.933 [0.924, 0.942] | 0.924 [0.915, 0.933] | 0.817 [0.807, 0.828] | 0.550 | 0.827 | 0.802 | 0.782 | 0.741 |

Chosen on val: no delay = **pre+entropy@1 (stack)**; within 2 tokens = **pre+late@2+entropy@1 (stack)**.

### Conformal false alarms per dataset (post head, alpha = 0.1; 300 re-splits)

| grouping | test FAR | FAR popqa | FAR triviaqa | gap | recall | OOD FAR | OOD recall | re-split gap | re-split recall | cluster purity |
|---|---|---|---|---|---|---|---|---|---|---|
| marginal | 0.123 | 0.199 | 0.100 | 0.099 | 0.798 | 0.247 | 0.694 | 0.083 | 0.787 | 0.51 |
| pre-risk bins (D51) | 0.090 | 0.053 | 0.100 | 0.048 | 0.433 | 0.261 | 0.389 | 0.025 | 0.458 | 0.76 |
| hidden-state clusters k=4 | 0.102 | 0.094 | 0.104 | 0.010 | 0.669 | 0.259 | 0.662 | 0.033 | 0.706 | 0.85 |
| hidden-state clusters k=8 | 0.098 | 0.098 | 0.098 | 0.000 | 0.643 | 0.205 | 0.605 | 0.027 | 0.653 | 0.87 |

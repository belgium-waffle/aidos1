### Pre-answer decision out of domain (greedy answers; mean answer 4.5 tokens)

| signal | decided after | val AUROC | test AUROC | OOD AUROC | OOD AURC | 2wikimultihopqa | hotpotqa | nq | sciq |
|---|---|---|---|---|---|---|---|---|---|
| pre (deployed) | prefill | 0.905 [0.892, 0.917] | 0.908 [0.898, 0.918] | 0.754 [0.744, 0.765] | 0.508 | 0.719 | 0.773 | 0.730 | 0.704 |
| entropy@1 | prefill | 0.883 [0.869, 0.896] | 0.883 [0.871, 0.895] | 0.739 [0.726, 0.751] | 0.543 | 0.799 | 0.790 | 0.702 | 0.623 |
| pre+entropy@1 (stack) | prefill | 0.919 [0.908, 0.930] | 0.923 [0.914, 0.932] | 0.789 [0.779, 0.799] | 0.492 | 0.792 | 0.810 | 0.753 | 0.718 |
| late@1 | 1 token(s) | 0.889 [0.875, 0.902] | 0.876 [0.863, 0.888] | 0.727 [0.716, 0.738] | 0.538 | 0.760 | 0.686 | 0.684 | 0.673 |
| late@2 | 2 token(s) | 0.915 [0.905, 0.928] | 0.906 [0.896, 0.915] | 0.764 [0.753, 0.775] | 0.507 | 0.792 | 0.742 | 0.707 | 0.708 |
| late@4 | 4 token(s) | 0.931 [0.921, 0.941] | 0.922 [0.913, 0.931] | 0.798 [0.789, 0.809] | 0.476 | 0.805 | 0.789 | 0.747 | 0.775 |
| pre+late@2+entropy@1 (stack) | 2 token(s) | 0.931 [0.920, 0.941] | 0.928 [0.920, 0.937] | 0.800 [0.790, 0.809] | 0.485 | 0.817 | 0.807 | 0.752 | 0.734 |

Chosen on val: no delay = **pre+entropy@1 (stack)**; within 2 tokens = **pre+late@2+entropy@1 (stack)**.

### Conformal false alarms per dataset (post head, alpha = 0.1; 300 re-splits)

| grouping | test FAR | FAR popqa | FAR triviaqa | gap | recall | OOD FAR | OOD recall | re-split gap | re-split recall | cluster purity |
|---|---|---|---|---|---|---|---|---|---|---|
| marginal | 0.125 | 0.261 | 0.083 | 0.178 | 0.819 | 0.209 | 0.675 | 0.169 | 0.796 | 0.51 |
| pre-risk bins (D51) | 0.095 | 0.155 | 0.076 | 0.079 | 0.457 | 0.131 | 0.311 | 0.098 | 0.527 | 0.75 |
| hidden-state clusters k=4 | 0.117 | 0.177 | 0.098 | 0.079 | 0.768 | 0.263 | 0.699 | 0.067 | 0.732 | 0.87 |
| hidden-state clusters k=8 | 0.116 | 0.166 | 0.101 | 0.065 | 0.654 | 0.227 | 0.689 | 0.071 | 0.673 | 0.88 |

### Pre-answer decision out of domain (greedy answers; mean answer 5.2 tokens)

| signal | decided after | val AUROC | test AUROC | OOD AUROC | OOD AURC | 2wikimultihopqa | hotpotqa | nq | sciq |
|---|---|---|---|---|---|---|---|---|---|
| pre (deployed) | prefill | 0.874 [0.861, 0.890] | 0.866 [0.855, 0.879] | 0.743 [0.730, 0.754] | 0.547 | 0.750 | 0.781 | 0.691 | 0.656 |
| entropy@1 | prefill | 0.893 [0.881, 0.907] | 0.884 [0.872, 0.895] | 0.792 [0.781, 0.804] | 0.521 | 0.790 | 0.809 | 0.769 | 0.751 |
| pre+entropy@1 (stack) | prefill | 0.910 [0.898, 0.922] | 0.899 [0.889, 0.910] | 0.800 [0.789, 0.812] | 0.510 | 0.796 | 0.824 | 0.773 | 0.745 |
| late@1 | 1 token(s) | 0.850 [0.836, 0.868] | 0.846 [0.831, 0.859] | 0.680 [0.666, 0.694] | 0.590 | 0.619 | 0.693 | 0.670 | 0.651 |
| late@2 | 2 token(s) | 0.883 [0.869, 0.895] | 0.883 [0.871, 0.894] | 0.696 [0.684, 0.709] | 0.561 | 0.586 | 0.718 | 0.715 | 0.727 |
| late@4 | 4 token(s) | 0.903 [0.892, 0.916] | 0.902 [0.891, 0.911] | 0.712 [0.700, 0.725] | 0.549 | 0.588 | 0.732 | 0.743 | 0.782 |
| pre+late@2+entropy@1 (stack) | 2 token(s) | 0.915 [0.903, 0.926] | 0.908 [0.899, 0.918] | 0.795 [0.785, 0.808] | 0.511 | 0.787 | 0.824 | 0.781 | 0.766 |

Chosen on val: no delay = **pre+entropy@1 (stack)**; within 2 tokens = **pre+late@2+entropy@1 (stack)**.

### Conformal false alarms per dataset (post head, alpha = 0.1; 300 re-splits)

| grouping | test FAR | FAR popqa | FAR triviaqa | gap | recall | OOD FAR | OOD recall | re-split gap | re-split recall | cluster purity |
|---|---|---|---|---|---|---|---|---|---|---|
| marginal | 0.105 | 0.256 | 0.048 | 0.209 | 0.736 | 0.325 | 0.639 | 0.201 | 0.739 | 0.51 |
| pre-risk bins (D51) | 0.096 | 0.151 | 0.075 | 0.076 | 0.498 | 0.350 | 0.467 | 0.089 | 0.505 | 0.75 |
| hidden-state clusters k=4 | 0.088 | 0.127 | 0.073 | 0.054 | 0.646 | 0.392 | 0.684 | 0.064 | 0.651 | 0.83 |
| hidden-state clusters k=8 | 0.100 | 0.146 | 0.083 | 0.063 | 0.650 | 0.397 | 0.702 | 0.049 | 0.646 | 0.89 |

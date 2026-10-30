### Pre-answer decision out of domain (greedy answers; mean answer 4.5 tokens)

| signal | decided after | val AUROC | test AUROC | OOD AUROC | OOD AURC | 2wikimultihopqa | hotpotqa | nq | sciq |
|---|---|---|---|---|---|---|---|---|---|
| pre (deployed) | prefill | 0.863 [0.848, 0.877] | 0.876 [0.862, 0.890] | 0.715 [0.701, 0.727] | 0.483 | 0.621 | 0.697 | 0.660 | 0.692 |
| entropy@1 | prefill | 0.828 [0.811, 0.843] | 0.836 [0.823, 0.850] | 0.753 [0.741, 0.765] | 0.451 | 0.724 | 0.765 | 0.691 | 0.719 |
| pre+entropy@1 (stack) | prefill | 0.885 [0.871, 0.899] | 0.896 [0.884, 0.908] | 0.759 [0.746, 0.770] | 0.454 | 0.704 | 0.753 | 0.696 | 0.738 |
| late@1 | 1 token(s) | 0.843 [0.824, 0.860] | 0.849 [0.835, 0.865] | 0.709 [0.695, 0.721] | 0.483 | 0.623 | 0.673 | 0.643 | 0.686 |
| late@2 | 2 token(s) | 0.866 [0.850, 0.882] | 0.874 [0.861, 0.887] | 0.734 [0.723, 0.746] | 0.468 | 0.662 | 0.711 | 0.668 | 0.722 |
| late@4 | 4 token(s) | 0.876 [0.860, 0.890] | 0.887 [0.875, 0.900] | 0.750 [0.738, 0.761] | 0.455 | 0.689 | 0.730 | 0.682 | 0.763 |
| pre+late@2+entropy@1 (stack) | 2 token(s) | 0.895 [0.880, 0.908] | 0.905 [0.894, 0.916] | 0.772 [0.760, 0.783] | 0.441 | 0.716 | 0.762 | 0.705 | 0.760 |

Chosen on val: no delay = **pre+entropy@1 (stack)**; within 2 tokens = **pre+late@2+entropy@1 (stack)**.

### Conformal false alarms per dataset (post head, alpha = 0.1; 300 re-splits)

| grouping | test FAR | FAR popqa | FAR triviaqa | gap | recall | OOD FAR | OOD recall | re-split gap | re-split recall | cluster purity |
|---|---|---|---|---|---|---|---|---|---|---|
| marginal | 0.102 | 0.241 | 0.035 | 0.206 | 0.692 | 0.203 | 0.572 | 0.207 | 0.689 | 0.51 |
| pre-risk bins (D51) | 0.097 | 0.161 | 0.066 | 0.095 | 0.492 | 0.117 | 0.300 | 0.066 | 0.458 | 0.78 |
| hidden-state clusters k=4 | 0.091 | 0.110 | 0.082 | 0.028 | 0.577 | 0.320 | 0.646 | 0.033 | 0.581 | 0.85 |
| hidden-state clusters k=8 | 0.090 | 0.083 | 0.093 | 0.009 | 0.559 | 0.320 | 0.657 | 0.017 | 0.577 | 0.94 |

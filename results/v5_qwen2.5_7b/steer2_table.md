### Steering along the pre head's direction (added at layer 14, read at layers [14, 18, 21]; shift = f x mean|h| (54.9); cos(probe, meandiff) = 0.10; 600 test questions)

**prompt: allow**

| direction | metric | -0.5 | -0.25 | -0.1 | +0 | +0.1 | +0.25 | +0.5 |
|---|---|---|---|---|---|---|---|---|
| probe | abstention | 0.015 | 0.157 | 0.292 | 0.368 | 0.443 | 0.545 | 0.585 |
| probe | accuracy | 0.355 | 0.365 | 0.367 | 0.348 | 0.330 | 0.280 | 0.252 |
| probe | hallucination | 0.630 | 0.478 | 0.342 | 0.283 | 0.227 | 0.175 | 0.163 |
| probe | selective_accuracy | 0.360 | 0.433 | 0.518 | 0.551 | 0.593 | 0.615 | 0.606 |
| probe | pre_risk_mean | 0.000 | 0.000 | 0.000 | 0.637 | 1.000 | 1.000 | 1.000 |
| probe | changed_vs_alpha0 | 0.577 | 0.368 | 0.152 | 0.000 | 0.128 | 0.248 | 0.372 |
| meandiff | abstention | 0.192 | 0.193 | 0.265 | 0.368 | 0.460 | 0.692 | 0.988 |
| meandiff | accuracy | 0.323 | 0.370 | 0.370 | 0.348 | 0.325 | 0.208 | 0.010 |
| meandiff | hallucination | 0.485 | 0.437 | 0.365 | 0.283 | 0.215 | 0.100 | 0.002 |
| meandiff | selective_accuracy | 0.400 | 0.459 | 0.503 | 0.551 | 0.602 | 0.676 | 0.857 |
| meandiff | pre_risk_mean | 0.007 | 0.225 | 0.485 | 0.637 | 0.771 | 0.922 | 0.996 |
| meandiff | changed_vs_alpha0 | 0.522 | 0.360 | 0.195 | 0.000 | 0.167 | 0.390 | 0.622 |
| random0 | abstention | 0.320 | 0.417 | 0.397 | 0.368 | 0.332 | 0.270 | 0.243 |
| random0 | accuracy | 0.342 | 0.333 | 0.340 | 0.348 | 0.352 | 0.355 | 0.335 |
| random0 | hallucination | 0.338 | 0.250 | 0.263 | 0.283 | 0.317 | 0.375 | 0.422 |
| random0 | selective_accuracy | 0.502 | 0.571 | 0.564 | 0.551 | 0.526 | 0.486 | 0.443 |
| random0 | pre_risk_mean | 0.569 | 0.605 | 0.626 | 0.637 | 0.645 | 0.654 | 0.678 |
| random0 | changed_vs_alpha0 | 0.355 | 0.182 | 0.082 | 0.000 | 0.100 | 0.260 | 0.400 |
| random1 | abstention | 0.167 | 0.282 | 0.332 | 0.368 | 0.412 | 0.477 | 0.710 |
| random1 | accuracy | 0.358 | 0.368 | 0.355 | 0.348 | 0.333 | 0.310 | 0.188 |
| random1 | hallucination | 0.475 | 0.350 | 0.313 | 0.283 | 0.255 | 0.213 | 0.102 |
| random1 | selective_accuracy | 0.430 | 0.513 | 0.531 | 0.551 | 0.567 | 0.592 | 0.649 |
| random1 | pre_risk_mean | 0.544 | 0.611 | 0.631 | 0.637 | 0.636 | 0.629 | 0.674 |
| random1 | changed_vs_alpha0 | 0.448 | 0.235 | 0.097 | 0.000 | 0.100 | 0.228 | 0.428 |
| random2 | abstention | 0.440 | 0.398 | 0.378 | 0.368 | 0.363 | 0.353 | 0.345 |
| random2 | accuracy | 0.310 | 0.333 | 0.343 | 0.348 | 0.350 | 0.357 | 0.353 |
| random2 | hallucination | 0.250 | 0.268 | 0.278 | 0.283 | 0.287 | 0.290 | 0.302 |
| random2 | selective_accuracy | 0.554 | 0.554 | 0.552 | 0.551 | 0.550 | 0.552 | 0.539 |
| random2 | pre_risk_mean | 0.623 | 0.650 | 0.646 | 0.637 | 0.625 | 0.594 | 0.498 |
| random2 | changed_vs_alpha0 | 0.335 | 0.165 | 0.072 | 0.000 | 0.075 | 0.163 | 0.268 |


### Steering along the pre head's direction (added at layer 12, read at layers [12, 16, 20]; shift = f x mean|h| (6.1); cos(probe, meandiff) = 0.14; 600 test questions)

**prompt: allow**

| direction | metric | -0.5 | -0.25 | -0.1 | +0 | +0.1 | +0.25 | +0.5 |
|---|---|---|---|---|---|---|---|---|
| probe | abstention | 0.235 | 0.195 | 0.160 | 0.150 | 0.137 | 0.127 | 0.090 |
| probe | accuracy | 0.433 | 0.450 | 0.455 | 0.457 | 0.468 | 0.468 | 0.467 |
| probe | hallucination | 0.332 | 0.355 | 0.385 | 0.393 | 0.395 | 0.405 | 0.443 |
| probe | selective_accuracy | 0.566 | 0.559 | 0.542 | 0.537 | 0.542 | 0.536 | 0.513 |
| probe | pre_risk_mean | 0.000 | 0.000 | 0.019 | 0.596 | 0.994 | 1.000 | 1.000 |
| probe | changed_vs_alpha0 | 0.353 | 0.230 | 0.137 | 0.000 | 0.135 | 0.303 | 0.523 |
| meandiff | abstention | 0.062 | 0.072 | 0.115 | 0.150 | 0.200 | 0.305 | 0.587 |
| meandiff | accuracy | 0.432 | 0.453 | 0.460 | 0.457 | 0.458 | 0.447 | 0.315 |
| meandiff | hallucination | 0.507 | 0.475 | 0.425 | 0.393 | 0.342 | 0.248 | 0.098 |
| meandiff | selective_accuracy | 0.460 | 0.488 | 0.520 | 0.537 | 0.573 | 0.643 | 0.762 |
| meandiff | pre_risk_mean | 0.060 | 0.266 | 0.456 | 0.596 | 0.731 | 0.887 | 0.986 |
| meandiff | changed_vs_alpha0 | 0.440 | 0.325 | 0.168 | 0.000 | 0.188 | 0.397 | 0.703 |
| random0 | abstention | 0.385 | 0.225 | 0.180 | 0.150 | 0.132 | 0.113 | 0.098 |
| random0 | accuracy | 0.412 | 0.447 | 0.455 | 0.457 | 0.463 | 0.480 | 0.470 |
| random0 | hallucination | 0.203 | 0.328 | 0.365 | 0.393 | 0.405 | 0.407 | 0.432 |
| random0 | selective_accuracy | 0.669 | 0.576 | 0.555 | 0.537 | 0.534 | 0.541 | 0.521 |
| random0 | pre_risk_mean | 0.614 | 0.598 | 0.594 | 0.596 | 0.601 | 0.615 | 0.662 |
| random0 | changed_vs_alpha0 | 0.442 | 0.240 | 0.160 | 0.000 | 0.197 | 0.422 | 0.728 |
| random1 | abstention | 0.268 | 0.192 | 0.165 | 0.150 | 0.143 | 0.140 | 0.150 |
| random1 | accuracy | 0.435 | 0.460 | 0.463 | 0.457 | 0.467 | 0.472 | 0.453 |
| random1 | hallucination | 0.297 | 0.348 | 0.372 | 0.393 | 0.390 | 0.388 | 0.397 |
| random1 | selective_accuracy | 0.595 | 0.569 | 0.555 | 0.537 | 0.545 | 0.548 | 0.533 |
| random1 | pre_risk_mean | 0.644 | 0.608 | 0.597 | 0.596 | 0.599 | 0.613 | 0.656 |
| random1 | changed_vs_alpha0 | 0.370 | 0.268 | 0.153 | 0.000 | 0.197 | 0.437 | 0.668 |
| random2 | abstention | 0.287 | 0.192 | 0.163 | 0.150 | 0.143 | 0.137 | 0.155 |
| random2 | accuracy | 0.438 | 0.460 | 0.457 | 0.457 | 0.457 | 0.465 | 0.467 |
| random2 | hallucination | 0.275 | 0.348 | 0.380 | 0.393 | 0.400 | 0.398 | 0.378 |
| random2 | selective_accuracy | 0.614 | 0.569 | 0.546 | 0.537 | 0.533 | 0.539 | 0.552 |
| random2 | pre_risk_mean | 0.466 | 0.530 | 0.570 | 0.596 | 0.623 | 0.668 | 0.759 |
| random2 | changed_vs_alpha0 | 0.365 | 0.197 | 0.140 | 0.000 | 0.180 | 0.360 | 0.728 |


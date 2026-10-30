### Policies at lam=1.0 (thresholds chosen on val; test split, simulated)

| family | signal | accuracy | hallucination | coverage | retrieval |
|---|---|---|---|---|---|
| vanilla | - | 0.484 | 0.516 | 1.000 | 0.000 |
| oracle-route | - | 0.624 | 0.363 | 0.986 | 0.480 |
| rag-always | - | 0.589 | 0.411 | 1.000 | 1.000 |
| abstain | tripwire | 0.411 | 0.073 | 0.483 | 0.000 |
| rollback+abstain | tripwire | 0.421 | 0.086 | 0.508 | 0.000 |
| route-noretrieve | tripwire | 0.414 | 0.075 | 0.489 | 0.000 |
| route | tripwire | 0.511 | 0.073 | 0.584 | 0.690 |
| retrieve+abstain | tripwire | 0.522 | 0.081 | 0.603 | 0.601 |
| abstain@logprob | logprob | 0.396 | 0.121 | 0.518 | 0.000 |
| route-noretrieve@logprob | logprob | 0.363 | 0.092 | 0.456 | 0.000 |
| route@logprob | logprob | 0.450 | 0.113 | 0.563 | 0.626 |
| abstain@entropy | entropy | 0.438 | 0.146 | 0.584 | 0.000 |
| route-noretrieve@entropy | entropy | 0.414 | 0.129 | 0.543 | 0.000 |
| route@entropy | entropy | 0.451 | 0.112 | 0.563 | 0.625 |
| flare | tripwire | 0.578 | 0.418 | 0.996 | 0.689 |
| flare+abstain | tripwire | 0.437 | 0.100 | 0.536 | 0.622 |
| dragin | tripwire | 0.590 | 0.408 | 0.997 | 0.687 |
| dragin+abstain | tripwire | 0.490 | 0.151 | 0.642 | 0.494 |

### accuracy / hallucination per lam (test, simulated)

| family | lam=0.1 | lam=0.25 | lam=0.5 | lam=1.0 | lam=2.0 | lam=4.0 |
|---|---|---|---|---|---|---|
| abstain | 0.479 / 0.294 | 0.455 / 0.153 | 0.436 / 0.111 | 0.411 / 0.073 | 0.356 / 0.038 | 0.284 / 0.020 |
| route | 0.589 / 0.263 | 0.584 / 0.214 | 0.559 / 0.144 | 0.511 / 0.073 | 0.449 / 0.042 | 0.404 / 0.031 |
| abstain@logprob | 0.473 / 0.294 | 0.457 / 0.210 | 0.440 / 0.174 | 0.396 / 0.121 | 0.309 / 0.044 | 0.250 / 0.025 |
| route@logprob | 0.581 / 0.392 | 0.561 / 0.298 | 0.553 / 0.273 | 0.450 / 0.113 | 0.333 / 0.054 | 0.292 / 0.037 |
| abstain@entropy | 0.474 / 0.298 | 0.462 / 0.212 | 0.449 / 0.169 | 0.438 / 0.146 | 0.310 / 0.045 | 0.241 / 0.021 |
| route@entropy | 0.583 / 0.389 | 0.563 / 0.274 | 0.562 / 0.272 | 0.451 / 0.112 | 0.372 / 0.062 | 0.256 / 0.030 |
| flare | 0.578 / 0.418 | 0.578 / 0.418 | 0.578 / 0.418 | 0.578 / 0.418 | 0.578 / 0.418 | 0.578 / 0.418 |
| flare+abstain | 0.578 / 0.418 | 0.566 / 0.318 | 0.486 / 0.176 | 0.437 / 0.100 | 0.412 / 0.084 | 0.282 / 0.034 |
| dragin | 0.590 / 0.408 | 0.590 / 0.408 | 0.590 / 0.408 | 0.590 / 0.408 | 0.590 / 0.408 | 0.590 / 0.408 |
| dragin+abstain | 0.589 / 0.387 | 0.578 / 0.315 | 0.518 / 0.212 | 0.490 / 0.151 | 0.419 / 0.082 | 0.284 / 0.035 |

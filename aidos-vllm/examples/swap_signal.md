# Swapping the signal without code changes

The engine scores whatever linear heads are in the bundle directory (head_<kind>.pt, the
`aidos-head-v1` format: weights per layer, standardisation and Platt scaling, folded at load
time). To try a different signal, copy the bundle and replace a head file, for example `head_pre.pt`
with a probe trained on your own labels or a different target (the paper's companion analysis uses
fixability probes this way). Nothing in the engine changes; run
`aidos verify` after any change to confirm the mechanics still match recomputation.

### Headline: route-eu minus each baseline, TEST (Holm over 12 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_qwen2.5_7b | 1|flare+abstain | 3878 | +0.235 [+0.216, +0.255] | 0.0001 | 0.0012 | +0.233 | -0.002 | -0.00 |
| sealed_v5_qwen2.5_7b | 1|dragin+abstain | 3878 | +0.194 [+0.174, +0.215] | 0.0001 | 0.0012 | +0.042 | -0.152 | -0.00 |
| sealed_v5_qwen2.5_7b | 1|probing-rag+abstain | 3878 | +0.186 [+0.166, +0.206] | 0.0001 | 0.0012 | +0.091 | -0.096 | +0.00 |
| sealed_v5_qwen2.5_7b | 1|se-rag+abstain | 3878 | +0.177 [+0.156, +0.199] | 0.0001 | 0.0012 | +0.010 | -0.169 | +0.07 |
| sealed_v5_qwen2.5_7b | 2|flare+abstain | 3878 | +0.234 [+0.210, +0.259] | 0.0001 | 0.0012 | +0.170 | -0.032 | -0.00 |
| sealed_v5_qwen2.5_7b | 2|dragin+abstain | 3878 | +0.235 [+0.210, +0.261] | 0.0001 | 0.0012 | +0.171 | -0.032 | -0.00 |
| sealed_v5_qwen2.5_7b | 2|probing-rag+abstain | 3878 | +0.213 [+0.188, +0.237] | 0.0001 | 0.0012 | +0.161 | -0.026 | +0.00 |
| sealed_v5_qwen2.5_7b | 2|se-rag+abstain | 3878 | +0.230 [+0.203, +0.257] | 0.0001 | 0.0012 | +0.124 | -0.054 | +0.06 |
| sealed_v5_qwen2.5_7b | 4|flare+abstain | 3878 | +0.254 [+0.230, +0.276] | 0.0001 | 0.0012 | +0.315 | +0.017 | -0.34 |
| sealed_v5_qwen2.5_7b | 4|dragin+abstain | 3878 | +0.254 [+0.231, +0.276] | 0.0001 | 0.0012 | +0.315 | +0.017 | -0.34 |
| sealed_v5_qwen2.5_7b | 4|probing-rag+abstain | 3878 | +0.286 [+0.249, +0.323] | 0.0001 | 0.0012 | +0.082 | -0.051 | -0.04 |
| sealed_v5_qwen2.5_7b | 4|se-rag+abstain | 3878 | +0.254 [+0.230, +0.276] | 0.0001 | 0.0012 | +0.315 | +0.017 | -0.34 |

### route-eu minus the unmodified baselines, TEST (Holm over 12 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_qwen2.5_7b | 1|flare | 3878 | +0.317 [+0.294, +0.341] | 0.0001 | 0.0012 | -0.081 | -0.392 | -0.30 |
| sealed_v5_qwen2.5_7b | 1|dragin | 3878 | +0.279 [+0.257, +0.302] | 0.0001 | 0.0012 | -0.097 | -0.376 | -0.00 |
| sealed_v5_qwen2.5_7b | 1|probing-rag | 3878 | +0.277 [+0.256, +0.298] | 0.0001 | 0.0012 | -0.101 | -0.372 | -0.30 |
| sealed_v5_qwen2.5_7b | 1|se-rag | 3878 | +0.269 [+0.246, +0.292] | 0.0001 | 0.0012 | -0.101 | -0.372 | +0.07 |
| sealed_v5_qwen2.5_7b | 2|flare | 3878 | +0.705 [+0.666, +0.745] | 0.0001 | 0.0012 | -0.143 | -0.421 | -0.30 |
| sealed_v5_qwen2.5_7b | 2|dragin | 3878 | +0.651 [+0.614, +0.690] | 0.0001 | 0.0012 | -0.159 | -0.405 | -0.00 |
| sealed_v5_qwen2.5_7b | 2|probing-rag | 3878 | +0.645 [+0.608, +0.683] | 0.0001 | 0.0012 | -0.163 | -0.401 | -0.30 |
| sealed_v5_qwen2.5_7b | 2|se-rag | 3878 | +0.637 [+0.597, +0.676] | 0.0001 | 0.0012 | -0.164 | -0.401 | +0.06 |
| sealed_v5_qwen2.5_7b | 4|flare | 3878 | +1.569 [+1.499, +1.644] | 0.0001 | 0.0012 | -0.222 | -0.446 | -0.34 |
| sealed_v5_qwen2.5_7b | 4|dragin | 3878 | +1.483 [+1.413, +1.556] | 0.0001 | 0.0012 | -0.238 | -0.430 | -0.04 |
| sealed_v5_qwen2.5_7b | 4|probing-rag | 3878 | +1.469 [+1.397, +1.540] | 0.0001 | 0.0012 | -0.242 | -0.426 | -0.34 |
| sealed_v5_qwen2.5_7b | 4|se-rag | 3878 | +1.469 [+1.397, +1.538] | 0.0001 | 0.0012 | -0.242 | -0.426 | -0.34 |

### Ablations (full minus ablated), TEST, policy lam (Holm over 10 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_qwen2.5_7b | probe heads -> token logprob | 3878 | +0.199 [+0.177, +0.220] | 0.0001 | 0.0010 | +0.044 | -0.155 | +0.04 |
| sealed_v5_qwen2.5_7b | probe heads -> top-k entropy | 3878 | +0.192 [+0.172, +0.212] | 0.0001 | 0.0010 | +0.046 | -0.147 | +0.04 |
| sealed_v5_qwen2.5_7b | evidence heads -> closed-book heads after retrieval | 3878 | +0.059 [+0.044, +0.074] | 0.0001 | 0.0010 | -0.013 | -0.073 | +0.05 |
| sealed_v5_qwen2.5_7b | retrieval -> none (abstain only) | 3878 | +0.158 [+0.138, +0.178] | 0.0001 | 0.0010 | +0.157 | -0.015 | +0.70 |
| sealed_v5_qwen2.5_7b | routing -> always retrieve (same heads) | 3878 | +0.012 [+0.003, +0.022] | 0.0123 | 0.0615 | -0.006 | -0.012 | -0.30 |
| sealed_v5_qwen2.5_7b | option-value signal -> help head | 3878 | +0.013 [+0.005, +0.020] | 0.0016 | 0.0096 | +0.029 | +0.012 | +0.20 |
| sealed_v5_qwen2.5_7b | EU rule -> tuned thresholds | 3878 | +0.003 [-0.008, +0.014] | 0.5984 | 0.5984 | -0.020 | -0.021 | -0.07 |
| sealed_v5_qwen2.5_7b | rollback / resample -> none | 3878 | -0.005 [-0.012, +0.002] | 0.1396 | 0.4188 | +0.000 | +0.005 | +0.00 |
| sealed_v5_qwen2.5_7b | drift (resample) branch -> none | 3878 | -0.002 [-0.005, +0.001] | 0.2076 | 0.4188 | -0.001 | +0.001 | -0.00 |
| sealed_v5_qwen2.5_7b | second retrieval attempt -> one | 3878 | -0.004 [-0.009, +0.000] | 0.0605 | 0.2420 | +0.011 | +0.010 | +0.29 |

### Per in-domain dataset, lam = policy lam (Holm over 10 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_qwen2.5_7b | test|popqa|flare+abstain | 1996 | +0.174 [+0.152, +0.198] | 0.0001 | 0.0010 | +0.148 | -0.022 | -0.23 |
| sealed_v5_qwen2.5_7b | test|popqa|dragin+abstain | 1996 | +0.255 [+0.226, +0.283] | 0.0001 | 0.0010 | -0.019 | -0.270 | -0.23 |
| sealed_v5_qwen2.5_7b | test|popqa|probing-rag+abstain | 1996 | +0.184 [+0.159, +0.209] | 0.0001 | 0.0010 | +0.038 | -0.140 | -0.31 |
| sealed_v5_qwen2.5_7b | test|popqa|se-rag+abstain | 1996 | +0.262 [+0.234, +0.291] | 0.0001 | 0.0010 | -0.028 | -0.286 | -0.19 |
| sealed_v5_qwen2.5_7b | test|popqa|rag+abstain | 1996 | +0.012 [-0.000, +0.023] | 0.0519 | 0.1038 | -0.011 | -0.014 | -0.40 |
| sealed_v5_qwen2.5_7b | test|triviaqa|flare+abstain | 1882 | +0.300 [+0.269, +0.331] | 0.0001 | 0.0010 | +0.324 | +0.019 | +0.24 |
| sealed_v5_qwen2.5_7b | test|triviaqa|dragin+abstain | 1882 | +0.130 [+0.101, +0.159] | 0.0001 | 0.0010 | +0.107 | -0.028 | +0.24 |
| sealed_v5_qwen2.5_7b | test|triviaqa|probing-rag+abstain | 1882 | +0.188 [+0.158, +0.218] | 0.0001 | 0.0010 | +0.146 | -0.049 | +0.33 |
| sealed_v5_qwen2.5_7b | test|triviaqa|se-rag+abstain | 1882 | +0.087 [+0.056, +0.118] | 0.0001 | 0.0010 | +0.049 | -0.045 | +0.34 |
| sealed_v5_qwen2.5_7b | test|triviaqa|rag+abstain | 1882 | +0.013 [-0.003, +0.028] | 0.1030 | 0.1038 | -0.002 | -0.011 | -0.19 |

### Per OOD dataset (no selection guarantee), lam = policy lam (Holm over 15 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_qwen2.5_7b | ood|2wikimultihopqa|flare+abstain | 998 | -0.050 [-0.091, -0.010] | 0.0127 | 0.0635 | -0.157 | -0.111 | +0.21 |
| sealed_v5_qwen2.5_7b | ood|2wikimultihopqa|dragin+abstain | 998 | +0.057 [+0.012, +0.105] | 0.0127 | 0.0635 | -0.201 | -0.264 | +0.24 |
| sealed_v5_qwen2.5_7b | ood|2wikimultihopqa|probing-rag+abstain | 998 | -0.051 [-0.089, -0.012] | 0.0080 | 0.0518 | -0.148 | -0.099 | +0.09 |
| sealed_v5_qwen2.5_7b | ood|2wikimultihopqa|se-rag+abstain | 998 | +0.068 [+0.019, +0.116] | 0.0074 | 0.0518 | -0.234 | -0.310 | +0.34 |
| sealed_v5_qwen2.5_7b | ood|2wikimultihopqa|rag+abstain | 998 | +0.024 [+0.011, +0.038] | 0.0005 | 0.0045 | +0.003 | -0.018 | -0.15 |
| sealed_v5_qwen2.5_7b | ood|hotpotqa|flare+abstain | 1000 | +0.073 [+0.030, +0.117] | 0.0006 | 0.0048 | +0.129 | +0.052 | +0.21 |
| sealed_v5_qwen2.5_7b | ood|hotpotqa|dragin+abstain | 1000 | +0.118 [+0.074, +0.162] | 0.0001 | 0.0015 | +0.002 | -0.120 | +0.21 |
| sealed_v5_qwen2.5_7b | ood|hotpotqa|probing-rag+abstain | 1000 | +0.008 [-0.032, +0.048] | 0.7360 | 1.0000 | +0.044 | +0.034 | +0.12 |
| sealed_v5_qwen2.5_7b | ood|hotpotqa|se-rag+abstain | 1000 | +0.133 [+0.090, +0.176] | 0.0001 | 0.0015 | -0.006 | -0.144 | +0.27 |
| sealed_v5_qwen2.5_7b | ood|hotpotqa|rag+abstain | 1000 | +0.019 [+0.001, +0.037] | 0.0399 | 0.1197 | +0.003 | -0.015 | -0.05 |
| sealed_v5_qwen2.5_7b | ood|nq|flare+abstain | 999 | +0.145 [+0.102, +0.188] | 0.0001 | 0.0015 | +0.141 | -0.007 | +0.13 |
| sealed_v5_qwen2.5_7b | ood|nq|dragin+abstain | 999 | +0.145 [+0.102, +0.188] | 0.0001 | 0.0015 | -0.028 | -0.176 | +0.14 |
| sealed_v5_qwen2.5_7b | ood|nq|probing-rag+abstain | 999 | +0.100 [+0.060, +0.138] | 0.0001 | 0.0015 | +0.011 | -0.091 | +0.09 |
| sealed_v5_qwen2.5_7b | ood|nq|se-rag+abstain | 999 | +0.165 [+0.121, +0.210] | 0.0001 | 0.0015 | -0.040 | -0.209 | +0.19 |
| sealed_v5_qwen2.5_7b | ood|nq|rag+abstain | 999 | -0.005 [-0.026, +0.016] | 0.7018 | 1.0000 | -0.008 | -0.001 | -0.12 |

### Re-simulation check and detector seeds

| model | max deviation from policy.json | pre AUROC (seeds mean +- std) | post AUROC (seeds mean +- std) |
|---|---|---|---|
| sealed_v5_qwen2.5_7b | sealed (frozen from v5_qwen2.5_7b) | 0.8985 +- 0.0018 | 0.9240 +- 0.0005 |

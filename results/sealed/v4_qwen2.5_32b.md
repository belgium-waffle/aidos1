### Headline: route-eu minus each baseline, TEST (Holm over 12 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v4_qwen2.5_32b | 1|flare+abstain | 3880 | +0.161 [+0.142, +0.179] | 0.0001 | 0.0012 | +0.119 | -0.043 | +0.02 |
| sealed_v4_qwen2.5_32b | 1|dragin+abstain | 3880 | +0.145 [+0.127, +0.163] | 0.0001 | 0.0012 | +0.088 | -0.059 | +0.09 |
| sealed_v4_qwen2.5_32b | 1|probing-rag+abstain | 3880 | +0.118 [+0.101, +0.134] | 0.0001 | 0.0012 | +0.069 | -0.050 | +0.09 |
| sealed_v4_qwen2.5_32b | 1|se-rag+abstain | 3880 | +0.111 [+0.094, +0.129] | 0.0001 | 0.0012 | +0.043 | -0.072 | +0.16 |
| sealed_v4_qwen2.5_32b | 2|flare+abstain | 3880 | +0.201 [+0.174, +0.227] | 0.0001 | 0.0012 | +0.068 | -0.067 | +0.04 |
| sealed_v4_qwen2.5_32b | 2|dragin+abstain | 3880 | +0.189 [+0.164, +0.215] | 0.0001 | 0.0012 | +0.059 | -0.065 | +0.04 |
| sealed_v4_qwen2.5_32b | 2|probing-rag+abstain | 3880 | +0.160 [+0.136, +0.184] | 0.0001 | 0.0012 | +0.038 | -0.062 | +0.05 |
| sealed_v4_qwen2.5_32b | 2|se-rag+abstain | 3880 | +0.180 [+0.154, +0.207] | 0.0001 | 0.0012 | -0.009 | -0.096 | +0.18 |
| sealed_v4_qwen2.5_32b | 4|flare+abstain | 3880 | +0.205 [+0.172, +0.239] | 0.0001 | 0.0012 | +0.168 | -0.010 | +0.03 |
| sealed_v4_qwen2.5_32b | 4|dragin+abstain | 3880 | +0.206 [+0.172, +0.240] | 0.0001 | 0.0012 | +0.160 | -0.012 | +0.03 |
| sealed_v4_qwen2.5_32b | 4|probing-rag+abstain | 3880 | +0.157 [+0.129, +0.185] | 0.0001 | 0.0012 | +0.142 | -0.004 | +0.04 |
| sealed_v4_qwen2.5_32b | 4|se-rag+abstain | 3880 | +0.238 [+0.199, +0.278] | 0.0001 | 0.0012 | +0.056 | -0.046 | +0.17 |

### route-eu minus the unmodified baselines, TEST (Holm over 12 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v4_qwen2.5_32b | 1|flare | 3880 | +0.285 [+0.262, +0.306] | 0.0001 | 0.0012 | -0.040 | -0.325 | +0.02 |
| sealed_v4_qwen2.5_32b | 1|dragin | 3880 | +0.245 [+0.225, +0.264] | 0.0001 | 0.0012 | -0.060 | -0.305 | +0.02 |
| sealed_v4_qwen2.5_32b | 1|probing-rag | 3880 | +0.245 [+0.226, +0.263] | 0.0001 | 0.0012 | -0.064 | -0.303 | -0.28 |
| sealed_v4_qwen2.5_32b | 1|se-rag | 3880 | +0.245 [+0.226, +0.263] | 0.0001 | 0.0012 | -0.064 | -0.303 | -0.28 |
| sealed_v4_qwen2.5_32b | 2|flare | 3880 | +0.607 [+0.570, +0.645] | 0.0001 | 0.0012 | -0.091 | -0.350 | +0.04 |
| sealed_v4_qwen2.5_32b | 2|dragin | 3880 | +0.547 [+0.511, +0.583] | 0.0001 | 0.0012 | -0.112 | -0.330 | +0.04 |
| sealed_v4_qwen2.5_32b | 2|probing-rag | 3880 | +0.545 [+0.512, +0.580] | 0.0001 | 0.0012 | -0.115 | -0.327 | -0.25 |
| sealed_v4_qwen2.5_32b | 2|se-rag | 3880 | +0.545 [+0.510, +0.579] | 0.0001 | 0.0012 | -0.115 | -0.327 | -0.25 |
| sealed_v4_qwen2.5_32b | 4|flare | 3880 | +1.320 [+1.250, +1.389] | 0.0001 | 0.0012 | -0.170 | -0.373 | +0.03 |
| sealed_v4_qwen2.5_32b | 4|dragin | 3880 | +1.220 [+1.154, +1.287] | 0.0001 | 0.0012 | -0.190 | -0.353 | +0.03 |
| sealed_v4_qwen2.5_32b | 4|probing-rag | 3880 | +1.213 [+1.148, +1.280] | 0.0001 | 0.0012 | -0.194 | -0.350 | -0.27 |
| sealed_v4_qwen2.5_32b | 4|se-rag | 3880 | +1.213 [+1.147, +1.281] | 0.0001 | 0.0012 | -0.194 | -0.350 | -0.27 |

### Ablations (full minus ablated), TEST, policy lam (Holm over 10 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v4_qwen2.5_32b | probe heads -> token logprob | 3880 | +0.140 [+0.122, +0.158] | 0.0001 | 0.0010 | +0.088 | -0.052 | +0.03 |
| sealed_v4_qwen2.5_32b | probe heads -> top-k entropy | 3880 | +0.136 [+0.119, +0.154] | 0.0001 | 0.0010 | +0.087 | -0.050 | +0.02 |
| sealed_v4_qwen2.5_32b | evidence heads -> closed-book heads after retrieval | 3880 | +0.040 [+0.029, +0.051] | 0.0001 | 0.0010 | +0.004 | -0.036 | +0.00 |
| sealed_v4_qwen2.5_32b | retrieval -> none (abstain only) | 3880 | +0.144 [+0.125, +0.162] | 0.0001 | 0.0010 | +0.151 | -0.007 | +0.72 |
| sealed_v4_qwen2.5_32b | routing -> always retrieve (same heads) | 3880 | +0.019 [+0.009, +0.029] | 0.0001 | 0.0010 | -0.023 | -0.037 | -0.28 |
| sealed_v4_qwen2.5_32b | option-value signal -> help head | 3880 | +0.015 [+0.007, +0.024] | 0.0003 | 0.0015 | +0.033 | +0.014 | +0.21 |
| sealed_v4_qwen2.5_32b | EU rule -> tuned thresholds | 3880 | +0.002 [-0.006, +0.010] | 0.6556 | 1.0000 | -0.014 | -0.016 | +0.02 |
| sealed_v4_qwen2.5_32b | rollback / resample -> none | 3880 | -0.005 [-0.010, -0.000] | 0.0527 | 0.1581 | +0.006 | +0.011 | +0.00 |
| sealed_v4_qwen2.5_32b | drift (resample) branch -> none | 3880 | -0.005 [-0.009, -0.002] | 0.0043 | 0.0172 | -0.002 | +0.003 | -0.01 |
| sealed_v4_qwen2.5_32b | second retrieval attempt -> one | 3880 | -0.001 [-0.007, +0.005] | 0.7054 | 1.0000 | +0.016 | +0.012 | +0.28 |

### Per in-domain dataset, lam = policy lam (Holm over 10 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v4_qwen2.5_32b | test|popqa|flare+abstain | 1998 | +0.189 [+0.163, +0.215] | 0.0001 | 0.0010 | +0.075 | -0.113 | -0.09 |
| sealed_v4_qwen2.5_32b | test|popqa|dragin+abstain | 1998 | +0.179 [+0.153, +0.204] | 0.0001 | 0.0010 | +0.044 | -0.134 | -0.04 |
| sealed_v4_qwen2.5_32b | test|popqa|probing-rag+abstain | 1998 | +0.152 [+0.129, +0.175] | 0.0001 | 0.0010 | +0.051 | -0.099 | -0.11 |
| sealed_v4_qwen2.5_32b | test|popqa|se-rag+abstain | 1998 | +0.169 [+0.143, +0.193] | 0.0001 | 0.0010 | +0.029 | -0.140 | -0.02 |
| sealed_v4_qwen2.5_32b | test|popqa|rag+abstain | 1998 | +0.024 [+0.010, +0.038] | 0.0008 | 0.0016 | -0.028 | -0.047 | -0.26 |
| sealed_v4_qwen2.5_32b | test|triviaqa|flare+abstain | 1882 | +0.131 [+0.103, +0.158] | 0.0001 | 0.0010 | +0.166 | +0.032 | +0.14 |
| sealed_v4_qwen2.5_32b | test|triviaqa|dragin+abstain | 1882 | +0.109 [+0.084, +0.135] | 0.0001 | 0.0010 | +0.135 | +0.022 | +0.22 |
| sealed_v4_qwen2.5_32b | test|triviaqa|probing-rag+abstain | 1882 | +0.082 [+0.058, +0.105] | 0.0001 | 0.0010 | +0.089 | +0.001 | +0.30 |
| sealed_v4_qwen2.5_32b | test|triviaqa|se-rag+abstain | 1882 | +0.050 [+0.026, +0.074] | 0.0001 | 0.0010 | +0.057 | +0.000 | +0.35 |
| sealed_v4_qwen2.5_32b | test|triviaqa|rag+abstain | 1882 | +0.015 [-0.000, +0.029] | 0.0495 | 0.0495 | -0.018 | -0.027 | -0.30 |

### Per OOD dataset (no selection guarantee), lam = policy lam (Holm over 15 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v4_qwen2.5_32b | ood|2wikimultihopqa|flare+abstain | 998 | +0.036 [-0.003, +0.078] | 0.0792 | 0.7037 | -0.042 | -0.082 | +0.21 |
| sealed_v4_qwen2.5_32b | ood|2wikimultihopqa|dragin+abstain | 998 | +0.028 [-0.013, +0.068] | 0.1937 | 0.7037 | -0.074 | -0.108 | +0.32 |
| sealed_v4_qwen2.5_32b | ood|2wikimultihopqa|probing-rag+abstain | 998 | -0.012 [-0.042, +0.018] | 0.4471 | 0.7037 | -0.012 | -0.001 | +0.04 |
| sealed_v4_qwen2.5_32b | ood|2wikimultihopqa|se-rag+abstain | 998 | +0.044 [-0.004, +0.092] | 0.0782 | 0.7037 | -0.120 | -0.173 | +0.46 |
| sealed_v4_qwen2.5_32b | ood|2wikimultihopqa|rag+abstain | 998 | +0.014 [-0.004, +0.032] | 0.0869 | 0.7037 | -0.031 | -0.045 | -0.01 |
| sealed_v4_qwen2.5_32b | ood|hotpotqa|flare+abstain | 999 | +0.038 [-0.005, +0.080] | 0.0797 | 0.7037 | +0.073 | +0.032 | +0.17 |
| sealed_v4_qwen2.5_32b | ood|hotpotqa|dragin+abstain | 999 | +0.035 [-0.008, +0.079] | 0.1141 | 0.7037 | +0.058 | +0.019 | +0.23 |
| sealed_v4_qwen2.5_32b | ood|hotpotqa|probing-rag+abstain | 999 | +0.031 [-0.008, +0.071] | 0.1296 | 0.7037 | +0.068 | +0.034 | +0.17 |
| sealed_v4_qwen2.5_32b | ood|hotpotqa|se-rag+abstain | 999 | +0.069 [+0.026, +0.112] | 0.0017 | 0.0187 | +0.057 | -0.018 | +0.28 |
| sealed_v4_qwen2.5_32b | ood|hotpotqa|rag+abstain | 999 | +0.034 [+0.013, +0.056] | 0.0022 | 0.0220 | -0.030 | -0.063 | -0.06 |
| sealed_v4_qwen2.5_32b | ood|nq|flare+abstain | 999 | +0.082 [+0.042, +0.122] | 0.0002 | 0.0028 | +0.034 | -0.051 | +0.17 |
| sealed_v4_qwen2.5_32b | ood|nq|dragin+abstain | 999 | +0.069 [+0.030, +0.109] | 0.0002 | 0.0028 | +0.006 | -0.068 | +0.25 |
| sealed_v4_qwen2.5_32b | ood|nq|probing-rag+abstain | 999 | +0.076 [+0.040, +0.114] | 0.0001 | 0.0015 | +0.038 | -0.041 | +0.14 |
| sealed_v4_qwen2.5_32b | ood|nq|se-rag+abstain | 999 | +0.076 [+0.036, +0.117] | 0.0004 | 0.0048 | -0.006 | -0.088 | +0.29 |
| sealed_v4_qwen2.5_32b | ood|nq|rag+abstain | 999 | +0.019 [-0.005, +0.045] | 0.1086 | 0.7037 | -0.034 | -0.051 | -0.12 |

### Re-simulation check and detector seeds

| model | max deviation from policy.json | pre AUROC (seeds mean +- std) | post AUROC (seeds mean +- std) |
|---|---|---|---|
| sealed_v4_qwen2.5_32b | sealed (frozen from v4_qwen2.5_32b) | 0.9034 +- 0.0007 | 0.9259 +- 0.0018 |

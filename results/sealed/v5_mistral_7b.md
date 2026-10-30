### Headline: route-eu minus each baseline, TEST (Holm over 12 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_mistral_7b | 1|flare+abstain | 3882 | +0.193 [+0.171, +0.214] | 0.0001 | 0.0012 | +0.117 | -0.076 | +0.06 |
| sealed_v5_mistral_7b | 1|dragin+abstain | 3882 | +0.164 [+0.143, +0.185] | 0.0001 | 0.0012 | +0.073 | -0.092 | +0.06 |
| sealed_v5_mistral_7b | 1|probing-rag+abstain | 3882 | +0.139 [+0.120, +0.158] | 0.0001 | 0.0012 | +0.047 | -0.094 | +0.11 |
| sealed_v5_mistral_7b | 1|se-rag+abstain | 3882 | +0.149 [+0.129, +0.169] | 0.0001 | 0.0012 | +0.073 | -0.077 | +0.04 |
| sealed_v5_mistral_7b | 2|flare+abstain | 3882 | +0.182 [+0.156, +0.208] | 0.0001 | 0.0012 | +0.149 | -0.015 | -0.11 |
| sealed_v5_mistral_7b | 2|dragin+abstain | 3882 | +0.180 [+0.155, +0.205] | 0.0001 | 0.0012 | +0.143 | -0.017 | -0.10 |
| sealed_v5_mistral_7b | 2|probing-rag+abstain | 3882 | +0.132 [+0.109, +0.154] | 0.0001 | 0.0012 | +0.128 | -0.001 | -0.10 |
| sealed_v5_mistral_7b | 2|se-rag+abstain | 3882 | +0.170 [+0.145, +0.195] | 0.0001 | 0.0012 | +0.138 | -0.015 | -0.10 |
| sealed_v5_mistral_7b | 4|flare+abstain | 3882 | +0.206 [+0.181, +0.230] | 0.0001 | 0.0012 | +0.288 | +0.022 | -0.36 |
| sealed_v5_mistral_7b | 4|dragin+abstain | 3882 | +0.216 [+0.177, +0.254] | 0.0001 | 0.0012 | +0.046 | -0.042 | -0.05 |
| sealed_v5_mistral_7b | 4|probing-rag+abstain | 3882 | +0.134 [+0.102, +0.166] | 0.0001 | 0.0012 | +0.030 | -0.026 | -0.05 |
| sealed_v5_mistral_7b | 4|se-rag+abstain | 3882 | +0.200 [+0.164, +0.237] | 0.0001 | 0.0012 | +0.041 | -0.040 | -0.05 |

### route-eu minus the unmodified baselines, TEST (Holm over 12 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_mistral_7b | 1|flare | 3882 | +0.268 [+0.244, +0.292] | 0.0001 | 0.0012 | -0.086 | -0.348 | -0.32 |
| sealed_v5_mistral_7b | 1|dragin | 3882 | +0.246 [+0.221, +0.269] | 0.0001 | 0.0012 | -0.094 | -0.340 | -0.01 |
| sealed_v5_mistral_7b | 1|probing-rag | 3882 | +0.238 [+0.216, +0.259] | 0.0001 | 0.0012 | -0.098 | -0.336 | -0.01 |
| sealed_v5_mistral_7b | 1|se-rag | 3882 | +0.229 [+0.206, +0.252] | 0.0001 | 0.0012 | -0.103 | -0.331 | -0.01 |
| sealed_v5_mistral_7b | 2|flare | 3882 | +0.610 [+0.569, +0.651] | 0.0001 | 0.0012 | -0.177 | -0.389 | -0.41 |
| sealed_v5_mistral_7b | 2|dragin | 3882 | +0.579 [+0.539, +0.619] | 0.0001 | 0.0012 | -0.185 | -0.381 | -0.10 |
| sealed_v5_mistral_7b | 2|probing-rag | 3882 | +0.568 [+0.528, +0.607] | 0.0001 | 0.0012 | -0.189 | -0.377 | -0.10 |
| sealed_v5_mistral_7b | 2|se-rag | 3882 | +0.554 [+0.514, +0.593] | 0.0001 | 0.0012 | -0.194 | -0.373 | -0.10 |
| sealed_v5_mistral_7b | 4|flare | 3882 | +1.390 [+1.317, +1.467] | 0.0001 | 0.0012 | -0.275 | -0.414 | -0.36 |
| sealed_v5_mistral_7b | 4|dragin | 3882 | +1.343 [+1.271, +1.415] | 0.0001 | 0.0012 | -0.283 | -0.406 | -0.05 |
| sealed_v5_mistral_7b | 4|probing-rag | 3882 | +1.324 [+1.252, +1.398] | 0.0001 | 0.0012 | -0.287 | -0.402 | -0.05 |
| sealed_v5_mistral_7b | 4|se-rag | 3882 | +1.300 [+1.228, +1.371] | 0.0001 | 0.0012 | -0.292 | -0.398 | -0.05 |

### Ablations (full minus ablated), TEST, policy lam (Holm over 10 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_mistral_7b | probe heads -> token logprob | 3882 | +0.155 [+0.135, +0.175] | 0.0001 | 0.0010 | +0.055 | -0.100 | +0.02 |
| sealed_v5_mistral_7b | probe heads -> top-k entropy | 3882 | +0.132 [+0.113, +0.152] | 0.0001 | 0.0010 | +0.019 | -0.113 | +0.00 |
| sealed_v5_mistral_7b | evidence heads -> closed-book heads after retrieval | 3882 | +0.036 [+0.024, +0.048] | 0.0001 | 0.0010 | +0.053 | +0.017 | +0.00 |
| sealed_v5_mistral_7b | retrieval -> none (abstain only) | 3882 | +0.107 [+0.087, +0.127] | 0.0001 | 0.0010 | +0.100 | -0.021 | +0.68 |
| sealed_v5_mistral_7b | routing -> always retrieve (same heads) | 3882 | +0.017 [+0.003, +0.030] | 0.0142 | 0.0568 | -0.039 | -0.050 | -0.32 |
| sealed_v5_mistral_7b | option-value signal -> help head | 3882 | +0.020 [+0.012, +0.028] | 0.0001 | 0.0010 | +0.032 | +0.009 | +0.20 |
| sealed_v5_mistral_7b | EU rule -> tuned thresholds | 3882 | +0.008 [-0.005, +0.023] | 0.2453 | 0.4977 | -0.046 | -0.053 | -0.06 |
| sealed_v5_mistral_7b | rollback / resample -> none | 3882 | -0.010 [-0.016, -0.004] | 0.0043 | 0.0215 | +0.016 | +0.026 | +0.00 |
| sealed_v5_mistral_7b | drift (resample) branch -> none | 3882 | +0.003 [-0.005, +0.011] | 0.4290 | 0.4977 | +0.002 | -0.001 | -0.01 |
| sealed_v5_mistral_7b | second retrieval attempt -> one | 3882 | -0.003 [-0.008, +0.002] | 0.1659 | 0.4977 | +0.011 | +0.009 | +0.27 |

### Per in-domain dataset, lam = policy lam (Holm over 10 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_mistral_7b | test|popqa|flare+abstain | 2000 | +0.201 [+0.173, +0.230] | 0.0001 | 0.0010 | +0.057 | -0.142 | -0.12 |
| sealed_v5_mistral_7b | test|popqa|dragin+abstain | 2000 | +0.193 [+0.165, +0.221] | 0.0001 | 0.0010 | +0.026 | -0.165 | -0.13 |
| sealed_v5_mistral_7b | test|popqa|probing-rag+abstain | 2000 | +0.153 [+0.129, +0.179] | 0.0001 | 0.0010 | +0.029 | -0.120 | -0.18 |
| sealed_v5_mistral_7b | test|popqa|se-rag+abstain | 2000 | +0.180 [+0.153, +0.208] | 0.0001 | 0.0010 | +0.035 | -0.142 | -0.16 |
| sealed_v5_mistral_7b | test|popqa|rag+abstain | 2000 | +0.023 [+0.006, +0.041] | 0.0069 | 0.0138 | -0.045 | -0.061 | -0.36 |
| sealed_v5_mistral_7b | test|triviaqa|flare+abstain | 1882 | +0.183 [+0.152, +0.215] | 0.0001 | 0.0010 | +0.182 | -0.006 | +0.24 |
| sealed_v5_mistral_7b | test|triviaqa|dragin+abstain | 1882 | +0.133 [+0.101, +0.165] | 0.0001 | 0.0010 | +0.123 | -0.015 | +0.27 |
| sealed_v5_mistral_7b | test|triviaqa|probing-rag+abstain | 1882 | +0.124 [+0.094, +0.154] | 0.0001 | 0.0010 | +0.066 | -0.066 | +0.43 |
| sealed_v5_mistral_7b | test|triviaqa|se-rag+abstain | 1882 | +0.117 [+0.088, +0.147] | 0.0001 | 0.0010 | +0.114 | -0.008 | +0.25 |
| sealed_v5_mistral_7b | test|triviaqa|rag+abstain | 1882 | +0.010 [-0.011, +0.032] | 0.3484 | 0.3484 | -0.033 | -0.038 | -0.27 |

### Per OOD dataset (no selection guarantee), lam = policy lam (Holm over 15 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_mistral_7b | ood|2wikimultihopqa|flare+abstain | 998 | +0.006 [-0.026, +0.036] | 0.7075 | 0.9513 | -0.055 | -0.063 | +0.10 |
| sealed_v5_mistral_7b | ood|2wikimultihopqa|dragin+abstain | 998 | +0.019 [-0.015, +0.054] | 0.2512 | 0.7535 | -0.077 | -0.098 | +0.09 |
| sealed_v5_mistral_7b | ood|2wikimultihopqa|probing-rag+abstain | 998 | +0.039 [+0.007, +0.070] | 0.0149 | 0.0876 | -0.051 | -0.090 | +0.02 |
| sealed_v5_mistral_7b | ood|2wikimultihopqa|se-rag+abstain | 998 | +0.046 [+0.013, +0.079] | 0.0060 | 0.0616 | -0.057 | -0.104 | +0.06 |
| sealed_v5_mistral_7b | ood|2wikimultihopqa|rag+abstain | 998 | +0.065 [+0.042, +0.088] | 0.0001 | 0.0015 | -0.041 | -0.106 | -0.01 |
| sealed_v5_mistral_7b | ood|hotpotqa|flare+abstain | 998 | +0.060 [+0.016, +0.103] | 0.0068 | 0.0616 | +0.049 | -0.015 | +0.21 |
| sealed_v5_mistral_7b | ood|hotpotqa|dragin+abstain | 998 | +0.059 [+0.016, +0.102] | 0.0106 | 0.0742 | +0.006 | -0.057 | +0.22 |
| sealed_v5_mistral_7b | ood|hotpotqa|probing-rag+abstain | 998 | +0.103 [+0.059, +0.146] | 0.0001 | 0.0015 | +0.018 | -0.089 | +0.24 |
| sealed_v5_mistral_7b | ood|hotpotqa|se-rag+abstain | 998 | +0.082 [+0.039, +0.126] | 0.0001 | 0.0015 | +0.020 | -0.066 | +0.21 |
| sealed_v5_mistral_7b | ood|hotpotqa|rag+abstain | 998 | +0.043 [+0.013, +0.073] | 0.0056 | 0.0616 | -0.076 | -0.118 | -0.06 |
| sealed_v5_mistral_7b | ood|nq|flare+abstain | 999 | +0.045 [+0.005, +0.086] | 0.0323 | 0.1292 | +0.030 | -0.016 | +0.05 |
| sealed_v5_mistral_7b | ood|nq|dragin+abstain | 999 | +0.054 [+0.010, +0.097] | 0.0146 | 0.0876 | -0.004 | -0.059 | +0.06 |
| sealed_v5_mistral_7b | ood|nq|probing-rag+abstain | 999 | +0.182 [+0.138, +0.228] | 0.0001 | 0.0015 | -0.020 | -0.208 | +0.30 |
| sealed_v5_mistral_7b | ood|nq|se-rag+abstain | 999 | +0.053 [+0.013, +0.093] | 0.0092 | 0.0736 | +0.017 | -0.036 | +0.00 |
| sealed_v5_mistral_7b | ood|nq|rag+abstain | 999 | +0.012 [-0.021, +0.045] | 0.4757 | 0.9513 | -0.064 | -0.073 | -0.17 |

### Re-simulation check and detector seeds

| model | max deviation from policy.json | pre AUROC (seeds mean +- std) | post AUROC (seeds mean +- std) |
|---|---|---|---|
| sealed_v5_mistral_7b | sealed (frozen from v5_mistral_7b) | 0.8720 +- 0.0014 | 0.8894 +- 0.0004 |

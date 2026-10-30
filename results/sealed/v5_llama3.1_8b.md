### Headline: route-eu minus each baseline, TEST (Holm over 12 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_llama3.1_8b | 1|flare+abstain | 3881 | +0.144 [+0.124, +0.164] | 0.0001 | 0.0012 | +0.063 | -0.084 | +0.17 |
| sealed_v5_llama3.1_8b | 1|dragin+abstain | 3881 | +0.101 [+0.081, +0.120] | 0.0001 | 0.0012 | +0.049 | -0.055 | +0.17 |
| sealed_v5_llama3.1_8b | 1|probing-rag+abstain | 3881 | +0.123 [+0.104, +0.141] | 0.0001 | 0.0012 | +0.070 | -0.055 | +0.12 |
| sealed_v5_llama3.1_8b | 1|se-rag+abstain | 3881 | +0.095 [+0.077, +0.114] | 0.0001 | 0.0012 | +0.044 | -0.054 | +0.16 |
| sealed_v5_llama3.1_8b | 2|flare+abstain | 3881 | +0.167 [+0.143, +0.192] | 0.0001 | 0.0012 | +0.132 | -0.019 | +0.10 |
| sealed_v5_llama3.1_8b | 2|dragin+abstain | 3881 | +0.127 [+0.103, +0.152] | 0.0001 | 0.0012 | +0.032 | -0.049 | +0.10 |
| sealed_v5_llama3.1_8b | 2|probing-rag+abstain | 3881 | +0.151 [+0.128, +0.174] | 0.0001 | 0.0012 | +0.061 | -0.045 | +0.03 |
| sealed_v5_llama3.1_8b | 2|se-rag+abstain | 3881 | +0.124 [+0.099, +0.149] | 0.0001 | 0.0012 | +0.012 | -0.057 | +0.12 |
| sealed_v5_llama3.1_8b | 4|flare+abstain | 3881 | +0.182 [+0.149, +0.217] | 0.0001 | 0.0012 | +0.086 | -0.024 | +0.04 |
| sealed_v5_llama3.1_8b | 4|dragin+abstain | 3881 | +0.137 [+0.102, +0.171] | 0.0001 | 0.0012 | +0.031 | -0.027 | +0.10 |
| sealed_v5_llama3.1_8b | 4|probing-rag+abstain | 3881 | +0.150 [+0.120, +0.180] | 0.0001 | 0.0012 | +0.090 | -0.015 | +0.02 |
| sealed_v5_llama3.1_8b | 4|se-rag+abstain | 3881 | +0.124 [+0.092, +0.157] | 0.0001 | 0.0012 | +0.033 | -0.023 | +0.09 |

### route-eu minus the unmodified baselines, TEST (Holm over 12 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_llama3.1_8b | 1|flare | 3881 | +0.259 [+0.236, +0.283] | 0.0001 | 0.0012 | -0.086 | -0.346 | +0.00 |
| sealed_v5_llama3.1_8b | 1|dragin | 3881 | +0.244 [+0.221, +0.266] | 0.0001 | 0.0012 | -0.093 | -0.339 | +0.11 |
| sealed_v5_llama3.1_8b | 1|probing-rag | 3881 | +0.266 [+0.245, +0.287] | 0.0001 | 0.0012 | -0.083 | -0.349 | -0.01 |
| sealed_v5_llama3.1_8b | 1|se-rag | 3881 | +0.238 [+0.216, +0.259] | 0.0001 | 0.0012 | -0.097 | -0.335 | +0.05 |
| sealed_v5_llama3.1_8b | 2|flare | 3881 | +0.598 [+0.559, +0.637] | 0.0001 | 0.0012 | -0.152 | -0.372 | -0.26 |
| sealed_v5_llama3.1_8b | 2|dragin | 3881 | +0.575 [+0.536, +0.615] | 0.0001 | 0.0012 | -0.156 | -0.367 | +0.15 |
| sealed_v5_llama3.1_8b | 2|probing-rag | 3881 | +0.613 [+0.577, +0.650] | 0.0001 | 0.0012 | -0.147 | -0.377 | -0.26 |
| sealed_v5_llama3.1_8b | 2|se-rag | 3881 | +0.566 [+0.530, +0.603] | 0.0001 | 0.0012 | -0.160 | -0.364 | +0.09 |
| sealed_v5_llama3.1_8b | 4|flare | 3881 | +1.341 [+1.270, +1.412] | 0.0001 | 0.0012 | -0.242 | -0.394 | -0.26 |
| sealed_v5_llama3.1_8b | 4|dragin | 3881 | +1.309 [+1.237, +1.380] | 0.0001 | 0.0012 | -0.247 | -0.390 | +0.15 |
| sealed_v5_llama3.1_8b | 4|probing-rag | 3881 | +1.365 [+1.298, +1.433] | 0.0001 | 0.0012 | -0.237 | -0.399 | -0.26 |
| sealed_v5_llama3.1_8b | 4|se-rag | 3881 | +1.293 [+1.222, +1.359] | 0.0001 | 0.0012 | -0.250 | -0.386 | +0.09 |

### Ablations (full minus ablated), TEST, policy lam (Holm over 10 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_llama3.1_8b | probe heads -> token logprob | 3881 | +0.118 [+0.097, +0.138] | 0.0001 | 0.0010 | +0.057 | -0.065 | +0.22 |
| sealed_v5_llama3.1_8b | probe heads -> top-k entropy | 3881 | +0.101 [+0.081, +0.120] | 0.0001 | 0.0010 | +0.054 | -0.051 | +0.21 |
| sealed_v5_llama3.1_8b | evidence heads -> closed-book heads after retrieval | 3881 | +0.039 [+0.025, +0.052] | 0.0001 | 0.0010 | +0.020 | -0.020 | +0.07 |
| sealed_v5_llama3.1_8b | retrieval -> none (abstain only) | 3881 | +0.122 [+0.101, +0.142] | 0.0001 | 0.0010 | +0.065 | -0.071 | +0.70 |
| sealed_v5_llama3.1_8b | routing -> always retrieve (same heads) | 3881 | +0.019 [+0.008, +0.031] | 0.0005 | 0.0025 | -0.032 | -0.046 | -0.30 |
| sealed_v5_llama3.1_8b | option-value signal -> help head | 3881 | +0.013 [+0.005, +0.022] | 0.0004 | 0.0024 | +0.028 | +0.010 | +0.21 |
| sealed_v5_llama3.1_8b | EU rule -> tuned thresholds | 3881 | +0.011 [-0.001, +0.024] | 0.0811 | 0.3244 | -0.038 | -0.049 | -0.04 |
| sealed_v5_llama3.1_8b | rollback / resample -> none | 3881 | -0.006 [-0.015, +0.003] | 0.2068 | 0.6203 | -0.013 | -0.007 | +0.00 |
| sealed_v5_llama3.1_8b | drift (resample) branch -> none | 3881 | +0.001 [-0.001, +0.003] | 0.2400 | 0.6203 | +0.001 | -0.000 | -0.00 |
| sealed_v5_llama3.1_8b | second retrieval attempt -> one | 3881 | -0.001 [-0.006, +0.004] | 0.7765 | 0.7765 | +0.015 | +0.010 | +0.32 |

### Per in-domain dataset, lam = policy lam (Holm over 10 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_llama3.1_8b | test|popqa|flare+abstain | 1999 | +0.162 [+0.135, +0.189] | 0.0001 | 0.0010 | +0.025 | -0.137 | -0.05 |
| sealed_v5_llama3.1_8b | test|popqa|dragin+abstain | 1999 | +0.110 [+0.085, +0.136] | 0.0001 | 0.0010 | +0.011 | -0.098 | -0.07 |
| sealed_v5_llama3.1_8b | test|popqa|probing-rag+abstain | 1999 | +0.111 [+0.088, +0.134] | 0.0001 | 0.0010 | +0.025 | -0.084 | -0.14 |
| sealed_v5_llama3.1_8b | test|popqa|se-rag+abstain | 1999 | +0.119 [+0.095, +0.143] | 0.0001 | 0.0010 | +0.017 | -0.100 | -0.09 |
| sealed_v5_llama3.1_8b | test|popqa|rag+abstain | 1999 | +0.026 [+0.011, +0.041] | 0.0009 | 0.0018 | -0.038 | -0.057 | -0.34 |
| sealed_v5_llama3.1_8b | test|triviaqa|flare+abstain | 1882 | +0.124 [+0.093, +0.153] | 0.0001 | 0.0010 | +0.104 | -0.029 | +0.42 |
| sealed_v5_llama3.1_8b | test|triviaqa|dragin+abstain | 1882 | +0.090 [+0.061, +0.120] | 0.0001 | 0.0010 | +0.089 | -0.009 | +0.41 |
| sealed_v5_llama3.1_8b | test|triviaqa|probing-rag+abstain | 1882 | +0.136 [+0.107, +0.165] | 0.0001 | 0.0010 | +0.118 | -0.026 | +0.39 |
| sealed_v5_llama3.1_8b | test|triviaqa|se-rag+abstain | 1882 | +0.070 [+0.041, +0.098] | 0.0001 | 0.0010 | +0.072 | -0.006 | +0.42 |
| sealed_v5_llama3.1_8b | test|triviaqa|rag+abstain | 1882 | +0.012 [-0.004, +0.029] | 0.1491 | 0.1491 | -0.027 | -0.035 | -0.25 |

### Per OOD dataset (no selection guarantee), lam = policy lam (Holm over 15 tests)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff | retrieval diff |
|---|---|---|---|---|---|---|---|---|
| sealed_v5_llama3.1_8b | ood|2wikimultihopqa|flare+abstain | 999 | -0.019 [-0.058, +0.020] | 0.3583 | 1.0000 | -0.118 | -0.105 | +0.30 |
| sealed_v5_llama3.1_8b | ood|2wikimultihopqa|dragin+abstain | 999 | -0.032 [-0.074, +0.009] | 0.1227 | 0.7361 | -0.140 | -0.114 | +0.32 |
| sealed_v5_llama3.1_8b | ood|2wikimultihopqa|probing-rag+abstain | 999 | -0.019 [-0.055, +0.017] | 0.2763 | 1.0000 | -0.087 | -0.072 | +0.22 |
| sealed_v5_llama3.1_8b | ood|2wikimultihopqa|se-rag+abstain | 999 | -0.017 [-0.054, +0.019] | 0.3747 | 1.0000 | -0.090 | -0.078 | +0.23 |
| sealed_v5_llama3.1_8b | ood|2wikimultihopqa|rag+abstain | 999 | +0.081 [+0.058, +0.104] | 0.0001 | 0.0015 | -0.033 | -0.113 | -0.02 |
| sealed_v5_llama3.1_8b | ood|hotpotqa|flare+abstain | 1000 | +0.093 [+0.049, +0.138] | 0.0002 | 0.0020 | +0.090 | -0.008 | +0.27 |
| sealed_v5_llama3.1_8b | ood|hotpotqa|dragin+abstain | 1000 | +0.044 [+0.001, +0.087] | 0.0501 | 0.3507 | +0.078 | +0.029 | +0.23 |
| sealed_v5_llama3.1_8b | ood|hotpotqa|probing-rag+abstain | 1000 | +0.046 [+0.005, +0.089] | 0.0337 | 0.2696 | +0.068 | +0.017 | +0.25 |
| sealed_v5_llama3.1_8b | ood|hotpotqa|se-rag+abstain | 1000 | +0.029 [-0.014, +0.071] | 0.1808 | 0.9039 | +0.086 | +0.053 | +0.20 |
| sealed_v5_llama3.1_8b | ood|hotpotqa|rag+abstain | 1000 | +0.092 [+0.065, +0.119] | 0.0001 | 0.0015 | -0.038 | -0.129 | -0.05 |
| sealed_v5_llama3.1_8b | ood|nq|flare+abstain | 1000 | +0.098 [+0.057, +0.140] | 0.0001 | 0.0015 | -0.005 | -0.109 | +0.29 |
| sealed_v5_llama3.1_8b | ood|nq|dragin+abstain | 1000 | +0.082 [+0.044, +0.122] | 0.0001 | 0.0015 | +0.002 | -0.085 | +0.25 |
| sealed_v5_llama3.1_8b | ood|nq|probing-rag+abstain | 1000 | +0.088 [+0.049, +0.125] | 0.0001 | 0.0015 | +0.016 | -0.076 | +0.19 |
| sealed_v5_llama3.1_8b | ood|nq|se-rag+abstain | 1000 | +0.049 [+0.010, +0.089] | 0.0115 | 0.1035 | +0.010 | -0.043 | +0.19 |
| sealed_v5_llama3.1_8b | ood|nq|rag+abstain | 1000 | -0.010 [-0.039, +0.019] | 0.5110 | 1.0000 | -0.065 | -0.052 | -0.16 |

### Re-simulation check and detector seeds

| model | max deviation from policy.json | pre AUROC (seeds mean +- std) | post AUROC (seeds mean +- std) |
|---|---|---|---|
| sealed_v5_llama3.1_8b | sealed (frozen from v5_llama3.1_8b) | 0.8675 +- 0.0012 | 0.9051 +- 0.0012 |

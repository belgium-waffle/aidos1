### Detector: question text only vs Tripwire's pre head (closed-book answers; positive = hallucination)

| model | split | signal | AUROC | AUPRC |
|---|---|---|---|---|
| v5_qwen2.5_7b | test | text router (question only) | 0.830 | 0.895 |
| v5_qwen2.5_7b | test | Tripwire pre head | 0.891 | 0.930 |
| v5_qwen2.5_7b | ood | text router (question only) | 0.658 | 0.844 |
| v5_qwen2.5_7b | ood | Tripwire pre head | 0.799 | 0.917 |
| v5_llama3.1_8b | test | text router (question only) | 0.803 | 0.813 |
| v5_llama3.1_8b | test | Tripwire pre head | 0.866 | 0.873 |
| v5_llama3.1_8b | ood | text router (question only) | 0.606 | 0.786 |
| v5_llama3.1_8b | ood | Tripwire pre head | 0.743 | 0.868 |
| v5_mistral_7b | test | text router (question only) | 0.817 | 0.814 |
| v5_mistral_7b | test | Tripwire pre head | 0.868 | 0.879 |
| v5_mistral_7b | ood | text router (question only) | 0.592 | 0.769 |
| v5_mistral_7b | ood | Tripwire pre head | 0.645 | 0.810 |
| v4_qwen2.5_32b | test | text router (question only) | 0.848 | 0.853 |
| v4_qwen2.5_32b | test | Tripwire pre head | 0.908 | 0.917 |
| v4_qwen2.5_32b | ood | text router (question only) | 0.633 | 0.788 |
| v4_qwen2.5_32b | ood | Tripwire pre head | 0.754 | 0.864 |
| v6_llama3.3_70b | test | text router (question only) | 0.801 | 0.664 |
| v6_llama3.3_70b | test | Tripwire pre head | 0.876 | 0.821 |
| v6_llama3.3_70b | ood | text router (question only) | 0.539 | 0.687 |
| v6_llama3.3_70b | ood | Tripwire pre head | 0.715 | 0.797 |

### Text router policies (selected on VAL)

| model | lam | policy | test acc | test halluc | test coverage | test retrieval |
|---|---|---|---|---|---|---|
| v5_qwen2.5_7b | 1 | text-router | 0.569 | 0.431 | 1.000 | 1.00 |
| v5_qwen2.5_7b | 1 | text-router+abstain | 0.495 | 0.309 | 0.803 | 1.00 |
| v5_qwen2.5_7b | 2 | text-router | 0.569 | 0.431 | 1.000 | 1.00 |
| v5_qwen2.5_7b | 2 | text-router+abstain | 0.219 | 0.096 | 0.315 | 0.69 |
| v5_qwen2.5_7b | 4 | text-router | 0.569 | 0.431 | 1.000 | 1.00 |
| v5_qwen2.5_7b | 4 | text-router+abstain | 0.000 | 0.000 | 0.000 | 1.00 |
| v5_llama3.1_8b | 1 | text-router | 0.602 | 0.398 | 1.000 | 1.00 |
| v5_llama3.1_8b | 1 | text-router+abstain | 0.429 | 0.161 | 0.590 | 0.56 |
| v5_llama3.1_8b | 2 | text-router | 0.602 | 0.398 | 1.000 | 1.00 |
| v5_llama3.1_8b | 2 | text-router+abstain | 0.382 | 0.113 | 0.495 | 0.69 |
| v5_llama3.1_8b | 4 | text-router | 0.602 | 0.398 | 1.000 | 1.00 |
| v5_llama3.1_8b | 4 | text-router+abstain | 0.242 | 0.051 | 0.293 | 1.00 |
| v5_mistral_7b | 1 | text-router | 0.592 | 0.408 | 1.000 | 1.00 |
| v5_mistral_7b | 1 | text-router+abstain | 0.421 | 0.166 | 0.587 | 0.61 |
| v5_mistral_7b | 2 | text-router | 0.592 | 0.408 | 1.000 | 1.00 |
| v5_mistral_7b | 2 | text-router+abstain | 0.302 | 0.087 | 0.390 | 0.61 |
| v5_mistral_7b | 4 | text-router | 0.592 | 0.408 | 1.000 | 1.00 |
| v5_mistral_7b | 4 | text-router+abstain | 0.000 | 0.000 | 0.000 | 1.00 |
| v4_qwen2.5_32b | 1 | text-router | 0.651 | 0.349 | 1.000 | 1.00 |
| v4_qwen2.5_32b | 1 | text-router+abstain | 0.481 | 0.130 | 0.611 | 0.69 |
| v4_qwen2.5_32b | 2 | text-router | 0.651 | 0.349 | 1.000 | 1.00 |
| v4_qwen2.5_32b | 2 | text-router+abstain | 0.481 | 0.130 | 0.611 | 0.69 |
| v4_qwen2.5_32b | 4 | text-router | 0.651 | 0.349 | 1.000 | 1.00 |
| v4_qwen2.5_32b | 4 | text-router+abstain | 0.263 | 0.053 | 0.316 | 0.69 |
| v6_llama3.3_70b | 1 | text-router | 0.709 | 0.291 | 1.000 | 1.00 |
| v6_llama3.3_70b | 1 | text-router+abstain | 0.597 | 0.129 | 0.727 | 0.43 |
| v6_llama3.3_70b | 2 | text-router | 0.709 | 0.291 | 1.000 | 1.00 |
| v6_llama3.3_70b | 2 | text-router+abstain | 0.580 | 0.116 | 0.696 | 0.43 |
| v6_llama3.3_70b | 4 | text-router | 0.709 | 0.291 | 1.000 | 1.00 |
| v6_llama3.3_70b | 4 | text-router+abstain | 0.431 | 0.058 | 0.489 | 1.00 |

### Paired utility differences (Holm within model and split)

| model | comparison | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff |
|---|---|---|---|---|---|---|---|
| v5_qwen2.5_7b | test|1|route-eu - text-router+abstain | 3166 | +0.226 [+0.204, +0.248] | 0.0001 | 0.0006 | -0.020 | -0.240 |
| v5_qwen2.5_7b | test|1|probing-rag+abstain - text-router+abstain | 3166 | +0.047 [+0.022, +0.072] | 0.0004 | 0.0008 | -0.106 | -0.147 |
| v5_qwen2.5_7b | ood|1|route-eu - text-router+abstain | 6992 | +0.196 [+0.180, +0.213] | 0.0001 | 0.0006 | -0.081 | -0.274 |
| v5_qwen2.5_7b | ood|1|probing-rag+abstain - text-router+abstain | 6992 | +0.152 [+0.132, +0.170] | 0.0001 | 0.0006 | -0.056 | -0.203 |
| v5_qwen2.5_7b | test|2|route-eu - text-router+abstain | 3166 | +0.307 [+0.276, +0.338] | 0.0001 | 0.0006 | +0.192 | -0.058 |
| v5_qwen2.5_7b | test|2|probing-rag+abstain - text-router+abstain | 3166 | +0.092 [+0.070, +0.116] | 0.0001 | 0.0006 | +0.032 | -0.030 |
| v5_qwen2.5_7b | ood|2|route-eu - text-router+abstain | 6992 | +0.204 [+0.181, +0.225] | 0.0001 | 0.0006 | +0.029 | -0.088 |
| v5_qwen2.5_7b | ood|2|probing-rag+abstain - text-router+abstain | 6992 | +0.102 [+0.083, +0.121] | 0.0001 | 0.0006 | +0.033 | -0.034 |
| v5_qwen2.5_7b | test|4|route-eu - text-router+abstain | 3166 | +0.259 [+0.233, +0.283] | 0.0001 | 0.0006 | +0.321 | +0.017 |
| v5_qwen2.5_7b | test|4|probing-rag+abstain - text-router+abstain | 3166 | -0.004 [-0.045, +0.036] | 0.8298 | 0.8298 | +0.251 | +0.065 |
| v5_qwen2.5_7b | ood|4|route-eu - text-router+abstain | 6992 | -0.051 [-0.070, -0.032] | 0.0001 | 0.0006 | +0.083 | +0.034 |
| v5_qwen2.5_7b | ood|4|probing-rag+abstain - text-router+abstain | 6992 | -0.364 [-0.398, -0.331] | 0.0001 | 0.0006 | +0.140 | +0.127 |
| v5_llama3.1_8b | test|1|route-eu - text-router+abstain | 3176 | +0.177 [+0.154, +0.200] | 0.0001 | 0.0006 | +0.084 | -0.096 |
| v5_llama3.1_8b | test|1|probing-rag+abstain - text-router+abstain | 3176 | +0.056 [+0.040, +0.072] | 0.0001 | 0.0006 | +0.021 | -0.035 |
| v5_llama3.1_8b | ood|1|route-eu - text-router+abstain | 6994 | +0.171 [+0.154, +0.188] | 0.0001 | 0.0006 | +0.005 | -0.174 |
| v5_llama3.1_8b | ood|1|probing-rag+abstain - text-router+abstain | 6994 | +0.139 [+0.125, +0.152] | 0.0001 | 0.0006 | +0.010 | -0.131 |
| v5_llama3.1_8b | test|2|route-eu - text-router+abstain | 3176 | +0.215 [+0.186, +0.246] | 0.0001 | 0.0006 | +0.071 | -0.073 |
| v5_llama3.1_8b | test|2|probing-rag+abstain - text-router+abstain | 3176 | +0.060 [+0.039, +0.082] | 0.0001 | 0.0006 | +0.003 | -0.029 |
| v5_llama3.1_8b | ood|2|route-eu - text-router+abstain | 6994 | +0.208 [+0.185, +0.230] | 0.0001 | 0.0006 | -0.011 | -0.111 |
| v5_llama3.1_8b | ood|2|probing-rag+abstain - text-router+abstain | 6994 | +0.161 [+0.141, +0.180] | 0.0001 | 0.0006 | -0.004 | -0.083 |
| v5_llama3.1_8b | test|4|route-eu - text-router+abstain | 3176 | +0.253 [+0.215, +0.291] | 0.0001 | 0.0006 | +0.118 | -0.032 |
| v5_llama3.1_8b | test|4|probing-rag+abstain - text-router+abstain | 3176 | +0.078 [+0.035, +0.123] | 0.0005 | 0.0006 | +0.013 | -0.015 |
| v5_llama3.1_8b | ood|4|route-eu - text-router+abstain | 6994 | +0.025 [+0.000, +0.049] | 0.0543 | 0.0543 | +0.019 | -0.001 |
| v5_llama3.1_8b | ood|4|probing-rag+abstain - text-router+abstain | 6994 | -0.107 [-0.140, -0.076] | 0.0001 | 0.0006 | +0.028 | +0.035 |
| v5_mistral_7b | test|1|route-eu - text-router+abstain | 3172 | +0.149 [+0.126, +0.171] | 0.0001 | 0.0006 | +0.063 | -0.087 |
| v5_mistral_7b | test|1|probing-rag+abstain - text-router+abstain | 3172 | +0.036 [+0.020, +0.052] | 0.0001 | 0.0006 | +0.026 | -0.008 |
| v5_mistral_7b | ood|1|route-eu - text-router+abstain | 6993 | +0.156 [+0.139, +0.173] | 0.0001 | 0.0006 | -0.023 | -0.185 |
| v5_mistral_7b | ood|1|probing-rag+abstain - text-router+abstain | 6993 | +0.055 [+0.042, +0.069] | 0.0001 | 0.0006 | -0.009 | -0.066 |
| v5_mistral_7b | test|2|route-eu - text-router+abstain | 3172 | +0.191 [+0.162, +0.220] | 0.0001 | 0.0006 | +0.096 | -0.048 |
| v5_mistral_7b | test|2|probing-rag+abstain - text-router+abstain | 3172 | +0.049 [+0.026, +0.072] | 0.0001 | 0.0006 | -0.036 | -0.043 |
| v5_mistral_7b | ood|2|route-eu - text-router+abstain | 6993 | +0.344 [+0.319, +0.369] | 0.0001 | 0.0006 | -0.037 | -0.193 |
| v5_mistral_7b | ood|2|probing-rag+abstain - text-router+abstain | 6993 | +0.287 [+0.264, +0.310] | 0.0001 | 0.0006 | -0.065 | -0.178 |
| v5_mistral_7b | test|4|route-eu - text-router+abstain | 3172 | +0.230 [+0.204, +0.257] | 0.0001 | 0.0006 | +0.306 | +0.021 |
| v5_mistral_7b | test|4|probing-rag+abstain - text-router+abstain | 3172 | +0.096 [+0.062, +0.129] | 0.0001 | 0.0006 | +0.267 | +0.044 |
| v5_mistral_7b | ood|4|route-eu - text-router+abstain | 6993 | -0.061 [-0.080, -0.044] | 0.0001 | 0.0006 | +0.063 | +0.032 |
| v5_mistral_7b | ood|4|probing-rag+abstain - text-router+abstain | 6993 | -0.270 [-0.299, -0.242] | 0.0001 | 0.0006 | +0.088 | +0.091 |
| v4_qwen2.5_32b | test|1|route-eu - text-router+abstain | 3172 | +0.167 [+0.147, +0.186] | 0.0001 | 0.0006 | +0.104 | -0.064 |
| v4_qwen2.5_32b | test|1|probing-rag+abstain - text-router+abstain | 3172 | +0.041 [+0.027, +0.055] | 0.0001 | 0.0006 | +0.033 | -0.007 |
| v4_qwen2.5_32b | ood|1|route-eu - text-router+abstain | 6994 | +0.090 [+0.075, +0.105] | 0.0001 | 0.0006 | +0.042 | -0.052 |
| v4_qwen2.5_32b | ood|1|probing-rag+abstain - text-router+abstain | 6994 | +0.065 [+0.053, +0.077] | 0.0001 | 0.0006 | +0.013 | -0.052 |
| v4_qwen2.5_32b | test|2|route-eu - text-router+abstain | 3172 | +0.227 [+0.198, +0.256] | 0.0001 | 0.0006 | +0.051 | -0.089 |
| v4_qwen2.5_32b | test|2|probing-rag+abstain - text-router+abstain | 3172 | +0.058 [+0.039, +0.077] | 0.0001 | 0.0006 | +0.013 | -0.022 |
| v4_qwen2.5_32b | ood|2|route-eu - text-router+abstain | 6994 | +0.212 [+0.189, +0.235] | 0.0001 | 0.0006 | -0.019 | -0.118 |
| v4_qwen2.5_32b | ood|2|probing-rag+abstain - text-router+abstain | 6994 | +0.155 [+0.137, +0.173] | 0.0001 | 0.0006 | -0.005 | -0.081 |
| v4_qwen2.5_32b | test|4|route-eu - text-router+abstain | 3172 | +0.314 [+0.277, +0.352] | 0.0001 | 0.0006 | +0.189 | -0.032 |
| v4_qwen2.5_32b | test|4|probing-rag+abstain - text-router+abstain | 3172 | +0.127 [+0.093, +0.161] | 0.0001 | 0.0006 | +0.026 | -0.025 |
| v4_qwen2.5_32b | ood|4|route-eu - text-router+abstain | 6994 | +0.358 [+0.319, +0.399] | 0.0001 | 0.0006 | +0.039 | -0.081 |
| v4_qwen2.5_32b | ood|4|probing-rag+abstain - text-router+abstain | 6994 | +0.341 [+0.306, +0.376] | 0.0001 | 0.0006 | -0.012 | -0.089 |
| v6_llama3.3_70b | test|1|route-eu - text-router+abstain | 3175 | +0.086 [+0.067, +0.105] | 0.0001 | 0.0006 | +0.035 | -0.056 |
| v6_llama3.3_70b | test|1|probing-rag+abstain - text-router+abstain | 3175 | +0.016 [+0.002, +0.029] | 0.0232 | 0.0232 | +0.028 | +0.014 |
| v6_llama3.3_70b | ood|1|route-eu - text-router+abstain | 6995 | +0.323 [+0.304, +0.342] | 0.0001 | 0.0006 | -0.009 | -0.348 |
| v6_llama3.3_70b | ood|1|probing-rag+abstain - text-router+abstain | 6995 | +0.255 [+0.241, +0.270] | 0.0001 | 0.0006 | -0.041 | -0.305 |
| v6_llama3.3_70b | test|2|route-eu - text-router+abstain | 3175 | +0.134 [+0.106, +0.162] | 0.0001 | 0.0006 | -0.000 | -0.071 |
| v6_llama3.3_70b | test|2|probing-rag+abstain - text-router+abstain | 3175 | +0.043 [+0.020, +0.066] | 0.0004 | 0.0012 | -0.062 | -0.053 |
| v6_llama3.3_70b | ood|2|route-eu - text-router+abstain | 6995 | +0.784 [+0.753, +0.815] | 0.0001 | 0.0006 | -0.072 | -0.436 |
| v6_llama3.3_70b | ood|2|probing-rag+abstain - text-router+abstain | 6995 | +0.719 [+0.691, +0.747] | 0.0001 | 0.0006 | -0.167 | -0.449 |
| v6_llama3.3_70b | test|4|route-eu - text-router+abstain | 3175 | +0.216 [+0.180, +0.253] | 0.0001 | 0.0006 | +0.056 | -0.039 |
| v6_llama3.3_70b | test|4|probing-rag+abstain - text-router+abstain | 3175 | +0.072 [+0.031, +0.115] | 0.0008 | 0.0016 | -0.053 | -0.029 |
| v6_llama3.3_70b | ood|4|route-eu - text-router+abstain | 6995 | +0.045 [+0.015, +0.076] | 0.0037 | 0.0037 | -0.010 | -0.014 |
| v6_llama3.3_70b | ood|4|probing-rag+abstain - text-router+abstain | 6995 | +0.059 [+0.028, +0.090] | 0.0002 | 0.0006 | -0.112 | -0.042 |

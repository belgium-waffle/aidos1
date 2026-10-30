### Cells (route, selected on VAL per lam; before | after retrieval)

| model | signal | lam | cell | test utility | test acc | test halluc | test retrieval | ood acc | ood halluc |
|---|---|---|---|---|---|---|---|---|---|
| v5_qwen2.5_7b | logprob | 1 | probe|probe | 0.401 | 0.502 | 0.086 | 0.75 | 0.209 | 0.171 |
| v5_qwen2.5_7b | logprob | 1 | probe|out | 0.255 | 0.420 | 0.152 | 0.69 | 0.207 | 0.192 |
| v5_qwen2.5_7b | logprob | 1 | out|probe | 0.373 | 0.478 | 0.085 | 1.00 | 0.182 | 0.150 |
| v5_qwen2.5_7b | logprob | 1 | out|out | 0.194 | 0.451 | 0.243 | 0.72 | 0.253 | 0.338 |
| v5_qwen2.5_7b | logprob | 2 | probe|probe | 0.315 | 0.502 | 0.086 | 0.75 | 0.209 | 0.171 |
| v5_qwen2.5_7b | logprob | 2 | probe|out | 0.159 | 0.262 | 0.044 | 0.69 | 0.108 | 0.085 |
| v5_qwen2.5_7b | logprob | 2 | out|probe | 0.288 | 0.478 | 0.085 | 1.00 | 0.182 | 0.150 |
| v5_qwen2.5_7b | logprob | 2 | out|out | 0.042 | 0.340 | 0.142 | 0.72 | 0.190 | 0.219 |
| v5_qwen2.5_7b | logprob | 4 | probe|probe | 0.218 | 0.328 | 0.023 | 1.00 | 0.078 | 0.039 |
| v5_qwen2.5_7b | logprob | 4 | probe|out | 0.089 | 0.247 | 0.036 | 0.72 | 0.099 | 0.070 |
| v5_qwen2.5_7b | logprob | 4 | out|probe | 0.195 | 0.383 | 0.042 | 1.00 | 0.110 | 0.067 |
| v5_qwen2.5_7b | logprob | 4 | out|out | -0.020 | 0.000 | 0.000 | 1.00 | 0.000 | 0.000 |
| v5_qwen2.5_7b | entropy | 1 | probe|probe | 0.401 | 0.502 | 0.086 | 0.75 | 0.209 | 0.171 |
| v5_qwen2.5_7b | entropy | 1 | probe|out | 0.253 | 0.405 | 0.137 | 0.69 | 0.193 | 0.171 |
| v5_qwen2.5_7b | entropy | 1 | out|probe | 0.373 | 0.478 | 0.085 | 1.00 | 0.182 | 0.150 |
| v5_qwen2.5_7b | entropy | 1 | out|out | 0.196 | 0.446 | 0.235 | 0.72 | 0.251 | 0.330 |
| v5_qwen2.5_7b | entropy | 2 | probe|probe | 0.315 | 0.502 | 0.086 | 0.75 | 0.209 | 0.171 |
| v5_qwen2.5_7b | entropy | 2 | probe|out | 0.159 | 0.262 | 0.044 | 0.69 | 0.108 | 0.085 |
| v5_qwen2.5_7b | entropy | 2 | out|probe | 0.288 | 0.478 | 0.085 | 1.00 | 0.182 | 0.150 |
| v5_qwen2.5_7b | entropy | 2 | out|out | 0.083 | 0.217 | 0.060 | 0.72 | 0.137 | 0.160 |
| v5_qwen2.5_7b | entropy | 4 | probe|probe | 0.218 | 0.328 | 0.023 | 1.00 | 0.078 | 0.039 |
| v5_qwen2.5_7b | entropy | 4 | probe|out | 0.089 | 0.247 | 0.036 | 0.72 | 0.099 | 0.070 |
| v5_qwen2.5_7b | entropy | 4 | out|probe | 0.198 | 0.382 | 0.041 | 1.00 | 0.109 | 0.065 |
| v5_qwen2.5_7b | entropy | 4 | out|out | -0.020 | 0.000 | 0.000 | 1.00 | 0.000 | 0.000 |
| v5_llama3.1_8b | logprob | 1 | probe|probe | 0.434 | 0.560 | 0.111 | 0.73 | 0.256 | 0.277 |
| v5_llama3.1_8b | logprob | 1 | probe|out | 0.342 | 0.495 | 0.141 | 0.59 | 0.208 | 0.191 |
| v5_llama3.1_8b | logprob | 1 | out|probe | 0.441 | 0.571 | 0.115 | 0.71 | 0.265 | 0.280 |
| v5_llama3.1_8b | logprob | 1 | out|out | 0.318 | 0.501 | 0.173 | 0.51 | 0.251 | 0.247 |
| v5_llama3.1_8b | logprob | 2 | probe|probe | 0.346 | 0.501 | 0.070 | 0.73 | 0.208 | 0.165 |
| v5_llama3.1_8b | logprob | 2 | probe|out | 0.256 | 0.428 | 0.079 | 0.64 | 0.158 | 0.108 |
| v5_llama3.1_8b | logprob | 2 | out|probe | 0.365 | 0.496 | 0.059 | 0.72 | 0.187 | 0.124 |
| v5_llama3.1_8b | logprob | 2 | out|out | 0.215 | 0.397 | 0.084 | 0.66 | 0.156 | 0.106 |
| v5_llama3.1_8b | logprob | 4 | probe|probe | 0.280 | 0.393 | 0.023 | 1.00 | 0.107 | 0.056 |
| v5_llama3.1_8b | logprob | 4 | probe|out | 0.156 | 0.271 | 0.025 | 0.70 | 0.083 | 0.047 |
| v5_llama3.1_8b | logprob | 4 | out|probe | 0.280 | 0.393 | 0.023 | 1.00 | 0.107 | 0.056 |
| v5_llama3.1_8b | logprob | 4 | out|out | 0.110 | 0.251 | 0.031 | 0.72 | 0.080 | 0.042 |
| v5_llama3.1_8b | entropy | 1 | probe|probe | 0.434 | 0.560 | 0.111 | 0.73 | 0.256 | 0.277 |
| v5_llama3.1_8b | entropy | 1 | probe|out | 0.331 | 0.515 | 0.172 | 0.64 | 0.227 | 0.220 |
| v5_llama3.1_8b | entropy | 1 | out|probe | 0.441 | 0.573 | 0.119 | 0.68 | 0.273 | 0.288 |
| v5_llama3.1_8b | entropy | 1 | out|out | 0.340 | 0.508 | 0.158 | 0.52 | 0.262 | 0.236 |
| v5_llama3.1_8b | entropy | 2 | probe|probe | 0.346 | 0.501 | 0.070 | 0.73 | 0.208 | 0.165 |
| v5_llama3.1_8b | entropy | 2 | probe|out | 0.256 | 0.428 | 0.079 | 0.64 | 0.157 | 0.108 |
| v5_llama3.1_8b | entropy | 2 | out|probe | 0.368 | 0.496 | 0.057 | 0.72 | 0.188 | 0.122 |
| v5_llama3.1_8b | entropy | 2 | out|out | 0.234 | 0.438 | 0.096 | 0.59 | 0.195 | 0.136 |
| v5_llama3.1_8b | entropy | 4 | probe|probe | 0.280 | 0.393 | 0.023 | 1.00 | 0.107 | 0.056 |
| v5_llama3.1_8b | entropy | 4 | probe|out | 0.156 | 0.271 | 0.025 | 0.70 | 0.083 | 0.047 |
| v5_llama3.1_8b | entropy | 4 | out|probe | 0.280 | 0.393 | 0.023 | 1.00 | 0.107 | 0.056 |
| v5_llama3.1_8b | entropy | 4 | out|out | 0.108 | 0.284 | 0.041 | 0.68 | 0.105 | 0.062 |
| v5_mistral_7b | logprob | 1 | probe|probe | 0.391 | 0.539 | 0.134 | 0.72 | 0.238 | 0.273 |
| v5_mistral_7b | logprob | 1 | probe|out | 0.279 | 0.471 | 0.181 | 0.59 | 0.199 | 0.227 |
| v5_mistral_7b | logprob | 1 | out|probe | 0.386 | 0.545 | 0.143 | 0.75 | 0.244 | 0.287 |
| v5_mistral_7b | logprob | 1 | out|out | 0.226 | 0.475 | 0.235 | 0.71 | 0.251 | 0.338 |
| v5_mistral_7b | logprob | 2 | probe|probe | 0.313 | 0.468 | 0.070 | 0.72 | 0.156 | 0.130 |
| v5_mistral_7b | logprob | 2 | probe|out | 0.192 | 0.354 | 0.074 | 0.68 | 0.114 | 0.097 |
| v5_mistral_7b | logprob | 2 | out|probe | 0.301 | 0.476 | 0.080 | 0.75 | 0.168 | 0.147 |
| v5_mistral_7b | logprob | 2 | out|out | 0.132 | 0.313 | 0.083 | 0.75 | 0.122 | 0.115 |
| v5_mistral_7b | logprob | 4 | probe|probe | 0.206 | 0.373 | 0.038 | 0.76 | 0.095 | 0.062 |
| v5_mistral_7b | logprob | 4 | probe|out | 0.117 | 0.222 | 0.022 | 0.76 | 0.046 | 0.030 |
| v5_mistral_7b | logprob | 4 | out|probe | 0.201 | 0.327 | 0.026 | 1.00 | 0.074 | 0.044 |
| v5_mistral_7b | logprob | 4 | out|out | 0.064 | 0.215 | 0.034 | 0.75 | 0.067 | 0.052 |
| v5_mistral_7b | entropy | 1 | probe|probe | 0.391 | 0.539 | 0.134 | 0.72 | 0.238 | 0.273 |
| v5_mistral_7b | entropy | 1 | probe|out | 0.284 | 0.472 | 0.175 | 0.66 | 0.211 | 0.263 |
| v5_mistral_7b | entropy | 1 | out|probe | 0.385 | 0.544 | 0.144 | 0.76 | 0.244 | 0.286 |
| v5_mistral_7b | entropy | 1 | out|out | 0.250 | 0.507 | 0.242 | 0.72 | 0.269 | 0.375 |
| v5_mistral_7b | entropy | 2 | probe|probe | 0.313 | 0.468 | 0.070 | 0.72 | 0.156 | 0.130 |
| v5_mistral_7b | entropy | 2 | probe|out | 0.195 | 0.355 | 0.073 | 0.68 | 0.113 | 0.096 |
| v5_mistral_7b | entropy | 2 | out|probe | 0.301 | 0.475 | 0.079 | 0.76 | 0.168 | 0.146 |
| v5_mistral_7b | entropy | 2 | out|out | 0.135 | 0.334 | 0.092 | 0.74 | 0.137 | 0.138 |
| v5_mistral_7b | entropy | 4 | probe|probe | 0.206 | 0.373 | 0.038 | 0.76 | 0.095 | 0.062 |
| v5_mistral_7b | entropy | 4 | probe|out | 0.117 | 0.222 | 0.022 | 0.76 | 0.046 | 0.030 |
| v5_mistral_7b | entropy | 4 | out|probe | 0.201 | 0.327 | 0.026 | 1.00 | 0.074 | 0.044 |
| v5_mistral_7b | entropy | 4 | out|out | 0.063 | 0.210 | 0.033 | 0.76 | 0.064 | 0.050 |
| v4_qwen2.5_32b | logprob | 1 | probe|probe | 0.500 | 0.596 | 0.082 | 0.68 | 0.319 | 0.209 |
| v4_qwen2.5_32b | logprob | 1 | probe|out | 0.409 | 0.564 | 0.143 | 0.60 | 0.329 | 0.241 |
| v4_qwen2.5_32b | logprob | 1 | out|probe | 0.489 | 0.604 | 0.094 | 1.00 | 0.337 | 0.242 |
| v4_qwen2.5_32b | logprob | 1 | out|out | 0.350 | 0.506 | 0.143 | 0.65 | 0.283 | 0.251 |
| v4_qwen2.5_32b | logprob | 2 | probe|probe | 0.420 | 0.537 | 0.051 | 0.68 | 0.267 | 0.143 |
| v4_qwen2.5_32b | logprob | 2 | probe|out | 0.292 | 0.501 | 0.098 | 0.68 | 0.249 | 0.135 |
| v4_qwen2.5_32b | logprob | 2 | out|probe | 0.412 | 0.518 | 0.043 | 1.00 | 0.245 | 0.125 |
| v4_qwen2.5_32b | logprob | 2 | out|out | 0.229 | 0.448 | 0.102 | 0.71 | 0.234 | 0.177 |
| v4_qwen2.5_32b | logprob | 4 | probe|probe | 0.338 | 0.513 | 0.040 | 0.68 | 0.222 | 0.107 |
| v4_qwen2.5_32b | logprob | 4 | probe|out | 0.203 | 0.352 | 0.034 | 0.68 | 0.150 | 0.069 |
| v4_qwen2.5_32b | logprob | 4 | out|probe | 0.355 | 0.488 | 0.028 | 1.00 | 0.194 | 0.085 |
| v4_qwen2.5_32b | logprob | 4 | out|out | 0.131 | 0.307 | 0.040 | 0.71 | 0.158 | 0.120 |
| v4_qwen2.5_32b | entropy | 1 | probe|probe | 0.500 | 0.596 | 0.082 | 0.68 | 0.319 | 0.209 |
| v4_qwen2.5_32b | entropy | 1 | probe|out | 0.409 | 0.564 | 0.143 | 0.60 | 0.330 | 0.243 |
| v4_qwen2.5_32b | entropy | 1 | out|probe | 0.489 | 0.604 | 0.094 | 1.00 | 0.337 | 0.242 |
| v4_qwen2.5_32b | entropy | 1 | out|out | 0.352 | 0.507 | 0.141 | 0.66 | 0.285 | 0.249 |
| v4_qwen2.5_32b | entropy | 2 | probe|probe | 0.420 | 0.537 | 0.051 | 0.68 | 0.267 | 0.143 |
| v4_qwen2.5_32b | entropy | 2 | probe|out | 0.307 | 0.497 | 0.088 | 0.68 | 0.260 | 0.142 |
| v4_qwen2.5_32b | entropy | 2 | out|probe | 0.398 | 0.540 | 0.064 | 0.71 | 0.286 | 0.194 |
| v4_qwen2.5_32b | entropy | 2 | out|out | 0.242 | 0.439 | 0.091 | 0.71 | 0.236 | 0.174 |
| v4_qwen2.5_32b | entropy | 4 | probe|probe | 0.338 | 0.513 | 0.040 | 0.68 | 0.222 | 0.107 |
| v4_qwen2.5_32b | entropy | 4 | probe|out | 0.183 | 0.337 | 0.035 | 0.63 | 0.144 | 0.082 |
| v4_qwen2.5_32b | entropy | 4 | out|probe | 0.355 | 0.488 | 0.028 | 1.00 | 0.194 | 0.085 |
| v4_qwen2.5_32b | entropy | 4 | out|out | 0.121 | 0.257 | 0.031 | 0.71 | 0.129 | 0.104 |
| v6_llama3.3_70b | logprob | 1 | probe|probe | 0.532 | 0.625 | 0.079 | 0.71 | 0.362 | 0.256 |
| v6_llama3.3_70b | logprob | 1 | probe|out | 0.479 | 0.643 | 0.155 | 0.49 | 0.371 | 0.268 |
| v6_llama3.3_70b | logprob | 1 | out|probe | 0.536 | 0.640 | 0.090 | 0.68 | 0.370 | 0.264 |
| v6_llama3.3_70b | logprob | 1 | out|out | 0.442 | 0.612 | 0.160 | 0.47 | 0.357 | 0.257 |
| v6_llama3.3_70b | logprob | 2 | probe|probe | 0.474 | 0.598 | 0.054 | 0.77 | 0.308 | 0.174 |
| v6_llama3.3_70b | logprob | 2 | probe|out | 0.380 | 0.572 | 0.090 | 0.61 | 0.289 | 0.149 |
| v6_llama3.3_70b | logprob | 2 | out|probe | 0.473 | 0.614 | 0.064 | 0.71 | 0.319 | 0.183 |
| v6_llama3.3_70b | logprob | 2 | out|out | 0.325 | 0.533 | 0.099 | 0.48 | 0.261 | 0.157 |
| v6_llama3.3_70b | logprob | 4 | probe|probe | 0.384 | 0.496 | 0.024 | 0.77 | 0.200 | 0.078 |
| v6_llama3.3_70b | logprob | 4 | probe|out | 0.273 | 0.521 | 0.059 | 0.63 | 0.225 | 0.098 |
| v6_llama3.3_70b | logprob | 4 | out|probe | 0.389 | 0.485 | 0.019 | 1.00 | 0.194 | 0.073 |
| v6_llama3.3_70b | logprob | 4 | out|out | 0.185 | 0.316 | 0.029 | 0.68 | 0.109 | 0.044 |
| v6_llama3.3_70b | entropy | 1 | probe|probe | 0.532 | 0.625 | 0.079 | 0.71 | 0.362 | 0.256 |
| v6_llama3.3_70b | entropy | 1 | probe|out | 0.480 | 0.642 | 0.152 | 0.49 | 0.371 | 0.265 |
| v6_llama3.3_70b | entropy | 1 | out|probe | 0.532 | 0.651 | 0.108 | 0.54 | 0.377 | 0.284 |
| v6_llama3.3_70b | entropy | 1 | out|out | 0.443 | 0.652 | 0.199 | 0.48 | 0.398 | 0.337 |
| v6_llama3.3_70b | entropy | 2 | probe|probe | 0.474 | 0.598 | 0.054 | 0.77 | 0.308 | 0.174 |
| v6_llama3.3_70b | entropy | 2 | probe|out | 0.381 | 0.571 | 0.089 | 0.61 | 0.289 | 0.147 |
| v6_llama3.3_70b | entropy | 2 | out|probe | 0.473 | 0.612 | 0.062 | 0.72 | 0.318 | 0.181 |
| v6_llama3.3_70b | entropy | 2 | out|out | 0.320 | 0.496 | 0.083 | 0.54 | 0.232 | 0.119 |
| v6_llama3.3_70b | entropy | 4 | probe|probe | 0.384 | 0.496 | 0.024 | 0.77 | 0.200 | 0.078 |
| v6_llama3.3_70b | entropy | 4 | probe|out | 0.282 | 0.451 | 0.039 | 0.64 | 0.160 | 0.065 |
| v6_llama3.3_70b | entropy | 4 | out|probe | 0.389 | 0.485 | 0.019 | 1.00 | 0.194 | 0.073 |
| v6_llama3.3_70b | entropy | 4 | out|out | 0.173 | 0.283 | 0.024 | 0.69 | 0.096 | 0.038 |

### Paired utility differences (Holm within model and split)

| model | comparison | what it isolates | n | utility diff [95% CI] | p | Holm p | acc diff | halluc diff |
|---|---|---|---|---|---|---|---|---|
| v5_qwen2.5_7b | test|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 3166 | +0.207 [+0.185, +0.229] | 0.0001 | 0.0030 | +0.051 | -0.157 |
| v5_qwen2.5_7b | test|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 3166 | +0.146 [+0.127, +0.165] | 0.0001 | 0.0030 | +0.081 | -0.066 |
| v5_qwen2.5_7b | test|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 3166 | +0.028 [+0.016, +0.039] | 0.0001 | 0.0030 | +0.024 | +0.001 |
| v5_qwen2.5_7b | test|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 3166 | +0.179 [+0.155, +0.203] | 0.0001 | 0.0030 | +0.027 | -0.158 |
| v5_qwen2.5_7b | test|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 3166 | +0.061 [+0.040, +0.082] | 0.0001 | 0.0030 | -0.031 | -0.091 |
| v5_qwen2.5_7b | ood|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 6992 | +0.120 [+0.103, +0.136] | 0.0001 | 0.0030 | -0.043 | -0.166 |
| v5_qwen2.5_7b | ood|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 6992 | +0.021 [+0.009, +0.034] | 0.0012 | 0.0072 | +0.002 | -0.020 |
| v5_qwen2.5_7b | ood|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 6992 | +0.008 [-0.001, +0.016] | 0.0600 | 0.1260 | +0.027 | +0.021 |
| v5_qwen2.5_7b | ood|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 6992 | +0.112 [+0.095, +0.129] | 0.0001 | 0.0030 | -0.070 | -0.188 |
| v5_qwen2.5_7b | ood|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 6992 | +0.098 [+0.083, +0.114] | 0.0001 | 0.0030 | -0.046 | -0.146 |
| v5_qwen2.5_7b | test|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 3166 | +0.273 [+0.239, +0.306] | 0.0001 | 0.0030 | +0.161 | -0.056 |
| v5_qwen2.5_7b | test|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 3166 | +0.155 [+0.130, +0.182] | 0.0001 | 0.0030 | +0.240 | +0.042 |
| v5_qwen2.5_7b | test|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 3166 | +0.026 [+0.010, +0.043] | 0.0020 | 0.0072 | +0.024 | +0.001 |
| v5_qwen2.5_7b | test|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 3166 | +0.246 [+0.211, +0.281] | 0.0001 | 0.0030 | +0.137 | -0.057 |
| v5_qwen2.5_7b | test|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 3166 | +0.117 [+0.086, +0.151] | 0.0001 | 0.0030 | -0.079 | -0.098 |
| v5_qwen2.5_7b | ood|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 6992 | +0.112 [+0.086, +0.138] | 0.0001 | 0.0030 | +0.019 | -0.048 |
| v5_qwen2.5_7b | ood|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 6992 | -0.072 [-0.092, -0.052] | 0.0001 | 0.0030 | +0.101 | +0.086 |
| v5_qwen2.5_7b | ood|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 6992 | -0.014 [-0.026, -0.001] | 0.0288 | 0.1260 | +0.027 | +0.021 |
| v5_qwen2.5_7b | ood|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 6992 | +0.126 [+0.099, +0.152] | 0.0001 | 0.0030 | -0.007 | -0.069 |
| v5_qwen2.5_7b | ood|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 6992 | +0.184 [+0.159, +0.208] | 0.0001 | 0.0030 | -0.082 | -0.134 |
| v5_qwen2.5_7b | test|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 3166 | +0.238 [+0.208, +0.265] | 0.0001 | 0.0030 | +0.328 | +0.023 |
| v5_qwen2.5_7b | test|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 3166 | +0.129 [+0.092, +0.164] | 0.0001 | 0.0030 | +0.081 | -0.013 |
| v5_qwen2.5_7b | test|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 3166 | +0.022 [+0.002, +0.044] | 0.0378 | 0.0756 | -0.055 | -0.019 |
| v5_qwen2.5_7b | test|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 3166 | +0.215 [+0.179, +0.250] | 0.0001 | 0.0030 | +0.383 | +0.042 |
| v5_qwen2.5_7b | test|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 3166 | +0.109 [+0.078, +0.139] | 0.0001 | 0.0030 | +0.247 | +0.036 |
| v5_qwen2.5_7b | ood|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 6992 | -0.079 [-0.099, -0.059] | 0.0001 | 0.0030 | +0.078 | +0.039 |
| v5_qwen2.5_7b | ood|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 6992 | +0.101 [+0.072, +0.131] | 0.0001 | 0.0030 | -0.021 | -0.031 |
| v5_qwen2.5_7b | ood|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 6992 | +0.078 [+0.062, +0.095] | 0.0001 | 0.0030 | -0.033 | -0.028 |
| v5_qwen2.5_7b | ood|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 6992 | -0.156 [-0.182, -0.130] | 0.0001 | 0.0030 | +0.110 | +0.067 |
| v5_qwen2.5_7b | ood|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 6992 | -0.180 [-0.205, -0.155] | 0.0001 | 0.0030 | +0.099 | +0.070 |
| v5_qwen2.5_7b | test|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 3166 | +0.205 [+0.183, +0.226] | 0.0001 | 0.0030 | +0.056 | -0.149 |
| v5_qwen2.5_7b | test|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 3166 | +0.147 [+0.128, +0.167] | 0.0001 | 0.0030 | +0.097 | -0.051 |
| v5_qwen2.5_7b | test|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 3166 | +0.028 [+0.016, +0.039] | 0.0001 | 0.0030 | +0.024 | +0.001 |
| v5_qwen2.5_7b | test|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 3166 | +0.177 [+0.153, +0.200] | 0.0001 | 0.0030 | +0.032 | -0.151 |
| v5_qwen2.5_7b | test|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 3166 | +0.057 [+0.037, +0.078] | 0.0001 | 0.0030 | -0.041 | -0.098 |
| v5_qwen2.5_7b | ood|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 6992 | +0.114 [+0.097, +0.131] | 0.0001 | 0.0030 | -0.041 | -0.159 |
| v5_qwen2.5_7b | ood|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 6992 | +0.014 [+0.002, +0.027] | 0.0252 | 0.1260 | +0.016 | +0.000 |
| v5_qwen2.5_7b | ood|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 6992 | +0.008 [-0.001, +0.016] | 0.0637 | 0.1260 | +0.027 | +0.021 |
| v5_qwen2.5_7b | ood|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 6992 | +0.106 [+0.089, +0.123] | 0.0001 | 0.0030 | -0.068 | -0.180 |
| v5_qwen2.5_7b | ood|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 6992 | +0.100 [+0.084, +0.115] | 0.0001 | 0.0030 | -0.057 | -0.159 |
| v5_qwen2.5_7b | test|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 3166 | +0.232 [+0.201, +0.264] | 0.0001 | 0.0030 | +0.285 | +0.026 |
| v5_qwen2.5_7b | test|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 3166 | +0.155 [+0.129, +0.182] | 0.0001 | 0.0030 | +0.240 | +0.042 |
| v5_qwen2.5_7b | test|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 3166 | +0.026 [+0.011, +0.043] | 0.0018 | 0.0072 | +0.024 | +0.001 |
| v5_qwen2.5_7b | test|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 3166 | +0.205 [+0.172, +0.238] | 0.0001 | 0.0030 | +0.261 | +0.025 |
| v5_qwen2.5_7b | test|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 3166 | +0.076 [+0.054, +0.099] | 0.0001 | 0.0030 | +0.045 | -0.015 |
| v5_qwen2.5_7b | ood|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 6992 | +0.047 [+0.019, +0.073] | 0.0006 | 0.0042 | +0.072 | +0.011 |
| v5_qwen2.5_7b | ood|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 6992 | -0.072 [-0.091, -0.053] | 0.0001 | 0.0030 | +0.101 | +0.086 |
| v5_qwen2.5_7b | ood|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 6992 | -0.014 [-0.025, -0.002] | 0.0313 | 0.1260 | +0.027 | +0.021 |
| v5_qwen2.5_7b | ood|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 6992 | +0.060 [+0.032, +0.087] | 0.0001 | 0.0030 | +0.046 | -0.010 |
| v5_qwen2.5_7b | ood|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 6992 | +0.118 [+0.097, +0.139] | 0.0001 | 0.0030 | -0.029 | -0.075 |
| v5_qwen2.5_7b | test|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 3166 | +0.238 [+0.210, +0.264] | 0.0001 | 0.0030 | +0.328 | +0.023 |
| v5_qwen2.5_7b | test|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 3166 | +0.129 [+0.094, +0.166] | 0.0001 | 0.0030 | +0.081 | -0.013 |
| v5_qwen2.5_7b | test|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 3166 | +0.020 [-0.000, +0.040] | 0.0577 | 0.0756 | -0.053 | -0.018 |
| v5_qwen2.5_7b | test|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 3166 | +0.218 [+0.183, +0.252] | 0.0001 | 0.0030 | +0.382 | +0.041 |
| v5_qwen2.5_7b | test|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 3166 | +0.109 [+0.077, +0.140] | 0.0001 | 0.0030 | +0.247 | +0.036 |
| v5_qwen2.5_7b | ood|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 6992 | -0.079 [-0.099, -0.059] | 0.0001 | 0.0030 | +0.078 | +0.039 |
| v5_qwen2.5_7b | ood|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 6992 | +0.101 [+0.071, +0.131] | 0.0001 | 0.0030 | -0.021 | -0.031 |
| v5_qwen2.5_7b | ood|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 6992 | +0.074 [+0.058, +0.089] | 0.0001 | 0.0030 | -0.031 | -0.026 |
| v5_qwen2.5_7b | ood|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 6992 | -0.152 [-0.178, -0.128] | 0.0001 | 0.0030 | +0.109 | +0.065 |
| v5_qwen2.5_7b | ood|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 6992 | -0.180 [-0.205, -0.154] | 0.0001 | 0.0030 | +0.099 | +0.070 |
| v5_llama3.1_8b | test|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 3176 | +0.116 [+0.094, +0.138] | 0.0001 | 0.0030 | +0.058 | -0.062 |
| v5_llama3.1_8b | test|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 3176 | +0.092 [+0.073, +0.112] | 0.0001 | 0.0030 | +0.065 | -0.030 |
| v5_llama3.1_8b | test|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 3176 | -0.007 [-0.019, +0.005] | 0.2580 | 1.0000 | -0.011 | -0.004 |
| v5_llama3.1_8b | test|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 3176 | +0.123 [+0.103, +0.144] | 0.0001 | 0.0030 | +0.069 | -0.058 |
| v5_llama3.1_8b | test|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 3176 | +0.024 [+0.007, +0.041] | 0.0048 | 0.0432 | -0.007 | -0.032 |
| v5_llama3.1_8b | ood|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 6994 | -0.031 [-0.048, -0.013] | 0.0003 | 0.0063 | +0.005 | +0.030 |
| v5_llama3.1_8b | ood|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | -0.042 [-0.056, -0.028] | 0.0001 | 0.0030 | +0.047 | +0.087 |
| v5_llama3.1_8b | ood|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | -0.006 [-0.014, +0.002] | 0.1536 | 1.0000 | -0.009 | -0.003 |
| v5_llama3.1_8b | ood|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 6994 | -0.025 [-0.041, -0.009] | 0.0027 | 0.0486 | +0.014 | +0.034 |
| v5_llama3.1_8b | ood|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.011 [-0.001, +0.024] | 0.0866 | 1.0000 | -0.042 | -0.056 |
| v5_llama3.1_8b | test|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 3176 | +0.131 [+0.103, +0.157] | 0.0001 | 0.0030 | +0.104 | -0.014 |
| v5_llama3.1_8b | test|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 3176 | +0.090 [+0.065, +0.115] | 0.0001 | 0.0030 | +0.074 | -0.009 |
| v5_llama3.1_8b | test|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 3176 | -0.019 [-0.039, +0.002] | 0.0718 | 0.4308 | +0.005 | +0.012 |
| v5_llama3.1_8b | test|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 3176 | +0.149 [+0.128, +0.172] | 0.0001 | 0.0030 | +0.099 | -0.026 |
| v5_llama3.1_8b | test|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 3176 | +0.041 [+0.020, +0.061] | 0.0001 | 0.0030 | +0.030 | -0.005 |
| v5_llama3.1_8b | ood|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 6994 | -0.066 [-0.088, -0.043] | 0.0001 | 0.0030 | +0.052 | +0.058 |
| v5_llama3.1_8b | ood|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | -0.063 [-0.084, -0.043] | 0.0001 | 0.0030 | +0.051 | +0.056 |
| v5_llama3.1_8b | ood|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | -0.060 [-0.075, -0.044] | 0.0001 | 0.0030 | +0.021 | +0.040 |
| v5_llama3.1_8b | ood|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 6994 | -0.006 [-0.024, +0.011] | 0.4856 | 1.0000 | +0.031 | +0.018 |
| v5_llama3.1_8b | ood|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 6994 | -0.003 [-0.019, +0.012] | 0.7264 | 1.0000 | +0.002 | +0.002 |
| v5_llama3.1_8b | test|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 3176 | +0.170 [+0.135, +0.205] | 0.0001 | 0.0030 | +0.143 | -0.008 |
| v5_llama3.1_8b | test|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 3176 | +0.124 [+0.091, +0.157] | 0.0001 | 0.0030 | +0.122 | -0.002 |
| v5_llama3.1_8b | test|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 3176 | +0.000 [+0.000, +0.000] | 1.0000 | 1.0000 | +0.000 | +0.000 |
| v5_llama3.1_8b | test|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 3176 | +0.170 [+0.136, +0.203] | 0.0001 | 0.0030 | +0.143 | -0.008 |
| v5_llama3.1_8b | test|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 3176 | +0.046 [+0.016, +0.076] | 0.0024 | 0.0264 | +0.020 | -0.006 |
| v5_llama3.1_8b | ood|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 6994 | -0.029 [-0.057, -0.002] | 0.0376 | 0.6015 | +0.027 | +0.014 |
| v5_llama3.1_8b | ood|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | -0.014 [-0.041, +0.013] | 0.3060 | 1.0000 | +0.024 | +0.009 |
| v5_llama3.1_8b | ood|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | +0.000 [+0.000, +0.000] | 1.0000 | 1.0000 | +0.000 | +0.000 |
| v5_llama3.1_8b | ood|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 6994 | -0.029 [-0.057, -0.002] | 0.0404 | 0.6059 | +0.027 | +0.014 |
| v5_llama3.1_8b | ood|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 6994 | -0.015 [-0.039, +0.009] | 0.2224 | 1.0000 | +0.004 | +0.005 |
| v5_llama3.1_8b | test|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 3176 | +0.094 [+0.073, +0.116] | 0.0001 | 0.0030 | +0.052 | -0.047 |
| v5_llama3.1_8b | test|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 3176 | +0.103 [+0.085, +0.121] | 0.0001 | 0.0030 | +0.044 | -0.061 |
| v5_llama3.1_8b | test|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 3176 | -0.006 [-0.019, +0.006] | 0.3328 | 1.0000 | -0.014 | -0.009 |
| v5_llama3.1_8b | test|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 3176 | +0.101 [+0.081, +0.121] | 0.0001 | 0.0030 | +0.065 | -0.038 |
| v5_llama3.1_8b | test|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 3176 | -0.009 [-0.027, +0.009] | 0.3523 | 1.0000 | +0.008 | +0.014 |
| v5_llama3.1_8b | ood|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 6994 | -0.052 [-0.068, -0.034] | 0.0001 | 0.0030 | -0.006 | +0.041 |
| v5_llama3.1_8b | ood|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | -0.030 [-0.043, -0.016] | 0.0001 | 0.0030 | +0.028 | +0.057 |
| v5_llama3.1_8b | ood|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | -0.007 [-0.016, +0.002] | 0.1372 | 1.0000 | -0.017 | -0.011 |
| v5_llama3.1_8b | ood|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 6994 | -0.045 [-0.060, -0.029] | 0.0001 | 0.0030 | +0.011 | +0.052 |
| v5_llama3.1_8b | ood|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 6994 | -0.022 [-0.036, -0.008] | 0.0011 | 0.0209 | -0.034 | -0.016 |
| v5_llama3.1_8b | test|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 3176 | +0.112 [+0.085, +0.140] | 0.0001 | 0.0030 | +0.063 | -0.026 |
| v5_llama3.1_8b | test|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 3176 | +0.090 [+0.065, +0.115] | 0.0001 | 0.0030 | +0.074 | -0.009 |
| v5_llama3.1_8b | test|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 3176 | -0.022 [-0.042, -0.001] | 0.0330 | 0.2632 | +0.005 | +0.013 |
| v5_llama3.1_8b | test|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 3176 | +0.134 [+0.111, +0.157] | 0.0001 | 0.0030 | +0.058 | -0.039 |
| v5_llama3.1_8b | test|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 3176 | +0.022 [+0.002, +0.042] | 0.0329 | 0.2632 | -0.010 | -0.017 |
| v5_llama3.1_8b | ood|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 6994 | -0.047 [-0.070, -0.023] | 0.0003 | 0.0063 | +0.013 | +0.028 |
| v5_llama3.1_8b | ood|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | -0.064 [-0.083, -0.044] | 0.0001 | 0.0030 | +0.051 | +0.057 |
| v5_llama3.1_8b | ood|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | -0.064 [-0.079, -0.048] | 0.0001 | 0.0030 | +0.021 | +0.042 |
| v5_llama3.1_8b | ood|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 6994 | +0.017 [-0.003, +0.036] | 0.0791 | 1.0000 | -0.008 | -0.014 |
| v5_llama3.1_8b | ood|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.017 [-0.001, +0.034] | 0.0571 | 0.7993 | -0.038 | -0.028 |
| v5_llama3.1_8b | test|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 3176 | +0.172 [+0.137, +0.208] | 0.0001 | 0.0030 | +0.110 | -0.017 |
| v5_llama3.1_8b | test|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 3176 | +0.124 [+0.091, +0.156] | 0.0001 | 0.0030 | +0.122 | -0.002 |
| v5_llama3.1_8b | test|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 3176 | +0.000 [+0.000, +0.000] | 1.0000 | 1.0000 | +0.000 | +0.000 |
| v5_llama3.1_8b | test|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 3176 | +0.172 [+0.136, +0.208] | 0.0001 | 0.0030 | +0.110 | -0.017 |
| v5_llama3.1_8b | test|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 3176 | +0.049 [+0.018, +0.079] | 0.0024 | 0.0264 | -0.013 | -0.015 |
| v5_llama3.1_8b | ood|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 6994 | +0.023 [-0.007, +0.053] | 0.1381 | 1.0000 | +0.002 | -0.006 |
| v5_llama3.1_8b | ood|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | -0.014 [-0.043, +0.013] | 0.3064 | 1.0000 | +0.024 | +0.009 |
| v5_llama3.1_8b | ood|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | +0.000 [+0.000, +0.000] | 1.0000 | 1.0000 | +0.000 | +0.000 |
| v5_llama3.1_8b | ood|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 6994 | +0.023 [-0.007, +0.052] | 0.1305 | 1.0000 | +0.002 | -0.006 |
| v5_llama3.1_8b | ood|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.037 [+0.011, +0.064] | 0.0072 | 0.1224 | -0.021 | -0.015 |
| v5_mistral_7b | test|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.165 [+0.144, +0.187] | 0.0001 | 0.0030 | +0.064 | -0.101 |
| v5_mistral_7b | test|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.113 [+0.092, +0.134] | 0.0001 | 0.0030 | +0.068 | -0.047 |
| v5_mistral_7b | test|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.005 [-0.009, +0.018] | 0.4674 | 1.0000 | -0.005 | -0.010 |
| v5_mistral_7b | test|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.160 [+0.142, +0.180] | 0.0001 | 0.0030 | +0.070 | -0.091 |
| v5_mistral_7b | test|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.052 [+0.032, +0.073] | 0.0001 | 0.0030 | -0.004 | -0.054 |
| v5_mistral_7b | ood|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 6993 | +0.051 [+0.034, +0.068] | 0.0001 | 0.0030 | -0.013 | -0.066 |
| v5_mistral_7b | ood|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 6993 | -0.009 [-0.024, +0.007] | 0.2711 | 0.8895 | +0.039 | +0.045 |
| v5_mistral_7b | ood|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 6993 | +0.008 [-0.001, +0.017] | 0.0946 | 0.6621 | -0.006 | -0.014 |
| v5_mistral_7b | ood|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 6993 | +0.044 [+0.029, +0.059] | 0.0001 | 0.0030 | -0.007 | -0.052 |
| v5_mistral_7b | ood|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 6993 | +0.060 [+0.045, +0.074] | 0.0001 | 0.0030 | -0.052 | -0.111 |
| v5_mistral_7b | test|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.181 [+0.151, +0.209] | 0.0001 | 0.0030 | +0.155 | -0.013 |
| v5_mistral_7b | test|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.121 [+0.097, +0.144] | 0.0001 | 0.0030 | +0.114 | -0.004 |
| v5_mistral_7b | test|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.012 [-0.008, +0.032] | 0.2256 | 1.0000 | -0.009 | -0.010 |
| v5_mistral_7b | test|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.168 [+0.144, +0.193] | 0.0001 | 0.0030 | +0.163 | -0.003 |
| v5_mistral_7b | test|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.060 [+0.037, +0.083] | 0.0001 | 0.0030 | +0.041 | -0.009 |
| v5_mistral_7b | ood|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 6993 | +0.004 [-0.017, +0.027] | 0.6731 | 0.8895 | +0.035 | +0.015 |
| v5_mistral_7b | ood|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 6993 | -0.024 [-0.041, -0.007] | 0.0049 | 0.0611 | +0.042 | +0.033 |
| v5_mistral_7b | ood|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 6993 | +0.022 [+0.008, +0.036] | 0.0014 | 0.0224 | -0.012 | -0.017 |
| v5_mistral_7b | ood|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 6993 | -0.018 [-0.035, -0.000] | 0.0459 | 0.4131 | +0.046 | +0.032 |
| v5_mistral_7b | ood|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 6993 | +0.029 [+0.013, +0.045] | 0.0004 | 0.0068 | -0.008 | -0.018 |
| v5_mistral_7b | test|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.142 [+0.104, +0.180] | 0.0001 | 0.0030 | +0.158 | +0.004 |
| v5_mistral_7b | test|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.089 [+0.066, +0.113] | 0.0001 | 0.0030 | +0.151 | +0.015 |
| v5_mistral_7b | test|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.005 [-0.019, +0.030] | 0.6821 | 1.0000 | +0.046 | +0.011 |
| v5_mistral_7b | test|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.137 [+0.100, +0.175] | 0.0001 | 0.0030 | +0.112 | -0.008 |
| v5_mistral_7b | test|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.053 [+0.021, +0.084] | 0.0012 | 0.0084 | +0.007 | -0.012 |
| v5_mistral_7b | ood|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 6993 | -0.012 [-0.042, +0.016] | 0.4181 | 0.8895 | +0.028 | +0.010 |
| v5_mistral_7b | ood|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 6993 | -0.076 [-0.094, -0.058] | 0.0001 | 0.0030 | +0.049 | +0.031 |
| v5_mistral_7b | ood|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 6993 | -0.047 [-0.062, -0.032] | 0.0001 | 0.0030 | +0.021 | +0.017 |
| v5_mistral_7b | ood|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 6993 | +0.035 [+0.006, +0.063] | 0.0166 | 0.1826 | +0.007 | -0.008 |
| v5_mistral_7b | ood|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 6993 | +0.063 [+0.039, +0.089] | 0.0001 | 0.0030 | -0.021 | -0.021 |
| v5_mistral_7b | test|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.141 [+0.119, +0.162] | 0.0001 | 0.0030 | +0.032 | -0.108 |
| v5_mistral_7b | test|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.108 [+0.089, +0.126] | 0.0001 | 0.0030 | +0.067 | -0.041 |
| v5_mistral_7b | test|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.007 [-0.007, +0.021] | 0.3418 | 1.0000 | -0.004 | -0.010 |
| v5_mistral_7b | test|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.134 [+0.117, +0.152] | 0.0001 | 0.0030 | +0.037 | -0.098 |
| v5_mistral_7b | test|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.033 [+0.014, +0.052] | 0.0005 | 0.0045 | -0.035 | -0.067 |
| v5_mistral_7b | ood|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 6993 | +0.070 [+0.054, +0.086] | 0.0001 | 0.0030 | -0.031 | -0.103 |
| v5_mistral_7b | ood|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 6993 | +0.017 [+0.002, +0.030] | 0.0199 | 0.1990 | +0.027 | +0.009 |
| v5_mistral_7b | ood|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 6993 | +0.007 [-0.002, +0.017] | 0.1139 | 0.6621 | -0.006 | -0.013 |
| v5_mistral_7b | ood|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 6993 | +0.063 [+0.049, +0.077] | 0.0001 | 0.0030 | -0.025 | -0.090 |
| v5_mistral_7b | ood|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 6993 | +0.054 [+0.040, +0.067] | 0.0001 | 0.0030 | -0.058 | -0.112 |
| v5_mistral_7b | test|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.178 [+0.149, +0.207] | 0.0001 | 0.0030 | +0.134 | -0.022 |
| v5_mistral_7b | test|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.118 [+0.093, +0.142] | 0.0001 | 0.0030 | +0.113 | -0.003 |
| v5_mistral_7b | test|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.012 [-0.008, +0.032] | 0.2472 | 1.0000 | -0.007 | -0.009 |
| v5_mistral_7b | test|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.166 [+0.142, +0.191] | 0.0001 | 0.0030 | +0.142 | -0.013 |
| v5_mistral_7b | test|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.060 [+0.036, +0.084] | 0.0001 | 0.0030 | +0.021 | -0.019 |
| v5_mistral_7b | ood|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 6993 | +0.035 [+0.013, +0.057] | 0.0025 | 0.0375 | +0.019 | -0.008 |
| v5_mistral_7b | ood|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 6993 | -0.025 [-0.043, -0.008] | 0.0047 | 0.0611 | +0.043 | +0.034 |
| v5_mistral_7b | ood|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 6993 | +0.020 [+0.006, +0.034] | 0.0040 | 0.0560 | -0.011 | -0.016 |
| v5_mistral_7b | ood|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 6993 | +0.015 [-0.003, +0.033] | 0.1080 | 0.6621 | +0.030 | +0.007 |
| v5_mistral_7b | ood|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 6993 | +0.060 [+0.043, +0.077] | 0.0001 | 0.0030 | -0.024 | -0.042 |
| v5_mistral_7b | test|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.144 [+0.108, +0.180] | 0.0001 | 0.0030 | +0.163 | +0.005 |
| v5_mistral_7b | test|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.089 [+0.066, +0.112] | 0.0001 | 0.0030 | +0.151 | +0.015 |
| v5_mistral_7b | test|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.005 [-0.020, +0.030] | 0.6883 | 1.0000 | +0.046 | +0.011 |
| v5_mistral_7b | test|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.139 [+0.102, +0.175] | 0.0001 | 0.0030 | +0.117 | -0.007 |
| v5_mistral_7b | test|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.055 [+0.023, +0.086] | 0.0006 | 0.0048 | +0.012 | -0.011 |
| v5_mistral_7b | ood|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 6993 | -0.018 [-0.047, +0.010] | 0.2224 | 0.8895 | +0.030 | +0.012 |
| v5_mistral_7b | ood|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 6993 | -0.076 [-0.094, -0.058] | 0.0001 | 0.0030 | +0.049 | +0.031 |
| v5_mistral_7b | ood|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 6993 | -0.047 [-0.063, -0.032] | 0.0001 | 0.0030 | +0.021 | +0.017 |
| v5_mistral_7b | ood|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 6993 | +0.028 [+0.000, +0.057] | 0.0471 | 0.4131 | +0.009 | -0.005 |
| v5_mistral_7b | ood|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 6993 | +0.057 [+0.031, +0.082] | 0.0001 | 0.0030 | -0.019 | -0.019 |
| v4_qwen2.5_32b | test|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.150 [+0.130, +0.169] | 0.0001 | 0.0030 | +0.090 | -0.061 |
| v4_qwen2.5_32b | test|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.091 [+0.075, +0.107] | 0.0001 | 0.0030 | +0.032 | -0.061 |
| v4_qwen2.5_32b | test|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.010 [-0.001, +0.022] | 0.0841 | 0.4205 | -0.008 | -0.012 |
| v4_qwen2.5_32b | test|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.140 [+0.119, +0.160] | 0.0001 | 0.0030 | +0.098 | -0.049 |
| v4_qwen2.5_32b | test|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.059 [+0.044, +0.074] | 0.0001 | 0.0030 | +0.058 | +0.000 |
| v4_qwen2.5_32b | ood|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 6994 | +0.074 [+0.058, +0.090] | 0.0001 | 0.0030 | +0.035 | -0.041 |
| v4_qwen2.5_32b | ood|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | +0.019 [+0.005, +0.033] | 0.0076 | 0.0456 | -0.010 | -0.032 |
| v4_qwen2.5_32b | ood|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | +0.018 [+0.009, +0.026] | 0.0003 | 0.0030 | -0.019 | -0.033 |
| v4_qwen2.5_32b | ood|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 6994 | +0.056 [+0.040, +0.073] | 0.0001 | 0.0030 | +0.054 | -0.008 |
| v4_qwen2.5_32b | ood|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.055 [+0.043, +0.067] | 0.0001 | 0.0030 | +0.046 | -0.010 |
| v4_qwen2.5_32b | test|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.191 [+0.164, +0.220] | 0.0001 | 0.0030 | +0.089 | -0.051 |
| v4_qwen2.5_32b | test|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.128 [+0.106, +0.152] | 0.0001 | 0.0030 | +0.036 | -0.046 |
| v4_qwen2.5_32b | test|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.009 [-0.006, +0.023] | 0.2208 | 0.4830 | +0.019 | +0.008 |
| v4_qwen2.5_32b | test|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.182 [+0.154, +0.211] | 0.0001 | 0.0030 | +0.070 | -0.059 |
| v4_qwen2.5_32b | test|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.063 [+0.045, +0.082] | 0.0001 | 0.0030 | +0.053 | -0.005 |
| v4_qwen2.5_32b | ood|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 6994 | +0.099 [+0.077, +0.121] | 0.0001 | 0.0030 | +0.032 | -0.034 |
| v4_qwen2.5_32b | ood|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | +0.002 [-0.015, +0.020] | 0.7829 | 1.0000 | +0.018 | +0.008 |
| v4_qwen2.5_32b | ood|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | -0.010 [-0.021, +0.000] | 0.0543 | 0.2715 | +0.022 | +0.017 |
| v4_qwen2.5_32b | ood|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 6994 | +0.109 [+0.087, +0.132] | 0.0001 | 0.0030 | +0.011 | -0.052 |
| v4_qwen2.5_32b | ood|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.097 [+0.080, +0.113] | 0.0001 | 0.0030 | +0.015 | -0.042 |
| v4_qwen2.5_32b | test|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.207 [+0.169, +0.246] | 0.0001 | 0.0030 | +0.206 | +0.000 |
| v4_qwen2.5_32b | test|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.136 [+0.110, +0.161] | 0.0001 | 0.0030 | +0.161 | +0.006 |
| v4_qwen2.5_32b | test|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | -0.017 [-0.040, +0.006] | 0.1610 | 0.4830 | +0.025 | +0.012 |
| v4_qwen2.5_32b | test|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.223 [+0.187, +0.261] | 0.0001 | 0.0030 | +0.181 | -0.012 |
| v4_qwen2.5_32b | test|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.071 [+0.041, +0.103] | 0.0001 | 0.0030 | +0.045 | -0.006 |
| v4_qwen2.5_32b | ood|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 6994 | +0.114 [+0.077, +0.151] | 0.0001 | 0.0030 | +0.064 | -0.013 |
| v4_qwen2.5_32b | ood|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | -0.082 [-0.108, -0.058] | 0.0001 | 0.0030 | +0.072 | +0.039 |
| v4_qwen2.5_32b | ood|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | -0.058 [-0.076, -0.040] | 0.0001 | 0.0030 | +0.028 | +0.022 |
| v4_qwen2.5_32b | ood|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 6994 | +0.172 [+0.134, +0.209] | 0.0001 | 0.0030 | +0.036 | -0.035 |
| v4_qwen2.5_32b | ood|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.196 [+0.167, +0.227] | 0.0001 | 0.0030 | -0.008 | -0.051 |
| v4_qwen2.5_32b | test|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.147 [+0.128, +0.167] | 0.0001 | 0.0030 | +0.089 | -0.059 |
| v4_qwen2.5_32b | test|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.090 [+0.074, +0.107] | 0.0001 | 0.0030 | +0.031 | -0.061 |
| v4_qwen2.5_32b | test|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.010 [-0.001, +0.022] | 0.0851 | 0.4205 | -0.008 | -0.012 |
| v4_qwen2.5_32b | test|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.137 [+0.118, +0.158] | 0.0001 | 0.0030 | +0.097 | -0.047 |
| v4_qwen2.5_32b | test|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.057 [+0.041, +0.073] | 0.0001 | 0.0030 | +0.058 | +0.002 |
| v4_qwen2.5_32b | ood|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 6994 | +0.071 [+0.055, +0.086] | 0.0001 | 0.0030 | +0.034 | -0.039 |
| v4_qwen2.5_32b | ood|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | +0.020 [+0.007, +0.034] | 0.0044 | 0.0308 | -0.011 | -0.033 |
| v4_qwen2.5_32b | ood|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | +0.018 [+0.008, +0.026] | 0.0003 | 0.0030 | -0.019 | -0.033 |
| v4_qwen2.5_32b | ood|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 6994 | +0.053 [+0.037, +0.070] | 0.0001 | 0.0030 | +0.052 | -0.006 |
| v4_qwen2.5_32b | ood|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.050 [+0.038, +0.063] | 0.0001 | 0.0030 | +0.045 | -0.006 |
| v4_qwen2.5_32b | test|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.179 [+0.151, +0.206] | 0.0001 | 0.0030 | +0.098 | -0.040 |
| v4_qwen2.5_32b | test|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.114 [+0.092, +0.137] | 0.0001 | 0.0030 | +0.040 | -0.037 |
| v4_qwen2.5_32b | test|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | +0.023 [+0.005, +0.041] | 0.0135 | 0.0810 | -0.003 | -0.013 |
| v4_qwen2.5_32b | test|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.156 [+0.132, +0.179] | 0.0001 | 0.0030 | +0.101 | -0.027 |
| v4_qwen2.5_32b | test|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.065 [+0.046, +0.084] | 0.0001 | 0.0030 | +0.058 | -0.003 |
| v4_qwen2.5_32b | ood|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 6994 | +0.092 [+0.069, +0.115] | 0.0001 | 0.0030 | +0.031 | -0.032 |
| v4_qwen2.5_32b | ood|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | +0.005 [-0.012, +0.023] | 0.5630 | 1.0000 | +0.007 | +0.001 |
| v4_qwen2.5_32b | ood|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | +0.083 [+0.067, +0.098] | 0.0001 | 0.0030 | -0.019 | -0.052 |
| v4_qwen2.5_32b | ood|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 6994 | +0.010 [-0.007, +0.026] | 0.2690 | 0.8069 | +0.050 | +0.020 |
| v4_qwen2.5_32b | ood|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.087 [+0.070, +0.103] | 0.0001 | 0.0030 | +0.024 | -0.032 |
| v4_qwen2.5_32b | test|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 3172 | +0.217 [+0.179, +0.254] | 0.0001 | 0.0030 | +0.256 | +0.010 |
| v4_qwen2.5_32b | test|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 3172 | +0.155 [+0.126, +0.184] | 0.0001 | 0.0030 | +0.177 | +0.005 |
| v4_qwen2.5_32b | test|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 3172 | -0.017 [-0.040, +0.006] | 0.1610 | 0.4830 | +0.025 | +0.012 |
| v4_qwen2.5_32b | test|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 3172 | +0.234 [+0.198, +0.271] | 0.0001 | 0.0030 | +0.231 | -0.002 |
| v4_qwen2.5_32b | test|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 3172 | +0.062 [+0.030, +0.094] | 0.0002 | 0.0030 | +0.079 | +0.005 |
| v4_qwen2.5_32b | ood|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 6994 | +0.078 [+0.041, +0.115] | 0.0002 | 0.0030 | +0.093 | +0.003 |
| v4_qwen2.5_32b | ood|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 6994 | -0.026 [-0.054, +0.002] | 0.0717 | 0.2868 | +0.078 | +0.026 |
| v4_qwen2.5_32b | ood|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 6994 | -0.058 [-0.076, -0.040] | 0.0001 | 0.0030 | +0.028 | +0.022 |
| v4_qwen2.5_32b | ood|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 6994 | +0.136 [+0.099, +0.173] | 0.0001 | 0.0030 | +0.065 | -0.019 |
| v4_qwen2.5_32b | ood|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 6994 | +0.104 [+0.072, +0.137] | 0.0001 | 0.0030 | +0.016 | -0.022 |
| v6_llama3.3_70b | test|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 3175 | +0.089 [+0.070, +0.109] | 0.0001 | 0.0030 | +0.014 | -0.081 |
| v6_llama3.3_70b | test|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 3175 | +0.053 [+0.035, +0.070] | 0.0001 | 0.0030 | -0.018 | -0.075 |
| v6_llama3.3_70b | test|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 3175 | -0.004 [-0.013, +0.006] | 0.4102 | 1.0000 | -0.014 | -0.011 |
| v6_llama3.3_70b | test|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 3175 | +0.093 [+0.075, +0.111] | 0.0001 | 0.0030 | +0.028 | -0.070 |
| v6_llama3.3_70b | test|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 3175 | +0.036 [+0.020, +0.052] | 0.0001 | 0.0030 | +0.031 | -0.005 |
| v6_llama3.3_70b | ood|logprob|1|probe|probe - out|out | both halves (the existing ablation) | 6995 | +0.002 [-0.013, +0.017] | 0.7985 | 1.0000 | +0.005 | -0.001 |
| v6_llama3.3_70b | ood|logprob|1|probe|probe - probe|out | probes after retrieval, given probes before | 6995 | +0.000 [-0.014, +0.015] | 0.9865 | 1.0000 | -0.009 | -0.013 |
| v6_llama3.3_70b | ood|logprob|1|probe|probe - out|probe | probes before retrieval, given probes after | 6995 | -0.000 [-0.007, +0.006] | 0.9044 | 1.0000 | -0.007 | -0.008 |
| v6_llama3.3_70b | ood|logprob|1|out|probe - out|out | probes after retrieval, given output signal before | 6995 | +0.002 [-0.012, +0.017] | 0.7371 | 1.0000 | +0.013 | +0.007 |
| v6_llama3.3_70b | ood|logprob|1|probe|out - out|out | probes before retrieval, given output signal after | 6995 | +0.002 [-0.009, +0.013] | 0.7286 | 1.0000 | +0.014 | +0.011 |
| v6_llama3.3_70b | test|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 3175 | +0.150 [+0.123, +0.178] | 0.0001 | 0.0030 | +0.066 | -0.045 |
| v6_llama3.3_70b | test|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 3175 | +0.094 [+0.071, +0.117] | 0.0001 | 0.0030 | +0.026 | -0.035 |
| v6_llama3.3_70b | test|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 3175 | +0.001 [-0.010, +0.013] | 0.8136 | 1.0000 | -0.016 | -0.009 |
| v6_llama3.3_70b | test|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 3175 | +0.148 [+0.123, +0.173] | 0.0001 | 0.0030 | +0.082 | -0.036 |
| v6_llama3.3_70b | test|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 3175 | +0.056 [+0.032, +0.081] | 0.0001 | 0.0030 | +0.040 | -0.009 |
| v6_llama3.3_70b | ood|logprob|2|probe|probe - out|out | both halves (the existing ablation) | 6995 | +0.007 [-0.016, +0.031] | 0.5254 | 1.0000 | +0.047 | +0.017 |
| v6_llama3.3_70b | ood|logprob|2|probe|probe - probe|out | probes after retrieval, given probes before | 6995 | -0.034 [-0.055, -0.013] | 0.0019 | 0.0361 | +0.018 | +0.025 |
| v6_llama3.3_70b | ood|logprob|2|probe|probe - out|probe | probes before retrieval, given probes after | 6995 | +0.005 [-0.003, +0.014] | 0.2218 | 1.0000 | -0.011 | -0.009 |
| v6_llama3.3_70b | ood|logprob|2|out|probe - out|out | probes after retrieval, given output signal before | 6995 | +0.002 [-0.020, +0.024] | 0.8557 | 1.0000 | +0.058 | +0.026 |
| v6_llama3.3_70b | ood|logprob|2|probe|out - out|out | probes before retrieval, given output signal after | 6995 | +0.041 [+0.023, +0.058] | 0.0001 | 0.0030 | +0.028 | -0.008 |
| v6_llama3.3_70b | test|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 3175 | +0.199 [+0.165, +0.232] | 0.0001 | 0.0030 | +0.180 | -0.005 |
| v6_llama3.3_70b | test|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 3175 | +0.111 [+0.075, +0.146] | 0.0001 | 0.0030 | -0.025 | -0.035 |
| v6_llama3.3_70b | test|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 3175 | -0.006 [-0.018, +0.006] | 0.3567 | 1.0000 | +0.011 | +0.005 |
| v6_llama3.3_70b | test|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 3175 | +0.205 [+0.172, +0.238] | 0.0001 | 0.0030 | +0.169 | -0.010 |
| v6_llama3.3_70b | test|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 3175 | +0.088 [+0.049, +0.128] | 0.0001 | 0.0030 | +0.206 | +0.030 |
| v6_llama3.3_70b | ood|logprob|4|probe|probe - out|out | both halves (the existing ablation) | 6995 | -0.045 [-0.074, -0.017] | 0.0026 | 0.0442 | +0.090 | +0.034 |
| v6_llama3.3_70b | ood|logprob|4|probe|probe - probe|out | probes after retrieval, given probes before | 6995 | +0.055 [+0.026, +0.085] | 0.0003 | 0.0072 | -0.026 | -0.021 |
| v6_llama3.3_70b | ood|logprob|4|probe|probe - out|probe | probes before retrieval, given probes after | 6995 | -0.013 [-0.022, -0.004] | 0.0038 | 0.0608 | +0.006 | +0.005 |
| v6_llama3.3_70b | ood|logprob|4|out|probe - out|out | probes after retrieval, given output signal before | 6995 | -0.032 [-0.061, -0.003] | 0.0293 | 0.3809 | +0.084 | +0.028 |
| v6_llama3.3_70b | ood|logprob|4|probe|out - out|out | probes before retrieval, given output signal after | 6995 | -0.101 [-0.131, -0.071] | 0.0001 | 0.0030 | +0.116 | +0.054 |
| v6_llama3.3_70b | test|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 3175 | +0.089 [+0.069, +0.108] | 0.0001 | 0.0030 | -0.027 | -0.120 |
| v6_llama3.3_70b | test|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 3175 | +0.052 [+0.034, +0.069] | 0.0001 | 0.0030 | -0.017 | -0.073 |
| v6_llama3.3_70b | test|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 3175 | -0.000 [-0.013, +0.012] | 0.9666 | 1.0000 | -0.026 | -0.029 |
| v6_llama3.3_70b | test|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 3175 | +0.089 [+0.075, +0.104] | 0.0001 | 0.0030 | -0.001 | -0.091 |
| v6_llama3.3_70b | test|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 3175 | +0.037 [+0.020, +0.055] | 0.0002 | 0.0030 | -0.010 | -0.047 |
| v6_llama3.3_70b | ood|entropy|1|probe|probe - out|out | both halves (the existing ablation) | 6995 | +0.041 [+0.027, +0.056] | 0.0001 | 0.0030 | -0.035 | -0.081 |
| v6_llama3.3_70b | ood|entropy|1|probe|probe - probe|out | probes after retrieval, given probes before | 6995 | -0.003 [-0.017, +0.011] | 0.6837 | 1.0000 | -0.009 | -0.010 |
| v6_llama3.3_70b | ood|entropy|1|probe|probe - out|probe | probes before retrieval, given probes after | 6995 | +0.010 [+0.001, +0.018] | 0.0243 | 0.3402 | -0.015 | -0.028 |
| v6_llama3.3_70b | ood|entropy|1|out|probe - out|out | probes after retrieval, given output signal before | 6995 | +0.032 [+0.019, +0.045] | 0.0001 | 0.0030 | -0.020 | -0.053 |
| v6_llama3.3_70b | ood|entropy|1|probe|out - out|out | probes before retrieval, given output signal after | 6995 | +0.044 [+0.031, +0.058] | 0.0001 | 0.0030 | -0.027 | -0.072 |
| v6_llama3.3_70b | test|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 3175 | +0.155 [+0.128, +0.181] | 0.0001 | 0.0030 | +0.102 | -0.028 |
| v6_llama3.3_70b | test|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 3175 | +0.093 [+0.070, +0.116] | 0.0001 | 0.0030 | +0.028 | -0.034 |
| v6_llama3.3_70b | test|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 3175 | +0.001 [-0.010, +0.013] | 0.8241 | 1.0000 | -0.014 | -0.008 |
| v6_llama3.3_70b | test|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 3175 | +0.153 [+0.129, +0.177] | 0.0001 | 0.0030 | +0.116 | -0.020 |
| v6_llama3.3_70b | test|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 3175 | +0.062 [+0.040, +0.085] | 0.0001 | 0.0030 | +0.075 | +0.006 |
| v6_llama3.3_70b | ood|entropy|2|probe|probe - out|out | both halves (the existing ablation) | 6995 | -0.037 [-0.059, -0.016] | 0.0007 | 0.0147 | +0.076 | +0.055 |
| v6_llama3.3_70b | ood|entropy|2|probe|probe - probe|out | probes after retrieval, given probes before | 6995 | -0.036 [-0.056, -0.016] | 0.0006 | 0.0132 | +0.019 | +0.027 |
| v6_llama3.3_70b | ood|entropy|2|probe|probe - out|probe | probes before retrieval, given probes after | 6995 | +0.003 [-0.005, +0.011] | 0.4828 | 1.0000 | -0.010 | -0.007 |
| v6_llama3.3_70b | ood|entropy|2|out|probe - out|out | probes after retrieval, given output signal before | 6995 | -0.040 [-0.061, -0.019] | 0.0003 | 0.0072 | +0.086 | +0.062 |
| v6_llama3.3_70b | ood|entropy|2|probe|out - out|out | probes before retrieval, given output signal after | 6995 | -0.001 [-0.018, +0.016] | 0.9159 | 1.0000 | +0.057 | +0.028 |
| v6_llama3.3_70b | test|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 3175 | +0.211 [+0.179, +0.244] | 0.0001 | 0.0030 | +0.213 | +0.000 |
| v6_llama3.3_70b | test|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 3175 | +0.102 [+0.072, +0.132] | 0.0001 | 0.0030 | +0.045 | -0.015 |
| v6_llama3.3_70b | test|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 3175 | -0.006 [-0.018, +0.006] | 0.3596 | 1.0000 | +0.011 | +0.005 |
| v6_llama3.3_70b | test|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 3175 | +0.217 [+0.185, +0.248] | 0.0001 | 0.0030 | +0.202 | -0.005 |
| v6_llama3.3_70b | test|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 3175 | +0.109 [+0.073, +0.146] | 0.0001 | 0.0030 | +0.168 | +0.015 |
| v6_llama3.3_70b | ood|entropy|4|probe|probe - out|out | both halves (the existing ablation) | 6995 | -0.058 [-0.087, -0.028] | 0.0001 | 0.0030 | +0.104 | +0.040 |
| v6_llama3.3_70b | ood|entropy|4|probe|probe - probe|out | probes after retrieval, given probes before | 6995 | -0.015 [-0.041, +0.013] | 0.2765 | 1.0000 | +0.039 | +0.013 |
| v6_llama3.3_70b | ood|entropy|4|probe|probe - out|probe | probes before retrieval, given probes after | 6995 | -0.013 [-0.022, -0.004] | 0.0046 | 0.0690 | +0.006 | +0.005 |
| v6_llama3.3_70b | ood|entropy|4|out|probe - out|out | probes after retrieval, given output signal before | 6995 | -0.045 [-0.073, -0.017] | 0.0019 | 0.0361 | +0.098 | +0.035 |
| v6_llama3.3_70b | ood|entropy|4|probe|out - out|out | probes before retrieval, given output signal after | 6995 | -0.043 [-0.069, -0.016] | 0.0008 | 0.0160 | +0.064 | +0.027 |

### Pure cells vs policy.json (route / route@signal), TEST

| model | key | stored family | acc dev | halluc dev |
|---|---|---|---|---|
| v5_qwen2.5_7b | logprob|1|probe|probe | route | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | logprob|1|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | logprob|2|probe|probe | route | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | logprob|2|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | logprob|4|probe|probe | route | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | logprob|4|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | entropy|1|probe|probe | route | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | entropy|1|out|out | route@entropy | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | entropy|2|probe|probe | route | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | entropy|2|out|out | route@entropy | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | entropy|4|probe|probe | route | 0.0000 | 0.0000 |
| v5_qwen2.5_7b | entropy|4|out|out | route@entropy | 0.0000 | 0.0000 |
| v5_llama3.1_8b | logprob|1|probe|probe | route | 0.0000 | 0.0000 |
| v5_llama3.1_8b | logprob|1|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_llama3.1_8b | logprob|2|probe|probe | route | 0.0000 | 0.0000 |
| v5_llama3.1_8b | logprob|2|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_llama3.1_8b | logprob|4|probe|probe | route | 0.0000 | 0.0000 |
| v5_llama3.1_8b | logprob|4|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_llama3.1_8b | entropy|1|probe|probe | route | 0.0000 | 0.0000 |
| v5_llama3.1_8b | entropy|1|out|out | route@entropy | 0.0000 | 0.0000 |
| v5_llama3.1_8b | entropy|2|probe|probe | route | 0.0000 | 0.0000 |
| v5_llama3.1_8b | entropy|2|out|out | route@entropy | 0.0000 | 0.0000 |
| v5_llama3.1_8b | entropy|4|probe|probe | route | 0.0000 | 0.0000 |
| v5_llama3.1_8b | entropy|4|out|out | route@entropy | 0.0000 | 0.0000 |
| v5_mistral_7b | logprob|1|probe|probe | route | 0.0000 | 0.0000 |
| v5_mistral_7b | logprob|1|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_mistral_7b | logprob|2|probe|probe | route | 0.0000 | 0.0000 |
| v5_mistral_7b | logprob|2|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_mistral_7b | logprob|4|probe|probe | route | 0.0000 | 0.0000 |
| v5_mistral_7b | logprob|4|out|out | route@logprob | 0.0000 | 0.0000 |
| v5_mistral_7b | entropy|1|probe|probe | route | 0.0000 | 0.0000 |
| v5_mistral_7b | entropy|1|out|out | route@entropy | 0.0000 | 0.0000 |
| v5_mistral_7b | entropy|2|probe|probe | route | 0.0000 | 0.0000 |
| v5_mistral_7b | entropy|2|out|out | route@entropy | 0.0000 | 0.0000 |
| v5_mistral_7b | entropy|4|probe|probe | route | 0.0000 | 0.0000 |
| v5_mistral_7b | entropy|4|out|out | route@entropy | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | logprob|1|probe|probe | route | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | logprob|1|out|out | route@logprob | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | logprob|2|probe|probe | route | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | logprob|2|out|out | route@logprob | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | logprob|4|probe|probe | route | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | logprob|4|out|out | route@logprob | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | entropy|1|probe|probe | route | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | entropy|1|out|out | route@entropy | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | entropy|2|probe|probe | route | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | entropy|2|out|out | route@entropy | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | entropy|4|probe|probe | route | 0.0000 | 0.0000 |
| v4_qwen2.5_32b | entropy|4|out|out | route@entropy | 0.0000 | 0.0000 |
| v6_llama3.3_70b | logprob|1|probe|probe | route | 0.0000 | 0.0000 |
| v6_llama3.3_70b | logprob|1|out|out | route@logprob | 0.0000 | 0.0000 |
| v6_llama3.3_70b | logprob|2|probe|probe | route | 0.0000 | 0.0000 |
| v6_llama3.3_70b | logprob|2|out|out | route@logprob | 0.0000 | 0.0000 |
| v6_llama3.3_70b | logprob|4|probe|probe | route | 0.0000 | 0.0000 |
| v6_llama3.3_70b | logprob|4|out|out | route@logprob | 0.0000 | 0.0000 |
| v6_llama3.3_70b | entropy|1|probe|probe | route | 0.0000 | 0.0000 |
| v6_llama3.3_70b | entropy|1|out|out | route@entropy | 0.0000 | 0.0000 |
| v6_llama3.3_70b | entropy|2|probe|probe | route | 0.0000 | 0.0000 |
| v6_llama3.3_70b | entropy|2|out|out | route@entropy | 0.0000 | 0.0000 |
| v6_llama3.3_70b | entropy|4|probe|probe | route | 0.0000 | 0.0000 |
| v6_llama3.3_70b | entropy|4|out|out | route@entropy | 0.0000 | 0.0000 |

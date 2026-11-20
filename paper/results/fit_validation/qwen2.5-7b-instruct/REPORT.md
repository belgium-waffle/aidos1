# Bundle for Qwen/Qwen2.5-7B-Instruct

Made by `aidos fit` on 2026-11-20 12:37:49; splits {'train': 7978, 'val': 2458, 'cal': 2348, 'test': 3216}; layers [14, 18, 21].

| head | val AUROC | test AUROC |
|---|---|---|
| pre | 0.901 | 0.893 |
| post | 0.923 | 0.913 |
| help | 0.830 | 0.824 |
| pre_rag | 0.897 | 0.887 |
| post_rag | 0.907 | 0.900 |

Offline estimate on test questions (utility = accuracy - λ·hallucination - 0.02·retrievals):

| λ | Aidos utility | accuracy | hallucination | abstain | retrieval rate | closed-book | always retrieve |
|---|---|---|---|---|---|---|---|
| 0.1 | 0.534 | 0.574 | 0.232 | 0.194 | 0.83 | 0.304 | 0.507 |
| 0.25 | 0.501 | 0.558 | 0.163 | 0.279 | 0.84 | 0.210 | 0.442 |
| 0.5 | 0.456 | 0.528 | 0.115 | 0.357 | 0.73 | 0.052 | 0.335 |
| 1 | 0.394 | 0.478 | 0.070 | 0.451 | 0.70 | -0.262 | 0.120 |
| 2 | 0.321 | 0.406 | 0.036 | 0.558 | 0.62 | -0.892 | -0.310 |
| 4 | 0.227 | 0.318 | 0.020 | 0.662 | 0.64 | -2.151 | -1.170 |

Check the engine on your GPU: `aidos verify --model MODEL --bundle THIS_DIR`.

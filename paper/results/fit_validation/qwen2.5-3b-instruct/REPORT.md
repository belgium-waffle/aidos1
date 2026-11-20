# Bundle for Qwen/Qwen2.5-3B-Instruct

Made by `aidos fit` on 2026-11-20 12:43:57; splits {'train': 7978, 'val': 2458, 'cal': 2348, 'test': 3216}; layers [18, 22, 27].

| head | val AUROC | test AUROC |
|---|---|---|
| pre | 0.870 | 0.862 |
| post | 0.920 | 0.920 |
| help | 0.808 | 0.814 |
| pre_rag | 0.872 | 0.868 |
| post_rag | 0.897 | 0.898 |

Offline estimate on test questions (utility = accuracy - λ·hallucination - 0.02·retrievals):

| λ | Aidos utility | accuracy | hallucination | abstain | retrieval rate | closed-book | always retrieve |
|---|---|---|---|---|---|---|---|
| 0.1 | 0.477 | 0.522 | 0.273 | 0.205 | 0.88 | 0.213 | 0.454 |
| 0.25 | 0.438 | 0.502 | 0.187 | 0.311 | 0.88 | 0.106 | 0.382 |
| 0.5 | 0.389 | 0.462 | 0.118 | 0.420 | 0.75 | -0.072 | 0.263 |
| 1 | 0.321 | 0.406 | 0.071 | 0.523 | 0.72 | -0.428 | 0.024 |
| 2 | 0.236 | 0.330 | 0.039 | 0.631 | 0.71 | -1.141 | -0.455 |
| 4 | 0.158 | 0.237 | 0.017 | 0.746 | 0.61 | -2.565 | -1.411 |

Check the engine on your GPU: `aidos verify --model MODEL --bundle THIS_DIR`.

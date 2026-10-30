### Sentence-level detection on the model's own biographies (vanilla answers; label = any unsupported atomic fact)

| signal | val AUROC | test AUROC | threshold (Youden on val) |
|---|---|---|---|
| Tripwire long-form head (max risk in the sentence) | 0.842 | 0.863 | tau = 0.4512 |
| FLARE (1 - min token probability) | 0.421 | 0.185 | theta = 0.6021 |

Sentences: {'val': 26, 'test': 39}; unsupported rate {'val': 0.7307692307692307, 'test': 0.7948717948717948}

### Biographies, test people (FActScore protocol, local judge)

| method | FActScore | FActScore (length pen.) | facts / answer | supported | unsupported | rare | medium | frequent | retrievals | prefill tok | decode tok | answers / s |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| vanilla | 0.433 | 0.337 | 10.1 | 5.2 | 4.9 | 0.328 | 0.272 | 0.680 | 0.00 | 39 | 100 | 55.04 |
| rag (always, up front) | 0.894 | 0.785 | 11.6 | 10.3 | 1.2 | 0.908 | 0.918 | 0.858 | 1.00 | 439 | 143 | 12.42 |
| flare | 0.794 | 0.718 | 12.4 | 9.7 | 2.7 | 0.722 | 0.838 | 0.823 | 2.92 | 1310 | 223 | 4.40 |
| tripwire lf-retrieve | 0.933 | 0.583 | 8.1 | 7.5 | 0.7 | 0.937 | 0.974 | 0.891 | 2.38 | 1278 | 104 | 1.60 |

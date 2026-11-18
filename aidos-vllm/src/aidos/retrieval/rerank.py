"""Cross-encoder reranking: BM25 finds candidates cheaply, a cross-encoder orders them.

BM25 recall@3 on PopQA was 0.35 (32B v2 run), and retrieval fixed only 26.6% of
knowledge-gap errors: the evidence, not the routing, was the bottleneck. A cross-encoder
reads query and passage together, so it can rank the passage that ANSWERS the question
above passages that merely share its words. Standard two-stage setup: BM25 top-N
(rerank_depth) -> cross-encoder -> top-k.

Model: BAAI/bge-reranker-v2-m3 by default (any HF sequence-classification cross-encoder
with one relevance logit works). fp16 on GPU; pairs are sorted by length so batches
carry little padding.
"""

from __future__ import annotations

from ..utils import get_logger

log = get_logger("aidos.rerank")


def passage_text(p: dict) -> str:
    return f"{p.get('title', '')}: {p.get('text', '')}".strip(": ")


def rerank_lists(score_fn, queries: list[str], cands: list[list[dict]], k: int) -> list[list[dict]]:
    """Order every candidate list by score_fn(pairs) -> list[float] (higher = more
    relevant), keep the top k. Passages get "rerank" (score) and "bm25_rank" fields.
    Pure logic, independent of the model (unit-tested with a fake scorer)."""
    pairs, owner = [], []
    for qi, (q, ps) in enumerate(zip(queries, cands)):
        for pi, p in enumerate(ps):
            pairs.append((q, passage_text(p)))
            owner.append((qi, pi))
    scores = score_fn(pairs) if pairs else []
    per_q: list[list[tuple[float, int]]] = [[] for _ in queries]
    for (qi, pi), s in zip(owner, scores):
        per_q[qi].append((float(s), pi))
    out = []
    for qi, ps in enumerate(cands):
        ranked = sorted(per_q[qi], key=lambda t: (-t[0], t[1]))[:k]  # ties: keep BM25 order
        out.append([{**ps[pi], "rerank": s, "bm25_rank": pi} for s, pi in ranked])
    return out


class CrossEncoderReranker:
    def __init__(self, model_name: str, batch_size: int = 128, max_length: int = 384, device: str | None = None):
        import torch
        from transformers import AutoModelForSequenceClassification, AutoTokenizer

        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        self.tok = AutoTokenizer.from_pretrained(model_name)
        dtype = torch.float16 if self.device == "cuda" else torch.float32
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name, torch_dtype=dtype).to(self.device).eval()
        self.batch_size, self.max_length = batch_size, max_length
        log.info("reranker %s on %s", model_name, self.device)

    def score(self, pairs: list[tuple[str, str]]) -> list[float]:
        import torch

        order = sorted(range(len(pairs)), key=lambda i: len(pairs[i][0]) + len(pairs[i][1]))
        out = [0.0] * len(pairs)
        with torch.inference_mode():
            for s in range(0, len(order), self.batch_size):
                idx = order[s : s + self.batch_size]
                enc = self.tok([pairs[i][0] for i in idx], [pairs[i][1] for i in idx], padding=True,
                               truncation="only_second", max_length=self.max_length, return_tensors="pt").to(self.device)
                logits = self.model(**enc).logits.view(len(idx), -1)[:, 0].float().cpu().tolist()
                for i, v in zip(idx, logits):
                    out[i] = v
        return out

    def rerank(self, queries: list[str], cands: list[list[dict]], k: int, chunk: int = 512) -> list[list[dict]]:
        out = []
        for i in range(0, len(queries), chunk):
            out.extend(rerank_lists(self.score, queries[i : i + chunk], cands[i : i + chunk], k))
            if (i // chunk) % 10 == 0:
                log.info("reranked %d/%d", min(i + chunk, len(queries)), len(queries))
        return out

    def close(self) -> None:
        """Free the GPU before vLLM starts (it sizes its KV cache from free memory)."""
        import gc

        import torch

        del self.model
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()


def make_reranker(cfg):
    rc = cfg.retrieval
    if not rc.rerank_model:
        return None
    return CrossEncoderReranker(rc.rerank_model, rc.rerank_batch, rc.rerank_max_length)

"""Runtime head bank: loads head_<kind>.pt (up to 8 kinds) and folds them into one [K, L, H] bank.

Heads may use different layers; the bank uses the union of layers and zero-fills the
weights a head does not use, so one aux capture + one kernel launch serves both.
"""

from __future__ import annotations

from pathlib import Path

import torch

from ..probe.head import LinearBoolHead

# post: "the token just read is part of a hallucination" (drives rollback)
# pre : "my answer to this prompt will be wrong"         (drives abstain / retrieve)
# know: "P(I can produce the right answer)"  regressed on sample accuracy; separates a
#       knowledge gap (retrieve) from generation drift (resample)
# help: "my answer WITH retrieved evidence will be wrong"  (pre row; route-eu)
# pre_rag / post_rag: pre / post trained with evidence in context (used after an insertion)
# gain: "retrieval turns my wrong answer into a right one"  (pre row; route-eu)
# harm: "retrieval turns my right answer into a wrong one"  (pre row; route-eu)
KINDS = ("post", "pre", "know", "help", "pre_rag", "post_rag", "gain", "harm")


class HeadBank:
    def __init__(self, payloads: dict[str, dict]):
        if not payloads:
            raise ValueError("no heads found")
        heads = {k: LinearBoolHead.from_payload(p) for k, p in payloads.items()}
        hidden = {h.hidden for h in heads.values()}
        if len(hidden) != 1:
            raise ValueError(f"heads disagree on hidden size: {hidden}")
        self.hidden = hidden.pop()
        self.kinds = [k for k in KINDS if k in heads]
        self.layers = sorted(set().union(*(h.layers for h in heads.values())))
        K, L = len(self.kinds), len(self.layers)
        W = torch.zeros(K, L, self.hidden, dtype=torch.float32)
        b = torch.zeros(K, dtype=torch.float32)
        for k, kind in enumerate(self.kinds):
            w_f, b_f = heads[kind].folded()
            for j, layer in enumerate(heads[kind].layers):
                W[k, self.layers.index(layer)] = w_f[j]
            b[k] = b_f
        self.W, self.b = W.contiguous(), b.contiguous()
        self.taus = {k: payloads[k].get("tau") for k in self.kinds}
        self.model = next(iter(payloads.values())).get("model")

    @staticmethod
    def _payloads(head_dir: str | Path, post_head: str = "post") -> dict[str, dict]:
        """post_head: the file that serves as the post head (e.g. "post_lf", the long-form
        entity head of the lf-train stage, which shares the deployed layers)."""
        out = {}
        for kind in KINDS:
            p = Path(head_dir) / f"head_{post_head if kind == 'post' else kind}.pt"
            if p.exists():
                out[kind] = torch.load(p, map_location="cpu", weights_only=True)
        return out

    @classmethod
    def from_dir(cls, head_dir: str | Path, post_head: str = "post") -> "HeadBank":
        return cls(cls._payloads(head_dir, post_head))

    @classmethod
    def read_taus(cls, head_dir: str | Path, post_head: str = "post") -> dict[str, float | None]:
        return {k: p.get("tau") for k, p in cls._payloads(head_dir, post_head).items()}

    @staticmethod
    def read_mondrian(head_dir: str | Path) -> dict | None:
        """Post-head taus per pre-risk group (written by the train-rag stage), if any."""
        p = Path(head_dir) / "head_post.pt"
        return torch.load(p, map_location="cpu", weights_only=True).get("mondrian") if p.exists() else None

    def to(self, device) -> "HeadBank":
        self.W = self.W.to(device)
        self.b = self.b.to(device)
        return self

    def index(self, kind: str) -> int | None:
        return self.kinds.index(kind) if kind in self.kinds else None

    @property
    def num_heads(self) -> int:
        return len(self.kinds)

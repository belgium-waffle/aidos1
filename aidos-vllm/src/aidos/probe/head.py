"""The System-One head: a calibrated, typed Bool decision over residual-stream features.

    risk = sigmoid( a * ( sum_l <(h_l - mu_l) / sd_l, w_l> + b ) + c )

It is linear on purpose:
  * standardization, Platt scaling and the weights fold into ONE vector per layer, so
    in-engine scoring is a single gathered GEMV (see aidos.kernels.score);
  * linear probes are already strong for this task, and they keep calibration stable;
  * it trains in seconds, so a full layer sweep is cheap.
"""

from __future__ import annotations

from pathlib import Path

import torch
from torch import nn

HEAD_FORMAT = "aidos-head-v1"


class LinearBoolHead(nn.Module):
    def __init__(self, layers: list[int], hidden: int):
        super().__init__()
        self.layers = [int(l) for l in layers]
        self.hidden = int(hidden)
        L = len(self.layers)
        self.register_buffer("mu", torch.zeros(L, hidden))
        self.register_buffer("sd", torch.ones(L, hidden))
        self.w = nn.Parameter(torch.zeros(L, hidden))
        self.b = nn.Parameter(torch.zeros(()))
        self.register_buffer("platt_a", torch.ones(()))
        self.register_buffer("platt_c", torch.zeros(()))

    # ---- training-time API -------------------------------------------------
    @torch.no_grad()
    def fit_standardizer(self, x: torch.Tensor, chunk: int = 8192) -> None:
        """x: [N, L, H] (any float dtype, any device). Streams in chunks to save memory."""
        dev = self.mu.device
        s = torch.zeros_like(self.mu, dtype=torch.float64)
        ss = torch.zeros_like(self.mu, dtype=torch.float64)
        n = 0
        for i in range(0, x.shape[0], chunk):
            xb = x[i : i + chunk].to(dev, dtype=torch.float64)
            s += xb.sum(0)
            ss += (xb * xb).sum(0)
            n += xb.shape[0]
        mean = s / max(n, 1)
        var = (ss / max(n, 1) - mean * mean).clamp_min(0)
        self.mu.copy_(mean.float())
        self.sd.copy_(var.sqrt().float().clamp_min(1e-3))

    def raw_logits(self, x: torch.Tensor) -> torch.Tensor:
        """Uncalibrated logit. x: [N, L, H]."""
        z = (x.float() - self.mu) / self.sd
        return (z * self.w).sum(dim=(-1, -2)) + self.b

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        """Calibrated logit."""
        return self.platt_a * self.raw_logits(x) + self.platt_c

    def set_platt(self, a: float, c: float) -> None:
        self.platt_a.fill_(a)
        self.platt_c.fill_(c)

    # ---- deployment API ----------------------------------------------------
    @torch.no_grad()
    def folded(self) -> tuple[torch.Tensor, torch.Tensor]:
        """(w_f [L, H] fp32, b_f scalar) with calibrated_logit(x) == <x, w_f> + b_f."""
        a, c = self.platt_a.double(), self.platt_c.double()
        w = self.w.double()
        mu, sd = self.mu.double(), self.sd.double()
        w_f = a * w / sd
        b_f = a * (self.b.double() - (w * mu / sd).sum()) + c
        return w_f.float(), b_f.float()

    def save(self, path: str | Path, **meta) -> None:
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        torch.save(
            {
                "format": HEAD_FORMAT,
                "layers": self.layers,
                "hidden": self.hidden,
                "state_dict": {k: v.detach().cpu() for k, v in self.state_dict().items()},
                **meta,
            },
            path,
        )

    @classmethod
    def from_payload(cls, payload: dict) -> "LinearBoolHead":
        if payload.get("format") != HEAD_FORMAT:
            raise ValueError(f"not an aidos head file (format={payload.get('format')})")
        head = cls(payload["layers"], payload["hidden"])
        head.load_state_dict(payload["state_dict"])
        return head

    @classmethod
    def load(cls, path: str | Path) -> tuple["LinearBoolHead", dict]:
        payload = torch.load(path, map_location="cpu", weights_only=True)
        return cls.from_payload(payload), payload

    def trainable(self) -> list[nn.Parameter]:
        return [self.w, self.b]


class MLPBoolHead(LinearBoolHead):
    """Ablation only (offline): a 1-hidden-layer MLP over the same standardized features.
    It cannot be folded into the engine's GEMV; it answers "is linear enough?"."""

    def __init__(self, layers: list[int], hidden: int, width: int = 256, dropout: float = 0.1):
        super().__init__(layers, hidden)
        self.net = nn.Sequential(
            nn.Linear(len(self.layers) * hidden, width), nn.GELU(), nn.Dropout(dropout), nn.Linear(width, 1)
        )

    def raw_logits(self, x: torch.Tensor) -> torch.Tensor:
        z = ((x.float() - self.mu) / self.sd).flatten(1)
        return self.net(z).squeeze(-1) + self.b

    def folded(self):
        raise NotImplementedError("MLP heads are offline ablations; the engine needs a linear head")

    def trainable(self) -> list[nn.Parameter]:
        return [*self.net.parameters(), self.b]

"""Fused multi-layer gather-GEMV for the verifier heads.

Inputs per decode step:
    aux  : list of NL tensors [T_padded, H] (bf16/fp16) - residual stream at NL layers
    rows : [R] int64 - which token rows to score (the last scheduled token of each request)
    W    : [K, NL, H] fp32 - folded head weights (standardization + Platt already folded in)
    b    : [K] fp32
Output:
    probs: [R, K] fp32 = sigmoid( sum_l <aux_l[rows], W[:, l]> + b )

PyTorch eager does: NL index_selects -> stack (materializes [R, NL, H]) -> upcast ->
einsum -> add -> sigmoid: ~6 kernel launches and an extra round-trip through HBM.
The Triton kernel does it in ONE launch: each program owns one row, streams the NL
hidden vectors straight from the aux buffers (no concat), accumulates up to eight heads
(post, pre, know, help, pre_rag, post_rag, gain, harm) in fp32 registers, and writes the probabilities.
Every hidden vector is read once whatever the number of heads, so extra heads cost FMAs,
not memory traffic. At decode batch sizes the
whole thing is launch-latency bound, so cutting launches is what matters.
"""

from __future__ import annotations

import torch

try:  # Triton is optional (CPU-only dev boxes, Windows without triton-windows)
    import triton
    import triton.language as tl

    HAS_TRITON = True
except Exception:  # pragma: no cover - environment dependent
    HAS_TRITON = False

MAX_LAYERS = 4
MAX_HEADS = 8  # post, pre, know, help, pre_rag, post_rag, gain, harm


def head_scores_torch(aux: list[torch.Tensor], rows: torch.Tensor, W: torch.Tensor, b: torch.Tensor) -> torch.Tensor:
    """Reference implementation (also the fallback)."""
    x = torch.stack([a.index_select(0, rows) for a in aux], dim=1).float()  # [R, NL, H]
    logits = torch.einsum("rlh,klh->rk", x, W) + b
    return torch.sigmoid(logits)


if HAS_TRITON:

    @triton.jit
    def _aidos_score_kernel(
        X0, X1, X2, X3,  # aux layer buffers (unused slots alias X0)
        S0, S1, S2, S3,  # row strides (elements)
        ROWS, W, B, OUT,
        H,
        NL: tl.constexpr,
        K: tl.constexpr,
        BLOCK: tl.constexpr,
    ):
        pid = tl.program_id(0)
        row = tl.load(ROWS + pid).to(tl.int64)
        offs = tl.arange(0, BLOCK)
        acc0 = tl.zeros([BLOCK], dtype=tl.float32)
        acc1 = tl.zeros([BLOCK], dtype=tl.float32)
        acc2 = tl.zeros([BLOCK], dtype=tl.float32)
        acc3 = tl.zeros([BLOCK], dtype=tl.float32)
        acc4 = tl.zeros([BLOCK], dtype=tl.float32)
        acc5 = tl.zeros([BLOCK], dtype=tl.float32)
        acc6 = tl.zeros([BLOCK], dtype=tl.float32)
        acc7 = tl.zeros([BLOCK], dtype=tl.float32)
        for l in tl.static_range(NL):
            if l == 0:
                base = X0 + row * S0
            elif l == 1:
                base = X1 + row * S1
            elif l == 2:
                base = X2 + row * S2
            else:
                base = X3 + row * S3
            for h0 in range(0, H, BLOCK):
                cols = h0 + offs
                m = cols < H
                x = tl.load(base + cols, mask=m, other=0.0).to(tl.float32)
                acc0 += x * tl.load(W + (0 * NL + l) * H + cols, mask=m, other=0.0)
                if K > 1:
                    acc1 += x * tl.load(W + (1 * NL + l) * H + cols, mask=m, other=0.0)
                if K > 2:
                    acc2 += x * tl.load(W + (2 * NL + l) * H + cols, mask=m, other=0.0)
                if K > 3:
                    acc3 += x * tl.load(W + (3 * NL + l) * H + cols, mask=m, other=0.0)
                if K > 4:
                    acc4 += x * tl.load(W + (4 * NL + l) * H + cols, mask=m, other=0.0)
                if K > 5:
                    acc5 += x * tl.load(W + (5 * NL + l) * H + cols, mask=m, other=0.0)
                if K > 6:
                    acc6 += x * tl.load(W + (6 * NL + l) * H + cols, mask=m, other=0.0)
                if K > 7:
                    acc7 += x * tl.load(W + (7 * NL + l) * H + cols, mask=m, other=0.0)
        z0 = tl.sum(acc0, axis=0) + tl.load(B + 0)
        tl.store(OUT + pid * K + 0, 1.0 / (1.0 + tl.exp(-z0)))
        if K > 1:
            z1 = tl.sum(acc1, axis=0) + tl.load(B + 1)
            tl.store(OUT + pid * K + 1, 1.0 / (1.0 + tl.exp(-z1)))
        if K > 2:
            z2 = tl.sum(acc2, axis=0) + tl.load(B + 2)
            tl.store(OUT + pid * K + 2, 1.0 / (1.0 + tl.exp(-z2)))
        if K > 3:
            z3 = tl.sum(acc3, axis=0) + tl.load(B + 3)
            tl.store(OUT + pid * K + 3, 1.0 / (1.0 + tl.exp(-z3)))
        if K > 4:
            z4 = tl.sum(acc4, axis=0) + tl.load(B + 4)
            tl.store(OUT + pid * K + 4, 1.0 / (1.0 + tl.exp(-z4)))
        if K > 5:
            z5 = tl.sum(acc5, axis=0) + tl.load(B + 5)
            tl.store(OUT + pid * K + 5, 1.0 / (1.0 + tl.exp(-z5)))
        if K > 6:
            z6 = tl.sum(acc6, axis=0) + tl.load(B + 6)
            tl.store(OUT + pid * K + 6, 1.0 / (1.0 + tl.exp(-z6)))
        if K > 7:
            z7 = tl.sum(acc7, axis=0) + tl.load(B + 7)
            tl.store(OUT + pid * K + 7, 1.0 / (1.0 + tl.exp(-z7)))


def triton_supported(aux: list[torch.Tensor], W: torch.Tensor) -> bool:
    return (
        HAS_TRITON
        and len(aux) > 0
        and aux[0].is_cuda
        and len(aux) <= MAX_LAYERS
        and W.shape[0] <= MAX_HEADS
    )


def head_scores(
    aux: list[torch.Tensor],
    rows: torch.Tensor,
    W: torch.Tensor,
    b: torch.Tensor,
    use_triton: bool = True,
    block: int = 1024,
) -> torch.Tensor:
    if not (use_triton and triton_supported(aux, W)):
        return head_scores_torch(aux, rows, W, b)
    R = rows.numel()
    K, NL, H = W.shape
    out = torch.empty((R, K), device=aux[0].device, dtype=torch.float32)
    if R == 0:
        return out
    xs = [a if a.stride(-1) == 1 else a.contiguous() for a in aux]
    strides = [x.stride(0) for x in xs]
    while len(xs) < MAX_LAYERS:
        xs.append(xs[0])
        strides.append(strides[0])
    _aidos_score_kernel[(R,)](
        *xs, *strides, rows, W, b, out, H,
        NL=NL, K=K, BLOCK=block, num_warps=4,
    )
    return out

import pytest
import torch

from aidos.engine.heads import HeadBank
from aidos.kernels.score import HAS_TRITON, head_scores, head_scores_torch
from aidos.probe.head import LinearBoolHead


def random_head(layers, hidden, seed=0):
    g = torch.Generator().manual_seed(seed)
    h = LinearBoolHead(layers, hidden)
    with torch.no_grad():
        h.mu.copy_(torch.randn(len(layers), hidden, generator=g))
        h.sd.copy_(torch.rand(len(layers), hidden, generator=g) + 0.5)
        h.w.copy_(torch.randn(len(layers), hidden, generator=g) * 0.05)
        h.b.fill_(0.3)
    h.set_platt(0.7, -0.2)
    return h


def test_folding_is_exact():
    h = random_head([4, 9], 64)
    x = torch.randn(32, 2, 64)
    w_f, b_f = h.folded()
    folded = (x * w_f).sum((-1, -2)) + b_f
    assert torch.allclose(h(x), folded, atol=1e-4)


def test_save_load_roundtrip(tmp_path):
    h = random_head([3], 16)
    h.save(tmp_path / "head_post.pt", kind="post", tau=0.42, model="m")
    h2, payload = LinearBoolHead.load(tmp_path / "head_post.pt")
    x = torch.randn(5, 1, 16)
    assert torch.allclose(h(x), h2(x)) and payload["tau"] == 0.42


def test_head_bank_union_layers(tmp_path):
    hp, hq = random_head([4, 9], 32, 1), random_head([9, 12], 32, 2)
    hp.save(tmp_path / "head_post.pt", kind="post", tau=0.5)
    hq.save(tmp_path / "head_pre.pt", kind="pre", tau=0.6)
    bank = HeadBank.from_dir(tmp_path)
    assert bank.layers == [4, 9, 12] and bank.kinds == ["post", "pre"]
    T = 10
    aux = [torch.randn(T, 32) for _ in bank.layers]
    rows = torch.tensor([0, 3, 9])
    probs = head_scores_torch(aux, rows, bank.W, bank.b)
    # post head reads layers 4, 9 only; pre head reads 9, 12 only
    xp = torch.stack([aux[0][rows], aux[1][rows]], 1)
    xq = torch.stack([aux[1][rows], aux[2][rows]], 1)
    assert torch.allclose(probs[:, 0], torch.sigmoid(hp(xp)), atol=1e-5)
    assert torch.allclose(probs[:, 1], torch.sigmoid(hq(xq)), atol=1e-5)
    assert HeadBank.read_taus(tmp_path) == {"post": 0.5, "pre": 0.6}


def test_head_bank_three_heads(tmp_path):
    for i, k in enumerate(("post", "pre", "know")):
        random_head([4, 9], 32, i).save(tmp_path / f"head_{k}.pt", kind=k, tau=0.1 * (i + 1))
    bank = HeadBank.from_dir(tmp_path)
    assert bank.kinds == ["post", "pre", "know"] and bank.index("know") == 2 and bank.num_heads == 3
    aux = [torch.randn(6, 32) for _ in bank.layers]
    assert head_scores_torch(aux, torch.tensor([1, 5]), bank.W, bank.b).shape == (2, 3)


def test_head_bank_eight_heads_in_kinds_order(tmp_path):
    kinds = ("post", "pre", "know", "help", "pre_rag", "post_rag", "gain", "harm")
    for i, k in enumerate(reversed(kinds)):  # file order must not matter
        random_head([4, 9], 32, i).save(tmp_path / f"head_{k}.pt", kind=k, tau=0.1)
    bank = HeadBank.from_dir(tmp_path)
    assert bank.kinds == list(kinds) and bank.index("harm") == 7 and bank.num_heads == 8
    aux = [torch.randn(6, 32) for _ in bank.layers]
    probs = head_scores_torch(aux, torch.tensor([1, 5]), bank.W, bank.b)
    h = LinearBoolHead.load(tmp_path / "head_help.pt")[0]
    assert torch.allclose(probs[:, 3], torch.sigmoid(h(torch.stack([a[[1, 5]] for a in aux], 1))), atol=1e-5)


def test_mondrian_taus_ride_along_in_the_post_head(tmp_path):
    random_head([4], 16).save(tmp_path / "head_post.pt", kind="post", tau=0.5)
    assert HeadBank.read_mondrian(tmp_path) is None
    pay = torch.load(tmp_path / "head_post.pt", weights_only=True)
    pay["mondrian"] = {"by": "pre", "edges": [0.2, 0.6], "taus": [0.3, 0.5, 0.8]}
    torch.save(pay, tmp_path / "head_post.pt")
    assert HeadBank.read_mondrian(tmp_path)["taus"] == [0.3, 0.5, 0.8]
    assert HeadBank.from_dir(tmp_path).taus == {"post": 0.5}  # still a loadable head


@pytest.mark.skipif(not (HAS_TRITON and torch.cuda.is_available()), reason="needs CUDA + Triton")
@pytest.mark.parametrize("NL,K,H,dtype", [(1, 1, 1536, torch.bfloat16), (3, 2, 5120, torch.bfloat16),
                                          (4, 2, 777, torch.float16), (3, 3, 5120, torch.bfloat16),
                                          (2, 4, 4096, torch.bfloat16), (3, 5, 5120, torch.bfloat16),
                                          (3, 6, 5120, torch.bfloat16), (4, 6, 777, torch.float16),
                                          (3, 7, 5120, torch.bfloat16), (3, 8, 5120, torch.bfloat16),
                                          (4, 8, 777, torch.float16)])
def test_triton_matches_torch(NL, K, H, dtype):
    T, R = 300, 64
    aux = [torch.randn(T, H, device="cuda", dtype=dtype) for _ in range(NL)]
    rows = torch.randperm(T, device="cuda")[:R]
    W = torch.randn(K, NL, H, device="cuda") * 0.02
    b = torch.randn(K, device="cuda")
    ref = head_scores_torch(aux, rows, W, b)
    out = head_scores(aux, rows, W, b, use_triton=True)
    assert torch.allclose(out, ref, atol=2e-4, rtol=1e-3)

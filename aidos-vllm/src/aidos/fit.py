"""aidos fit: train and calibrate a head bundle for your own model.

    aidos fit --model Qwen/Qwen2.5-3B-Instruct --retriever my_corpus.jsonl --out bundles/qwen2.5-3b-instruct

Writes a bundle in the same format as the released ones (head_*.pt, runtime_lam<λ>.json, PROVENANCE.json,
REPORT.md), usable with `aidos config`, `runtime_config` and `aidos verify`. Stages, each cached in --work so an
interrupted run resumes:

  1 generate   closed-book and evidence answers with vLLM (the plugin inactive), labelled by alias matching
  2 features   residual-stream rows with HF transformers: the exact rows the engine scores (the last prompt
               token, each answer token, and the last token of the inserted evidence turn)
  3 heads      a layer sweep on validation data, then the five heads route-eu reads: pre, post, help,
               pre_rag, post_rag (linear; Platt-calibrated on validation data)
  4 calibrate  per λ: answer-level Platt maps for the post heads, and the value of retrieving as a function
               of the help head (the realized utility of the retrieval branch on validation questions,
               binned and fitted non-increasing)
  5 bundle     files + an offline estimate of utility on held-out test questions

Questions: TriviaQA + PopQA by default (downloaded with `datasets`), or your own file (--questions, one
{"question", "answers": [...]} per line). The retriever is the one you will deploy with (a corpus .jsonl,
a BM25 index directory, a query cache, or python:module:factory). One GPU that fits the model is enough;
a 7-8B model takes well under an hour for the default 10,000 questions.
"""

from __future__ import annotations

import argparse
import gc
import json
import math
import os
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

STAGES = ("generate", "features", "heads", "calibrate", "bundle")
CANDIDATE_LAYERS = (0.25, 0.375, 0.5, 0.625, 0.75, 0.875)
SPLIT_FRACS = (0.5, 0.15, 0.15, 0.2)  # train / val / cal / test, as for the released bundles
LAMS = (0.1, 0.25, 0.5, 1.0, 2.0, 4.0)
KINDS_FIT = ("pre", "post", "help", "pre_rag", "post_rag")
# runtime settings of the released bundles; calibrated fields are filled per λ
RUNTIME_DEFAULTS = {
    "policy": "route-eu", "horizon": 8, "max_rollbacks": 3, "max_bans_per_position": 3, "low_ratio": 0.8,
    "on_budget_exhausted": "continue", "tau_post": None, "tau_pre": None, "use_triton": True,
    "force_rollback_every": 0, "aux_mode": "auto", "rollback_mode": "auto", "gap_signal": "pre", "tau_gap": None,
    "drift_ratio": 0.5, "tau_pre_rag": None, "tau_post_rag": None, "retrieve_k": 3, "passage_chars": 600,
    "retrieval_workers": 8, "retrieve_rewind": "answer", "max_retrievals": 1, "eu_retrieve_signal": "option",
    "rag_heads": True, "conformal": "marginal", "eu_cost": 0.02, "force_retrieve_at": 0, "force_retry": False,
    "retrieval_delay_ms": 0.0, "post_head": "post", "release": "horizon", "lf_max_hold": 96, "lf_insert": "seeded",
}


def log(msg: str) -> None:
    print(f"[aidos fit {time.strftime('%H:%M:%S')}] {msg}", flush=True)


# =========================================================================== metrics / calibration
def auroc(scores, labels) -> float:
    """P(score of a positive > score of a negative), ties counted half. labels: 1 = positive."""
    s, y = np.asarray(scores, float), np.asarray(labels).astype(bool)
    ok = np.isfinite(s)
    s, y = s[ok], y[ok]
    n1, n0 = int(y.sum()), int((~y).sum())
    if not n1 or not n0:
        return float("nan")
    _, inv, cnt = np.unique(s, return_inverse=True, return_counts=True)
    r = (np.concatenate([[0], np.cumsum(cnt)[:-1]]) + (cnt + 1) / 2)[inv]
    return float((r[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def fit_platt(logits, labels, iters: int = 200) -> tuple[float, float]:
    """p = sigmoid(a * z + c) by log loss (temperature and bias)."""
    import torch

    z = torch.as_tensor(np.asarray(logits), dtype=torch.float64)
    y = torch.as_tensor(np.asarray(labels), dtype=torch.float64)
    a = torch.ones((), dtype=torch.float64, requires_grad=True)
    c = torch.zeros((), dtype=torch.float64, requires_grad=True)
    opt = torch.optim.LBFGS([a, c], lr=0.5, max_iter=iters, line_search_fn="strong_wolfe")

    def closure():
        opt.zero_grad()
        loss = torch.nn.functional.binary_cross_entropy_with_logits(a * z + c, y)
        loss.backward()
        return loss

    opt.step(closure)
    return float(a.detach()), float(c.detach())


def conformal_threshold(negative_scores, alpha: float) -> float:
    """Smallest tau with at most alpha of the negatives above it (finite-sample corrected)."""
    s = np.sort(np.asarray(negative_scores, float))
    n = len(s)
    if n == 0:
        return float("nan")
    k = int(math.ceil((n + 1) * (1 - alpha))) - 1
    return float(s[min(max(k, 0), n - 1)])


def answer_prob(p, platt):
    """Running max of a post head -> P(answer wrong); the engine's formula."""
    if p is None or not platt:
        return p
    q = min(max(p, 1e-6), 1 - 1e-6)
    return float(1.0 / (1.0 + math.exp(-(platt[0] * math.log(q / (1 - q)) + platt[1]))))


def fit_answer_platt(scores, wrong):
    pairs = [(s, w) for s, w in zip(scores, wrong) if s is not None and w is not None and np.isfinite(s)]
    if len(pairs) < 20 or len({w for _, w in pairs}) < 2:
        return None
    s = np.clip(np.array([p[0] for p in pairs], float), 1e-6, 1 - 1e-6)
    a, c = fit_platt(np.log(s / (1 - s)), np.array([p[1] for p in pairs], float))
    return [a, c]


def isotonic_decreasing(v, w):
    """Pool-adjacent-violators: weighted least-squares non-increasing fit."""
    blocks = []
    for x, wt in zip(v, w):
        blocks.append([x, wt, 1])
        while len(blocks) > 1 and blocks[-2][0] < blocks[-1][0]:
            b = blocks.pop()
            a = blocks[-1]
            a[0] = (a[0] * a[1] + b[0] * b[1]) / (a[1] + b[1])
            a[1] += b[1]
            a[2] += b[2]
    out = []
    for val, _, c in blocks:
        out += [val] * c
    return out


def option_value(table, x: float) -> float:
    xs, vs = table
    if x <= xs[0]:
        return float(vs[0])
    if x >= xs[-1]:
        return float(vs[-1])
    import bisect

    i = bisect.bisect_right(xs, x)
    a = (x - xs[i - 1]) / (xs[i] - xs[i - 1]) if xs[i] > xs[i - 1] else 0.0
    return float(vs[i - 1] + a * (vs[i] - vs[i - 1]))


# =========================================================================== stage 1: generate
def load_questions(a) -> list[dict]:
    from .data.qa import assign_split, load_items

    if a.questions:
        rows = [json.loads(l) for l in open(a.questions, encoding="utf-8") if l.strip()]
        out = []
        for i, r in enumerate(rows):
            qid = str(r.get("qid", f"q{i}"))
            out.append({"qid": qid, "dataset": r.get("dataset", "custom"), "question": r["question"],
                        "answers": list(r["answers"]), "split": r.get("split") or assign_split(qid, list(SPLIT_FRACS), a.seed)})
        return out
    ds = {k: int(v) for k, v in (kv.split("=") for kv in a.datasets.split(","))}
    return [{"qid": it.qid, "dataset": it.dataset, "question": it.question, "answers": list(it.answers),
             "split": assign_split(it.qid, list(SPLIT_FRACS), a.seed)} for it in load_items(ds, a.seed)]


def stage_generate(a, work: Path) -> None:
    """Runs in a child process so vLLM's GPU memory is released before the features stage."""
    from concurrent.futures import ThreadPoolExecutor

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams

    from .data.qa import build_prompt_ids, build_rag_prompt_ids, is_abstention, is_correct
    from .retrieval import load_retriever

    Q = load_questions(a)
    log(f"generate: {len(Q)} questions; splits " + json.dumps({s: sum(q['split'] == s for q in Q) for s in ('train', 'val', 'cal', 'test')}))
    tok = AutoTokenizer.from_pretrained(a.model)
    ret = load_retriever(a.retriever)
    with ThreadPoolExecutor(max_workers=8) as pool:
        passages = list(pool.map(lambda q: ret.search(q["question"], a.k), Q))
    log("generate: retrieval done")
    llm = LLM(model=a.model, max_model_len=a.max_model_len, gpu_memory_utilization=a.gpu_mem, seed=a.seed,
              tensor_parallel_size=a.tp, enforce_eager=False)
    sp = SamplingParams(temperature=0, max_tokens=a.max_tokens)

    def run(prompts):
        outs = llm.generate([{"prompt_token_ids": p} for p in prompts], sp, use_tqdm=False)
        return [(list(o.outputs[0].token_ids), o.outputs[0].text) for o in outs]

    cb_prompts = [build_prompt_ids(tok, q["question"]) for q in Q]
    rag_prompts = [build_rag_prompt_ids(tok, q["question"], ps[: a.k], a.passage_chars) for q, ps in zip(Q, passages)]
    cb, rag = run(cb_prompts), run(rag_prompts)
    with open(work / "generations.jsonl", "w", encoding="utf-8") as f:
        for q, pc, (ac, tc), pr, (ar, tr) in zip(Q, cb_prompts, cb, rag_prompts, rag):
            rec = dict(q)
            for key, p, ids, text in (("cb", pc, ac, tc), ("rag", pr, ar, tr)):
                ab = is_abstention(text)
                rec[key] = {"prompt_ids": p, "answer_ids": ids, "text": text, "abstained": ab,
                            "correct": (not ab) and is_correct(text, q["answers"])}
            f.write(json.dumps(rec) + "\n")
    n_cb = sum(1 for _ in open(work / "generations.jsonl", encoding="utf-8"))
    log(f"generate: wrote {n_cb} records to {work / 'generations.jsonl'}")


# =========================================================================== stage 2: features
class _Stop(Exception):
    pass


def resolve_layers(fracs, num_layers: int) -> list[int]:
    return sorted({min(max(int(round(f * num_layers)), 1), num_layers - 1) for f in fracs})


def _stop_ids(tok, model) -> set[int]:
    ids = set()
    if tok.eos_token_id is not None:
        ids.add(int(tok.eos_token_id))
    eos = getattr(getattr(model, "generation_config", None), "eos_token_id", None)
    if isinstance(eos, int):
        ids.add(eos)
    elif isinstance(eos, (list, tuple)):
        ids.update(int(e) for e in eos)
    return ids


class FeatureExtractor:
    """feature(l, p) = residual stream entering decoder layer l at position p = HF hidden_states[l][p]
    = vLLM's aux hidden state for layer l: the rows the engine scores."""

    def __init__(self, model_name: str):
        import torch
        from transformers import AutoTokenizer

        from .modeling import find_text_decoder, load_hf_lm, text_hidden_size

        self.tok = AutoTokenizer.from_pretrained(model_name)
        self.model = load_hf_lm(model_name, dtype=torch.bfloat16, device_map="auto").eval()
        self.base = find_text_decoder(self.model)
        self.layers_all = self.base.layers
        self.num_layers = len(self.layers_all)
        self.hidden = text_hidden_size(self.model.config)
        self.stops = _stop_ids(self.tok, self.model)

    def examples(self, G: list[dict], key: str) -> list[dict]:
        """One example per non-abstained answer: rows = [last prompt token] + [each answer token]."""
        from .data.qa import first_error_token

        out = []
        for gi, r in enumerate(G):
            g = r[key]
            if g["abstained"] or not g["text"].strip():
                continue
            ans = list(g["answer_ids"])
            while ans and ans[-1] in self.stops:
                ans.pop()
            if not ans:
                continue
            P = len(g["prompt_ids"])
            wrong = 0 if g["correct"] else 1
            fe = None
            if wrong and key == "cb":
                try:
                    fe = first_error_token(self.tok, ans, r["answers"])
                except Exception:
                    fe = None
            span = [wrong if (fe is None or j >= fe) else 0 for j in range(len(ans))] if wrong else [0] * len(ans)
            out.append({"gi": gi, "ids": list(g["prompt_ids"]) + ans, "rows": [P - 1] + [P + j for j in range(len(ans))],
                        "label": wrong, "span": [wrong] + span})
        return out

    def extract(self, examples: list[dict], layers: list[int], batch_tokens: int = 16384):
        """-> dict(x [N, L, H] fp16, gi, is_pre, label, span) over all rows of all examples."""
        import torch

        captured, deepest = {}, max(layers)

        def hook_for(li):
            def hook(module, args, kwargs):
                captured[li] = args[0] if args else kwargs["hidden_states"]
                if li == deepest:
                    raise _Stop
            return hook

        handles = [self.layers_all[l].register_forward_pre_hook(hook_for(l), with_kwargs=True) for l in layers]
        pad = self.tok.pad_token_id if self.tok.pad_token_id is not None else 0
        dev = self.model.get_input_embeddings().weight.device
        xs, gis, is_pre, labels, spans = [], [], [], [], []
        order = sorted(range(len(examples)), key=lambda i: len(examples[i]["ids"]))
        batch, longest, done = [], 0, 0

        def flush(batch):
            T = max(len(examples[i]["ids"]) for i in batch)
            ids = torch.full((len(batch), T), pad, dtype=torch.long)
            mask = torch.zeros((len(batch), T), dtype=torch.long)
            for j, i in enumerate(batch):
                n = len(examples[i]["ids"])
                ids[j, :n] = torch.tensor(examples[i]["ids"])
                mask[j, :n] = 1
            captured.clear()
            with torch.no_grad():
                try:
                    self.base(input_ids=ids.to(dev), attention_mask=mask.to(dev))
                except _Stop:
                    pass
            for j, i in enumerate(batch):
                e = examples[i]
                rows = torch.tensor(e["rows"])
                xs.append(torch.stack([captured[l][j].index_select(0, rows.to(captured[l].device)).float().cpu()
                                       for l in layers], 1).half())
                gis.extend([e["gi"]] * len(e["rows"]))  # extend, not +=: these lists belong to the enclosing scope
                is_pre.extend([True] + [False] * (len(e["rows"]) - 1))
                labels.extend([e["label"]] * len(e["rows"]))
                spans.extend(e["span"])

        for i in order:
            n = len(examples[i]["ids"])
            if batch and max(longest, n) * (len(batch) + 1) > batch_tokens:
                flush(batch)
                done += len(batch)
                batch, longest = [], 0
            batch.append(i)
            longest = max(longest, n)
        if batch:
            flush(batch)
        for h in handles:
            h.remove()
        return {"x": torch.cat(xs), "gi": np.array(gis), "is_pre": np.array(is_pre), "label": np.array(labels, np.int8),
                "span": np.array(spans, np.int8), "layers": list(layers)}


# =========================================================================== stage 3: heads
def _group_max(values: np.ndarray, groups: np.ndarray):
    order = np.argsort(groups, kind="stable")
    g, v = groups[order], values[order]
    keys, start = np.unique(g, return_index=True)
    return keys, np.maximum.reduceat(v, start)


def fit_head(x_tr, y_tr, w_tr, x_va, y_va, w_va, layers, epochs, device, lr=2e-3, wd=1e-3, bs=1024, seed=0):
    """AdamW on weighted BCE; early stopping on validation loss (the released post / help / *_rag recipe)."""
    import torch
    import torch.nn.functional as F

    from .probe.head import LinearBoolHead

    torch.manual_seed(seed)
    head = LinearBoolHead(layers, x_tr.shape[-1]).to(device)
    head.fit_standardizer(x_tr)
    base = float((y_tr.float() * w_tr).sum() / w_tr.sum())
    base = min(max(base, 1e-3), 1 - 1e-3)
    with torch.no_grad():
        head.b.fill_(math.log(base / (1 - base)))
    xg, yg, wg = x_tr.to(device), y_tr.float().to(device), (w_tr / w_tr.mean()).to(device)
    xv, yv, wv = x_va.to(device), y_va.float().to(device), (w_va / w_va.mean()).to(device)
    opt = torch.optim.AdamW(head.trainable(), lr=lr, weight_decay=wd)
    best, best_state = float("inf"), None
    g = torch.Generator(device=device).manual_seed(seed)
    for _ in range(epochs):
        head.train()
        perm = torch.randperm(xg.shape[0], device=device, generator=g)
        for i in range(0, xg.shape[0], bs):
            idx = perm[i: i + bs]
            loss = F.binary_cross_entropy_with_logits(head.raw_logits(xg[idx]), yg[idx], weight=wg[idx])
            opt.zero_grad(set_to_none=True)
            loss.backward()
            opt.step()
        head.eval()
        with torch.no_grad():
            vl = float(F.binary_cross_entropy_with_logits(head.raw_logits(xv), yv, weight=wv))
        if vl < best:
            best, best_state = vl, {k: v.detach().clone() for k, v in head.state_dict().items()}
    head.load_state_dict(best_state)
    return head.eval()


def fit_head_auroc(x_tr, y_tr, x_va, y_va, layers, device, epochs=40, wds=(1e-4, 1e-3, 1e-2), lr=1e-3, bs=256,
                   patience=5, min_steps=150, seed=0):
    """The released pre-head recipe: small batches, early stopping on validation AUROC, weight decay chosen on it."""
    import torch
    import torch.nn.functional as F

    from .probe.head import LinearBoolHead

    xg, yg, xv = x_tr.to(device), y_tr.float().to(device), x_va.to(device)
    yv = y_va.numpy()
    min_epochs = math.ceil(min_steps / max(1, math.ceil(xg.shape[0] / bs)))
    best_all = None
    for wd in wds:
        torch.manual_seed(seed)
        head = LinearBoolHead(layers, x_tr.shape[-1]).to(device)
        head.fit_standardizer(x_tr)
        opt = torch.optim.AdamW(head.trainable(), lr=lr, weight_decay=wd)
        g = torch.Generator(device=device).manual_seed(seed)
        best, best_state, bad = -1.0, None, 0
        for ep in range(max(epochs, min_epochs)):
            head.train()
            perm = torch.randperm(xg.shape[0], device=device, generator=g)
            for i in range(0, xg.shape[0], bs):
                idx = perm[i: i + bs]
                loss = F.binary_cross_entropy_with_logits(head.raw_logits(xg[idx]), yg[idx])
                opt.zero_grad(set_to_none=True)
                loss.backward()
                opt.step()
            head.eval()
            with torch.no_grad():
                a = auroc(head.raw_logits(xv).float().cpu().numpy(), yv)
            if a > best + 1e-4:
                best, bad, best_state = a, 0, {k: v.detach().clone() for k, v in head.state_dict().items()}
            else:
                bad += 1
                if bad >= patience and ep + 1 >= min_epochs:
                    break
        head.load_state_dict(best_state)
        head.eval()
        if best_all is None or best > best_all[1]:
            best_all = (head, best, wd)
    return best_all[0]


def predict(head, x, device, calibrated=True, bs=8192) -> np.ndarray:
    import torch

    out = []
    with torch.no_grad():
        for i in range(0, x.shape[0], bs):
            z = head(x[i: i + bs].to(device)) if calibrated else head.raw_logits(x[i: i + bs].to(device))
            out.append(z.float().cpu())
    z = torch.cat(out) if out else torch.zeros(0)
    return (torch.sigmoid(z) if calibrated else z).numpy()


def _answer_weights(gi):
    """Each answer contributes total weight 1, however many tokens it has."""
    import torch

    _, inv, cnt = np.unique(gi, return_inverse=True, return_counts=True)
    return torch.from_numpy((1.0 / cnt[inv]).astype(np.float32))


def _split_codes(G):
    code = {"train": 0, "val": 1, "cal": 2, "test": 3}
    return np.array([code.get(r["split"], 3) for r in G])


def train_heads(G, F_cb, F_rag, layers, device, alpha=0.1, sweep_epochs=15, epochs=40):
    """F_cb: closed-book rows at the chosen layers; F_rag: evidence rows. Returns heads + per-row scores."""
    import torch

    S = _split_codes(G)
    out, metrics = {}, {}

    def rows(F, sel, label="label"):
        idx = np.nonzero(sel)[0]
        it = torch.from_numpy(idx)
        return F["x"].index_select(0, it), torch.from_numpy(F[label][idx].astype(np.float32)), F["gi"][idx], idx

    def weights(gi, per_answer):
        return _answer_weights(gi) if per_answer else torch.ones(len(gi))

    def split_of(F):
        return S[F["gi"]]

    cb_wrong = np.array([0 if r["cb"]["correct"] else 1 for r in G])
    rag_ok = np.array([not (r["rag"]["abstained"] or not r["rag"]["text"].strip()) for r in G])
    rag_wrong = np.array([0 if r["rag"]["correct"] else 1 for r in G])

    specs = {  # kind: (features, row selector, label field or per-gi label, answer-weighted, recipe)
        "pre": (F_cb, F_cb["is_pre"], "label", False, "auroc"),
        "post": (F_cb, ~F_cb["is_pre"], "span", True, "loss"),
        "help": (F_cb, F_cb["is_pre"] & rag_ok[F_cb["gi"]], rag_wrong, False, "loss"),
        "pre_rag": (F_rag, F_rag["is_pre"], "label", False, "loss"),
        "post_rag": (F_rag, ~F_rag["is_pre"], "label", True, "loss"),
    }
    scores = {}
    for kind, (F, base_sel, lab, per_answer, recipe) in specs.items():
        sp = split_of(F)
        if isinstance(lab, np.ndarray):  # per-question label (help)
            F = dict(F, ylab=lab[F["gi"]].astype(np.int8))
            lab = "ylab"
        xt, yt, gt, _ = rows(F, base_sel & (sp == 0), lab)
        xv, yv, gv, _ = rows(F, base_sel & (sp == 1), lab)
        if recipe == "auroc":
            head = fit_head_auroc(xt, yt, xv, yv, layers, device, epochs=epochs)
        else:
            head = fit_head(xt, yt, weights(gt, per_answer), xv, yv, weights(gv, per_answer), layers, epochs, device)
        a, c = fit_platt(predict(head, xv, device, calibrated=False), yv.numpy())
        head.set_platt(a, c)
        x_all, _, g_all, idx_all = rows(F, base_sel, lab)
        p_all = predict(head, x_all, device)
        # answer level (max over rows of an answer), as the engine's running max
        keys, smax = _group_max(p_all, g_all)
        labels_q = (rag_wrong if kind in ("help", "pre_rag", "post_rag") else cb_wrong)[keys]
        sq = S[keys]
        neg_cal = smax[(sq == 2) & (labels_q == 0)]
        tau = conformal_threshold(neg_cal, alpha) if len(neg_cal) else None
        metrics[kind] = {"val_auroc": auroc(smax[sq == 1], labels_q[sq == 1]),
                         "test_auroc": auroc(smax[sq == 3], labels_q[sq == 3]),
                         "n_test": int((sq == 3).sum()), "tau": tau, "platt": [a, c]}
        scores[kind] = dict(zip(keys.tolist(), smax.tolist()))
        out[kind] = (head, tau)
        log(f"heads: {kind:8s} val AUROC {metrics[kind]['val_auroc']:.4f}  test AUROC {metrics[kind]['test_auroc']:.4f}")
    return out, metrics, scores


def layer_sweep(G, F_all, device, sweep_epochs=15, n_layers=3):
    """One post head per candidate layer, ranked by validation AUROC at the answer level (the released recipe)."""
    import torch

    S = _split_codes(G)
    cb_wrong = np.array([0 if r["cb"]["correct"] else 1 for r in G])
    sel_post = ~F_all["is_pre"]
    sp = S[F_all["gi"]]
    res = {}
    for j, layer in enumerate(F_all["layers"]):
        def T(m):
            idx = torch.from_numpy(np.nonzero(m)[0])
            return F_all["x"].index_select(0, idx)[:, [j]], torch.from_numpy(F_all["span"][m].astype(np.float32)), F_all["gi"][m]
        xt, yt, gt = T(sel_post & (sp == 0))
        xv, yv, gv = T(sel_post & (sp == 1))
        head = fit_head(xt, yt, _answer_weights(gt), xv, yv, _answer_weights(gv), [layer], sweep_epochs, device)
        keys, smax = _group_max(predict(head, xv, device, calibrated=False), gv)
        res[layer] = auroc(smax, cb_wrong[keys])
        log(f"sweep: layer {layer:3d}  val AUROC {res[layer]:.4f}")
    chosen = sorted(sorted(res, key=lambda l: -np.nan_to_num(res[l]))[:n_layers])
    return chosen, res


# =========================================================================== stage 4: calibrate
def question_table(G, scores) -> list[dict]:
    S = _split_codes(G)
    rows = []
    for gi, r in enumerate(G):
        rows.append({"split": int(S[gi]), "pre": scores["pre"].get(gi), "post": scores["post"].get(gi),
                     "help": scores["help"].get(gi), "rag_pre": scores["pre_rag"].get(gi),
                     "rag_post": scores["post_rag"].get(gi), "cb_correct": bool(r["cb"]["correct"]),
                     "cb_abstained": bool(r["cb"]["abstained"]), "rag_correct": bool(r["rag"]["correct"]),
                     "rag_abstained": bool(r["rag"]["abstained"])})
    return rows


def _eu(p, lam):
    return 1.0 - (1.0 + lam) * p


def retrieval_branch(r, lam, post_rag_platt) -> float:
    """Realized utility after retrieving (max_retrievals = 1): abstain if answering with the evidence has
    negative expected utility at the insertion row or while answering, else +1 right / -lam wrong."""
    if r["rag_abstained"]:
        return 0.0
    if r["rag_pre"] is not None and _eu(r["rag_pre"], lam) < 0:
        return 0.0
    q = answer_prob(r["rag_post"], post_rag_platt)
    if q is not None and _eu(q, lam) < 0:
        return 0.0
    return 1.0 if r["rag_correct"] else -lam


def fit_option_table(rows, lam, post_rag_platt, n_bins=20, min_rows=30):
    pts = sorted((r["help"], retrieval_branch(r, lam, post_rag_platt)) for r in rows if r["help"] is not None)
    if len(pts) < min_rows:
        return None
    bins = np.array_split(np.array(pts), min(n_bins, len(pts) // 10))
    xs = [float(b[:, 0].mean()) for b in bins]
    vs = isotonic_decreasing([float(b[:, 1].mean()) for b in bins], [len(b) for b in bins])
    return [[round(x, 6) for x in xs], [round(v, 6) for v in vs]]


def simulate(rows, lam, cal, cost=0.02) -> dict:
    """Offline estimate of route-eu on the given questions (the engine's decision rules, max_retrievals 1)."""
    n = len(rows)
    correct = wrong = abstain = retr = 0
    for r in rows:
        u_ans = _eu(r["pre"], lam) if r["pre"] is not None else 1.0
        u_ret = option_value(cal["eu_option_table"], r["help"]) - cost if (cal["eu_option_table"] and r["help"] is not None) else -math.inf
        go_retrieve = False
        if u_ans >= max(u_ret, 0.0):
            q = answer_prob(r["post"], cal["eu_post_platt"])
            if r["cb_abstained"]:
                abstain += 1
                continue
            if q is not None and _eu(q, lam) < max(0.0, u_ret):
                if u_ret > 0:
                    go_retrieve = True
                else:
                    abstain += 1
                    continue
            if not go_retrieve:
                correct += r["cb_correct"]
                wrong += not r["cb_correct"]
                continue
        elif u_ret >= 0:
            go_retrieve = True
        else:
            abstain += 1
            continue
        retr += 1
        u = retrieval_branch(r, lam, cal["eu_post_rag_platt"])
        if u == 0.0:
            abstain += 1
        elif u > 0:
            correct += 1
        else:
            wrong += 1
    return {"n": n, "accuracy": correct / n, "hallucination": wrong / n, "abstain": abstain / n,
            "retrieval_rate": retr / n, "utility": (correct - lam * wrong - cost * retr) / n}


def calibrate(rows, lams):
    val = [r for r in rows if r["split"] == 1]
    post_platt = fit_answer_platt([r["post"] for r in val], [0 if r["cb_correct"] else 1 for r in val])
    post_rag_platt = fit_answer_platt([r["rag_post"] for r in val], [0 if r["rag_correct"] else 1 for r in val])
    out = {}
    for lam in lams:
        out[lam] = {"eu_lambda": lam, "eu_post_platt": post_platt, "eu_post_rag_platt": post_rag_platt,
                    "eu_option_table": fit_option_table(val, lam, post_rag_platt)}
    return out


# =========================================================================== orchestration
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="aidos fit", description="Train and calibrate a head bundle for your own model.")
    ap.add_argument("--model", required=True, help="HF model id or path (an instruct model with a chat template)")
    ap.add_argument("--retriever", required=True, help="corpus .jsonl, BM25 index dir, query cache .jsonl, or python:module:factory")
    ap.add_argument("--out", required=True, help="bundle directory to write")
    ap.add_argument("--work", default=None, help="cache for intermediate files (default: <out>.work)")
    ap.add_argument("--datasets", default="triviaqa=6000,popqa=4000", help="name=count,... (see aidos.data.qa)")
    ap.add_argument("--questions", default=None, help='your own .jsonl: {"question", "answers": [...]} per line')
    ap.add_argument("--lams", default=",".join(f"{x:g}" for x in LAMS))
    ap.add_argument("--layers", default="auto", help='"auto" (sweep on val) or e.g. "14,18,21"')
    ap.add_argument("--k", type=int, default=3, help="passages per retrieval (as at serving time)")
    ap.add_argument("--passage-chars", type=int, default=600)
    ap.add_argument("--max-tokens", type=int, default=32)
    ap.add_argument("--max-model-len", type=int, default=2048)
    ap.add_argument("--gpu-mem", type=float, default=0.85)
    ap.add_argument("--tp", type=int, default=1, help="tensor parallel size for generation")
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--from-stage", choices=STAGES, default="generate", help="recompute from this stage on")
    ap.add_argument("--_child-generate", action="store_true", help=argparse.SUPPRESS)
    a = ap.parse_args(argv)
    out = Path(a.out)
    work = Path(a.work) if a.work else out.with_name(out.name + ".work")
    work.mkdir(parents=True, exist_ok=True)

    if a._child_generate:
        stage_generate(a, work)
        return 0

    t0 = time.time()
    first = STAGES.index(a.from_stage)
    gen_file = work / "generations.jsonl"
    if first <= 0 or not gen_file.exists():
        env = {k: v for k, v in os.environ.items() if k != "AIDOS_CONFIG"}
        cmd = [sys.executable, "-m", "aidos.fit", *(argv if argv is not None else sys.argv[1:]), "--_child-generate"]
        if subprocess.run(cmd, env=env).returncode != 0:
            log("generate stage failed")
            return 1
    G = [json.loads(l) for l in open(gen_file, encoding="utf-8")]
    S = _split_codes(G)
    acc = lambda key, s: float(np.mean([r[key]["correct"] for r, c in zip(G, S) if c == s]))  # noqa: E731
    log(f"{len(G)} questions; closed-book accuracy (val) {acc('cb', 1):.3f}, with evidence {acc('rag', 1):.3f}")

    import torch

    device = "cuda" if torch.cuda.is_available() else "cpu"
    feat_cb, feat_rag = work / "features_cb.pt", work / "features_rag.pt"
    fx = None
    if first <= 1 or not feat_cb.exists():
        fx = FeatureExtractor(a.model)
        cand = resolve_layers(CANDIDATE_LAYERS, fx.num_layers) if a.layers == "auto" else sorted(int(x) for x in a.layers.split(","))
        log(f"features: {fx.num_layers} decoder layers, hidden {fx.hidden}; closed-book rows at layers {cand}")
        F_all = fx.extract(fx.examples(G, "cb"), cand)
        torch.save(F_all, feat_cb)
    F_all = torch.load(feat_cb, weights_only=False)
    if a.layers == "auto":
        layers, sweep = layer_sweep(G, F_all, device)
    else:
        layers, sweep = sorted(int(x) for x in a.layers.split(",")), {}
    log(f"layers {layers}")
    cols = [F_all["layers"].index(l) for l in layers]
    F_cb = dict(F_all, x=F_all["x"][:, cols], layers=layers)
    if first <= 1 or not feat_rag.exists() or torch.load(feat_rag, weights_only=False)["layers"] != layers:
        fx = fx or FeatureExtractor(a.model)
        log("features: evidence rows")
        torch.save(fx.extract(fx.examples(G, "rag"), layers), feat_rag)
    F_rag = torch.load(feat_rag, weights_only=False)
    if fx is not None:
        del fx
        gc.collect()
        torch.cuda.empty_cache() if torch.cuda.is_available() else None

    heads, metrics, scores = train_heads(G, F_cb, F_rag, layers, device)
    rows = question_table(G, scores)
    lams = [float(x) for x in a.lams.split(",")]
    cal = calibrate(rows, lams)
    test = [r for r in rows if r["split"] == 3]
    estimate = {}
    for lam in lams:
        estimate[f"{lam:g}"] = {
            "aidos": simulate(test, lam, cal[lam]),
            "closed_book": {"utility": float(np.mean([1.0 if r["cb_correct"] else (0.0 if r["cb_abstained"] else -lam) for r in test]))},
            "always_retrieve": {"utility": float(np.mean([1.0 if r["rag_correct"] else (0.0 if r["rag_abstained"] else -lam) for r in test])) - 0.02},
        }

    # ---- write the bundle (never over an existing one) ----------------------------------------------------
    if out.exists() and any(out.iterdir()):
        stamp = time.strftime("%Y%m%d_%H%M%S")
        out = out.with_name(f"{out.name}_{stamp}")
        log(f"output exists; writing to {out}")
    out.mkdir(parents=True, exist_ok=True)
    for kind, (head, tau) in heads.items():
        head.cpu().save(out / f"head_{kind}.pt", kind=kind, model=a.model, tau=tau, alpha=0.1,
                        metrics={"auroc": metrics[kind]["test_auroc"]})
    for lam in lams:
        rt = dict(RUNTIME_DEFAULTS, retrieve_k=a.k, passage_chars=a.passage_chars, **cal[lam])
        (out / f"runtime_lam{lam:g}.json").write_text(json.dumps(rt, indent=1), encoding="utf-8")
    n_split = {s: int((S == c).sum()) for s, c in (("train", 0), ("val", 1), ("cal", 2), ("test", 3))}
    prov = {"model": a.model, "created": time.strftime("%Y-%m-%d %H:%M:%S"), "made_by": "aidos fit",
            "questions": a.questions or a.datasets, "splits": n_split, "retriever": os.path.basename(str(a.retriever).rstrip("/")),
            "layers": layers, "layer_sweep_val_auroc": {str(k): v for k, v in sweep.items()},
            "heads": metrics, "lams": lams, "policy": "route-eu", "max_model_len_used": a.max_model_len,
            "offline_estimate_test": estimate,
            "note": "Heads trained on the train split; layers, early stopping and Platt maps on val; conformal taus on cal; "
                    "test is reported only. The estimate replays the engine's decision rules offline."}
    (out / "PROVENANCE.json").write_text(json.dumps(prov, indent=1), encoding="utf-8")
    lines = [f"# Bundle for {a.model}", "", f"Made by `aidos fit` on {prov['created']}; splits {n_split}; layers {layers}.", "",
             "| head | val AUROC | test AUROC |", "|---|---|---|"]
    lines += [f"| {k} | {m['val_auroc']:.3f} | {m['test_auroc']:.3f} |" for k, m in metrics.items()]
    lines += ["", "Offline estimate on test questions (utility = accuracy - λ·hallucination - 0.02·retrievals):", "",
              "| λ | Aidos utility | accuracy | hallucination | abstain | retrieval rate | closed-book | always retrieve |",
              "|---|---|---|---|---|---|---|---|"]
    for lam, e in estimate.items():
        s = e["aidos"]
        lines.append(f"| {lam} | {s['utility']:.3f} | {s['accuracy']:.3f} | {s['hallucination']:.3f} | {s['abstain']:.3f} | "
                     f"{s['retrieval_rate']:.2f} | {e['closed_book']['utility']:.3f} | {e['always_retrieve']['utility']:.3f} |")
    lines += ["", "Check the engine on your GPU: `aidos verify --model MODEL --bundle THIS_DIR`."]
    (out / "REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    log(f"wrote {out} in {(time.time() - t0) / 60:.1f} min")
    print("\n".join(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

"""Paper 2 figures/tables from downloaded job results (run locally).

  python remote/paper2_figs.py goodput <goodput_job_dir>   -> table (markdown) + fig_goodput.svg/.pdf
  python remote/paper2_figs.py stall <status_trace.jsonl>  -> stall statistics for the live-view recording

goodput_job_dir holds goodput_cache_d0 / goodput_cache_d50 / goodput_live, each with runs.jsonl (examples/goodput.py).
Stall = a snapshot with no running request while requests wait (every slot paused for retrieval).
"""
import json
import sys
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "tripwire" / "docs" / "papers" / "figures"
SETTINGS = [("goodput_overhead", "overhead check (sync baseline)"), ("goodput_cache_d0", "query cache, 0 ms"), ("goodput_cache_d50", "query cache, +50 ms"), ("goodput_live", "live BM25 (21M)")]
COND = [("vanilla", "vLLM, closed-book"), ("vanilla_sync", "vLLM, closed-book, sync scheduling"), ("always_rag", "vLLM, always retrieve"), ("aidos_observe", "Aidos, scoring only"), ("aidos", "Aidos, λ = 1")]


def goodput(d):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    d = Path(d)
    R = {}
    for key, _ in SETTINGS:
        f = d / key / "runs.jsonl"
        if f.exists():
            R[key] = [json.loads(l) for l in open(f, encoding="utf-8")]
    lines = ["| retrieval | system | load | req/s | out tok/s | accuracy | abstain | hallucination | correct/s | (correct+abstain)/s |",
             "|---|---|---|---|---|---|---|---|---|---|"]
    for key, lab in SETTINGS:
        for c, cl in COND:
            for r in sorted([r for r in R.get(key, []) if r["condition"] == c], key=lambda r: r["load"]):
                lines.append(f"| {lab} | {cl} | {r['load']} | {r['req_per_s']:.1f} | {r['out_tok_per_s']:.0f} | {r['accuracy']:.3f} | "
                             f"{r['abstain']:.3f} | {r['hallucination']:.3f} | {r['goodput']:.1f} | {r['safe_goodput']:.1f} |")
    # overhead of scoring vs vanilla (same retrieval-free path), per load
    allr = R.get("goodput_cache_d0", []) + R.get("goodput_overhead", [])
    base = {r["load"]: r for r in allr if r["condition"] == "vanilla_sync"} or {r["load"]: r for r in allr if r["condition"] == "vanilla"}
    obs = {r["load"]: r for r in allr if r["condition"] == "aidos_observe"}
    over = {L: 1 - obs[L]["out_tok_per_s"] / base[L]["out_tok_per_s"] for L in base if L in obs}
    lines.append("")
    lines.append("Scoring overhead (output tokens/s, scoring-only vs vanilla): " + ", ".join(f"load {L}: {100 * v:.1f}%" for L, v in sorted(over.items())))
    print("\n".join(lines))
    fig, ax = plt.subplots(1, len(R), figsize=(3.3 * max(len(R), 1), 2.8), sharey=False, squeeze=False)
    for i, (key, lab) in enumerate([s for s in SETTINGS if s[0] in R]):
        a = ax[0][i]
        for c, cl in COND:
            rr = sorted([r for r in R[key] if r["condition"] == c], key=lambda r: r["load"])
            if rr:
                a.plot([r["load"] for r in rr], [r["safe_goodput"] for r in rr], marker="o", label=cl)
        a.set_xscale("log", base=2); a.set_yscale("log"); a.set_title(lab, fontsize=9)
        a.set_xlabel("concurrent requests", fontsize=8); a.tick_params(labelsize=7)
        if i == 0:
            a.set_ylabel("(correct + abstained) / s", fontsize=8)
    ax[0][0].legend(fontsize=6.5, frameon=False)
    fig.tight_layout()
    OUT.mkdir(parents=True, exist_ok=True)
    for ext in ("svg", "pdf"):
        fig.savefig(OUT / f"fig_goodput.{ext}")
    (OUT / "table_goodput.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT / 'fig_goodput.svg'} and table_goodput.md")


def stall(f):
    L = [json.loads(l) for l in open(f, encoding="utf-8") if l.strip()]
    t0 = L[0]["t"]
    st, run_len, longest, prev_t = 0, 0.0, 0.0, None
    for s in L:
        running = sum(a["state"] == "running" for a in s["active"])
        stalled = running == 0 and s.get("waiting", 0) > 0 and len(s["active"]) > 0
        st += stalled
        if stalled and prev_t is not None:
            run_len += s["t"] - prev_t
            longest = max(longest, run_len)
        elif not stalled:
            run_len = 0.0
        prev_t = s["t"]
    print(json.dumps({"snapshots": len(L), "span_s": round(L[-1]["t"] - t0, 1), "stalled_share": round(st / len(L), 3),
                      "longest_stall_s": round(longest, 1),
                      "max_paused": max(sum(a["state"] == "paused" for a in s["active"]) for s in L)}))


def lamsweep(d):
    """d = goodput_lamsweep dir (job 458179): Aidos at several λ vs always-retrieve, load 256, cached retrieval.
    -> fig_lamsweep.svg/.pdf/.png and table_lamsweep.md"""
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    BLUE, ORANGE, INK, INK2, GRID = "#2a78d6", "#eb6834", "#0b0b0b", "#52514e", "#e4e3df"
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8, "axes.edgecolor": INK2, "axes.labelcolor": INK,
                         "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
                         "axes.linewidth": 0.6})
    rows = [json.loads(l) for l in open(Path(d) / "runs.jsonl", encoding="utf-8")]
    ai = sorted([r for r in rows if r["condition"] == "aidos"], key=lambda r: r["lam"])
    rag = next(r for r in rows if r["condition"] == "always_rag")
    cb = next(r for r in rows if r["condition"] == "vanilla")
    lines = ["| system | λ | req/s | accuracy | abstain | hallucination | correct/s | (correct+abstain)/s |", "|---|---|---|---|---|---|---|---|"]
    for r, name in [(cb, "vLLM, closed-book"), (rag, "vLLM, always retrieve")] + [(r, "Aidos") for r in ai]:
        lines.append(f"| {name} | {r['lam'] if r['lam'] is not None else '-'} | {r['req_per_s']:.1f} | {r['accuracy']:.3f} | {r['abstain']:.3f} | "
                     f"{r['hallucination']:.3f} | {r['goodput']:.1f} | {r['safe_goodput']:.1f} |")
    print("\n".join(lines))
    fig, (a, b) = plt.subplots(1, 2, figsize=(6.6, 2.4), gridspec_kw=dict(wspace=0.35))
    for ax, key, ylab, title in ((a, "accuracy", "accuracy", "(a) Answer quality"),
                                 (b, "goodput", "correct answers per second", "(b) Throughput (256 concurrent requests)")):
        ax.plot([r["hallucination"] for r in ai], [r[key] for r in ai], color=BLUE, lw=2, marker="o", ms=5, mec="white", mew=0.8,
                label=f"Aidos (λ from {ai[0]['lam']:g} to {ai[-1]['lam']:g})")
        for r in ai:
            # in (b) the λ = 0.25 / 0.5 / 1 points sit within 0.5 correct/s of each other: label only the ends and λ = 1, 2
            if key == "goodput" and r["lam"] not in (0.1, 1, 2, 4):
                continue
            ax.annotate(f"λ={r['lam']:g}", (r["hallucination"], r[key]), textcoords="offset points",
                        xytext=(4, 5) if key == "goodput" else (6, -9), fontsize=6, color=INK2)
        ax.plot(rag["hallucination"], rag[key], "s", color=ORANGE, ms=6, mec="white", mew=0.8, label="vLLM, always retrieve")
        ax.set_xlabel("hallucination rate (wrong answers / questions)")
        ax.set_ylabel(ylab)
        ax.set_title(title, fontsize=8, loc="left")
        ax.grid(color=GRID, lw=0.6)
        ax.set_xlim(0, max(0.36, rag["hallucination"] + 0.05))
    a.legend(frameon=False, fontsize=6.5, loc="lower right")
    OUT.mkdir(parents=True, exist_ok=True)
    for ext in ("svg", "pdf", "png"):
        fig.savefig(OUT / f"fig_lamsweep.{ext}", dpi=300, bbox_inches="tight")
    (OUT / "table_lamsweep.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT / 'fig_lamsweep.svg'} and table_lamsweep.md")


if __name__ == "__main__":
    {"goodput": goodput, "stall": stall, "lamsweep": lamsweep}[sys.argv[1]](sys.argv[2])

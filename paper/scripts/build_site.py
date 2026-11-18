"""Build the static demo site (GitHub Pages, served from docs/) from the package's demo pages and the recorded results.

    python paper/scripts/build_site.py          # run from the repository root; writes docs/

Pages (no GPU, no server; everything runs in the browser):
  docs/index.html               landing page
  docs/cost-explorer/           the `aidos lambda` page with its measured data
  docs/live-view/               the `aidos live` page replaying a recorded batch, with a timeline
  docs/verify/                  the eight exactness checks from `aidos verify`
"""
import html
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEMO = ROOT / "aidos-vllm" / "src" / "aidos" / "demo"
RES = ROOT / "paper" / "results"
FIG = ROOT / "paper" / "figures"
OUT = ROOT / "docs"
REPO = "https://github.com/belgium-waffle/aidos1"

STYLE = """
:root{--bg:#fbfaf7;--panel:#fff;--ink:#1d1d1b;--muted:#6b6a65;--line:#e4e1d8;--accent:#2f6f5e;--chip:#f1efe8;--code:#f4f2ec}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#151514;--panel:#1d1d1b;--ink:#ecebe6;--muted:#a3a19a;
--line:#33322e;--accent:#6fc2a8;--chip:#262522;--code:#232220}}
:root[data-theme="dark"]{--bg:#151514;--panel:#1d1d1b;--ink:#ecebe6;--muted:#a3a19a;--line:#33322e;--accent:#6fc2a8;--chip:#262522;--code:#232220}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--ink);font:15px/1.55 system-ui,-apple-system,"Segoe UI",sans-serif}
main{max-width:980px;margin:0 auto;padding:32px 16px 56px}
a{color:var(--accent)}h1{font-size:28px;line-height:1.2;margin:0 0 8px}h2{font-size:18px;margin:32px 0 10px}
.lead{color:var(--muted);font-size:16px;margin:0 0 20px;max-width:760px}
.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}
@media (max-width:760px){.cards{grid-template-columns:1fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 16px;text-decoration:none;color:inherit;display:block}
.card:hover{border-color:var(--accent)}.card b{display:block;font-size:15px;margin-bottom:4px;color:var(--accent)}
.card span{color:var(--muted);font-size:13.5px}
pre{background:var(--code);border:1px solid var(--line);border-radius:10px;padding:12px 14px;overflow-x:auto;font-size:13px;line-height:1.5}
code{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}
ul{padding-left:20px}li{margin:4px 0}
img.fig{width:100%;height:auto;background:#fff;border:1px solid var(--line);border-radius:10px;padding:8px}
table{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums;background:var(--panel);border:1px solid var(--line);border-radius:10px;overflow:hidden}
th,td{text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);vertical-align:top}th{font-size:13px;color:var(--muted);font-weight:500}
.ok{display:inline-block;font-size:12px;padding:1px 9px;border-radius:999px;background:var(--accent);color:var(--bg)}
.note{color:var(--muted);font-size:13.5px}
.top{display:flex;gap:16px;font-size:13.5px;margin-bottom:24px}.top a{text-decoration:none}
"""


def page(title, body, desc):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}">
<style>{STYLE}</style></head><body><main>
<nav class="top"><a href="{'./' if title == 'Aidos' else '../'}">Aidos</a><a href="{'' if title == 'Aidos' else '../'}live-view/">Live view</a>
<a href="{'' if title == 'Aidos' else '../'}cost-explorer/">Cost explorer</a><a href="{'' if title == 'Aidos' else '../'}verify/">Exactness checks</a>
<a href="{REPO}">Code</a></nav>
{body}
</main></body></html>
"""


def landing():
    body = f"""
<h1>Aidos: answer, retrieve or abstain from inside the vLLM decode loop</h1>
<p class="lead">A plugin for vLLM V1 that reads small linear probes from the model's hidden states at every step and acts
on them in the scheduler: it decides whether to answer, fetch evidence or decline to answer, pauses a request with its
KV cache intact while retrieval runs, and can roll back mid-answer, all token-exact with recomputation.</p>

<h2>Try it in your browser (no GPU needed)</h2>
<div class="cards">
<a class="card" href="live-view/"><b>Live view</b><span>Replay a recorded batch on Qwen2.5-7B: requests decoding, paused for
retrieval with their KV cache kept, and abstaining, with the probe's risk at every token. Scrub the timeline.</span></a>
<a class="card" href="cost-explorer/"><b>Cost explorer</b><span>Move λ, the cost of a wrong answer, and watch Aidos re-plan how much
it answers. A reasoning model told the same λ stays put. Every point is a measured result.</span></a>
<a class="card" href="verify/"><b>Exactness checks</b><span>The eight engine checks run by <code>aidos verify</code>: insertion,
rollback and retries reproduce recomputation token for token (24 of 24 prompts each).</span></a>
</div>

<h2>Run it on your GPU</h2>
<pre><code>git clone {REPO}
cd aidos1/aidos-vllm
pip install -e ".[bm25]"          # pins vllm 0.21.*
aidos info
python examples/quickstart.py     # three questions on a two-document corpus

# OpenAI-compatible server
aidos config bundles/qwen2.5-7b-instruct --lam 1 --retriever my_corpus.jsonl --status aidos_status.json -o aidos.json
AIDOS_CONFIG=$PWD/aidos.json vllm serve Qwen/Qwen2.5-7B-Instruct \\
    --scheduler-cls aidos.engine.scheduler.AidosScheduler --no-async-scheduling
aidos live --status aidos_status.json     # the live view, on your own traffic
aidos verify --model Qwen/Qwen2.5-7B-Instruct --bundle bundles/qwen2.5-7b-instruct</code></pre>
<p class="note">Heads ship for Qwen2.5-7B / 32B, Llama-3.1-8B, Llama-3.3-70B, Mistral-7B and Qwen3-8B, each calibrated for
λ ∈ {{0.1, 0.25, 0.5, 1, 2, 4}}. Retrievers: your own documents (BM25 in memory), a precomputed cache, a BM25 index, or any
Python search function. MIT licence.</p>

<h2>How it works</h2>
<img class="fig" src="figures/fig1_architecture.svg" alt="Architecture: the worker computes hidden states, a fused kernel scores the probes, scores ride back on the runner output, and the scheduler pauses, inserts evidence or rolls back.">

<h2>Results</h2>
<ul>
<li><b>Exact:</b> all eight engine checks match recomputation on every model, including tensor-parallel 70B.</li>
<li><b>Better answers:</b> higher utility than five adaptive-retrieval pipelines run in the same engine in 75 of 75 paired
comparisons (48 of 48 on a sealed held-out set), with 0.40–0.57 times the hallucination of the strongest.</li>
<li><b>Cost-aware:</b> wrong on 6.9% / 3.8% / 1.7% of questions at λ = 1 / 2 / 4, where a reasoning model with search stays at
about 25%, and 6–21 times faster.</li>
<li><b>Cheap to run:</b> 2–3% fewer requests per second than vLLM with the same scheduling (7B, 256 concurrent requests).</li>
</ul>
<img class="fig" src="figures/fig_lamsweep.png" alt="Accuracy and correct answers per second against hallucination rate for Aidos at several λ and for always-retrieve.">
<p class="note">Throughput figure: Qwen2.5-7B, one H100, 256 concurrent requests, cached retrieval; measured on a 2,000-question test
subset that over-represents TriviaQA (full-split numbers will replace it). Paper under review; source data in
<a href="{REPO}/tree/main/paper">paper/</a>.</p>
"""
    return page("Aidos", body, "Aidos: answer, retrieve or abstain from inside the vLLM decode loop. Live demos and code.")


REPLAY = """
<div id="replay" style="position:sticky;top:0;z-index:5;background:var(--panel);border-bottom:1px solid var(--line);padding:10px 16px;font:13px system-ui,sans-serif;color:var(--ink)">
<div style="max-width:1120px;margin:0 auto;display:flex;gap:12px;align-items:center;flex-wrap:wrap">
<b>Replay</b><span style="color:var(--muted)">a recorded batch: 64 questions on Qwen2.5-7B, 16 slots, live BM25 over 21M passages, 300 ms added retrieval latency</span>
<button id="rp-play" style="font:inherit;padding:3px 12px;border:1px solid var(--line);border-radius:8px;background:var(--chip);color:var(--ink);cursor:pointer">Pause</button>
<input id="rp-pos" type="range" min="0" max="0" value="0" style="flex:1;min-width:160px" aria-label="Snapshot">
<span id="rp-t" style="font-variant-numeric:tabular-nums;min-width:110px">0.0 s</span>
<a href="../" style="color:var(--run)">Aidos</a></div></div>
<script>
// Serves the page's status.json requests from the recorded trace, in the browser (no server).
(function(){
  let L=[],T=[],i=0,playing=true,t0=performance.now(),base=0;
  const pos=()=>document.getElementById("rp-pos"),lab=()=>document.getElementById("rp-t"),btn=()=>document.getElementById("rp-play");
  const ready=fetch("trace.jsonl").then(r=>r.text()).then(x=>{L=x.split("\\n").filter(Boolean).map(l=>JSON.parse(l));
    T=L.map(s=>s.t-L[0].t);pos().max=L.length-1;});
  function at(e){let k=0;for(let j=0;j<T.length;j++){if(T[j]<=e)k=j;}return k}
  function show(){pos().value=i;lab().textContent=T[i].toFixed(1)+" s of "+T[T.length-1].toFixed(1)+" s"}
  const real=window.fetch.bind(window);
  window.fetch=async function(u,o){
    if(String(u).startsWith("status.json")){await ready;
      if(playing){const span=T[T.length-1]+2,e=(base+(performance.now()-t0)/1000)%span;i=at(e);}
      show();const s=Object.assign({},L[i],{t:Date.now()/1000});
      return new Response(JSON.stringify(s),{headers:{"Content-Type":"application/json"}});}
    return real(u,o)};
  document.addEventListener("DOMContentLoaded",()=>{
    pos().addEventListener("input",()=>{playing=false;i=+pos().value;base=T[i];btn().textContent="Play"});
    btn().addEventListener("click",()=>{playing=!playing;if(playing){base=T[i];t0=performance.now()}btn().textContent=playing?"Pause":"Play"});
  });
})();
</script>
"""


def live_view(dst):
    s = (DEMO / "live_view.html").read_text(encoding="utf-8")
    s = s.replace("<title>Aidos Live View</title>", "<title>Aidos Live View (replay)</title>")
    s = s.replace("<body>\n<main>", "<body>\n" + REPLAY + "<main>", 1)
    assert REPLAY in s
    dst.mkdir(parents=True, exist_ok=True)
    (dst / "index.html").write_text(s, encoding="utf-8", newline="\n")
    shutil.copyfile(RES / "live_view_recording" / "status_trace.jsonl", dst / "trace.jsonl")


def cost_explorer(dst):
    dst.mkdir(parents=True, exist_ok=True)
    s = (DEMO / "lambda_explorer.html").read_text(encoding="utf-8")
    s = s.replace("<body>", f'<body>\n<div style="max-width:1120px;margin:0 auto;padding:10px 16px 0;font:13px system-ui,sans-serif"><a href="../" style="color:#2f6f5e">Aidos</a> · the same page as <code>aidos lambda</code>, served statically</div>', 1)
    (dst / "index.html").write_text(s, encoding="utf-8", newline="\n")
    shutil.copyfile(DEMO / "lambda_data.json", dst / "data.json")


CHECKS = {
    "observe == vanilla": "Observe-only mode (probes scored, never acted on) produces exactly the tokens of unmodified vLLM.",
    "prefill-insert == reference": "Retrieval decided at prefill equals a fresh request with the evidence in its prompt.",
    "mid-insert == reference": "Evidence inserted after k generated tokens equals a fresh request with the prompt, those tokens and the evidence.",
    "mid-insert-delayed == reference": "The same with 300 ms of retrieval latency while the rest of the batch keeps decoding.",
    "mid-insert-recompute == reference": "The same on the recomputation path instead of the KV-insertion path.",
    "rewind-insert == prefill reference": "The deployed rewind (roll back, then insert) equals evidence at prefill.",
    "retry-insert == reference": "A second retrieval attempt equals a request with both evidence turns in its prompt.",
    "forced-rollback completes": "Forced rollbacks every three steps run to completion without corrupting other requests.",
}


def verify(dst):
    r = json.loads((RES / "verify_qwen2.5-7b" / "result.json").read_text(encoding="utf-8"))
    rows = "".join(
        f"<tr><td><code>{html.escape(k)}</code></td><td>{html.escape(CHECKS.get(k, ''))}</td>"
        f"<td>{v.get('exact')}/{v.get('n')}</td><td><span class='ok'>{'pass' if v.get('pass') else 'FAIL'}</span></td></tr>"
        for k, v in r["checks"].items())
    body = f"""
<h1>Exactness checks</h1>
<p class="lead">Aidos edits requests mid-generation: it inserts evidence into a paused request's KV cache and can roll the cache
back. <code>aidos verify</code> checks that every such edit produces exactly the tokens a recomputation from scratch would.
Greedy decoding makes the expected output exact; a mismatch is accepted only at a bf16 near-tie (the reference's runner-up token,
margin below 1 nat).</p>
<table><tr><th>check</th><th>what it tests</th><th>exact</th><th></th></tr>{rows}</table>
<p class="note">This run: Qwen2.5-7B-Instruct, vLLM 0.21.0, one GPU, 24 prompts per check, installed from the release package with
plain pip on a fresh node; overall result: {'all pass' if r.get('pass') else 'FAIL'}. Raw outputs:
<a href="{REPO}/tree/main/paper/results/verify_qwen2.5-7b">paper/results/verify_qwen2.5-7b</a>. In the paper the same checks pass on
five models from 7B to 70B, including tensor parallelism. Run it yourself:</p>
<pre><code>aidos verify --model Qwen/Qwen2.5-7B-Instruct --bundle bundles/qwen2.5-7b-instruct</code></pre>
"""
    dst.mkdir(parents=True, exist_ok=True)
    (dst / "index.html").write_text(page("Aidos exactness checks", body, "The eight exactness checks of aidos verify."),
                                    encoding="utf-8", newline="\n")


def main():
    OUT.mkdir(exist_ok=True)
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    (OUT / "index.html").write_text(landing(), encoding="utf-8", newline="\n")
    (OUT / "figures").mkdir(exist_ok=True)
    for f in ("fig1_architecture.svg", "fig_lamsweep.png"):
        shutil.copyfile(FIG / f, OUT / "figures" / f)
    live_view(OUT / "live-view")
    cost_explorer(OUT / "cost-explorer")
    verify(OUT / "verify")
    print("wrote", sorted(str(p.relative_to(ROOT)) for p in OUT.rglob("*") if p.is_file()))


if __name__ == "__main__":
    main()

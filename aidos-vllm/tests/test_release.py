"""Release-only tests: bundles, retrievers, CLI wiring (CPU, no vLLM needed)."""
import json

import pytest


def _bundle(tmp_path, **kw):
    rt = {"policy": "route-eu", "eu_lambda": 1.0, "retriever": None, **kw}
    (tmp_path / "runtime_lam1.json").write_text(json.dumps(rt))
    (tmp_path / "runtime_lam2.json").write_text(json.dumps({**rt, "eu_lambda": 2.0}))
    return tmp_path


def test_runtime_config_from_bundle(tmp_path):
    from aidos.engine.factory import bundle_lams, runtime_config

    b = _bundle(tmp_path)
    assert bundle_lams(b) == [1.0, 2.0]
    rt = runtime_config(b, lam=2, retriever="x.jsonl")
    assert rt.eu_lambda == 2.0 and rt.retriever == "x.jsonl" and rt.head_dir == str(b.resolve())
    assert runtime_config(b, policy="observe").policy == "observe"
    with pytest.raises(ValueError):  # a retrieving policy needs a retriever
        runtime_config(b)
    with pytest.raises(FileNotFoundError):
        runtime_config(b, lam=4)
    with pytest.raises(ValueError):
        runtime_config(b, retriever="x.jsonl", not_a_setting=1)


def test_status_path_is_a_runtime_setting(tmp_path):
    from aidos.engine.factory import runtime_config

    rt = runtime_config(_bundle(tmp_path), policy="observe", status_path=str(tmp_path / "s.json"))
    assert rt.status_path.endswith("s.json")


def test_query_cache_vs_corpus(tmp_path):
    from aidos.retrieval import CachedRetriever, load_retriever

    cache = tmp_path / "cache.jsonl"
    cache.write_text(json.dumps({"query": "q", "passages": [{"title": "t", "text": "x"}]}) + "\n")
    r = load_retriever(str(cache))
    assert isinstance(r, CachedRetriever) and r.search("q", 1)[0]["text"] == "x"


def test_memory_bm25(tmp_path):
    pytest.importorskip("bm25s")
    pytest.importorskip("Stemmer")
    from aidos.retrieval import load_retriever

    corpus = tmp_path / "corpus.jsonl"
    docs = [{"title": "Mars", "text": "Mars is called the Red Planet because of iron oxide."},
            {"title": "Venus", "text": "Venus is the hottest planet in the Solar System."},
            {"title": "Paris", "text": "Paris is the capital of France."}]
    corpus.write_text("".join(json.dumps(d) + "\n" for d in docs))
    r = load_retriever(str(corpus))
    hits = r.search("Which planet is red?", 2)
    assert hits and hits[0]["title"] == "Mars"


def test_python_retriever_spec(tmp_path, monkeypatch):
    from aidos.retrieval import load_retriever

    (tmp_path / "my_ret.py").write_text(
        "class R:\n    def search(self, q, k):\n        return [{'title': 'a', 'text': q}][:k]\n"
        "def make():\n    return R()\n")
    monkeypatch.syspath_prepend(str(tmp_path))
    assert load_retriever("python:my_ret:make").search("hello", 1)[0]["text"] == "hello"


def test_demo_files_packaged():
    from aidos.cli import DEMO

    for f in ("live_view.html", "lambda_explorer.html", "lambda_data.json"):
        assert (DEMO / f).exists(), f
    d = json.loads((DEMO / "lambda_data.json").read_text())
    a = d["runs"]["v5_qwen2.5_7b"]["methods"]["Aidos"]
    lams = d["runs"]["v5_qwen2.5_7b"]["lams"]
    wrong = {l: x["test"]["hallucination_rate"] for l, x in zip(lams, a)}
    assert abs(wrong[1.0] - 0.069) < 0.001 and abs(wrong[4.0] - 0.017) < 0.001  # the paper's B10 numbers

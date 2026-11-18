"""aidos command line.

  aidos verify  --model M --bundle B          token-exactness tests on your GPU / vLLM build
  aidos config  B --lam 1 --retriever R -o F  write a runtime file for `AIDOS_CONFIG=F vllm serve ...`
  aidos live    --status F [--port 8765]      live view of request states and scores (browser)
  aidos lambda  [--data F] [--port 8766]      cost explorer: move lambda, watch coverage / errors
  aidos info                                   installed versions and plugin registration
"""

from __future__ import annotations

import argparse
import functools
import http.server
import json
import sys
import threading
import webbrowser
from pathlib import Path

DEMO = Path(__file__).resolve().parent / "demo"


def _serve(routes: dict[str, callable], port: int, open_path: str) -> None:
    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            path = self.path.split("?", 1)[0]
            fn = routes.get(path)
            if fn is None:
                self.send_error(404)
                return
            body, ctype = fn()
            self.send_response(200)
            self.send_header("Content-Type", ctype)
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, *a):  # quiet
            pass

    srv = http.server.ThreadingHTTPServer(("127.0.0.1", port), H)
    url = f"http://127.0.0.1:{port}{open_path}"
    print(f"aidos: serving {url}  (Ctrl+C to stop)", flush=True)
    threading.Timer(0.5, functools.partial(webbrowser.open, url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        pass


def _file(path: Path, ctype: str):
    def f():
        try:
            return path.read_bytes(), ctype
        except FileNotFoundError:
            return b"{}", ctype
    return f


def cmd_live(a) -> int:
    status = Path(a.status)
    _serve({"/": _file(DEMO / "live_view.html", "text/html; charset=utf-8"),
            "/status.json": _file(status, "application/json")}, a.port, "/")
    return 0


def cmd_lambda(a) -> int:
    data = Path(a.data) if a.data else DEMO / "lambda_data.json"
    _serve({"/": _file(DEMO / "lambda_explorer.html", "text/html; charset=utf-8"),
            "/data.json": _file(data, "application/json")}, a.port, "/")
    return 0


def cmd_config(a) -> int:
    from .engine.factory import runtime_config

    kw = {}
    if a.status:
        kw["status_path"] = str(Path(a.status).resolve())
    if a.telemetry:
        kw["telemetry_path"] = str(Path(a.telemetry).resolve())
    rt = runtime_config(a.bundle, lam=a.lam, policy=a.policy, retriever=a.retriever, **kw)
    p = rt.write(a.output)
    print(f"wrote {p}\nrun:  AIDOS_CONFIG={p.resolve()} vllm serve <model> "
          "--scheduler-cls aidos.engine.scheduler.AidosScheduler --no-async-scheduling")
    return 0


def cmd_info(a) -> int:
    from importlib.metadata import entry_points, version

    for pkg in ("aidos-vllm", "vllm", "torch", "transformers"):
        try:
            print(f"{pkg:13s} {version(pkg)}")
        except Exception:
            print(f"{pkg:13s} not installed")
    eps = [e for e in entry_points(group="vllm.general_plugins") if e.name == "aidos"]
    print("vLLM plugin   ", "registered" if eps else "NOT registered (reinstall the package)")
    return 0


def main(argv=None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if argv and argv[0] == "verify":
        from .verify import main as verify_main

        return verify_main(argv[1:])
    ap = argparse.ArgumentParser(prog="aidos", description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("verify", help="token-exactness tests (see aidos verify -h)")
    c = sub.add_parser("config", help="write a runtime file for vllm serve")
    c.add_argument("bundle")
    c.add_argument("--lam", type=float, default=1.0)
    c.add_argument("--policy", default=None)
    c.add_argument("--retriever", default=None)
    c.add_argument("--status", default=None, help="live-view snapshot file (enables the live view)")
    c.add_argument("--telemetry", default=None, help="per-request telemetry .jsonl")
    c.add_argument("-o", "--output", default="aidos_runtime.json")
    lv = sub.add_parser("live", help="live view of request states")
    lv.add_argument("--status", required=True)
    lv.add_argument("--port", type=int, default=8765)
    lm = sub.add_parser("lambda", help="cost explorer")
    lm.add_argument("--data", default=None)
    lm.add_argument("--port", type=int, default=8766)
    sub.add_parser("info", help="versions and plugin registration")
    a = ap.parse_args(argv)
    return {"config": cmd_config, "live": cmd_live, "lambda": cmd_lambda, "info": cmd_info}[a.cmd](a)


if __name__ == "__main__":
    raise SystemExit(main())

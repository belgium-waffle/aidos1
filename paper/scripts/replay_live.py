"""Replay a recorded status_trace.jsonl into the aidos live view: status.json advances in real time (loops).
Optional 3rd argument: a snapshot index to freeze on (for figure screenshots)."""
import http.server, json, sys, time
from pathlib import Path
DEMO, TRACE = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
L = [l for l in TRACE.read_text(encoding="utf-8").splitlines() if l.strip()]
FREEZE = int(sys.argv[3]) if len(sys.argv) > 3 else None
T = [json.loads(l)["t"] for l in L]; span = T[-1] - T[0] + 3.0; t0 = time.time()
class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **k): super().__init__(*a, directory=str(DEMO), **k)
    def log_message(self, *a): pass
    def do_GET(self):
        p = self.path.split("?")[0]
        if p == "/status.json":
            el = (time.time() - t0) % span
            i = max([k for k, t in enumerate(T) if t - T[0] <= el] or [0]) if FREEZE is None else FREEZE
            d = json.loads(L[i]); d["t"] = time.time(); b = json.dumps(d).encode(); self.send_response(200); self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(b))); self.end_headers(); self.wfile.write(b); return
        if p in ("/", "/index.html"): self.path = "/live_view.html"
        return super().do_GET()
http.server.ThreadingHTTPServer(("127.0.0.1", 8765), H).serve_forever()

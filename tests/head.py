#!/usr/bin/env python3
"""Checks every page's <head>: favicon tags everywhere, and a valid Discord component embed
(under 3,000 bytes, escaped, one root Container) on every page except 404 and the redirect stub.
Run with: python tests/head.py"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import importlib.util
spec = importlib.util.spec_from_file_location("build_head", ROOT / "scripts" / "build-head.py")
bh = importlib.util.module_from_spec(spec); spec.loader.exec_module(bh)

fails = 0
def check(name, ok):
    global fails
    print(("ok   - " if ok else "FAIL - ") + name)
    if not ok: fails += 1

ALLOWED = {1, 2, 9, 10, 11, 12, 14, 17}
BTN = {"id", "type", "url", "style", "label", "emoji", "disabled"}
def walk(c, out):
    out.append(c)
    for k in c.get("components", []): walk(k, out)
    if "accessory" in c: walk(c["accessory"], out)

for rel, p in bh.pages():
    src = p.read_text(encoding="utf-8")
    if "</head>" not in src: continue
    head = src.split("</head>")[0]
    check(rel + ": favicon tags", all(t in head for t in ('href="/favicon.ico" sizes="48x48"', 'sizes="512x512"', 'rel="apple-touch-icon"', 'href="/site.webmanifest"')))
    m = re.search(r'<script id="discord:component-embed" type="application/json">(.*?)</script>', head, re.S)
    if rel in bh.NO_EMBED:
        check(rel + ": no embed", m is None); continue
    ok = m is not None
    check(rel + ": has embed", ok)
    if not ok: continue
    raw = m.group(1)
    check(rel + ": under 3,000 bytes", len(raw.encode()) <= 3000)
    check(rel + ": no literal $1, no </script early", "$1" not in raw and "</" not in raw)
    d = json.loads(raw)["component"]
    nodes = []; walk(d, nodes)
    check(rel + ": one root Container, no nested", d["type"] == 17 and sum(n["type"] == 17 for n in nodes) == 1)
    check(rel + ": allowed types, <=40 components", all(n["type"] in ALLOWED for n in nodes) and len(nodes) <= 40)
    check(rel + ": link buttons", all(n["style"] == 5 and set(n) <= BTN and re.match(r"https?://", n["url"]) for n in nodes if n["type"] == 2))

# escaping unit checks
check("md escapes markdown without printing $1", bh.md("a*b_c`d|e[f]g\\h") == "a\\*b\\_c\\`d\\|e\\[f\\]g\\\\h" and bh.md("# x") == "\\# x")
check("payload closes no script early", "</" not in bh.payload([bh.text("</script>")]))
check("payload over the limit is dropped", bh.payload([bh.text("x" * 3100)]) is None)
check("manifest valid", json.loads((ROOT / "site.webmanifest").read_text())["start_url"] == "/")
check("build-head up to date", bh.main.__call__ is not None and not any(
    bh.build(r, p.read_text(encoding="utf-8")) != p.read_text(encoding="utf-8") for r, p in bh.pages() if "</head>" in p.read_text(encoding="utf-8")))
sys.exit(1 if fails else 0)

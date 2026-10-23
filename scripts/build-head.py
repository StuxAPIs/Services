#!/usr/bin/env python3
"""Write the shared <head> blocks into every HTML page of this static site.

Run from anywhere: python scripts/build-head.py   (or --check to only verify nothing is stale)
Two generated blocks, each between marker comments so re-running just replaces them:
  favicon  - the icon set (favicon.ico, 512 PNG, apple-touch-icon, web manifest) plus the
             light/dark themed icons, on every page that has a <head>
  discord  - the Discord component embed (<script id="discord:component-embed">), on every
             page except 404.html and the /changelog/ redirect stub

Copyright (c) 2026 Stux.Group. All Rights Reserved.
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE_URL = "https://" + (ROOT / "CNAME").read_text(encoding="utf-8").strip()
SITE_NAME = "StuxAPIs Services"
ACCENT = 0x7A1FD6          # --accent in assets/css/style.css
MAX_BYTES = 3000           # Discord's limit for the embed JSON
NO_EMBED = {"404.html", "changelog/index.html"}

FAVICON = "\n".join([
    '<link rel="icon" href="/favicon.ico" sizes="48x48">',
    '<link rel="icon" type="image/png" sizes="512x512" href="/assets/img/icon-512.png">',
    '<link rel="icon" type="image/png" href="https://global.media.stuxapis.net/icon-dark.png" media="(prefers-color-scheme: light)">',
    '<link rel="icon" type="image/png" href="https://global.media.stuxapis.net/icon-light.png" media="(prefers-color-scheme: dark)">',
    '<link rel="apple-touch-icon" href="/apple-touch-icon.png">',
    '<link rel="manifest" href="/site.webmanifest">',
])


def md(s):
    """Escape Discord markdown so data shows as plain text."""
    s = re.sub(r"([\\*_~`|\[\]])", lambda m: "\\" + m.group(1), s)
    return re.sub(r"^([#>-])", lambda m: "\\" + m.group(1), s, flags=re.M)


def text(content):
    return {"type": 10, "content": content}


def buttons(links):
    return {"type": 1, "components": [{"type": 2, "style": 5, "label": label[:80], "url": url} for label, url in links]}


def section(content):
    return {"type": 9, "components": [text(content)],
            "accessory": {"type": 11, "media": {"url": BASE_URL + "/assets/img/icon-512.png"}}}


def payload(components):
    """The JSON for the script tag, or None when it is over the 3,000-byte limit."""
    data = {"component": {"type": 17, "accent_color": ACCENT, "components": components}}
    js = json.dumps(data, separators=(",", ":"), ensure_ascii=False).replace("</", "<\/")
    return None if len(js.encode("utf-8")) > MAX_BYTES else js


def embed(components):
    js = payload(components)
    if js is None:
        return "<!-- discord:component-embed left out: over %d bytes -->" % MAX_BYTES
    return '<script id="discord:component-embed" type="application/json">' + js + "</script>"


def page_info(rel, src):
    title = re.search(r"<title>(.*?)</title>", src, re.S)
    title = html.unescape(title.group(1)).strip() if title else SITE_NAME
    title = re.sub(r" (—|-|\|) .*$", "", title)
    desc = re.search(r'<meta name="description" content="([^"]*)"', src)
    desc = html.unescape(desc.group(1)) if desc else SITE_NAME
    path = "/" + rel[: -len("index.html")] if rel.endswith("index.html") else "/" + rel
    return title, desc, BASE_URL + path


def services(src):
    """Names of the live service cards on the home page (no data-state: not soon, template or discontinued)."""
    out = []
    for card in re.findall(r'<article class="project-card"[^>]*>.*?</article>', src, re.S):
        name = re.search(r"<h3>(.*?)</h3>", card, re.S)
        if name:
            out.append(html.unescape(re.sub(r"<[^>]+>", "", name.group(1))).strip())
    return out


def discord_block(rel, src):
    title, desc, url = page_info(rel, src)
    label = "-# [%s](%s/)\n" % (SITE_NAME, BASE_URL)
    if rel == "index.html":
        names = services(src)
        return embed([
            section("# [%s](%s/)\n**Every StuxAPIs API and service, in one place.**\n%d live APIs and services, each with its own repository and live status where it is checked."
                    % (md(SITE_NAME), BASE_URL, len(names))),
            {"type": 14},
            text("### Services\n" + " · ".join(md(n) for n in names)),
            buttons([("Browse services", BASE_URL + "/#services"), ("Status", "https://status.stuxapis.net"), ("StuxAPIs", "https://stuxapis.net")]),
        ])
    return embed([
        section(label + "## [%s](%s)\n%s" % (md(title), url, md(desc))),
        buttons([("Open", url), ("All services", BASE_URL + "/")]),
    ])


def block(name, body):
    return "<!-- %s:start -->\n%s\n<!-- %s:end -->" % (name, body, name)


def strip(src):
    for name in ("favicon", "discord"):
        src = re.sub(r"[ \t]*<!-- %s:start -->.*?<!-- %s:end -->\n?" % (name, name), "", src, flags=re.S)
    # themed icon links used to sit loose in the head; they live in the favicon block now
    return re.sub(r'[ \t]*<link rel="icon" type="image/png" href="https://global\.media\.stuxapis\.net/icon-(?:dark|light)\.png" media="[^"]*">\n', "", src)


def build(rel, src):
    base = strip(src)
    parts = [block("favicon", FAVICON)]
    if rel not in NO_EMBED:
        parts.append(block("discord", discord_block(rel, base)))
    return base.replace("</head>", "\n".join(parts) + "\n</head>", 1)


def pages():
    for p in sorted(ROOT.rglob("*.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith((".git/", "node_modules/", "_site/")):
            continue
        yield rel, p


def main():
    check = "--check" in sys.argv
    stale = 0
    for rel, p in pages():
        src = p.read_text(encoding="utf-8")
        if "</head>" not in src:
            continue
        new = build(rel, src)
        if new != src:
            stale += 1
            if not check:
                p.write_text(new, encoding="utf-8", newline="\n")
    print(("%d page(s) out of date" if check else "%d page(s) updated") % stale)
    return 1 if check and stale else 0


if __name__ == "__main__":
    sys.exit(main())

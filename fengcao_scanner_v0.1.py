#!/usr/bin/env python3
import re
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE = "https://smcy.xyz/new"
LIST_URL = BASE + "/forum.php?mod=forumdisplay&fid=368"


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def parse_threads(html):
    soup = BeautifulSoup(html, "html.parser")
    out = []
    for tb in soup.select('tbody[id^="normalthread_"]'):
        a = tb.select_one("a.s.xst, a.xst")
        if not a:
            continue
        href = a.get("href", "")
        m = re.search(r"tid=(\d+)", href)
        tid = m.group(1) if m else ""
        title = a.get_text(strip=True)
        author = (tb.select_one("td.by cite a") or tb.select_one("td.by cite"))
        author_text = author.get_text(" ", strip=True) if author else ""
        pub = (tb.select_one("td.by em span") or tb.select_one("td.by em"))
        pub_text = pub.get_text(" ", strip=True) if pub else ""
        out.append({
            "tid": tid,
            "title": title,
            "author": author_text,
            "pub": pub_text,
            "url": f"{BASE}/forum.php?mod=viewthread&tid={tid}",
        })
    return out


def check_seal(session, tid):
    url = f"{BASE}/forum.php?mod=viewthread&tid={tid}"
    r = session.get(url, timeout=20)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    title = (soup.select_one("#thread_subject") or soup.select_one("title"))
    title_text = title.get_text(" ", strip=True) if title else ""

    has_seal = False
    seal_author = ""
    for post in soup.select('#postlist > div[id^="post_"]'):
        author = post.select_one(".authi a.xw1, .authi a")
        author_text = author.get_text(" ", strip=True) if author else ""
        body = post.select_one(".t_f")
        body_text = body.get_text("\n", strip=True) if body else ""
        if "心舟草" in author_text and ("封草信息" in body_text or re.search(r"封.+为.+草", body_text)):
            has_seal = True
            seal_author = author_text
            break

    return {
        "tid": tid,
        "title": title_text,
        "hasSeal": has_seal,
        "sealAuthor": seal_author,
        "url": url,
    }


def load_cookies(path):
    if not path:
        return {}
    p = Path(path)
    if not p.exists():
        return {}
    raw = p.read_text(encoding="utf-8").strip()
    if not raw:
        return {}
    # supports JSON object or cookie header string
    if raw.startswith("{"):
        return json.loads(raw)
    out = {}
    for part in raw.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            out[k.strip()] = v.strip()
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--cookies", default="", help="path to cookie json/header text")
    ap.add_argument("--limit", type=int, default=12)
    ap.add_argument("--out", default="/root/.openclaw/workspace/fengcao_scan_report_v0.1.json")
    args = ap.parse_args()

    s = requests.Session()
    s.headers.update({"User-Agent": "Mozilla/5.0 OpenClaw FENGCAO Scanner"})
    ck = load_cookies(args.cookies)
    if ck:
        s.cookies.update(ck)

    r = s.get(LIST_URL, timeout=20)
    r.raise_for_status()
    threads = parse_threads(r.text)[: args.limit]

    results = []
    for t in threads:
        try:
            results.append(check_seal(s, t["tid"]))
        except Exception as e:
            results.append({"tid": t["tid"], "title": t["title"], "hasSeal": False, "error": str(e), "url": t["url"]})

    report = {
        "ts": now_iso(),
        "listUrl": LIST_URL,
        "count": len(results),
        "pending": [x for x in results if not x.get("hasSeal")],
        "sealed": [x for x in results if x.get("hasSeal")],
        "all": results,
    }

    Path(args.out).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"WROTE {args.out}")
    print(f"pending={len(report['pending'])} sealed={len(report['sealed'])}")


if __name__ == "__main__":
    main()

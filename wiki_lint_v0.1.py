#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path

ALLOWED_FILES = {"index.md", "friendly.md", "academic.md", "internal.md"}
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def add_issue(issues, level, code, path, line, message):
    issues.append({
        "level": level,
        "code": code,
        "path": str(path),
        "line": line,
        "message": message,
    })


def check_structure(root: Path, issues):
    for lang in ["zh", "en"]:
        lang_dir = root / lang
        if not lang_dir.exists():
            add_issue(issues, "ERROR", "LANG_DIR_MISSING", lang, 0, f"Missing language dir: {lang}")
            continue

        for p in lang_dir.iterdir():
            if not p.is_dir():
                continue
            slug = p.name
            if not SLUG_RE.match(slug):
                add_issue(issues, "WARN", "BAD_SLUG", p, 0, f"Slug format not standard: {slug}")

            files = {x.name for x in p.glob("*.md")}
            missing = ALLOWED_FILES - files
            extra = files - ALLOWED_FILES
            for m in sorted(missing):
                add_issue(issues, "ERROR", "MISSING_FILE", p / m, 0, f"Missing required file: {m}")
            for e in sorted(extra):
                add_issue(issues, "WARN", "EXTRA_FILE", p / e, 0, f"Unexpected markdown file: {e}")


def check_file(path: Path, issues):
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()

    # filename typo hint
    if path.name == "fridenly.md":
        add_issue(issues, "ERROR", "FILENAME_TYPO", path, 0, "Possible typo: fridenly.md -> friendly.md")

    # YAML front matter detection (simple)
    if lines and lines[0].strip() == "---":
        add_issue(issues, "ERROR", "YAML_FRONT_MATTER", path, 1, "YAML front matter is disallowed")

    # metadata comment at top (within first 8 lines)
    top = "\n".join(lines[:8])
    if "<!--" not in top or "id:" not in top or "lang:" not in top:
        add_issue(issues, "WARN", "MISSING_HTML_META", path, 1, "Top HTML comment metadata not found")

    # wikilink
    for i, line in enumerate(lines, 1):
        if "[[" in line and "]]" in line:
            add_issue(issues, "ERROR", "WIKILINK_FOUND", path, i, "Wikilink [[...]] is disallowed")

    # heading depth
    for i, line in enumerate(lines, 1):
        m = re.match(r"^(#+)\s+", line)
        if m and len(m.group(1)) >= 4:
            add_issue(issues, "WARN", "HEADING_TOO_DEEP", path, i, "Heading level >= 4 detected")

    # tag zone check (if 标签/Classification section exists)
    in_tag_zone = False
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if s.startswith("## 标签") or s.startswith("## Classification") or s.startswith("## 体系归属"):
            in_tag_zone = True
            continue

        if in_tag_zone:
            if s.startswith("## ") and not (s.startswith("## 体系归属") or s.startswith("## Classification")):
                in_tag_zone = False
            elif s.startswith("#"):
                add_issue(issues, "ERROR", "TAG_HEADING_STYLE", path, i, "Tag/classification line uses heading/hash style")

    # language-specific internal links
    lang = "zh" if "/zh/" in str(path).replace("\\", "/") else ("en" if "/en/" in str(path).replace("\\", "/") else None)
    for i, line in enumerate(lines, 1):
        for m in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", line):
            link = m.group(1).strip()
            if link.startswith("http://") or link.startswith("https://"):
                continue
            if link.startswith("/"):
                if lang == "zh" and link.startswith("/en/"):
                    add_issue(issues, "WARN", "CROSS_LANG_LINK", path, i, f"Chinese file links to English path: {link}")
                if lang == "en" and link.startswith("/zh/"):
                    add_issue(issues, "WARN", "CROSS_LANG_LINK", path, i, f"English file links to Chinese path: {link}")


def summarize(issues):
    counts = {"ERROR": 0, "WARN": 0, "INFO": 0}
    by_code = {}
    for it in issues:
        counts[it["level"]] = counts.get(it["level"], 0) + 1
        by_code[it["code"]] = by_code.get(it["code"], 0) + 1
    return counts, by_code


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("repo", help="path to lifecosmos-wiki-pages repo")
    ap.add_argument("--json", dest="json_path", default="", help="write JSON report path")
    args = ap.parse_args()

    root = Path(args.repo).resolve()
    issues = []

    check_structure(root, issues)

    for md in root.rglob("*.md"):
        if "/.git/" in str(md).replace("\\", "/"):
            continue
        check_file(md, issues)

    counts, by_code = summarize(issues)

    print("=== Encyclopedia Lint v0.1 Report ===")
    print(f"Repo: {root}")
    print(f"ERROR: {counts['ERROR']} | WARN: {counts['WARN']} | INFO: {counts['INFO']}")
    print("-- Top issue codes --")
    for code, n in sorted(by_code.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"{code}: {n}")

    print("\n-- Sample issues (first 50) --")
    for it in issues[:50]:
        print(f"[{it['level']}] {it['code']} {it['path']}:{it['line']} :: {it['message']}")

    if args.json_path:
        out = {
            "summary": {"counts": counts, "by_code": by_code},
            "issues": issues,
        }
        Path(args.json_path).write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"\nJSON report written: {args.json_path}")


if __name__ == "__main__":
    main()

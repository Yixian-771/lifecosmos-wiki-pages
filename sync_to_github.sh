#!/usr/bin/env bash
set -euo pipefail
cd /root/wiki-pages

# 若无变化，直接退出
if git diff --quiet && git diff --cached --quiet; then
  echo "[sync] no changes"
  exit 0
fi

git add -A
ts="$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
git commit -m "chore: sync wiki pages ${ts}"
git push origin main
echo "[sync] pushed ${ts}"

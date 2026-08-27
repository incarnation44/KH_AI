#!/bin/bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_DIR"

MSG="${1:-chore: auto sync update $(date +'%Y-%m-%d %H:%M:%S')}"

echo "=== [1/3] 원격 저장소 최신 변경사항 당겨오기 (Pull) ==="
git pull --rebase origin main 2>/dev/null || true

echo "=== [2/3] 로컬 변경사항 스테이징 및 커밋 ==="
git add .
if git diff --staged --quiet; then
    echo "변경사항이 없습니다."
else
    git commit -m "$MSG"
fi

echo "=== [3/3] GitHub로 업로드 (Push) ==="
git push origin main
echo "✅ GitHub (KH_AI) 동기화 완료!"
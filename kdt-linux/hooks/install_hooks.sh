#!/bin/bash
# ===============================================================
# hooks/install_hooks.sh — Git 훅 자동 설치 스크립트
# ===============================================================
set -e
HOOK_SRC="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
GIT_DIR="$(git rev-parse --git-dir 2>/dev/null || echo ".git")"
HOOK_DST="$GIT_DIR/hooks"

mkdir -p "$HOOK_DST"

for h in pre-commit commit-msg; do
    if [ -f "$HOOK_SRC/$h" ]; then
        cp "$HOOK_SRC/$h" "$HOOK_DST/$h"
        chmod +x "$HOOK_DST/$h" 2>/dev/null || true
        echo "[OK] $h 훅이 설치되었습니다."
    fi
done

echo "전체 Git 훅 설치 완료 ($HOOK_DST)"

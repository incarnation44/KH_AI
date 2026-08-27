#!/bin/bash
# ===============================================================
# scripts/dataset_check.sh — 단독 실행용 데이터셋 정합성 검사 CLI
# ===============================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/lib/common.sh"
source "$SCRIPT_DIR/lib/cmd_check.sh"
cmd_check "$@"

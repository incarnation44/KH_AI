#!/bin/bash
# ===============================================================
# scripts/split_dataset.sh — 단독 실행용 데이터셋 분할 CLI
# ===============================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/lib/common.sh"
source "$SCRIPT_DIR/lib/cmd_split.sh"
cmd_split "$@"

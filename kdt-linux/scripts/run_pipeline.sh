#!/bin/bash
# ===============================================================
# scripts/run_pipeline.sh — 단독 실행용 전체 파이프라인 스크립트
# ===============================================================
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
source "$SCRIPT_DIR/lib/common.sh"
source "$SCRIPT_DIR/lib/cmd_run.sh"
cmd_run "$@"

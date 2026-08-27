#!/bin/bash
# ===============================================================
# scripts/auto_backup.sh — cron 연동 가능한 데이터셋 자동 백업 스크립트
# ===============================================================
set -uo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PATH="/usr/local/bin:/usr/bin:/bin:$PATH"

ROOT_DIR="${1:-$SCRIPT_DIR/dataset}"
LOGFILE="$SCRIPT_DIR/logs/backup.log"
KEEP_DAYS=30

mkdir -p "$SCRIPT_DIR/logs"

log () { echo "[$(date '+%Y-%m-%d %H:%M:%S')] $*" | tee -a "$LOGFILE"; }

log "===== [데이터셋 자동 백업 시작] ====="

for ds in "$ROOT_DIR"/*/; do
    [ -d "$ds" ] || continue
    name=$(basename "$ds")
    stamp=$(date +%Y%m%d_%H%M%S)
    backup_dir="$ds/backup"
    out_file="$backup_dir/${name}_meta_${stamp}.tar.gz"

    mkdir -p "$backup_dir"

    if [ -d "$ds/meta" ]; then
        if tar -czf "$out_file" -C "$ds" meta 2>/dev/null; then
            sz=$(du -h "$out_file" 2>/dev/null | cut -f1)
            log "OK   $name -> $(basename "$out_file") ($sz)"
        else
            log "ERR  $name 백업 실패"
        fi
    fi

    # 정합성 검사도 병행 실행
    if "$SCRIPT_DIR/visionops" check "$ds" >/dev/null 2>&1; then
        log "OK   $name 정합성 검사 통과 (PASS)"
    else
        log "WARN $name 정합성 검사 결함 발견 (FAIL)"
    fi
done

deleted=$(find "$ROOT_DIR" -name "*_meta_*.tar.gz" -mtime +"$KEEP_DAYS" -print -delete 2>/dev/null | wc -l)
log "보존 주기(${KEEP_DAYS}일) 초과 오래된 백업 ${deleted}건 정리 완료"
log "===== [데이터셋 자동 백업 종료] ====="

#!/bin/bash
# ===============================================================
# lib/common.sh — visionops 공통 라이브러리 (로깅, 색상, 유틸리티)
# ===============================================================

readonly C_RED='\033[0;31m'
readonly C_GRN='\033[0;32m'
readonly C_YEL='\033[0;33m'
readonly C_BLU='\033[0;34m'
readonly C_CYN='\033[0;36m'
readonly C_NC='\033[0m'

LOG_DIR="${LOG_DIR:-./logs}"
QUIET="${QUIET:-0}"

_ts () { date '+%Y-%m-%d %H:%M:%S'; }

_write_log () {
    mkdir -p "$LOG_DIR"
    echo "[$(_ts)] $*" >> "$LOG_DIR/visionops.log"
}

log ()   { [ "$QUIET" -eq 1 ] || echo "  $*";                    _write_log "INFO  $*"; }
ok ()    { [ "$QUIET" -eq 1 ] || echo -e "  ${C_GRN}[OK]${C_NC}   $*";  _write_log "OK    $*"; }
warn ()  { echo -e "  ${C_YEL}[WARN]${C_NC} $*" >&2;             _write_log "WARN  $*"; }
fail ()  { echo -e "  ${C_RED}[FAIL]${C_NC} $*" >&2;             _write_log "FAIL  $*"; }
die ()   { fail "$*"; exit 1; }

section () {
    [ "$QUIET" -eq 1 ] && return
    echo ""
    echo -e "${C_BLU}[$1]${C_NC} $2"
}

banner () {
    [ "$QUIET" -eq 1 ] && return
    echo -e "${C_CYN}══════════════════════════════════════════════${C_NC}"
    echo "  $1"
    echo "  $(_ts)"
    echo -e "${C_CYN}══════════════════════════════════════════════${C_NC}"
}

require_dir () { [ -d "$1" ] || die "디렉토리 없음: $1"; }
require_cmd () { command -v "$1" >/dev/null 2>&1 || die "필수 명령어 없음: $1"; }

count_files () { find "$1" -maxdepth 1 -name "$2" 2>/dev/null | wc -l; }

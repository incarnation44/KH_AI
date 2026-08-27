#!/bin/bash
# ===============================================================
# lib/cmd_backup.sh — visionops backup 서브커맨드
# 목적: 데이터셋 메타데이터 자동 아카이브 백업 및 보존 주기 관리
# ===============================================================

cmd_backup_usage () {
    cat << EOF
사용법: visionops backup <dataset_dir> [옵션]

인자:
  dataset_dir       백업할 데이터셋 루트 디렉토리

옵션:
  --keep-days <N>   백업 파일 보존 일수 (기본: 30일)
  -h, --help        도움말
EOF
}

cmd_backup () {
    local DS=""
    local KEEP_DAYS=30

    [ $# -eq 0 ] && { cmd_backup_usage; exit 2; }
    DS="$1"; shift
    while [ $# -gt 0 ]; do
        case "$1" in
            --keep-days) shift; KEEP_DAYS="$1" ;;
            -h|--help)   cmd_backup_usage; exit 0 ;;
            *) die "알 수 없는 옵션: $1" ;;
        esac
        shift
    done

    [ -d "$DS" ] || die "경로 없음: $DS"

    banner "visionops backup :: $(basename "$DS")"

    local name
    name=$(basename "$DS")
    local stamp
    stamp=$(date +%Y%m%d_%H%M%S)
    local backup_dir="$DS/backup"
    local out_file="$backup_dir/${name}_meta_${stamp}.tar.gz"

    mkdir -p "$backup_dir"

    if [ -d "$DS/meta" ]; then
        if tar -czf "$out_file" -C "$DS" meta 2>/dev/null; then
            local sz
            sz=$(du -h "$out_file" 2>/dev/null | cut -f1)
            ok "메타데이터 아카이브 생성 완료: $(basename "$out_file") ($sz)"
        else
            die "아카이브 압축 생성 실패"
        fi
    else
        die "백업 대상 meta/ 디렉토리가 없습니다."
    fi

    local deleted
    deleted=$(find "$backup_dir" -name "*_meta_*.tar.gz" -mtime +"$KEEP_DAYS" -print -delete 2>/dev/null | wc -l)
    if [ "$deleted" -gt 0 ]; then
        log "${KEEP_DAYS}일 초과된 오래된 백업 ${deleted}건 정리 완료"
    fi

    return 0
}

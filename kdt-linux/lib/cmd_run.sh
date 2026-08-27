#!/bin/bash
# ===============================================================
# lib/cmd_run.sh — visionops run 서브커맨드
# 목적: 검증 → 분할 → 리포트 → 백업 전체 파이프라인 자동 실행
# ===============================================================

cmd_run_usage () {
    cat << EOF
사용법: visionops run <dataset_dir> [옵션]

인자:
  dataset_dir       파이프라인을 실행할 데이터셋 루트 디렉토리

옵션:
  --min <N>         최소 요구 이미지 장수 (기본: 500)
  --ratio <T:V:S>   분할 비율 (기본: 70:15:15)
  --seed <N>        분할 시드 (기본: 42)
  --fix             검증 단계에서 단순 문제 자동 수정
  -h, --help        도움말
EOF
}

cmd_run () {
    local DS=""
    local MIN_IMAGES=500
    local RATIO="70:15:15"
    local SEED=42
    local DO_FIX_OPT=""

    [ $# -eq 0 ] && { cmd_run_usage; exit 2; }
    DS="$1"; shift
    while [ $# -gt 0 ]; do
        case "$1" in
            --min)   shift; MIN_IMAGES="$1" ;;
            --ratio) shift; RATIO="$1" ;;
            --seed)  shift; SEED="$1" ;;
            --fix)   DO_FIX_OPT="--fix" ;;
            -h|--help) cmd_run_usage; exit 0 ;;
            *) die "알 수 없는 옵션: $1" ;;
        esac
        shift
    done

    [ -d "$DS" ] || die "경로 없음: $DS"

    local start_time
    start_time=$(date +%s)
    banner "visionops run :: 통합 파이프라인 ($(basename "$DS"))"

    # 1. 검증 단계
    section 1 "파이프라인 1단계: 정합성 검증"
    source "$LIB_DIR/cmd_check.sh"
    if ! cmd_check "$DS" --min "$MIN_IMAGES" $DO_FIX_OPT; then
        die "검증 단계 실패로 파이프라인이 중단되었습니다."
    fi

    # 2. 분할 단계
    section 2 "파이프라인 2단계: 데이터셋 분할 (70:15:15)"
    source "$LIB_DIR/cmd_split.sh"
    cmd_split "$DS" --ratio "$RATIO" --seed "$SEED" --clean || die "분할 단계 실패"

    # 3. 리포트 단계
    section 3 "파이프라인 3단계: 통계 리포트 생성"
    source "$LIB_DIR/cmd_report.sh"
    cmd_report "$DS" || die "리포트 생성 실패"

    # 4. 백업 단계
    section 4 "파이프라인 4단계: 메타데이터 아카이브 백업"
    source "$LIB_DIR/cmd_backup.sh"
    cmd_backup "$DS" || die "백업 단계 실패"

    local end_time
    end_time=$(date +%s)
    local elapsed=$((end_time - start_time))

    echo ""
    echo -e "${C_GRN}══════════════════════════════════════════════${C_NC}"
    echo -e "  ${C_GRN}✔ 파이프라인 전체 완료!${C_NC} (소요 시간: ${elapsed}초)"
    echo -e "${C_GRN}══════════════════════════════════════════════${C_NC}"
    return 0
}

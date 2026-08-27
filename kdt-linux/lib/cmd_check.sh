#!/bin/bash
# ===============================================================
# lib/cmd_check.sh — visionops check 서브커맨드
# 목적: Vision AI YOLO 데이터셋 정합성 검증
# ===============================================================

cmd_check_usage () {
    cat << EOF
사용법: visionops check <dataset_dir> [옵션]

인자:
  dataset_dir       검사할 데이터셋 루트 디렉토리

옵션:
  --fix             발견된 단순 문제(빈 라벨 파일 삭제, 공백 파일명 변경) 자동 수정
  --min <N>         최소 요구 이미지 장수 (기본: 500)
  --balance-ratio <R> 클래스 최대/최소 비율 허용치 (기본: 5)
  -h, --help        도움말

종료 코드:
  0: PASS (정상)
  1: FAIL (오류 발견)
  2: 사용법 오류
EOF
}

cmd_check () {
    local DATASET_DIR=""
    local MIN_IMAGES=500
    local BALANCE_RATIO=5
    local DO_FIX=0
    local ERRORS=0
    local WARNINGS=0
    local NUM_CLASSES=0
    local IMG_COUNT=0
    local LBL_COUNT=0

    [ $# -eq 0 ] && { cmd_check_usage; exit 2; }
    DATASET_DIR="$1"; shift
    while [ $# -gt 0 ]; do
        case "$1" in
            --fix)           DO_FIX=1 ;;
            --min)           shift; MIN_IMAGES="$1" ;;
            --balance-ratio) shift; BALANCE_RATIO="$1" ;;
            -h|--help)       cmd_check_usage; exit 0 ;;
            *) die "알 수 없는 옵션: $1" ;;
        esac
        shift
    done

    [ -d "$DATASET_DIR" ] || die "데이터셋 디렉토리가 존재하지 않습니다: $DATASET_DIR"

    banner "visionops check :: $(basename "$DATASET_DIR")"

    # [1] 구조 검사
    section 1 "디렉토리 구조 검증"
    local raw_dir="$DATASET_DIR/raw"
    local img_raw="$DATASET_DIR/raw/images"
    local lbl_raw="$DATASET_DIR/raw/labels"

    # raw 내부에 images/labels 가 없는 경우 raw 자체를 대상 디렉토리로 호환
    if [ ! -d "$img_raw" ] && [ -d "$raw_dir" ]; then
        img_raw="$raw_dir"
        lbl_raw="$raw_dir"
    fi

    if [ -d "$DATASET_DIR/raw" ]; then
        ok "raw/ 디렉토리 존재"
    else
        fail "raw/ 디렉토리 누락"; ERRORS=$((ERRORS+1))
    fi

    if [ -f "$DATASET_DIR/meta/classes.txt" ]; then
        NUM_CLASSES=$(grep -c . "$DATASET_DIR/meta/classes.txt" 2>/dev/null || echo 0)
        ok "meta/classes.txt 존재 (${NUM_CLASSES}종 정의됨)"
    else
        warn "meta/classes.txt 없음"; WARNINGS=$((WARNINGS+1))
        NUM_CLASSES=0
    fi

    # [2] 이미지-라벨 짝 검증
    section 2 "이미지-라벨 짝(Pairing) 검증"
    IMG_COUNT=$(find "$img_raw" -maxdepth 1 -name "*.jpg" -o -name "*.png" 2>/dev/null | wc -l)
    LBL_COUNT=$(find "$lbl_raw" -maxdepth 1 -name "*.txt" 2>/dev/null | wc -l)
    log "발견: 이미지 ${IMG_COUNT}장 / 라벨 ${LBL_COUNT}개"

    local tmp_i="/tmp/_vo_i_$$"
    local tmp_l="/tmp/_vo_l_$$"
    find "$img_raw" -maxdepth 1 \( -name "*.jpg" -o -name "*.png" \) -exec basename {} \; 2>/dev/null \
      | sed -E 's/\.(jpg|png)$//' | sort > "$tmp_i" 2>/dev/null || true
    find "$lbl_raw" -maxdepth 1 -name "*.txt" -exec basename {} .txt \; 2>/dev/null \
      | sort > "$tmp_l" 2>/dev/null || true

    local no_lbl no_img
    no_lbl=$(comm -23 "$tmp_i" "$tmp_l" 2>/dev/null | wc -l)
    no_img=$(comm -13 "$tmp_i" "$tmp_l" 2>/dev/null | wc -l)

    if [ "$no_lbl" -eq 0 ]; then
        ok "라벨 누락 이미지 없음"
    else
        warn "라벨 없는 이미지 ${no_lbl}건 발견 (미라벨링/배경 학습 유의)"
        comm -23 "$tmp_i" "$tmp_l" 2>/dev/null | head -3 | sed 's/^/         - /'
        WARNINGS=$((WARNINGS+1))
    fi

    if [ "$no_img" -eq 0 ]; then
        ok "이미지 누락 라벨 없음"
    else
        fail "이미지 없는 고아 라벨 ${no_img}건 발견"; ERRORS=$((ERRORS+1))
        comm -13 "$tmp_i" "$tmp_l" 2>/dev/null | head -3 | sed 's/^/         - /'
    fi
    rm -f "$tmp_i" "$tmp_l" 2>/dev/null

    # [3] 라벨 포맷 및 데이터 정합성 검증
    section 3 "라벨 포맷 및 데이터 정합성 검증"
    local empty_lbls
    empty_lbls=$(find "$lbl_raw" -maxdepth 1 -name "*.txt" -size 0 2>/dev/null | wc -l)
    if [ "$empty_lbls" -eq 0 ]; then
        ok "빈 라벨 파일 없음 (0 바이트)"
    else
        warn "빈 라벨 파일 ${empty_lbls}건 발견"; WARNINGS=$((WARNINGS+1))
        if [ "$DO_FIX" -eq 1 ]; then
            find "$lbl_raw" -maxdepth 1 -name "*.txt" -size 0 -delete 2>/dev/null
            log "     → [--fix] 빈 라벨 파일 자동 삭제 완료"
        fi
    fi

    # 필드 개수(5) 검사
    local bad_nf
    bad_nf=$(awk 'NF!=5 && NF!=0 {print FILENAME}' "$lbl_raw"/*.txt 2>/dev/null | sort -u | wc -l)
    if [ "$bad_nf" -eq 0 ]; then
        ok "YOLO 필드 개수 (클래스+좌표 5개) 정상"
    else
        fail "필드 개수 오류 파일 ${bad_nf}건 발견"; ERRORS=$((ERRORS+1))
    fi

    # 좌표 범위 0~1 검사
    local bad_range
    bad_range=$(awk '{for(i=2;i<=5;i++) if($i<0 || $i>1){print FILENAME; next}}' "$lbl_raw"/*.txt 2>/dev/null | sort -u | wc -l)
    if [ "$bad_range" -eq 0 ]; then
        ok "바운딩 박스 좌표 정규화 범위 (0.0 ~ 1.0) 정상"
    else
        fail "좌표 범위 초과 파일 ${bad_range}건 발견"; ERRORS=$((ERRORS+1))
        awk '{for(i=2;i<=5;i++) if($i<0 || $i>1){print "         - "FILENAME": "$0; next}}' "$lbl_raw"/*.txt 2>/dev/null | head -3
    fi

    # 클래스 ID 유효 범위 검사
    if [ "$NUM_CLASSES" -gt 0 ]; then
        local max_c=$((NUM_CLASSES-1))
        local bad_cls
        bad_cls=$(awk -v m="$max_c" '$1<0 || $1>m {print FILENAME}' "$lbl_raw"/*.txt 2>/dev/null | sort -u | wc -l)
        if [ "$bad_cls" -eq 0 ]; then
            ok "클래스 ID 범위 (0 ~ ${max_c}) 정상"
        else
            fail "미정의 클래스 ID 사용 파일 ${bad_cls}건 발견"; ERRORS=$((ERRORS+1))
        fi
    fi

    # [4] 파일명 규칙 검사
    section 4 "파일명 규칙 검증"
    local spaced_files
    spaced_files=$(find "$img_raw" "$lbl_raw" -maxdepth 1 -name "* *" 2>/dev/null | wc -l)
    if [ "$spaced_files" -eq 0 ]; then
        ok "공백 포함 비표준 파일명 없음"
    else
        warn "공백 포함 파일명 ${spaced_files}건 발견"; WARNINGS=$((WARNINGS+1))
        if [ "$DO_FIX" -eq 1 ]; then
            find "$img_raw" "$lbl_raw" -maxdepth 1 -name "* *" 2>/dev/null | while read -r f; do
                mv "$f" "$(echo "$f" | tr ' ' '_')" 2>/dev/null
            done
            log "     → [--fix] 파일명 공백을 언더스코어(_)로 자동 치환 완료"
        fi
    fi

    # [5] 데이터 규모 검사
    section 5 "데이터 규모 요건 검증"
    log "요구 요건: 최소 ${MIN_IMAGES}장"
    if [ "$IMG_COUNT" -ge "$MIN_IMAGES" ]; then
        ok "데이터 규모 충족 (${IMG_COUNT}장 >= ${MIN_IMAGES}장)"
    else
        fail "데이터 규모 미달 (${IMG_COUNT}장 / 최소 요구 ${MIN_IMAGES}장)"; ERRORS=$((ERRORS+1))
    fi

    # [6] 클래스 불균형 검사
    section 6 "클래스 불균형 검증"
    local cls_stats
    cls_stats=$(cat "$lbl_raw"/*.txt 2>/dev/null | awk '{print $1}' | sort -n | uniq -c | awk '{print $1}' | sort -n)
    local min_cnt max_cnt ratio
    min_cnt=$(echo "$cls_stats" | head -1)
    max_cnt=$(echo "$cls_stats" | tail -1)
    if [ -n "$min_cnt" ] && [ "$min_cnt" -gt 0 ]; then
        ratio=$(awk -v a="$max_cnt" -v b="$min_cnt" 'BEGIN{printf "%.1f", a/b}')
        log "최다/최소 클래스 비율: ${ratio}:1 (최대 $max_cnt 개, 최소 $min_cnt 개)"
        if awk -v r="$ratio" -v l="$BALANCE_RATIO" 'BEGIN{exit !(r>l)}'; then
            warn "클래스 불균형 감지 (${ratio}:1 > ${BALANCE_RATIO}:1) — 데이터 증강 권장"; WARNINGS=$((WARNINGS+1))
        else
            ok "클래스 분포 균형 양호"
        fi
    else
        log "(라벨 통계 데이터 없음)"
    fi

    # [7] 종합 판정
    echo ""
    echo "=============================================="
    printf "  결과 요약: 오류 %d건 / 경고 %d건\n" "$ERRORS" "$WARNINGS"
    if [ "$ERRORS" -eq 0 ]; then
        echo -e "  최종 판정: ${C_GRN}PASS ✔${C_NC}"
        echo "=============================================="
        return 0
    else
        echo -e "  최종 판정: ${C_RED}FAIL ✘${C_NC}"
        echo "=============================================="
        return 1
    fi
}

#!/bin/bash
# ===============================================================
# lib/cmd_report.sh — visionops report 서브커맨드
# 목적: 데이터셋 통계 및 클래스 분포 리포트 생성
# ===============================================================

cmd_report_usage () {
    cat << EOF
사용법: visionops report <dataset_dir> [옵션]

인자:
  dataset_dir       통계를 산출할 데이터셋 루트 디렉토리

옵션:
  -o, --output <f>  리포트 저장 경로 (기본: <dataset_dir>/meta/dataset_report.txt)
  -h, --help        도움말
EOF
}

cmd_report () {
    local DS=""
    local OUT=""

    [ $# -eq 0 ] && { cmd_report_usage; exit 2; }
    DS="$1"; shift
    while [ $# -gt 0 ]; do
        case "$1" in
            -o|--output) shift; OUT="$1" ;;
            -h|--help)   cmd_report_usage; exit 0 ;;
            *) die "알 수 없는 옵션: $1" ;;
        esac
        shift
    done

    [ -d "$DS" ] || die "경로 없음: $DS"
    [ -z "$OUT" ] && OUT="$DS/meta/dataset_report.txt"

    banner "visionops report :: $(basename "$DS")"

    local raw_img="$DS/raw/images"
    local raw_lbl="$DS/raw/labels"
    if [ ! -d "$raw_img" ]; then
        raw_img="$DS/raw"
        raw_lbl="$DS/raw"
    fi

    local cls_file="$DS/meta/classes.txt"
    local total_img total_lbl total_box
    total_img=$(find "$raw_img" -maxdepth 1 -name "*.jpg" -o -name "*.png" 2>/dev/null | wc -l)
    total_lbl=$(find "$raw_lbl" -maxdepth 1 -name "*.txt" 2>/dev/null | wc -l)
    total_box=$(cat "$raw_lbl"/*.txt 2>/dev/null | wc -l)

    mkdir -p "$(dirname "$OUT")"

    {
        echo "=============================================="
        echo "  Vision AI Dataset Report :: $(basename "$DS")"
        echo "  일시: $(date '+%Y-%m-%d %H:%M:%S')"
        echo "=============================================="
        echo ""
        printf "  %-20s %10d 장\n" "총 이미지 수:" "$total_img"
        printf "  %-20s %10d 개\n" "총 라벨 파일 수:" "$total_lbl"
        printf "  %-20s %10d 개\n" "총 바운딩 박스:" "$total_box"
        if [ "$total_img" -gt 0 ]; then
            local avg_box
            avg_box=$(awk -v b="$total_box" -v i="$total_img" 'BEGIN{printf "%.2f", b/i}')
            printf "  %-20s %10s 개/장\n" "이미지당 평균 객체:" "$avg_box"
        fi
        echo ""
        echo "  [클래스별 Bounding Box 분포]"
        printf "  %-6s %-24s %8s\n" "ID" "CLASS NAME" "COUNT"
        printf "  %-6s %-24s %8s\n" "----" "------------------------" "--------"

        if [ -f "$cls_file" ]; then
            awk 'NR==FNR {name[$1]=$2; next}
                 NF==5 {c[$1]++}
                 END {
                     for (k in name) {
                         cnt = (c[k] ? c[k] : 0)
                         printf "  %-6s %-24s %8d\n", k, name[k], cnt
                     }
                 }' "$cls_file" "$raw_lbl"/*.txt 2>/dev/null | sort -k1,1n
        else
            cat "$raw_lbl"/*.txt 2>/dev/null | awk '{c[$1]++} END{for(k in c) printf "  %-6s %-24s %8d\n", k, "class_"k, c[k]}' | sort -k1,1n
        fi
        echo "=============================================="
    } > "$OUT"

    cat "$OUT"
    ok "리포트가 생성되어 저장되었습니다 ($OUT)"
    return 0
}

#!/bin/bash
# ===============================================================
# lib/cmd_split.sh — visionops split 서브커맨드
# 목적: 고정 시드 기반 train/val/test 데이터셋 분할
# ===============================================================

cmd_split_usage () {
    cat << EOF
사용법: visionops split <dataset_dir> [옵션]

인자:
  dataset_dir       분할할 데이터셋 루트 디렉토리

옵션:
  --ratio <T:V:S>   분할 비율 (기본: 70:15:15)
  --seed <N>        난수 고정 시드 (기본: 42)
  --copy            심볼릭 링크 대신 파일 복사 모드 사용
  --clean           기존 분할 디렉토리 초기화 후 재분할
  -h, --help        도움말
EOF
}

cmd_split () {
    local DS=""
    local TRAIN_R=70; local VAL_R=15; local TEST_R=15
    local SEED=42
    local MODE="link"
    local CLEAN=0

    [ $# -eq 0 ] && { cmd_split_usage; exit 2; }
    DS="$1"; shift
    while [ $# -gt 0 ]; do
        case "$1" in
            --ratio) shift
                TRAIN_R=$(echo "$1" | cut -d: -f1)
                VAL_R=$(echo   "$1" | cut -d: -f2)
                TEST_R=$(echo  "$1" | cut -d: -f3) ;;
            --seed)  shift; SEED="$1" ;;
            --copy)  MODE="copy" ;;
            --clean) CLEAN=1 ;;
            -h|--help) cmd_split_usage; exit 0 ;;
            *) die "알 수 없는 옵션: $1" ;;
        esac
        shift
    done

    [ -d "$DS" ] || die "경로 없음: $DS"

    local raw_img="$DS/raw/images"
    local raw_lbl="$DS/raw/labels"
    if [ ! -d "$raw_img" ]; then
        raw_img="$DS/raw"
        raw_lbl="$DS/raw"
    fi

    local sum=$((TRAIN_R + VAL_R + TEST_R))
    [ "$sum" -eq 100 ] || die "분할 비율 합이 100이 아닙니다 (입력: $sum)"

    banner "visionops split :: $(basename "$DS")"

    if [ "$CLEAN" -eq 1 ]; then
        log "기존 분할 디렉토리 정리 중..."
        rm -rf "$DS"/images/{train,val,test} "$DS"/labels/{train,val,test}
    fi

    # 유효 쌍(이미지 + 라벨) 수집
    local tmp_valid="/tmp/_vo_valid_$$"
    local tmp_shuf="/tmp/_vo_shuf_$$"
    : > "$tmp_valid"

    for img in "$raw_img"/*.jpg "$raw_img"/*.png; do
        [ -e "$img" ] || continue
        local base ext
        base=$(basename "$img" | sed -E 's/\.(jpg|png)$//')
        ext="${img##*.}"
        if [ -s "$raw_lbl/$base.txt" ]; then
            echo "$base.$ext" >> "$tmp_valid"
        fi
    done

    local TOTAL
    TOTAL=$(wc -l < "$tmp_valid" 2>/dev/null || echo 0)
    log "유효 샘플 쌍(이미지+라벨 모두 존재): ${TOTAL}개"
    [ "$TOTAL" -gt 0 ] || die "분할할 유효 데이터가 없습니다."

    # 고정 시드 셔플
    awk -v seed="$SEED" 'BEGIN{srand(seed)} {print rand() "\t" $0}' "$tmp_valid" \
      | sort -k1,1n | cut -f2 > "$tmp_shuf"

    local N_TRAIN=$(( TOTAL * TRAIN_R / 100 ))
    local N_VAL=$(( TOTAL * VAL_R / 100 ))
    local N_TEST=$(( TOTAL - N_TRAIN - N_VAL ))

    log "분할 계획: Train=$N_TRAIN / Val=$N_VAL / Test=$N_TEST (시드=$SEED, 모드=$MODE)"

    mkdir -p "$DS"/images/{train,val,test} "$DS"/labels/{train,val,test}

    local tmp_tr="/tmp/_vo_tr_$$"
    local tmp_va="/tmp/_vo_va_$$"
    local tmp_te="/tmp/_vo_te_$$"

    head -n "$N_TRAIN"                          "$tmp_shuf" > "$tmp_tr"
    sed -n "$((N_TRAIN+1)),$((N_TRAIN+N_VAL))p" "$tmp_shuf" > "$tmp_va"
    sed -n "$((N_TRAIN+N_VAL+1)),\$p"           "$tmp_shuf" > "$tmp_te"

    for split in train val test; do
        local list_file="/tmp/_vo_${split}_$$"
        case "$split" in
            train) list_file="$tmp_tr" ;;
            val)   list_file="$tmp_va" ;;
            test)  list_file="$tmp_te" ;;
        esac

        while read -r file_with_ext; do
            [ -z "$file_with_ext" ] && continue
            local base="${file_with_ext%.*}"
            local ext="${file_with_ext##*.}"
            local src_i="$raw_img/$file_with_ext"
            local src_l="$raw_lbl/$base.txt"

            if [ "$MODE" = "link" ]; then
                # 심볼릭 링크 시도 후 실패 시 복사 fallback
                ln -sf "$(cd "$(dirname "$src_i")" 2>/dev/null && pwd)/$(basename "$src_i")" "$DS/images/$split/$file_with_ext" 2>/dev/null \
                  || cp "$src_i" "$DS/images/$split/"
                ln -sf "$(cd "$(dirname "$src_l")" 2>/dev/null && pwd)/$(basename "$src_l")" "$DS/labels/$split/$base.txt" 2>/dev/null \
                  || cp "$src_l" "$DS/labels/$split/"
            else
                cp "$src_i" "$DS/images/$split/"
                cp "$src_l" "$DS/labels/$split/"
            fi
        done < "$list_file"
    done

    # 시드 정보 기록
    mkdir -p "$DS/meta"
    cat > "$DS/meta/split_seed.txt" << EOF
seed=$SEED
ratio=${TRAIN_R}:${VAL_R}:${TEST_R}
mode=$MODE
total=$TOTAL
train=$N_TRAIN
val=$N_VAL
test=$N_TEST
generated=$(date '+%Y-%m-%d %H:%M:%S')
command=visionops split $DS --ratio ${TRAIN_R}:${VAL_R}:${TEST_R} --seed $SEED
EOF

    rm -f "$tmp_valid" "$tmp_shuf" "$tmp_tr" "$tmp_va" "$tmp_te" 2>/dev/null

    echo ""
    echo "=============================================="
    printf "  %-8s %10s %10s\n" "SPLIT" "IMAGES" "LABELS"
    printf "  %-8s %10s %10s\n" "-------" "------" "------"
    for s in train val test; do
        printf "  %-8s %10d %10d\n" "$s" \
            "$(find "$DS/images/$s" -maxdepth 1 -type f 2>/dev/null | wc -l)" \
            "$(find "$DS/labels/$s" -maxdepth 1 -type f 2>/dev/null | wc -l)"
    done
    echo "  --------------------------------------------"
    ok "분할 완료 및 시드 기록 ($DS/meta/split_seed.txt)"
    echo "=============================================="
    return 0
}

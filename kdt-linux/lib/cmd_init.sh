#!/bin/bash
# ===============================================================
# lib/cmd_init.sh — visionops init 서브커맨드
# 목적: YOLO 표준 데이터셋 디렉토리 구조 및 메타 문서 생성
# ===============================================================

cmd_init_usage () {
    cat << EOF
사용법: visionops init <name> [옵션]

인자:
  name              데이터셋 이름 (예: kimchi, conveyor)

옵션:
  --root <path>     데이터셋 생성 상위 디렉토리 (기본: ./dataset)
  --classes <n>     초기 클래스 수 (기본: 5)
  -h, --help        도움말
EOF
}

cmd_init () {
    local NAME="" ROOT="./dataset" NCLS=5

    [ $# -eq 0 ] && { cmd_init_usage; exit 2; }
    NAME="$1"; shift
    while [ $# -gt 0 ]; do
        case "$1" in
            --root)    shift; ROOT="$1" ;;
            --classes) shift; NCLS="$1" ;;
            -h|--help) cmd_init_usage; exit 0 ;;
            *) die "알 수 없는 옵션: $1" ;;
        esac
        shift
    done

    local DS="$ROOT/$NAME"
    banner "visionops init :: $NAME"

    [ -d "$DS" ] && die "데이터셋 디렉토리가 이미 존재합니다: $DS"

    section 1 "표준 디렉토리 계층 생성"
    mkdir -p "$DS"/raw/{images,labels}
    mkdir -p "$DS"/images/{train,val,test}
    mkdir -p "$DS"/labels/{train,val,test}
    mkdir -p "$DS"/{processed,meta,backup}
    ok "표준 디렉토리 생성 완료 ($DS)"

    section 2 "메타데이터 및 클래스 정의서 생성"
    : > "$DS/meta/classes.txt"
    for i in $(seq 0 $((NCLS-1))); do
        echo "$i class_$i" >> "$DS/meta/classes.txt"
    done
    ok "meta/classes.txt 생성 (${NCLS}종)"

    cat > "$DS/meta/data.yaml" << EOF
# Vision AI YOLO Dataset Config
path: $(cd "$DS" 2>/dev/null && pwd || echo "$DS")
train: images/train
val: images/val
test: images/test

nc: $NCLS
names:
$(awk '{printf "  %s: %s\n", $1, $2}' "$DS/meta/classes.txt")
EOF
    ok "meta/data.yaml 생성"

    cat > "$DS/meta/DATASET.md" << EOF
# $NAME Dataset

## 개요
| 항목 | 내용 |
|---|---|
| 데이터셋명 | $NAME |
| 생성일자 | $(date +%Y-%m-%d) |
| 클래스 수 | $NCLS |
| 라벨 포맷 | YOLO (class x_center y_center width height, 0~1 정규화) |
| 분할 비율 | train : val : test = 70 : 15 : 15 |

## 클래스 목록
\`\`\`
$(cat "$DS/meta/classes.txt")
\`\`\`

## 보안 및 사용 제한 ⚠️
- ㈜비솔 제공 데이터는 **원내 폐쇄망 전용**이며 GitHub 및 외부 클라우드 업로드가 금지됩니다.
- 원본 raw/ 디렉토리는 읽기 전용으로 관리하십시오.
EOF
    ok "meta/DATASET.md 생성"

    section 3 "초기화 완료 안내"
    log "생성 위치: $DS"
    log "다음 단계: $DS/raw/images 및 $DS/raw/labels 에 원본 데이터를 배치한 후"
    log "           visionops check $DS 를 실행하여 검증하십시오."
    return 0
}

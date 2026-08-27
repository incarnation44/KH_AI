#!/bin/bash
# ===============================================================
# tests/test_basic.sh — visionops 기본 기능 및 종료 코드 검증
# ===============================================================
set -uo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$SCRIPT_DIR"

PASS=0
FAIL=0

t_ok () {
    local name="$1"; shift
    if "$@" >/dev/null 2>&1; then
        echo -e "  \033[0;32m[PASS]\033[0m $name"
        PASS=$((PASS+1))
    else
        echo -e "  \033[0;31m[FAIL]\033[0m $name"
        FAIL=$((FAIL+1))
    fi
}

t_exit () {
    local name="$1" expect="$2"; shift 2
    local rc=0
    "$@" >/dev/null 2>&1 || rc=$?
    if [ "$rc" -eq "$expect" ]; then
        echo -e "  \033[0;32m[PASS]\033[0m $name (Exit Code: $rc)"
        PASS=$((PASS+1))
    else
        echo -e "  \033[0;31m[FAIL]\033[0m $name (기대: $expect / 실제: $rc)"
        FAIL=$((FAIL+1))
    fi
}

echo "=============================================="
echo " visionops 자동화 테스트 스위트"
echo "=============================================="

# 1. 기본 CLI 플래그
t_ok    "1. --help 플래그 정상 출력"             bash visionops --help
t_ok    "2. --version 플래그 정상 출력"          bash visionops --version
t_exit  "3. 인자 없음 -> 종료 코드 2 반환"       2 bash visionops
t_exit  "4. 잘못된 명령 -> 종료 코드 2 반환"     2 bash visionops nosuchcommand

# 2. 데이터셋 생성 및 파이프라인
TEST_DIR="./dataset/_test_unit"
rm -rf "$TEST_DIR"

t_ok    "5. visionops init 데이터셋 생성"        bash visionops init _test_unit --root ./dataset --classes 3

# 테스트용 더미 샘플 생성
mkdir -p "$TEST_DIR/raw/images" "$TEST_DIR/raw/labels"
for i in 01 02 03 04 05; do
    printf '\xff\xd8\xff\xe0' > "$TEST_DIR/raw/images/sample_${i}.jpg"
    echo "0 0.5 0.5 0.2 0.2" > "$TEST_DIR/raw/labels/sample_${i}.txt"
done

t_ok    "6. visionops check 정합성 검사 (PASS)"   bash visionops check "$TEST_DIR" --min 5
t_ok    "7. visionops split 데이터셋 분할"       bash visionops split "$TEST_DIR" --ratio 60:20:20 --seed 42 --clean --copy
t_ok    "8. visionops report 통계 리포트 생성"   bash visionops report "$TEST_DIR"
t_ok    "9. visionops backup 메타 백업 생성"     bash visionops backup "$TEST_DIR"

rm -rf "$TEST_DIR"

echo "----------------------------------------------"
echo "  결과 요약: 통과 $PASS / 실패 $FAIL"
echo "=============================================="

[ "$FAIL" -eq 0 ]

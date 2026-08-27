#!/bin/bash
# ===============================================================
# scripts/make_sample_dataset.sh
# 교과 8/14 실데이터와 동일한 구조의 더미 데이터셋 생성 (순수 bash 호환)
# ===============================================================
set -euo pipefail

DATASET_NAME="${1:-kimchi}"
ROOT_DIR="${2:-./dataset}"
N="${3:-1000}"

DS="$ROOT_DIR/$DATASET_NAME"
RAW_IMG="$DS/raw/images"
RAW_LBL="$DS/raw/labels"

mkdir -p "$RAW_IMG" "$RAW_LBL" "$DS/meta" "$DS/backup"

echo "[1/4] 이미지 ${N}장 생성 중 ($DATASET_NAME)..."
for ((i=1; i<=N; i++)); do
    printf -v num "%04d" "$i"
    printf '\xff\xd8\xff\xe0dummy-jpeg-%s' "$num" > "$RAW_IMG/${DATASET_NAME}_${num}.jpg"
done

echo "[2/4] 라벨 TXT 생성 중..."
for ((i=1; i<=N; i++)); do
    printf -v num "%04d" "$i"
    CLS=$(( RANDOM % 6 ))
    X=$(awk -v s=$RANDOM 'BEGIN{srand(s);printf "%.6f", rand()*0.6+0.2}')
    Y=$(awk -v s=$RANDOM 'BEGIN{srand(s);printf "%.6f", rand()*0.6+0.2}')
    W=$(awk -v s=$RANDOM 'BEGIN{srand(s);printf "%.6f", rand()*0.2+0.05}')
    H=$(awk -v s=$RANDOM 'BEGIN{srand(s);printf "%.6f", rand()*0.2+0.05}')
    echo "$CLS $X $Y $W $H" > "$RAW_LBL/${DATASET_NAME}_${num}.txt"
done

echo "[3/4] classes.txt 및 메타 문서 생성..."
cat > "$DS/meta/classes.txt" << 'EOF'
0 leaf
1 plastic_stone_metal
2 branch
3 rubber_glove
4 disease_browning
5 green_onion_pepper
EOF

cat > "$DS/meta/data.yaml" << EOF
path: $(cd "$DS" 2>/dev/null && pwd || echo "$DS")
train: images/train
val: images/val
test: images/test
nc: 6
names:
  0: leaf
  1: plastic_stone_metal
  2: branch
  3: rubber_glove
  4: disease_browning
  5: green_onion_pepper
EOF

echo "[4/4] 의도적 검증 결함 데이터 주입..."
rm -f "$RAW_LBL/${DATASET_NAME}_0007.txt" 2>/dev/null || true                       # 1. 라벨 누락
rm -f "$RAW_IMG/${DATASET_NAME}_0123.jpg" 2>/dev/null || true                       # 2. 이미지 누락
echo "9 1.500000 0.400000 0.200000 0.200000" > "$RAW_LBL/${DATASET_NAME}_0456.txt"  # 3. 범위초과 + 없는 클래스
: > "$RAW_LBL/${DATASET_NAME}_0789.txt"                                              # 4. 빈 파일
touch "$RAW_IMG/${DATASET_NAME} 0999.jpg" 2>/dev/null || true                       # 5. 파일명 공백

echo "생성 완료: 이미지 $(find "$RAW_IMG" -name "*.jpg" | wc -l)장 / 라벨 $(find "$RAW_LBL" -name "*.txt" | wc -l)개"

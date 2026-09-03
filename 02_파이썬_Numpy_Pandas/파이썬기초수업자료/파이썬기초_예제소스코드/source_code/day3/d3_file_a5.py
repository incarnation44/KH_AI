# [목적] 폴더 안 모든 라벨 파일을 읽어 통계를 낸다
# [설명] glob으로 파일 목록을 찾는 실전 패턴입니다.

import os, glob

os.makedirs("labels", exist_ok=True)

# 실습용 라벨 파일 3개 생성
sample = {
    "labels/img_001.txt": ["1 0.42 0.35 0.10 0.08", "6 0.71 0.60 0.15 0.12"],
    "labels/img_002.txt": ["1 0.30 0.25 0.09 0.07"],
    "labels/img_003.txt": ["2 0.55 0.45 0.20 0.18", "1 0.15 0.80 0.08 0.06",
                           "6 0.90 0.10 0.05 0.05"],
}
for path, lines in sample.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

# 전체 파일 순회
files = sorted(glob.glob("labels/*.txt"))
class_counts = {}
total_boxes = 0

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        boxes = [ln for ln in f.read().split("\n") if ln.strip()]
    total_boxes += len(boxes)
    for b in boxes:
        cid = int(b.split()[0])
        class_counts[cid] = class_counts.get(cid, 0) + 1
    print(f"{os.path.basename(path)}: {len(boxes)}개 객체")

print("-" * 34)
print(f"파일 {len(files)}개 / 총 객체 {total_boxes}개")
print(f"이미지당 평균 {total_boxes/len(files):.1f}개")
for cid in sorted(class_counts):
    n = class_counts[cid]
    print(f"  클래스 {cid}: {n}개 ({n/total_boxes:.0%})")

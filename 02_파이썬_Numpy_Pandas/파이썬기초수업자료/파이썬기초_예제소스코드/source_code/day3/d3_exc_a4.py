# [목적] 데이터셋 전체를 검사하며 문제를 유형별로 집계한다
# [설명] 오류를 분류해 세는 것이 데이터 품질 리포트의 핵심입니다.

import os

os.makedirs("ds/images", exist_ok=True)
os.makedirs("ds/labels", exist_ok=True)

# 실습 데이터: 정상 2건, 라벨 누락 1건, 빈 라벨 1건, 형식오류 1건
for name in ["a", "b", "c", "d", "e"]:
    open(f"ds/images/{name}.jpg", "w").close()

with open("ds/labels/a.txt", "w") as f: f.write("1 0.4 0.3 0.1 0.1\n")
with open("ds/labels/b.txt", "w") as f: f.write("2 0.5 0.5 0.2 0.2\n")
with open("ds/labels/d.txt", "w") as f: f.write("")
with open("ds/labels/e.txt", "w") as f: f.write("x 0.1 0.1 0.1 0.1\n")

report = {"정상": [], "라벨없음": [], "빈라벨": [], "형식오류": []}

for img in sorted(os.listdir("ds/images")):
    name = img.replace(".jpg", "")
    label_path = f"ds/labels/{name}.txt"
    try:
        with open(label_path, "r", encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        report["라벨없음"].append(img)
        continue

    if not lines:
        report["빈라벨"].append(img)
        continue

    try:
        for ln in lines:
            p = ln.split()
            int(p[0]); [float(v) for v in p[1:5]]
        report["정상"].append(img)
    except (ValueError, IndexError):
        report["형식오류"].append(img)

print("=== 데이터셋 검증 리포트 ===")
for key, items in report.items():
    print(f"{key:<8}: {len(items)}건  {items}")

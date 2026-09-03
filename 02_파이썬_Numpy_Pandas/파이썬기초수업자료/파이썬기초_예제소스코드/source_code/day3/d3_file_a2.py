# [목적] 여러 이미지의 검사 결과를 표로 정리해 저장한다
# [설명] 엑셀로 열어 바로 확인·공유할 수 있는 형태입니다.

import csv

CLASS_MAP = {1: "나뭇잎류", 2: "플라스틱류", 6: "파·고추"}
detections = [
    {"file": "img_001.jpg", "class_id": 1, "conf": 0.92, "bbox": [120, 85, 40, 30]},
    {"file": "img_002.jpg", "class_id": 6, "conf": 0.55, "bbox": [300, 210, 55, 60]},
    {"file": "img_003.jpg", "class_id": 2, "conf": 0.88, "bbox": [50, 40, 90, 70]},
]

rows = []
for d in detections:
    rows.append({
        "파일명": d["file"],
        "클래스": CLASS_MAP.get(d["class_id"], "미등록"),
        "신뢰도": f"{d['conf']:.3f}",
        "면적": d["bbox"][2] * d["bbox"][3],
        "판정": "NG" if d["conf"] >= 0.7 else "보류",
    })

fields = ["파일명", "클래스", "신뢰도", "면적", "판정"]
with open("detection_report.csv", "w", encoding="utf-8-sig", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fields)
    writer.writeheader()
    writer.writerows(rows)

print("리포트 저장 완료 (총", len(rows), "건)")
print()
with open("detection_report.csv", "r", encoding="utf-8-sig") as f:
    print(f.read())

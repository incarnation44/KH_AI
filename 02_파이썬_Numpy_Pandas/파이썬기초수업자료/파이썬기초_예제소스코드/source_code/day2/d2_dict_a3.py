# [목적] 여러 검출 결과를 파일 단위로 묶어 정리한다
# [설명] 이미지 한 장에 여러 이물이 있을 때 필요한 처리입니다.

detections = [
    {"file": "img_001.jpg", "class_id": 1, "conf": 0.92},
    {"file": "img_002.jpg", "class_id": 6, "conf": 0.55},
    {"file": "img_001.jpg", "class_id": 3, "conf": 0.81},
    {"file": "img_003.jpg", "class_id": 2, "conf": 0.88},
    {"file": "img_001.jpg", "class_id": 6, "conf": 0.76},
]

grouped = {}
for d in detections:
    fname = d["file"]
    if fname not in grouped:
        grouped[fname] = []
    grouped[fname].append(d)

for fname in sorted(grouped):
    items = grouped[fname]
    max_conf = max(x["conf"] for x in items)
    verdict = "NG" if max_conf >= 0.7 else "보류"
    print(f"{fname}: 검출 {len(items)}건, 최고신뢰도 {max_conf:.0%} -> {verdict}")

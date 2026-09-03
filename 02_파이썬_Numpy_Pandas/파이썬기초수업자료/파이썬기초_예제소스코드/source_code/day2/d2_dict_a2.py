# [목적] 검출 하나가 가진 여러 정보를 하나의 딕셔너리로 묶는다
# [설명] 모델 출력을 다루는 표준적인 형태입니다.

detections = [
    {"file": "img_001.jpg", "class_id": 1, "bbox": [120, 85, 40, 30], "conf": 0.92},
    {"file": "img_001.jpg", "class_id": 6, "bbox": [300, 210, 55, 60], "conf": 0.55},
    {"file": "img_002.jpg", "class_id": 2, "bbox": [50, 40, 90, 70], "conf": 0.88},
]

CLASS_MAP = {1: "나뭇잎류", 2: "플라스틱류", 6: "파·고추"}

for d in detections:
    name = CLASS_MAP.get(d["class_id"], "?")
    w, h = d["bbox"][2], d["bbox"][3]
    verdict = "채택" if d["conf"] >= 0.7 else "제외"
    print(f"{d['file']} | {name:<8} | 면적 {w*h:>5} | {d['conf']:.0%} | {verdict}")

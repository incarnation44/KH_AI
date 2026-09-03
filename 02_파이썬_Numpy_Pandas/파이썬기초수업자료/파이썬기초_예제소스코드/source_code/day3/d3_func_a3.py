# [목적] 여러 조건을 인자로 받아 유연하게 필터링한다
# [설명] 기본값 덕분에 간단히 쓸 수도, 세밀하게 조정할 수도 있습니다.

def filter_detections(detections, min_conf=0.7, min_area=100, valid_classes=None):
    if valid_classes is None:
        valid_classes = [1, 2, 3, 5, 6]

    result = []
    for d in detections:
        area = d["bbox"][2] * d["bbox"][3]
        if d["conf"] < min_conf:
            continue
        if area < min_area:
            continue
        if d["class_id"] not in valid_classes:
            continue
        result.append(d)
    return result

data = [
    {"class_id": 1, "conf": 0.92, "bbox": [10, 10, 40, 30]},
    {"class_id": 6, "conf": 0.55, "bbox": [20, 20, 55, 60]},
    {"class_id": 2, "conf": 0.88, "bbox": [30, 30, 5, 5]},
    {"class_id": 4, "conf": 0.95, "bbox": [40, 40, 50, 50]},
    {"class_id": 3, "conf": 0.81, "bbox": [50, 50, 60, 40]},
]

print("기본 조건:", len(filter_detections(data)), "건")
print("느슨하게 :", len(filter_detections(data, min_conf=0.5)), "건")
print("엄격하게 :", len(filter_detections(data, min_conf=0.9, min_area=500)), "건")

for d in filter_detections(data):
    print(f"  통과: 클래스{d['class_id']} ({d['conf']:.0%})")

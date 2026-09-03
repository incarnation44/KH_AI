# [목적] 신뢰도 기준을 넘는 검출만 골라 필요한 형태로 변환한다
# [설명] 모델 후처리를 컴프리헨션으로 간결하게 표현합니다.

detections = [
    {"class_id": 1, "conf": 0.92, "bbox": [120, 85, 40, 30]},
    {"class_id": 6, "conf": 0.55, "bbox": [300, 210, 55, 60]},
    {"class_id": 2, "conf": 0.88, "bbox": [50, 40, 90, 70]},
    {"class_id": 3, "conf": 0.41, "bbox": [10, 10, 20, 15]},
]
CLASS_MAP = {1: "나뭇잎류", 2: "플라스틱류", 3: "나뭇가지류", 6: "파·고추"}

# 1) 신뢰도 0.7 이상만 남기기
accepted = [d for d in detections if d["conf"] >= 0.7]

# 2) 표시용 문자열로 변환
lines = [f"{CLASS_MAP[d['class_id']]} ({d['conf']:.0%})" for d in accepted]

# 3) 면적만 뽑기
areas = [d["bbox"][2] * d["bbox"][3] for d in accepted]

print(f"전체 {len(detections)}건 -> 채택 {len(accepted)}건")
for line in lines:
    print(" -", line)
print("면적 목록:", areas, "/ 합계:", sum(areas))

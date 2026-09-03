# [목적] 검출 결과 하나를 표현하는 클래스를 정의한다
# [설명] 딕셔너리로 하던 것을 클래스로 옮기면 동작까지 함께 담깁니다.

CLASS_MAP = {1: "나뭇잎류", 2: "플라스틱류", 3: "나뭇가지류",
             5: "병해·갈변", 6: "파·고추"}

class Detection:
    def __init__(self, class_id, bbox, confidence):
        self.class_id = class_id
        self.bbox = bbox                 # [x, y, w, h]
        self.confidence = confidence

    def area(self):
        return self.bbox[2] * self.bbox[3]

    def class_name(self):
        return CLASS_MAP.get(self.class_id, "미등록")

    def is_valid(self, threshold=0.7, min_area=100):
        return self.confidence >= threshold and self.area() >= min_area

    def __str__(self):
        mark = "채택" if self.is_valid() else "제외"
        return f"[{mark}] {self.class_name():<8} {self.confidence:.0%} (면적 {self.area()})"

dets = [
    Detection(1, [120, 85, 40, 30], 0.92),
    Detection(6, [300, 210, 55, 60], 0.55),
    Detection(2, [50, 40, 8, 9], 0.88),
]

for d in dets:
    print(d)

valid = [d for d in dets if d.is_valid()]
print(f"\n전체 {len(dets)}건 중 유효 {len(valid)}건")

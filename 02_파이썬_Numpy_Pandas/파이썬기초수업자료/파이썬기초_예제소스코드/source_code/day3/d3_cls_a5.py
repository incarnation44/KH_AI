# [목적] 공통 기능은 부모 클래스에 두고, 차이만 자식에서 정의한다
# [설명] 교과 14(제조검사)와 교과 15(동작인식)의 공통 구조를 표현합니다.

class BaseResult:
    def __init__(self, file_name, confidence):
        self.file_name = file_name
        self.confidence = confidence

    def is_confident(self, threshold=0.7):
        return self.confidence >= threshold

    def __str__(self):
        return f"{self.file_name}: {self.summary()}"

    def summary(self):
        return "기본 결과"

class DefectResult(BaseResult):          # BaseResult를 물려받음
    def __init__(self, file_name, confidence, class_name, area):
        super().__init__(file_name, confidence)   # 부모의 __init__ 실행
        self.class_name = class_name
        self.area = area

    def summary(self):
        v = "NG" if self.is_confident() else "OK"
        return f"[{v}] {self.class_name} 면적 {self.area} ({self.confidence:.0%})"

class ActionResult(BaseResult):
    def __init__(self, file_name, confidence, action, keypoints):
        super().__init__(file_name, confidence)
        self.action = action
        self.keypoints = keypoints

    def summary(self):
        return f"동작 '{self.action}' 관절 {self.keypoints}개 ({self.confidence:.0%})"

results = [
    DefectResult("img_001.jpg", 0.92, "나뭇잎류", 1200),
    DefectResult("img_002.jpg", 0.55, "파·고추", 3300),
    ActionResult("clip_01.mp4", 0.88, "정지 신호", 17),
]

for r in results:
    print(r)

print(f"\n신뢰도 기준 통과: {sum(1 for r in results if r.is_confident())}건")

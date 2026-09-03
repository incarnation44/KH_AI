# [목적] 여러 Detection을 담아 이미지 단위 판정을 내리는 클래스
# [설명] 클래스 안에 다른 클래스의 객체를 담는 구조입니다.

class Detection:
    def __init__(self, class_id, confidence):
        self.class_id = class_id
        self.confidence = confidence

class ImageResult:
    def __init__(self, file_name):
        self.file_name = file_name
        self.detections = []

    def add(self, detection):
        self.detections.append(detection)

    def count(self):
        return len(self.detections)

    def max_confidence(self):
        if not self.detections:
            return 0.0
        return max(d.confidence for d in self.detections)

    def verdict(self, threshold=0.7):
        if self.count() == 0:
            return "OK"
        return "NG" if self.max_confidence() >= threshold else "보류"

    def __str__(self):
        return (f"{self.file_name:<16} 검출 {self.count()}건 "
                f"최고 {self.max_confidence():.0%} -> {self.verdict()}")

img1 = ImageResult("img_001.jpg")
img1.add(Detection(1, 0.92))
img1.add(Detection(6, 0.76))

img2 = ImageResult("img_002.jpg")
img2.add(Detection(2, 0.55))

img3 = ImageResult("img_003.jpg")     # 검출 없음

for img in [img1, img2, img3]:
    print(img)

ng = [i for i in [img1, img2, img3] if i.verdict() == "NG"]
print(f"\nNG 판정: {len(ng)}건 / 전체 3건")

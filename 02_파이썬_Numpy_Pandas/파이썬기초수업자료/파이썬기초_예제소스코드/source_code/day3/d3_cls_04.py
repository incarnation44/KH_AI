# [목적] print()했을 때 보기 좋은 문자열이 나오도록 한다
# [설명] __str__을 정의하지 않으면 메모리 주소가 출력됩니다.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class NicePoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(120, 85)
p2 = NicePoint(120, 85)

print("__str__ 없음:", p1)
print("__str__ 있음:", p2)
print("문자열로 변환:", str(p2))
print(f"f-string 안에서도: {p2}")

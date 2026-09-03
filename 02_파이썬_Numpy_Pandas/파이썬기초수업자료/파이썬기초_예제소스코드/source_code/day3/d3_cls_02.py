# [목적] 클래스에 동작(함수)을 넣는다
# [설명] 메서드의 첫 매개변수는 항상 self입니다.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

r1 = Rectangle(40, 30)
r2 = Rectangle(50, 50)

print(f"r1 - 넓이 {r1.area()}, 둘레 {r1.perimeter()}, 정사각형 {r1.is_square()}")
print(f"r2 - 넓이 {r2.area()}, 둘레 {r2.perimeter()}, 정사각형 {r2.is_square()}")

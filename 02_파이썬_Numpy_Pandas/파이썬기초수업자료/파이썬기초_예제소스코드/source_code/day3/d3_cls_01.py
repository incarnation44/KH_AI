# [목적] 클래스를 정의하고 인스턴스를 만드는 기본 형태
# [설명] __init__에서 받은 값을 self.속성에 저장합니다.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("홍길동", 25)
p2 = Person("이영희", 30)

print(p1.name, p1.age)
print(p2.name, p2.age)
print("p1과 p2가 같은 객체인가?", p1 is p2)

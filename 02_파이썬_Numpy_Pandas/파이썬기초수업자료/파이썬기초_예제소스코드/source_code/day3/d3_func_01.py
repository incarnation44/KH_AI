# [목적] 함수를 정의하고 호출하는 기본 형태
# [설명] def로 만들고, 이름(인자)로 호출합니다.

def say_hello():
    print("안녕하세요!")

say_hello()          # 호출
say_hello()          # 몇 번이든 재사용 가능

def greet(name):
    print(f"{name}님, 환영합니다")

greet("홍길동")
greet("이영희")

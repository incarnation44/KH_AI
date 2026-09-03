# [목적] 계산 결과를 함수 밖으로 돌려준다
# [설명] return이 있어야 결과를 변수에 담을 수 있습니다.

def add(a, b):
    return a + b

def multiply(a, b):
    result = a * b
    return result

x = add(3, 5)
y = multiply(4, 6)

print("합:", x)
print("곱:", y)
print("함수 결과를 바로 사용:", add(x, y))

# return이 없는 함수
def no_return():
    print("출력만 함")

value = no_return()
print("반환값:", value)

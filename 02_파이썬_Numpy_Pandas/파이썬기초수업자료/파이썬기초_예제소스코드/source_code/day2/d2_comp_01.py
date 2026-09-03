# [목적] 같은 결과를 두 가지 방법으로 만들어 비교한다
# [설명] 컴프리헨션은 반복문을 압축한 것입니다.

numbers = [1, 2, 3, 4, 5]

# 방법 1 : 일반 반복문
squares_1 = []
for n in numbers:
    squares_1.append(n ** 2)

# 방법 2 : 리스트 컴프리헨션
squares_2 = [n ** 2 for n in numbers]

print("반복문   :", squares_1)
print("컴프리헨션:", squares_2)
print("결과 동일:", squares_1 == squares_2)

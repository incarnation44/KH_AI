# [목적] 리스트의 값을 하나씩 꺼내 반복 처리한다
# [설명] "for 변수 in 목록:" 형태가 기본입니다.

fruits = ["사과", "바나나", "딸기"]

for fruit in fruits:
    print("과일:", fruit)

print("---")

# 문자열도 한 글자씩 순회 가능
for ch in "파이썬":
    print(ch)

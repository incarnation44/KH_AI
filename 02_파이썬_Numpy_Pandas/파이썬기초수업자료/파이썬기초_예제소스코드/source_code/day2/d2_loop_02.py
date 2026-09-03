# [목적] 숫자를 자동 생성해 정해진 횟수만큼 반복한다
# [설명] range(끝) / range(시작, 끝) / range(시작, 끝, 간격)

for i in range(3):              # 0, 1, 2
    print("i =", i)

print("---")
for i in range(1, 4):           # 1, 2, 3 (끝 번호는 제외)
    print("i =", i)

print("---")
for i in range(0, 10, 3):       # 0, 3, 6, 9 (3씩 증가)
    print("i =", i)

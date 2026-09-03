# [목적] 공백으로 구분된 여러 값을 한 번에 받아 나눈다
# [설명] input() 후 split()으로 쪼개는 것이 정석입니다.

data = input("너비와 높이를 공백으로 구분해 입력: ")
parts = data.split()

width = int(parts[0])
height = int(parts[1])

print("면적:", width * height)

# 더 짧게 쓰는 방법
w, h = input("다시 입력: ").split()
print("면적:", int(w) * int(h))

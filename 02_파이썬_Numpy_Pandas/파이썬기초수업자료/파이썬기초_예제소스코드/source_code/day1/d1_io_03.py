# [목적] input()으로 받은 문자열을 계산 가능한 숫자로 바꾼다
# [설명] int()나 float()로 감싸는 것이 핵심입니다.

age_text = input("나이를 입력하세요: ")
age = int(age_text)                    # 문자열 -> 정수

print("10년 후에는", age + 10, "살입니다")

# 한 줄로 줄여 쓰기
height = float(input("키(cm)를 입력하세요: "))
print("키(m):", height / 100)

# [목적] if-else를 앞자리에 넣어 값을 골라 담는다
# [설명] 필터용 if는 뒤에, 값 선택용 if-else는 앞에 옵니다.

scores = [88, 45, 72, 91, 58]

# 필터: 뒤쪽 if -> 조건에 맞는 것만 남김
passed = [s for s in scores if s >= 60]

# 선택: 앞쪽 if-else -> 모든 항목을 변환
grades = ["합격" if s >= 60 else "불합격" for s in scores]

print("점수  :", scores)
print("합격만:", passed)
print("판정  :", grades)

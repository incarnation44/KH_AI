# [목적] 세 가지 이상의 경우를 순서대로 판정한다
# [설명] 위에서부터 검사하다가 처음 맞는 곳에서 멈춥니다.

score = 78

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"점수 {score} -> 등급 {grade}")

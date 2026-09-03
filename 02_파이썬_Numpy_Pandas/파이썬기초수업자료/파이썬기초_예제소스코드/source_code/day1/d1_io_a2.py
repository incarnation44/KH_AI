# [목적] 신뢰도를 입력받아 등급과 채택 여부를 알려준다
# [설명] 검출 결과를 수동 검수할 때 기준을 확인하는 용도입니다.

threshold = 0.7
conf = float(input("신뢰도(0~1)를 입력하세요: "))

is_pass = conf >= threshold
grade = "상" if conf >= 0.9 else ("중" if conf >= 0.7 else "하")

print(f"입력 신뢰도 : {conf:.2%}")
print(f"기준({threshold:.0%}) 통과: {is_pass}")
print(f"등급        : {grade}")

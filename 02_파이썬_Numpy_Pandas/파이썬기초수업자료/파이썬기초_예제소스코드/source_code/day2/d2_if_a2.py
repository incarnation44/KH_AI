# [목적] 제품검사 시스템의 최종 판정 로직을 구현한다
# [설명] 교과 14 프로젝트의 핵심 판정부에 해당합니다.

detected_count = 2          # 검출된 이물 개수
max_confidence = 0.93       # 가장 확신하는 검출의 신뢰도
threshold = 0.7

if detected_count == 0:
    verdict = "OK"
    reason = "이물 없음"
elif max_confidence < threshold:
    verdict = "보류"
    reason = f"검출되었으나 신뢰도 낮음 ({max_confidence:.0%})"
else:
    verdict = "NG"
    reason = f"이물 {detected_count}건 검출 (최대 신뢰도 {max_confidence:.0%})"

print(f"판정: {verdict}")
print(f"사유: {reason}")

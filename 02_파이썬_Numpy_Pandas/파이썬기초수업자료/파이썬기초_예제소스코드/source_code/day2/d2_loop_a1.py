# [목적] 한 이미지에서 나온 여러 검출 결과를 순회하며 필터링한다
# [설명] 모델 출력 후처리 단계의 전형적인 형태입니다.

confidences = [0.92, 0.55, 0.81, 0.40, 0.77, 0.68]
threshold = 0.7

accepted = 0
rejected = 0

for idx, conf in enumerate(confidences, start=1):
    if conf >= threshold:
        print(f"[채택] {idx}번 검출 (신뢰도 {conf:.0%})")
        accepted += 1
    else:
        print(f"[제외] {idx}번 검출 (신뢰도 {conf:.0%})")
        rejected += 1

print("-" * 32)
print(f"전체 {len(confidences)}건 중 채택 {accepted}건 / 제외 {rejected}건")

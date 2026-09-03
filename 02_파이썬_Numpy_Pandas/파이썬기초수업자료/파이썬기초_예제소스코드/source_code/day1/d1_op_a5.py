# [목적] 실제 후처리 단계에서 쓰이는 다중 조건 필터를 구현한다
# [설명] NMS 이후 최종 결과를 걸러낼 때 이런 조건 조합을 사용합니다.

confidence = 0.81
box_w, box_h = 15, 12
class_id = 6
img_w, img_h = 640, 640

area = box_w * box_h
area_ratio = area / (img_w * img_h)

is_confident = confidence >= 0.7
is_not_tiny = area >= 100                  # 너무 작은 노이즈 제거
is_not_huge = area_ratio <= 0.5            # 화면 절반 넘는 오검출 제거
is_valid_class = class_id in [1, 2, 3, 5, 6]   # 4번은 미사용

accept = is_confident and is_not_tiny and is_not_huge and is_valid_class

print("신뢰도 통과:", is_confident)
print("최소 크기 통과:", is_not_tiny)
print("최대 크기 통과:", is_not_huge)
print("유효 클래스:", is_valid_class)
print("=> 최종 채택:", accept)

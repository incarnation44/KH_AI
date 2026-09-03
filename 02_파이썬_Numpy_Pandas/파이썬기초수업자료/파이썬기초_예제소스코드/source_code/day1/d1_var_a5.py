# [목적] 여러 조건의 판정 결과를 bool 변수로 저장해 둔다
# [설명] is_ 로 시작하는 이름은 참/거짓 값을 담는다는 관례적 표시입니다.

confidence = 0.92
box_area = 1200
class_id = 1

is_confident = confidence >= 0.7          # 신뢰도 기준 통과?
is_big_enough = box_area >= 100           # 너무 작은 검출 아님?
is_known_class = class_id != 4            # 4번(고무장갑)은 미사용 클래스

print("신뢰도 기준 통과:", is_confident)
print("크기 기준 통과:", is_big_enough)
print("유효한 클래스:", is_known_class)
print("최종 채택 여부:", is_confident and is_big_enough and is_known_class)

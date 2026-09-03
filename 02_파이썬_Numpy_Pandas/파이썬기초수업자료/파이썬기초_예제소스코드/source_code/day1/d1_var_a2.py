# [목적] 객체검출 모델이 내놓는 결과 한 건을 변수들로 표현한다
# [설명] 클래스ID, bbox 좌표, 신뢰도가 검출 결과의 3요소입니다.

class_id = 1                      # 1 = 나뭇잎류
class_name = "나뭇잎류"
x, y = 120, 85                    # bbox 좌상단 좌표
box_width, box_height = 40, 30    # bbox 크기
confidence = 0.9237               # 모델이 확신하는 정도

area = box_width * box_height
print("검출:", class_name)
print("위치:", x, y, "크기:", box_width, "x", box_height)
print("면적:", area, "픽셀")
print("신뢰도:", confidence)

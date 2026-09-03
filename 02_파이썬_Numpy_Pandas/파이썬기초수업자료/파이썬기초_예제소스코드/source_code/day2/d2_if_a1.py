# [목적] 라벨의 클래스ID를 사람이 읽을 수 있는 이름으로 변환한다
# [설명] 교과 8의 이물 분류 6종 기준을 그대로 적용합니다.
#        4번(고무장갑)은 사용하지 않는 클래스입니다.

class_id = 5

if class_id == 1:
    name = "나뭇잎류"
elif class_id == 2:
    name = "플라스틱·돌·금속 등"
elif class_id == 3:
    name = "나뭇가지류"
elif class_id == 4:
    name = "고무장갑 (사용하지 않는 분류)"
elif class_id == 5:
    name = "병해·갈변"
elif class_id == 6:
    name = "파·고추"
else:
    name = "등록되지 않은 클래스"

print(f"클래스 {class_id} => {name}")

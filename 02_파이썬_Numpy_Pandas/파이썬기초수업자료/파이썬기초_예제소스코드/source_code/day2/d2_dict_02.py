# [목적] 없는 key에 접근할 때 오류를 피한다
# [설명] 대괄호는 오류, get()은 기본값을 반환합니다.

class_map = {1: "나뭇잎류", 2: "플라스틱류", 6: "파·고추"}

print(class_map.get(1))
print(class_map.get(9))                      # 없으면 None
print(class_map.get(9, "미등록 클래스"))       # 기본값 지정

# 있는지 먼저 확인하는 방법
if 9 in class_map:
    print(class_map[9])
else:
    print("9번은 등록되어 있지 않습니다")

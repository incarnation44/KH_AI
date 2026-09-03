# [목적] 어떤 값이 문자열이나 목록 안에 있는지 확인한다
# [설명] in 은 "~안에 들어있다"를 그대로 코드로 옮긴 것입니다.

file_name = "kimchi_0001.jpg"

print("jpg" in file_name)        # 문자열 안에 특정 글자가 있는가
print("png" in file_name)

valid_ids = [1, 2, 3, 5, 6]
print(3 in valid_ids)            # 목록 안에 값이 있는가
print(4 in valid_ids)
print(4 not in valid_ids)        # 없는지 확인

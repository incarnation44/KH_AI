# [목적] 리스트의 중복 값을 한 번에 제거한다
# [설명] set()으로 감싸면 중복이 자동으로 사라집니다.

ids = [1, 3, 1, 6, 3, 1, 2, 6]

unique = set(ids)
print("원본:", ids)
print("중복 제거:", unique)
print("종류 수:", len(unique))

# 다시 리스트로 되돌리고 정렬
unique_list = sorted(set(ids))
print("정렬된 리스트:", unique_list)

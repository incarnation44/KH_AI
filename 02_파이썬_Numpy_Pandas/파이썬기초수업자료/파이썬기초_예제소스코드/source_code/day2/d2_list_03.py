# [목적] 리스트를 정렬하는 두 가지 방법의 차이를 확인한다
# [설명] sort()는 원본 변경, sorted()는 새 리스트 반환

scores = [78, 92, 55, 88, 63]

new_list = sorted(scores)              # 원본 유지
print("원본  :", scores)
print("정렬본:", new_list)

scores.sort()                          # 원본 자체를 정렬
print("sort 후 원본:", scores)

scores.sort(reverse=True)              # 내림차순
print("내림차순:", scores)

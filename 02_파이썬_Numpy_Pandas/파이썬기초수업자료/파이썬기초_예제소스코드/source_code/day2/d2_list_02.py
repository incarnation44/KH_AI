# [목적] append, insert, remove, pop 사용법
# [설명] 빈 리스트로 시작해 값을 채워가는 것이 일반적인 패턴입니다.

items = []
items.append("사과")
items.append("바나나")
items.append("딸기")
print("추가 후:", items)

items.insert(1, "포도")        # 1번 위치에 끼워넣기
print("insert 후:", items)

items.remove("바나나")          # 값으로 삭제
print("remove 후:", items)

last = items.pop()             # 마지막 값 꺼내며 삭제
print("pop한 값:", last, "/ 남은 것:", items)

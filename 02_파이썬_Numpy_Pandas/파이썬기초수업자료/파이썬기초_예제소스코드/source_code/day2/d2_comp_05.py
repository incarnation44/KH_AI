# [목적] 대괄호 대신 중괄호로 딕셔너리와 집합을 만든다
# [설명] 형태만 다를 뿐 원리는 같습니다.

names = ["사과", "바나나", "딸기"]
prices = [1200, 3000, 8000]

# 딕셔너리 컴프리헨션
price_map = {n: p for n, p in zip(names, prices)}
print(price_map)

# 조건 추가
cheap = {n: p for n, p in price_map.items() if p < 5000}
print("5000원 미만:", cheap)

# 집합 컴프리헨션 (중복 자동 제거)
ids = [1, 3, 1, 6, 3]
unique = {i for i in ids}
print("고유 ID:", unique)

# [목적] 어떤 값이 몇 번 나왔는지 집계한다
# [설명] 가장 자주 쓰이는 딕셔너리 활용 패턴입니다.

votes = ["사과", "바나나", "사과", "딸기", "사과", "바나나"]

counts = {}
for item in votes:
    counts[item] = counts.get(item, 0) + 1   # 없으면 0에서 시작

print(counts)

for name, n in counts.items():
    print(f"{name}: {'★' * n} ({n}표)")

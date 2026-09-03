# [목적] 신뢰도가 높은 순서로 검출 결과를 정렬해 상위만 남긴다
# [설명] Top-K 결과만 표시하는 화면 구성에 쓰입니다.

results = [
    ["나뭇잎류", 0.92],
    ["파·고추", 0.55],
    ["플라스틱류", 0.81],
    ["병해·갈변", 0.40],
    ["나뭇가지류", 0.77],
]

# 두 번째 값(신뢰도) 기준 내림차순 정렬
results.sort(key=lambda item: item[1], reverse=True)

print("=== 신뢰도 높은 순 ===")
for name, conf in results:
    print(f"{name:<12} {conf:.0%}")

print("\n=== 상위 3개만 ===")
for name, conf in results[:3]:
    print(f"{name:<12} {conf:.0%}")

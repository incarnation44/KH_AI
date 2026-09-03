# [목적] 꺼낸 값을 가공해서 새 리스트에 담는다
# [설명] for 앞의 자리가 "무엇을 담을지"를 결정합니다.

words = ["apple", "Banana", "CHERRY"]

lower = [w.lower() for w in words]
lengths = [len(w) for w in words]
labeled = [f"과일: {w.capitalize()}" for w in words]

print("소문자:", lower)
print("길이  :", lengths)
print("가공  :", labeled)

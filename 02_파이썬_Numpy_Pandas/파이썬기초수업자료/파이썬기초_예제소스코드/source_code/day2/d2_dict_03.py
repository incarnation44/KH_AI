# [목적] key만, value만, 또는 둘 다 순회하는 방법
# [설명] items()가 가장 자주 쓰입니다.

scores = {"국어": 88, "영어": 92, "수학": 76}

print("--- key만 ---")
for subject in scores.keys():
    print(subject)

print("--- value만 ---")
for score in scores.values():
    print(score)

print("--- 둘 다 ---")
for subject, score in scores.items():
    print(f"{subject}: {score}점")

print("평균:", sum(scores.values()) / len(scores))

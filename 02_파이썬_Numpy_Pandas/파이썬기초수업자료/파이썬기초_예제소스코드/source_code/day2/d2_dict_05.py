# [목적] 여러 개의 대상을 각각 딕셔너리로 표현해 리스트에 모은다
# [설명] 실무 데이터의 가장 일반적인 구조입니다.

students = [
    {"name": "김철수", "score": 88},
    {"name": "이영희", "score": 95},
    {"name": "박민수", "score": 72},
]

for s in students:
    print(f"{s['name']}: {s['score']}점")

# 전체 평균
total = sum(s["score"] for s in students)
print("평균:", round(total / len(students), 1))

# 최고점 학생 찾기
best = max(students, key=lambda s: s["score"])
print("최고점:", best["name"], best["score"])

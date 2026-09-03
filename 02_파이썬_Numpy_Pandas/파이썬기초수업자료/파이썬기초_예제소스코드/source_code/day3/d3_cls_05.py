# [목적] 클래스로 만든 객체들을 모아 일괄 처리한다
# [설명] 딕셔너리 리스트와 같은 구조지만 메서드를 쓸 수 있습니다.

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self, cutoff=60):
        return self.score >= cutoff

    def __str__(self):
        mark = "합격" if self.is_passed() else "불합격"
        return f"{self.name}({self.score}점, {mark})"

students = [
    Student("김철수", 88),
    Student("이영희", 95),
    Student("박민수", 52),
]

for s in students:
    print(s)

passed = [s for s in students if s.is_passed()]
avg = sum(s.score for s in students) / len(students)

print(f"\n합격자 {len(passed)}명 / 평균 {avg:.1f}점")
print("최고점:", max(students, key=lambda s: s.score))

# [목적] return 뒤에 콤마로 여러 값을 나열한다
# [설명] 실제로는 튜플 하나로 묶여서 반환됩니다.

def get_min_max(numbers):
    return min(numbers), max(numbers)

scores = [78, 92, 55, 88, 63]

low, high = get_min_max(scores)      # 각각 받기
print("최저:", low, "/ 최고:", high)

result = get_min_max(scores)         # 튜플로 통째로 받기
print("튜플로:", result, type(result))

def analyze(numbers):
    return len(numbers), sum(numbers), sum(numbers) / len(numbers)

n, total, avg = analyze(scores)
print(f"개수 {n} / 합계 {total} / 평균 {avg:.1f}")

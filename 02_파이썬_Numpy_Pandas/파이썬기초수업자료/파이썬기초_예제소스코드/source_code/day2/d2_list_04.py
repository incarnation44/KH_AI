# [목적] 합계·최대·최소·평균을 구하는 내장 함수를 사용한다
# [설명] 반복문 없이 한 줄로 처리할 수 있습니다.

values = [0.92, 0.55, 0.81, 0.40, 0.77]

print("개수:", len(values))
print("합계:", sum(values))
print("최댓값:", max(values))
print("최솟값:", min(values))
print("평균:", sum(values) / len(values))
print("평균(반올림):", round(sum(values) / len(values), 3))

print("0.81의 위치:", values.index(0.81))

# [목적] 비교 연산의 결과가 bool 값이라는 것을 확인한다
# [설명] 비교식 자체를 변수에 담을 수 있습니다.

score = 78

print(score > 90)
print(score >= 70)
print(score == 78)
print(score != 78)

result = score >= 70          # 비교 결과를 변수에 저장
print("합격 여부:", result, type(result))

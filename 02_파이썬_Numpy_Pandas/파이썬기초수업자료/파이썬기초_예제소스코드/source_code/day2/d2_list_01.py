# [목적] 리스트 생성과 인덱싱, 슬라이싱의 기본
# [설명] 문자열과 마찬가지로 0번부터 시작합니다.

numbers = [10, 20, 30, 40, 50]

print(numbers)
print("첫 값:", numbers[0])
print("마지막 값:", numbers[-1])
print("일부 구간:", numbers[1:4])
print("길이:", len(numbers))

# 값 바꾸기
numbers[0] = 99
print("변경 후:", numbers)

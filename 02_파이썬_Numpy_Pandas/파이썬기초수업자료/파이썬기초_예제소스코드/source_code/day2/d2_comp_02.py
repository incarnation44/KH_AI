# [목적] 조건에 맞는 항목만 골라 새 리스트를 만든다
# [설명] for 뒤에 if를 붙이면 필터 역할을 합니다.

numbers = list(range(1, 11))

evens = [n for n in numbers if n % 2 == 0]
big = [n for n in numbers if n > 6]
both = [n for n in numbers if n % 2 == 0 and n > 6]

print("전체  :", numbers)
print("짝수  :", evens)
print("6 초과:", big)
print("둘 다 :", both)

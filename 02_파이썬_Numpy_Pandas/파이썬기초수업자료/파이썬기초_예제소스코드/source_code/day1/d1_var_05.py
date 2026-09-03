# [목적] 문자열로 된 숫자를 계산 가능한 숫자로 바꾸는 방법
# [설명] int(), float(), str() 로 자료형을 서로 변환합니다.

text_number = "42"
print(text_number + text_number)      # 문자열끼리 더하면 이어붙이기

real_number = int(text_number)
print(real_number + real_number)      # 숫자끼리 더하면 덧셈

score = 0.876
print("신뢰도: " + str(score))         # 숫자를 문자열로 바꿔야 이어붙일 수 있음

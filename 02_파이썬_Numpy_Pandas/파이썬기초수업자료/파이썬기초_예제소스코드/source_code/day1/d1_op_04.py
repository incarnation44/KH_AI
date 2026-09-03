# [목적] 여러 조건을 묶어 하나의 판정으로 만드는 방법
# [설명] and는 "모두", or는 "하나라도", not은 "반대로"입니다.

is_weekday = True
is_raining = False

print("둘 다 참?", is_weekday and is_raining)
print("하나라도 참?", is_weekday or is_raining)
print("비가 안 오는가?", not is_raining)

# 숫자 조건과 함께 쓰기
temperature = 25
print("야외 작업 가능?", temperature > 10 and not is_raining)

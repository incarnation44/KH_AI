# [목적] 두 개 이상의 조건을 하나의 판정으로 결합한다
# [설명] and는 모두 만족, or는 하나라도 만족.

age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("입장 가능")
else:
    print("입장 불가")

# or 사용
day = "토요일"
if day == "토요일" or day == "일요일":
    print("주말입니다")

# in 을 쓰면 더 간결
if day in ["토요일", "일요일"]:
    print("주말입니다 (in 버전)")

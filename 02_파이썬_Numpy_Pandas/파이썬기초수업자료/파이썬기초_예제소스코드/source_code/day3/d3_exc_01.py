# [목적] 오류가 나도 프로그램이 계속 실행되게 한다
# [설명] try 블록에서 오류가 나면 except 블록으로 넘어갑니다.

print("프로그램 시작")

try:
    result = 10 / 0
    print("이 줄은 실행되지 않습니다")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다")

print("프로그램 계속 진행")
print("정상 종료")

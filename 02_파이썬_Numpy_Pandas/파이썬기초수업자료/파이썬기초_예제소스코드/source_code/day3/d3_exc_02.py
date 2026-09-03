# [목적] except를 여러 개 나열해 각각 다르게 대응한다
# [설명] 위에서부터 맞는 것을 찾아 실행합니다.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("  -> 0으로 나눌 수 없어 0을 반환합니다")
        return 0
    except TypeError:
        print("  -> 숫자가 아닌 값이 들어왔습니다")
        return None

print("10 / 2 =", safe_divide(10, 2))
print("10 / 0 =", safe_divide(10, 0))
print("10 / 'a' =", safe_divide(10, "a"))

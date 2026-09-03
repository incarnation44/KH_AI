# [목적] 성공했을 때와 항상 실행할 코드를 구분한다
# [설명] else는 오류가 없을 때만, finally는 언제나 실행됩니다.

def check(value):
    print(f"--- 입력: {value} ---")
    try:
        num = int(value)
    except ValueError:
        print("변환 실패")
    else:
        print(f"변환 성공: {num}, 제곱: {num ** 2}")
    finally:
        print("검사 종료\n")

check("7")
check("abc")

# [목적] 조건문 안에 조건문을 넣는 방법과 한 줄 축약형
# [설명] 중첩은 들여쓰기가 한 단계 더 깊어집니다.

is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("관리자 화면")
    else:
        print("일반 사용자 화면")
else:
    print("로그인이 필요합니다")

# 한 줄로 쓰는 조건부 표현식
status = "관리자" if is_admin else "일반"
print("권한:", status)

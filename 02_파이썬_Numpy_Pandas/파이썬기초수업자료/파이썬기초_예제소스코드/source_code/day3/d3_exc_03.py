# [목적] 실제 오류 내용을 변수로 받아 출력한다
# [설명] as 뒤에 이름을 붙이면 오류 객체를 사용할 수 있습니다.

tests = ["123", "45.6", "abc", ""]

for t in tests:
    try:
        value = int(t)
        print(f"'{t}' -> {value} (성공)")
    except ValueError as e:
        print(f"'{t}' -> 변환 실패: {e}")

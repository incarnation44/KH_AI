# [목적] 자주 쓰는 값을 미리 정해두고 필요할 때만 바꾼다
# [설명] 기본값이 있는 매개변수는 뒤쪽에 배치해야 합니다.

def make_tag(text, level=1, upper=False):
    if upper:
        text = text.upper()
    return "#" * level + " " + text

print(make_tag("제목"))                        # 기본값 사용
print(make_tag("소제목", 2))                    # level만 지정
print(make_tag("강조", 3, True))                # 둘 다 지정
print(make_tag("이름으로 지정", upper=True))      # 이름 지정 (순서 무관)

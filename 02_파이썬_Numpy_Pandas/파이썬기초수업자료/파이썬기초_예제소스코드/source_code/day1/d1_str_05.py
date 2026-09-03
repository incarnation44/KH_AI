# [목적] 변수 값을 문장 안에 자연스럽게 삽입한다
# [설명] 문자열 앞에 f를 붙이고 {변수} 형태로 넣습니다.

name = "나뭇잎류"
count = 27
ratio = 0.8734

print(f"클래스: {name}")
print(f"검출 개수: {count}건")
print(f"비율: {ratio}")

# 형식 지정
print(f"비율(소수 2자리): {ratio:.2f}")
print(f"비율(퍼센트): {ratio:.1%}")
print(f"번호(4자리 0채움): {count:04d}")
print(f"큰 수(천단위 콤마): {1234567:,}")

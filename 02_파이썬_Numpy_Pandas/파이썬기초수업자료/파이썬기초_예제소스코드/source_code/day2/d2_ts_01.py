# [목적] 튜플의 생성과 접근, 그리고 변경 불가 성질 확인
# [설명] 소괄호를 쓰며, 만든 뒤에는 값을 바꿀 수 없습니다.

point = (120, 85)

print(point)
print("x:", point[0], "/ y:", point[1])
print("길이:", len(point))

# 언패킹 : 각 변수에 나눠 담기
x, y = point
print(f"언패킹 결과 x={x}, y={y}")

# 값 변경 시도 -> 오류 발생
try:
    point[0] = 999
except TypeError as e:
    print("변경 시도 결과:", e)

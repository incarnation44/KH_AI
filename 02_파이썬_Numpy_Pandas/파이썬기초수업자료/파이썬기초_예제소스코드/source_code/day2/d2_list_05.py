# [목적] 리스트 안에 리스트가 들어간 구조를 이해한다
# [설명] 표(행과 열) 형태의 데이터를 표현할 때 사용합니다.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print("전체:", matrix)
print("두 번째 행:", matrix[1])
print("두 번째 행의 세 번째 값:", matrix[1][2])

print("--- 전체 순회 ---")
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()          # 행이 끝나면 줄바꿈

# [목적] 하나의 문자열을 여러 조각으로 나눈다
# [설명] 결과는 리스트로 반환됩니다.

line = "1 0.42 0.35 0.10 0.08"
parts = line.split()          # 인자 없으면 공백 기준
print(parts)
print("조각 개수:", len(parts))

csv_line = "kimchi_0001.jpg,나뭇잎류,0.92"
fields = csv_line.split(",")  # 콤마 기준
print(fields)
print("파일명만:", fields[0])

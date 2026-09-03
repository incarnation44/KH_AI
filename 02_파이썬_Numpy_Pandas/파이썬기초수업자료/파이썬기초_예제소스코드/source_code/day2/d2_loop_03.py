# [목적] 몇 번째 데이터인지 알아야 할 때 사용한다
# [설명] enumerate는 (순번, 값) 쌍을 만들어 줍니다.

files = ["a.jpg", "b.jpg", "c.jpg"]

for idx, name in enumerate(files):
    print(idx, name)

print("---")
# 1번부터 세고 싶을 때
for idx, name in enumerate(files, start=1):
    print(f"{idx}번째 파일: {name}")

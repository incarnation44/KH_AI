# [목적] 파일에 문자열을 저장하고 다시 읽어온다
# [설명] with 구문과 encoding 지정이 기본입니다.

# 쓰기 (기존 내용은 삭제됨)
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("첫 번째 줄\n")
    f.write("두 번째 줄\n")
    f.write("세 번째 줄\n")

# 전체를 한 번에 읽기
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print("=== 전체 읽기 ===")
print(content)

# 줄 단위로 읽기
with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        print("한 줄:", line.strip())

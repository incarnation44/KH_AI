# [목적] "a" 모드로 기존 파일에 내용을 추가한다
# [설명] 로그를 계속 쌓아나갈 때 사용합니다.

with open("log.txt", "w", encoding="utf-8") as f:
    f.write("[시작] 프로그램 실행\n")

# 덧붙이기
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("[진행] 데이터 로드 완료\n")
    f.write("[완료] 정상 종료\n")

# readlines()로 리스트로 받기
with open("log.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("총 줄 수:", len(lines))
for i, line in enumerate(lines, 1):
    print(f"{i}: {line.strip()}")

# [목적] os 모듈로 파일·폴더를 확인하고 만든다
# [설명] 파일을 열기 전에 존재 여부를 확인하는 것이 안전합니다.

import os

# 폴더 만들기 (이미 있어도 오류 안 남)
os.makedirs("output/labels", exist_ok=True)
print("폴더 생성 완료")

# 파일 만들고 확인
with open("output/test.txt", "w", encoding="utf-8") as f:
    f.write("테스트\n")

print("파일 존재?", os.path.exists("output/test.txt"))
print("없는 파일?", os.path.exists("output/none.txt"))
print("파일 크기:", os.path.getsize("output/test.txt"), "byte")

# 경로 다루기
path = "output/labels/img_001.txt"
print("폴더 부분:", os.path.dirname(path))
print("파일명 부분:", os.path.basename(path))
print("확장자 분리:", os.path.splitext(os.path.basename(path)))

# [목적] 촬영한 이미지에 규칙적인 이름을 붙인다
# [설명] 교과 14에서 컨베이어 촬영 이미지 500장 이상을 정리할 때 쓰입니다.

prefix = "conveyor"
category = "leaf"
start_number = 1

for i in range(start_number, start_number + 5):
    file_name = f"{prefix}_{category}_{i:04d}.jpg"
    print(file_name)

print("---")
# 날짜를 포함한 형태
date = "20260902"
for i in range(1, 4):
    print(f"{date}_{category}_{i:03d}.jpg")

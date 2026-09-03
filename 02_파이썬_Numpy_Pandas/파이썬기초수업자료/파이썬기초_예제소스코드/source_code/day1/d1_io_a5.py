# [목적] YOLO 정규화 좌표를 입력받아 픽셀 좌표로 변환해 보여준다
# [설명] 라벨이 제대로 찍혔는지 수동 확인할 때 쓰는 도구입니다.

img_w = int(input("이미지 너비(px): "))
img_h = int(input("이미지 높이(px): "))
line = input("라벨 한 줄 (class cx cy w h): ")

parts = line.split()
class_id = int(parts[0])
cx, cy, w, h = float(parts[1]), float(parts[2]), float(parts[3]), float(parts[4])

px_w, px_h = w * img_w, h * img_h
x1 = cx * img_w - px_w / 2
y1 = cy * img_h - px_h / 2
x2 = x1 + px_w
y2 = y1 + px_h

print(f"\n클래스 ID : {class_id}")
print(f"좌상단    : ({x1:.0f}, {y1:.0f})")
print(f"우하단    : ({x2:.0f}, {y2:.0f})")
print(f"크기      : {px_w:.0f} x {px_h:.0f} px")
print(f"범위 정상 : {0 <= x1 and 0 <= y1 and x2 <= img_w and y2 <= img_h}")

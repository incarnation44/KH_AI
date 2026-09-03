# [목적] 라벨 파일의 0~1 비율 좌표를 실제 픽셀 좌표로 바꾼다
# [설명] YOLO 라벨은 중심점(x,y)과 크기(w,h)를 전체 대비 비율로 저장합니다.

img_width, img_height = 4848, 2704

# 라벨 파일에서 읽은 값 (모두 0~1 사이 비율)
cx, cy = 0.42, 0.35
w, h = 0.10, 0.08

# 비율 -> 픽셀
px_cx = cx * img_width
px_cy = cy * img_height
px_w = w * img_width
px_h = h * img_height

# 중심점 기준 -> 좌상단 기준으로 변환
x1 = px_cx - px_w / 2
y1 = px_cy - px_h / 2

print("중심점(픽셀):", round(px_cx), round(px_cy))
print("크기(픽셀):", round(px_w), "x", round(px_h))
print("좌상단 좌표:", round(x1), round(y1))

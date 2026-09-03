# [목적] 정규화 좌표 <-> 픽셀 좌표 변환을 함수로 정리한다
# [설명] 라벨링 툴과 시각화 코드에서 계속 재사용됩니다.

def yolo_to_pixel(cx, cy, w, h, img_w, img_h):
    """YOLO 정규화 좌표를 픽셀 [x1,y1,x2,y2]로 변환"""
    px_w, px_h = w * img_w, h * img_h
    x1 = cx * img_w - px_w / 2
    y1 = cy * img_h - px_h / 2
    return [round(x1), round(y1), round(x1 + px_w), round(y1 + px_h)]

def pixel_to_yolo(x1, y1, x2, y2, img_w, img_h):
    """픽셀 좌표를 YOLO 정규화 좌표로 변환"""
    cx = (x1 + x2) / 2 / img_w
    cy = (y1 + y2) / 2 / img_h
    w = (x2 - x1) / img_w
    h = (y2 - y1) / img_h
    return round(cx, 4), round(cy, 4), round(w, 4), round(h, 4)

IMG_W, IMG_H = 4848, 2704

box = yolo_to_pixel(0.42, 0.35, 0.10, 0.08, IMG_W, IMG_H)
print("YOLO -> 픽셀:", box)

back = pixel_to_yolo(box[0], box[1], box[2], box[3], IMG_W, IMG_H)
print("픽셀 -> YOLO:", back)

# 반올림 때문에 완전히 같지는 않다 -> 오차 범위로 비교해야 한다
original = (0.42, 0.35, 0.10, 0.08)
print("완전히 일치?", back == original)
diffs = [abs(a - b) for a, b in zip(back, original)]
print("항목별 오차:", [round(d, 5) for d in diffs])
print("오차 0.001 이내로 일치?", max(diffs) < 0.001)

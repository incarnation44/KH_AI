# [목적] 객체검출 평가에 쓰이는 핵심 계산을 함수로 만든다
# [설명] IOU = 겹치는 넓이 / 전체 합친 넓이 (0~1 사이 값)
#        box 형식: [x1, y1, x2, y2] (좌상단, 우하단)

def get_area(box):
    return (box[2] - box[0]) * (box[3] - box[1])

def calc_iou(box_a, box_b):
    # 겹치는 영역의 좌표
    x1 = max(box_a[0], box_b[0])
    y1 = max(box_a[1], box_b[1])
    x2 = min(box_a[2], box_b[2])
    y2 = min(box_a[3], box_b[3])

    inter = max(0, x2 - x1) * max(0, y2 - y1)     # 안 겹치면 0
    union = get_area(box_a) + get_area(box_b) - inter
    return inter / union if union > 0 else 0.0

pred = [50, 50, 150, 150]
truth = [60, 60, 140, 160]

print("예측 면적:", get_area(pred))
print("정답 면적:", get_area(truth))
print(f"IOU: {calc_iou(pred, truth):.3f}")
print("검출 성공(IOU>=0.5)?", calc_iou(pred, truth) >= 0.5)

# 전혀 안 겹치는 경우
far = [500, 500, 600, 600]
print(f"멀리 있는 박스와의 IOU: {calc_iou(pred, far):.3f}")

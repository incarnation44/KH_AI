# [목적] 검출된 bbox가 전체 이미지에서 차지하는 비율을 구한다
# [설명] 너무 작은 검출을 걸러내는 기준으로 활용됩니다.

img_width, img_height = 4848, 2704
box_width, box_height = 240, 180

box_area = box_width * box_height
img_area = img_width * img_height
ratio = box_area / img_area * 100

print("bbox 면적:", box_area, "픽셀")
print("이미지 면적:", img_area, "픽셀")
print("화면 점유율:", round(ratio, 4), "%")

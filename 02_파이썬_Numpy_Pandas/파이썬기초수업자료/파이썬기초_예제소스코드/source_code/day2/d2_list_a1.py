# [목적] 한 이미지에서 검출된 여러 bbox의 면적을 계산하고 정렬한다
# [설명] bbox 형식: [x, y, width, height]

boxes = [
    [120, 85, 40, 30],
    [300, 210, 55, 60],
    [10, 10, 20, 15],
    [450, 120, 80, 45],
]

areas = []
for box in boxes:
    area = box[2] * box[3]
    areas.append(area)
    print(f"bbox {box} -> 면적 {area}")

print("-" * 36)
print("전체 면적 합:", sum(areas))
print("가장 큰 검출 면적:", max(areas))
print("가장 큰 검출의 순번:", areas.index(max(areas)))
print("평균 면적:", round(sum(areas) / len(areas), 1))

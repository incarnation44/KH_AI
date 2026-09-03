# [목적] YOLO 라벨 텍스트 한 줄을 의미 있는 값들로 분해한다
# [설명] 형식: class_id  x_center  y_center  width  height

line = "1 0.4231 0.3547 0.1024 0.0813\n"

parts = line.strip().split()

class_id = int(parts[0])
cx = float(parts[1])
cy = float(parts[2])
w = float(parts[3])
h = float(parts[4])

print(f"클래스 ID : {class_id}")
print(f"중심 좌표 : ({cx}, {cy})")
print(f"크기      : {w} x {h}")
print(f"면적 비율 : {w * h:.4%}")

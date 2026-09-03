# [목적] 실제 라벨 파일 형식으로 저장하고 다시 파싱한다
# [설명] 형식: class_id  cx  cy  w  h (공백 구분)

labels = [
    {"class_id": 1, "cx": 0.4231, "cy": 0.3547, "w": 0.1024, "h": 0.0813},
    {"class_id": 6, "cx": 0.7102, "cy": 0.6033, "w": 0.1500, "h": 0.1200},
]

# 저장
with open("kimchi_0001.txt", "w", encoding="utf-8") as f:
    for lb in labels:
        f.write(f"{lb['class_id']} {lb['cx']} {lb['cy']} {lb['w']} {lb['h']}\n")

print("=== 저장된 라벨 파일 ===")
with open("kimchi_0001.txt", "r", encoding="utf-8") as f:
    print(f.read())

# 읽어서 파싱
print("=== 파싱 결과 ===")
with open("kimchi_0001.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split()
        if not parts:
            continue
        cid = int(parts[0])
        cx, cy, w, h = [float(v) for v in parts[1:]]
        print(f"클래스 {cid} | 중심({cx}, {cy}) | 면적비 {w*h:.2%}")

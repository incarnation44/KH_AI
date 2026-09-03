# [목적] 라벨 파일의 여러 줄을 한 번에 구조화된 데이터로 바꾼다
# [설명] 파일 읽기와 결합하면 그대로 실무 코드가 됩니다.

lines = [
    "1 0.4231 0.3547 0.1024 0.0813",
    "6 0.7102 0.6033 0.1500 0.1200",
    "2 0.2210 0.8100 0.0800 0.0650",
]

# 각 줄을 딕셔너리로 변환
labels = [
    {
        "class_id": int(parts[0]),
        "cx": float(parts[1]),
        "cy": float(parts[2]),
        "w": float(parts[3]),
        "h": float(parts[4]),
    }
    for parts in (line.split() for line in lines)
]

for lb in labels:
    area = lb["w"] * lb["h"]
    print(f"클래스 {lb['class_id']} | 중심({lb['cx']:.2f}, {lb['cy']:.2f}) | 면적비 {area:.2%}")

# 클래스 ID만 모으기
ids = [lb["class_id"] for lb in labels]
print("\n등장 클래스:", sorted(set(ids)))

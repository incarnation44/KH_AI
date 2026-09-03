# [목적] 이미지마다 대응하는 라벨 파일이 있는지 확인한다
# [설명] 데이터셋 무결성 검사의 가장 기본이 되는 항목입니다.

images = ["img_001.jpg", "img_002.jpg", "img_003.jpg", "img_004.jpg"]
labels = ["img_001.txt", "img_003.txt", "img_004.txt"]

missing = []

for img in images:
    expected_label = img.replace(".jpg", ".txt")
    if expected_label in labels:
        print(f"[OK]   {img}")
    else:
        print(f"[누락] {img} -> {expected_label} 없음")
        missing.append(img)

print("-" * 40)
if missing:
    print(f"라벨이 없는 이미지 {len(missing)}건: {missing}")
else:
    print("모든 이미지에 라벨이 존재합니다.")

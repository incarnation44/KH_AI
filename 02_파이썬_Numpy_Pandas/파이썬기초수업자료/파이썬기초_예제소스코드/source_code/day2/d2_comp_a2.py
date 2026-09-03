# [목적] 이미지 경로 목록에서 대응하는 라벨 경로를 한 번에 만든다
# [설명] 반복문 여러 줄이 한 줄로 줄어듭니다.

img_paths = [
    "dataset/train/images/img_001.jpg",
    "dataset/train/images/img_002.jpg",
    "dataset/train/images/img_003.jpg",
]

label_paths = [p.replace("/images/", "/labels/").replace(".jpg", ".txt")
               for p in img_paths]

for img, lbl in zip(img_paths, label_paths):
    print(f"{img.split('/')[-1]:<16} -> {lbl.split('/')[-1]}")

# 파일명만 뽑기
names = [p.split("/")[-1].split(".")[0] for p in img_paths]
print("\n파일명(확장자 제외):", names)

# [목적] 폴더 내 파일 중 이미지와 라벨을 분리한다
# [설명] 데이터셋 정리의 첫 단계입니다.

files = ["img_001.jpg", "img_001.txt", "img_002.jpg", "img_002.txt",
         "README.md", "img_003.JPG", "config.yaml"]

images = [f for f in files if f.lower().endswith((".jpg", ".png"))]
labels = [f for f in files if f.endswith(".txt")]
others = [f for f in files if f not in images and f not in labels]

print(f"이미지 {len(images)}건: {images}")
print(f"라벨   {len(labels)}건: {labels}")
print(f"기타   {len(others)}건: {others}")

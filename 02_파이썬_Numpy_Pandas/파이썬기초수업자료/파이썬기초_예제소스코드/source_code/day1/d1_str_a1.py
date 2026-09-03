# [목적] YOLO 데이터셋 규칙에 따라 짝이 되는 라벨 경로를 생성한다
# [설명] images 폴더의 .jpg -> labels 폴더의 .txt 가 표준 구조입니다.

img_path = "dataset/train/images/kimchi_0042.jpg"

label_path = img_path.replace("/images/", "/labels/").replace(".jpg", ".txt")

print("이미지:", img_path)
print("라벨  :", label_path)

# 파일명만 따로 뽑기
file_name = img_path.split("/")[-1]        # 마지막 조각
name_only = file_name.split(".")[0]        # 확장자 앞부분

print("파일명:", file_name)
print("이름부:", name_only)

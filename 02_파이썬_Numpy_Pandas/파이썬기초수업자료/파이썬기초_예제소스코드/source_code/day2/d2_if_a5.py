# [목적] 확장자를 보고 어떤 처리를 할지 결정한다
# [설명] 데이터셋 폴더 정리 스크립트의 기본 구조입니다.

file_name = "kimchi_0042.txt"
ext = file_name.split(".")[-1].lower()

if ext in ["jpg", "jpeg", "png", "bmp"]:
    category = "이미지"
    action = "학습 데이터로 복사"
elif ext == "txt":
    category = "라벨"
    action = "형식 검증 후 복사"
elif ext in ["csv", "json"]:
    category = "메타데이터"
    action = "별도 폴더로 이동"
elif ext in ["md", "yaml", "yml"]:
    category = "설정/문서"
    action = "그대로 유지"
else:
    category = "알 수 없음"
    action = "건너뛰기"

print(f"파일 : {file_name}")
print(f"종류 : {category}")
print(f"처리 : {action}")

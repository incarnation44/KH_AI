# [목적] 앞뒤 공백을 제거하고 특정 부분을 교체한다
# [설명] 파일에서 읽은 줄에는 끝에 줄바꿈(\n)이 붙어 있어 strip()이 필수입니다.

raw = "  kimchi_0001.jpg \n"
clean = raw.strip()
print("원본:", repr(raw))
print("정리:", repr(clean))

# 확장자 바꾸기
label = clean.replace(".jpg", ".txt")
print("라벨 파일명:", label)

# 여러 번 바꾸기
path = "data/train/images/kimchi_0001.jpg"
print(path.replace("images", "labels").replace(".jpg", ".txt"))

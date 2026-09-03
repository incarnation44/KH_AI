# [목적] 집합의 내용을 동적으로 바꾼다
# [설명] add로 추가, discard로 안전하게 삭제합니다.

seen = set()

seen.add("img_001.jpg")
seen.add("img_002.jpg")
seen.add("img_001.jpg")      # 중복 -> 무시됨
print("현재:", seen, "개수:", len(seen))

seen.discard("img_002.jpg")  # 없어도 오류 안 남
seen.discard("없는파일.jpg")
print("삭제 후:", seen)

print("img_001.jpg 처리했나?", "img_001.jpg" in seen)

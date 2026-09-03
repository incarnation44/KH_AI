# [목적] 파일 목록을 7:1.5:1.5 비율로 실제로 분할한다
# [설명] 슬라이싱으로 구간을 잘라 나눕니다.

files = [f"img_{i:03d}.jpg" for i in range(1, 21)]   # 20장 가정
total = len(files)

train_end = int(total * 0.7)
val_end = train_end + int(total * 0.15)

train = files[:train_end]
val = files[train_end:val_end]
test = files[val_end:]

print(f"전체 {total}장")
print(f"Train {len(train)}장: {train[0]} ~ {train[-1]}")
print(f"Val   {len(val)}장: {val}")
print(f"Test  {len(test)}장: {test}")
print(f"검증 - 합계 일치: {len(train)+len(val)+len(test) == total}")

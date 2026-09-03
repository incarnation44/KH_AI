# [목적] 파일명, 클래스, 신뢰도 세 목록을 나란히 묶어 처리한다
# [설명] zip은 여러 리스트를 동시에 순회하게 해줍니다.

files = ["img_001.jpg", "img_002.jpg", "img_003.jpg"]
classes = ["나뭇잎류", "파·고추", "플라스틱류"]
confs = [0.92, 0.55, 0.81]

print(f"{'파일명':<14}{'클래스':<12}{'신뢰도':>7}  판정")
print("-" * 44)

ng_count = 0
for f, c, conf in zip(files, classes, confs):
    verdict = "NG" if conf >= 0.7 else "보류"
    if verdict == "NG":
        ng_count += 1
    print(f"{f:<14}{c:<12}{conf:>7.0%}  {verdict}")

print("-" * 44)
print(f"NG 판정: {ng_count}건 / 전체 {len(files)}건")

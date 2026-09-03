# [목적] 텍스트 로그를 읽어 성능 추이를 분석한다
# [설명] 리눅스의 grep·awk로 하던 일을 파이썬으로 처리합니다.

log_lines = [
    "Epoch 1/5 | loss: 0.8421 | mAP50: 0.3120",
    "Epoch 2/5 | loss: 0.5233 | mAP50: 0.5410",
    "Epoch 3/5 | loss: 0.3891 | mAP50: 0.6630",
    "Epoch 4/5 | loss: 0.2745 | mAP50: 0.7550",
    "Epoch 5/5 | loss: 0.2510 | mAP50: 0.7410",
]

with open("train.log", "w", encoding="utf-8") as f:
    for line in log_lines:
        f.write(line + "\n")

best_map, best_epoch = 0.0, 0
maps = []

with open("train.log", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("|")
        if len(parts) < 3:
            continue
        epoch = int(parts[0].split()[1].split("/")[0])
        map50 = float(parts[2].split(":")[1])
        maps.append(map50)
        if map50 > best_map:
            best_map, best_epoch = map50, epoch

print(f"총 {len(maps)} epoch 기록")
print(f"최고 성능: Epoch {best_epoch} (mAP50 {best_map:.4f})")
print(f"최종 성능: {maps[-1]:.4f}")
print(f"과적합 의심: {'예' if maps[-1] < best_map else '아니오'}")

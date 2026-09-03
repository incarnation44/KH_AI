# [목적] 모델 학습 중 출력되는 로그에서 필요한 숫자만 뽑아낸다
# [설명] 로그 파일 분석은 실무에서 매우 자주 하는 작업입니다.

log = "Epoch 45/100 | loss: 0.0342 | mAP50: 0.7821 | time: 12.4s"

parts = log.split("|")
for p in parts:
    print(repr(p.strip()))

print("---")
# mAP 값만 뽑기
map_part = parts[2].strip()            # "mAP50: 0.7821"
map_value = float(map_part.split(":")[1])
print("mAP50 =", map_value)
print("목표(0.7) 달성?", map_value >= 0.7)

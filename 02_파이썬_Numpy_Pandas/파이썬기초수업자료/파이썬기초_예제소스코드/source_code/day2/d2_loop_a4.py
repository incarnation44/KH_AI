# [목적] 여러 epoch의 성능 기록에서 최고값과 그 시점을 찾는다
# [설명] 어느 체크포인트를 최종 모델로 쓸지 결정할 때 필요합니다.

map_history = [0.312, 0.541, 0.663, 0.702, 0.755, 0.741, 0.768, 0.752]

best_map = 0
best_epoch = 0

for epoch, value in enumerate(map_history, start=1):
    marker = ""
    if value > best_map:
        best_map = value
        best_epoch = epoch
        marker = "  <- 최고 갱신"
    print(f"Epoch {epoch:2d} | mAP50 {value:.3f}{marker}")

print("-" * 36)
print(f"최고 성능: Epoch {best_epoch} (mAP50 {best_map:.3f})")
print(f"목표 0.7 달성: {'예' if best_map >= 0.7 else '아니오'}")

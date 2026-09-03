# [목적] Train : Validation : Test = 7 : 1.5 : 1.5 로 데이터를 나눌 때 개수를 구한다
# [설명] 교과 14 프로젝트의 데이터 분할 기준을 그대로 계산해 봅니다.

total_images = 500                # 최소 촬영 요구량

train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

train_count = int(total_images * train_ratio)
val_count = int(total_images * val_ratio)
test_count = total_images - train_count - val_count   # 나머지 전부

print("전체:", total_images, "장")
print("학습용(Train):", train_count, "장")
print("검증용(Validation):", val_count, "장")
print("시험용(Test):", test_count, "장")

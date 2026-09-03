# [목적] 전체 이미지 수를 입력하면 Train/Val/Test 분할 결과를 알려준다
# [설명] 교과 14의 7:1.5:1.5 기준을 바로 적용합니다.

total = int(input("전체 이미지 장수: "))

train = int(total * 0.7)
val = int(total * 0.15)
test = total - train - val

print("-" * 30)
print(f"{'구분':<14}{'장수':>6}{'비율':>8}")
print("-" * 30)
print(f"{'Train':<14}{train:>6}{train/total:>8.1%}")
print(f"{'Validation':<14}{val:>6}{val/total:>8.1%}")
print(f"{'Test':<14}{test:>6}{test/total:>8.1%}")
print("-" * 30)
print(f"{'합계':<14}{train+val+test:>6}")

if total < 500:
    print("\n[주의] 프로젝트 최소 요구량(500장)에 미달합니다.")

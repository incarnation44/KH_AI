# [목적] 평균에서 크게 벗어난 값을 찾아낸다
# [설명] 라벨링 오류나 촬영 불량을 걸러내는 데 활용합니다.

areas = [1200, 3300, 1150, 1300, 45, 1250, 8900, 1180]

avg = sum(areas) / len(areas)
print(f"평균 면적: {avg:.1f}")

normal = []
outliers = []

for a in areas:
    if a < avg * 0.3 or a > avg * 2.5:
        outliers.append(a)
    else:
        normal.append(a)

print(f"정상 범위 ({len(normal)}건): {normal}")
print(f"이상치   ({len(outliers)}건): {outliers}")
print(f"이상치 제외 평균: {sum(normal)/len(normal):.1f}")

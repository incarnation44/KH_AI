# [목적] 반복문 대신 집합 연산으로 데이터셋 무결성을 검사한다
# [설명] 앞서 반복문으로 하던 작업을 세 줄로 줄입니다.

images = {"img_001", "img_002", "img_003", "img_004", "img_005"}
labels = {"img_001", "img_003", "img_004", "img_006"}

no_label = images - labels      # 이미지만 있고 라벨 없음
no_image = labels - images      # 라벨만 있고 이미지 없음
matched = images & labels       # 정상 짝

print(f"정상 짝     ({len(matched)}건): {sorted(matched)}")
print(f"라벨 누락   ({len(no_label)}건): {sorted(no_label)}")
print(f"이미지 누락 ({len(no_image)}건): {sorted(no_image)}")

if not no_label and not no_image:
    print("\n데이터셋 무결성 검사 통과")
else:
    print(f"\n총 {len(no_label) + len(no_image)}건의 불일치 발견")

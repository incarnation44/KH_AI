# [목적] 클래스별로 정해진 장수만큼 파일명을 자동 생성한다
# [설명] 촬영 계획을 세우거나 파일 목록을 만들 때 사용합니다.

classes = ["leaf", "plastic", "branch", "disease", "pepper"]
per_class = 3

total = 0
for class_name in classes:
    for i in range(1, per_class + 1):
        file_name = f"conveyor_{class_name}_{i:03d}.jpg"
        print(file_name)
        total += 1

print("-" * 30)
print(f"총 {len(classes)}개 클래스 x {per_class}장 = {total}장")

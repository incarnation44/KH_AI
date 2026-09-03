# [목적] 여러 검출 결과를 클래스별로 세어 분포를 파악한다
# [설명] 데이터 불균형을 확인하는 필수 작업입니다.

detected_ids = [1, 6, 1, 3, 1, 6, 2, 1, 3, 6, 1, 5]
class_names = {1: "나뭇잎류", 2: "플라스틱류", 3: "나뭇가지류",
               5: "병해·갈변", 6: "파·고추"}

counts = {}
for cid in detected_ids:
    if cid in counts:
        counts[cid] += 1
    else:
        counts[cid] = 1

total = len(detected_ids)
print(f"{'클래스':<12}{'개수':>5}{'비율':>9}")
print("-" * 27)
for cid in sorted(counts):
    name = class_names[cid]
    n = counts[cid]
    print(f"{name:<12}{n:>5}{n/total:>9.1%}")
print("-" * 27)
print(f"{'합계':<12}{total:>5}")

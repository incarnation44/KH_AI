# [목적] 앞서 반복문으로 하던 집계를 컴프리헨션으로 처리한다
# [설명] 딕셔너리 컴프리헨션과 count()의 조합입니다.

detected = [1, 6, 1, 3, 1, 6, 2, 1, 3, 6, 1, 5]
CLASS_MAP = {1: "나뭇잎류", 2: "플라스틱류", 3: "나뭇가지류",
             5: "병해·갈변", 6: "파·고추"}

# 집합으로 고유 클래스를 뽑고, count로 개수를 센다
counts = {cid: detected.count(cid) for cid in sorted(set(detected))}
print("집계:", counts)

total = len(detected)
report = [f"{CLASS_MAP[cid]}: {n}건 ({n/total:.0%})"
          for cid, n in counts.items()]

print("\n=== 클래스 분포 ===")
for line in report:
    print(" -", line)

# 부족한 클래스 찾기 (전체의 10% 미만)
rare = [CLASS_MAP[cid] for cid, n in counts.items() if n / total < 0.10]
print("\n추가 촬영 권장:", rare)

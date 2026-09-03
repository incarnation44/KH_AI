# [목적] 긴 elif 체인을 딕셔너리 하나로 대체한다
# [설명] 조건마다 값만 다를 때는 딕셔너리가 훨씬 간결합니다.

CLASS_MAP = {
    1: "나뭇잎류",
    2: "플라스틱·돌·금속 등",
    3: "나뭇가지류",
    4: "고무장갑(미사용)",
    5: "병해·갈변",
    6: "파·고추",
}

detected = [1, 6, 3, 9, 5]

for cid in detected:
    name = CLASS_MAP.get(cid, "등록되지 않은 클래스")
    print(f"클래스 {cid}: {name}")

print("\n등록된 클래스 수:", len(CLASS_MAP))
print("사용 가능한 ID:", [k for k in CLASS_MAP if k != 4])

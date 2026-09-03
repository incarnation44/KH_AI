# [목적] 데이터가 없는 클래스에서도 리포트가 생성되게 한다
# [설명] 검출이 0건인 클래스는 실제로 자주 발생합니다.

def safe_ratio(numerator, denominator, default=0.0):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return default

stats = {
    "나뭇잎류": {"tp": 85, "fp": 15, "fn": 10},
    "플라스틱류": {"tp": 42, "fp": 8, "fn": 12},
    "고무장갑": {"tp": 0, "fp": 0, "fn": 0},      # 검출 0건
}

print(f"{'클래스':<12}{'Precision':>11}{'Recall':>9}{'F1':>8}")
print("-" * 40)

for name, s in stats.items():
    p = safe_ratio(s["tp"], s["tp"] + s["fp"])
    r = safe_ratio(s["tp"], s["tp"] + s["fn"])
    f1 = safe_ratio(2 * p * r, p + r)
    print(f"{name:<12}{p:>11.3f}{r:>9.3f}{f1:>8.3f}")

print("\n[참고] 지표가 0인 클래스는 검출 데이터가 없는지 확인이 필요합니다.")

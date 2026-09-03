# [목적] Precision, Recall, F1을 각각 함수로 만들어 재사용한다
# [설명] 최종 프로젝트 평가 리포트에 그대로 쓰입니다.

def precision(tp, fp):
    return tp / (tp + fp) if (tp + fp) > 0 else 0.0

def recall(tp, fn):
    return tp / (tp + fn) if (tp + fn) > 0 else 0.0

def f1_score(tp, fp, fn):
    p = precision(tp, fp)
    r = recall(tp, fn)
    return 2 * p * r / (p + r) if (p + r) > 0 else 0.0

def print_report(name, tp, fp, fn):
    print(f"[{name}]")
    print(f"  Precision: {precision(tp, fp):.3f}")
    print(f"  Recall   : {recall(tp, fn):.3f}")
    print(f"  F1 Score : {f1_score(tp, fp, fn):.3f}")

print_report("나뭇잎류", tp=85, fp=15, fn=10)
print_report("파·고추", tp=42, fp=28, fn=35)
print_report("데이터없음", tp=0, fp=0, fn=0)

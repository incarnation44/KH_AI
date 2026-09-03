# [목적] 클래스마다 검출 개수와 평균 신뢰도를 집계한다
# [설명] 어느 클래스가 잘 안 잡히는지 파악하는 데 쓰입니다.

detections = [
    {"class_id": 1, "conf": 0.92}, {"class_id": 1, "conf": 0.88},
    {"class_id": 6, "conf": 0.55}, {"class_id": 1, "conf": 0.79},
    {"class_id": 2, "conf": 0.91}, {"class_id": 6, "conf": 0.61},
    {"class_id": 2, "conf": 0.85}, {"class_id": 6, "conf": 0.58},
]
CLASS_MAP = {1: "나뭇잎류", 2: "플라스틱류", 6: "파·고추"}

stats = {}
for d in detections:
    cid = d["class_id"]
    if cid not in stats:
        stats[cid] = {"count": 0, "conf_sum": 0.0}
    stats[cid]["count"] += 1
    stats[cid]["conf_sum"] += d["conf"]

print(f"{'클래스':<12}{'개수':>5}{'평균신뢰도':>11}  상태")
print("-" * 40)
for cid in sorted(stats):
    s = stats[cid]
    avg = s["conf_sum"] / s["count"]
    status = "양호" if avg >= 0.7 else "학습 보강 필요"
    print(f"{CLASS_MAP[cid]:<12}{s['count']:>5}{avg:>11.1%}  {status}")

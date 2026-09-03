# [목적] 대량 처리 중 실패한 항목만 따로 모아 재시도할 수 있게 한다
# [설명] 실무 파이프라인에서 반드시 필요한 구조입니다.

import csv

def process_one(record):
    """한 건을 처리 (오류 상황을 재현하기 위한 예제)"""
    conf = float(record["conf"])          # 잘못된 값이면 ValueError
    area = int(record["w"]) * int(record["h"])
    if area == 0:
        raise ValueError("면적이 0입니다")
    return {"file": record["file"], "conf": conf, "area": area,
            "verdict": "NG" if conf >= 0.7 else "OK"}

records = [
    {"file": "img_001.jpg", "conf": "0.92", "w": "40", "h": "30"},
    {"file": "img_002.jpg", "conf": "abc", "w": "55", "h": "60"},
    {"file": "img_003.jpg", "conf": "0.88", "w": "90", "h": "0"},
    {"file": "img_004.jpg", "conf": "0.65", "w": "20", "h": "15"},
]

results, failures = [], []

for r in records:
    try:
        results.append(process_one(r))
    except Exception as e:
        failures.append({"file": r["file"], "error": str(e)})

print(f"성공 {len(results)}건 / 실패 {len(failures)}건\n")
for r in results:
    print(f"  [{r['verdict']}] {r['file']} (면적 {r['area']})")

if failures:
    with open("failed.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["file", "error"])
        w.writeheader()
        w.writerows(failures)
    print("\n실패 목록을 failed.csv에 저장했습니다:")
    for x in failures:
        print(f"  {x['file']}: {x['error']}")

# [목적] 표 형태의 데이터를 csv 모듈로 다룬다
# [설명] DictWriter를 쓰면 딕셔너리를 그대로 저장할 수 있습니다.

import csv

rows = [
    {"name": "김철수", "score": 88},
    {"name": "이영희", "score": 95},
    {"name": "박민수", "score": 72},
]

with open("scores.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "score"])
    writer.writeheader()
    for row in rows:
        writer.writerow(row)

print("=== 저장된 파일 내용 ===")
with open("scores.csv", "r", encoding="utf-8") as f:
    print(f.read())

print("=== DictReader로 읽기 ===")
with open("scores.csv", "r", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], "->", row["score"], "점")

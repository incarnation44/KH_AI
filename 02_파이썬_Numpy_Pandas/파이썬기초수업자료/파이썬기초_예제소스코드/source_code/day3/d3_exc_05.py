# [목적] 일부 데이터에 문제가 있어도 나머지는 계속 처리한다
# [설명] 대량 데이터 처리에서 가장 중요한 패턴입니다.

data = ["10", "20", "abc", "30", "", "40"]

total = 0
success = 0
failed = []

for item in data:
    try:
        total += int(item)
        success += 1
    except ValueError:
        failed.append(item)
        continue

print(f"성공 {success}건 / 실패 {len(failed)}건")
print(f"실패 항목: {failed}")
print(f"합계: {total}")
print(f"평균: {total / success:.1f}")

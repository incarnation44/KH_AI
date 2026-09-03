# [목적] 라벨 한 줄이 올바른 형식인지 여러 단계로 검사한다
# [설명] 데이터 품질 평가(10점) 항목과 직결되는 작업입니다.

line = "3 0.42 0.35 1.20 0.08"      # 세 번째 값이 1을 초과 -> 오류
parts = line.split()

if len(parts) != 5:
    result = "오류: 컬럼이 5개가 아님"
elif not parts[0].isdigit():
    result = "오류: 클래스ID가 숫자가 아님"
elif int(parts[0]) not in [1, 2, 3, 5, 6]:
    result = "오류: 등록되지 않은 클래스ID"
else:
    coords = [float(p) for p in parts[1:]]
    if min(coords) < 0 or max(coords) > 1:
        result = "오류: 좌표가 0~1 범위를 벗어남"
    else:
        result = "정상"

print(f"검사 대상: {line}")
print(f"결과: {result}")

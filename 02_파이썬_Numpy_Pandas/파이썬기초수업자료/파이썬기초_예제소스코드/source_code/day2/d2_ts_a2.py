# [목적] 촬영 데이터에 모든 클래스가 포함되었는지 확인한다
# [설명] 교과 14 요건: 분류 5종 이상

REQUIRED = {1, 2, 3, 5, 6}          # 사용해야 할 클래스 (4번 제외)

collected = [1, 1, 6, 3, 1, 6, 2, 1, 3, 6, 1]
present = set(collected)

missing = REQUIRED - present
extra = present - REQUIRED

print("촬영된 클래스:", sorted(present), f"({len(present)}종)")
print("요구 클래스  :", sorted(REQUIRED), f"({len(REQUIRED)}종)")

if missing:
    print(f"[미충족] 촬영이 필요한 클래스: {sorted(missing)}")
else:
    print("[충족] 모든 클래스가 포함되었습니다")

if extra:
    print(f"[확인필요] 정의되지 않은 클래스 발견: {sorted(extra)}")

print(f"요건(5종 이상) 달성: {len(present & REQUIRED) >= 5}")

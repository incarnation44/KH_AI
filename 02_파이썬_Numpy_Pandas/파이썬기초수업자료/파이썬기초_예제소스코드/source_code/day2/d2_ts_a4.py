# [목적] COCO 표준 관절 데이터를 튜플로 관리하고 분석한다
# [설명] 교과 15 동작인식 프로젝트의 입력 데이터 형태입니다.

# (관절명, x, y, 신뢰도)
pose = [
    ("nose", 320, 120, 0.95),
    ("left_shoulder", 280, 200, 0.91),
    ("right_shoulder", 360, 200, 0.93),
    ("left_wrist", 250, 150, 0.72),
    ("right_wrist", 390, 380, 0.88),
]

print(f"{'관절':<16}{'X':>6}{'Y':>6}{'신뢰도':>8}")
print("-" * 36)
for name, x, y, conf in pose:
    print(f"{name:<16}{x:>6}{y:>6}{conf:>8.2f}")

# 수신호 판정: 손목이 어깨보다 위에 있는가? (y가 작을수록 위)
shoulder_y = 200
left_up = any(y < shoulder_y for n, x, y, c in pose if n == "left_wrist")
right_up = any(y < shoulder_y for n, x, y, c in pose if n == "right_wrist")

print(f"\n왼손 들어올림 : {left_up}")
print(f"오른손 들어올림: {right_up}")
print(f"동작 판정: {'한손 신호' if left_up != right_up else ('양손 신호' if left_up else '대기')}")

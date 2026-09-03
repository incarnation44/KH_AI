# [목적] 추론 시간을 입력받아 두 프로젝트의 성능 목표 달성 여부를 판정한다
# [설명] 교과 14는 20FPS, 교과 15는 30FPS가 목표입니다.

ms = float(input("이미지 1장 추론 시간(ms): "))
fps = 1000 / ms

print(f"\n측정 결과: {fps:.1f} FPS")
print(f"교과14 목표(20 FPS): {'달성' if fps >= 20 else '미달'}")
print(f"교과15 목표(30 FPS): {'달성' if fps >= 30 else '미달'}")

need_ms_30 = 1000 / 30
print(f"\n30 FPS를 위해 필요한 처리시간: {need_ms_30:.1f} ms 이하")
print(f"현재 대비 {ms - need_ms_30:.1f} ms 단축 필요")

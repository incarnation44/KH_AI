# [목적] 한 장 처리 시간으로 FPS를 계산하고 목표 달성 여부를 판정한다
# [설명] 교과 14 목표: Jetson에서 20 FPS 이상, 교과 15: PC에서 30 FPS 이상

inference_time_ms = 42          # 이미지 한 장 처리에 걸린 시간(밀리초)

fps = 1000 / inference_time_ms  # 1초(1000ms)에 몇 장 처리 가능한가

print("처리 시간:", inference_time_ms, "ms/장")
print("FPS:", round(fps, 1))
print("교과14 기준(20 FPS) 충족?", fps >= 20)
print("교과15 기준(30 FPS) 충족?", fps >= 30)

# [목적] 프로젝트 목표 성능 3가지를 모두 검사해 종합 판정한다
# [설명] 교과 15 기준: AP 0.7 / Top-1 80% / 30 FPS

pose_ap = 0.72
action_acc = 0.83
fps = 27.5

pass_ap = pose_ap >= 0.7
pass_acc = action_acc >= 0.80
pass_fps = fps >= 30

print(f"Pose AP      : {pose_ap:.2f}  -> {'통과' if pass_ap else '미달'}")
print(f"Action Top-1 : {action_acc:.0%}  -> {'통과' if pass_acc else '미달'}")
print(f"속도          : {fps:.1f} FPS -> {'통과' if pass_fps else '미달'}")
print("-" * 34)

if pass_ap and pass_acc and pass_fps:
    print("종합 판정: 전 항목 목표 달성")
elif pass_ap and pass_acc:
    print("종합 판정: 정확도는 달성, 속도 최적화 필요")
else:
    print("종합 판정: 모델 성능 개선 필요")

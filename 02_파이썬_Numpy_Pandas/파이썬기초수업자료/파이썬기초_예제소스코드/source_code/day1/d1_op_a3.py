# [목적] Confusion Matrix 값에서 Precision·Recall·F1을 직접 계산한다
# [설명] 최종 프로젝트 평가에서 직접 설명해야 하는 지표들입니다.

TP = 85     # True Positive : 이물인데 이물이라 맞춘 것
FP = 15     # False Positive: 정상인데 이물이라 잘못 잡은 것
FN = 10     # False Negative: 이물인데 놓친 것

precision = TP / (TP + FP)      # 이물이라 한 것 중 진짜 이물 비율
recall = TP / (TP + FN)         # 진짜 이물 중 찾아낸 비율
f1 = 2 * precision * recall / (precision + recall)

print("Precision:", round(precision, 3))
print("Recall   :", round(recall, 3))
print("F1 Score :", round(f1, 3))
print("목표(0.7) 달성?", f1 >= 0.7)

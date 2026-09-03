# [목적] 하이퍼파라미터를 하나의 설정 딕셔너리로 묶는다
# [설명] 나중에 JSON 파일로 저장하면 그대로 설정 파일이 됩니다.

config = {
    "model": "yolov8n",
    "img_size": 640,
    "batch_size": 16,
    "epochs": 100,
    "lr": 0.001,
    "classes": [1, 2, 3, 5, 6],
}

print("=== 학습 설정 ===")
for key, value in config.items():
    print(f"{key:<12}: {value}")

print("\n클래스 수:", len(config["classes"]))
print("총 학습 스텝:", 500 // config["batch_size"] * config["epochs"])

# 설정 일부만 바꿔서 실험하기
config["batch_size"] = 8
config["epochs"] = 60
print("\n변경 후 총 스텝:", 500 // config["batch_size"] * config["epochs"])

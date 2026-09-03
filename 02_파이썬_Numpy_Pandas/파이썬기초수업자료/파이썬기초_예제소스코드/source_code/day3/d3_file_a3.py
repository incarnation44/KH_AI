# [목적] 실험 조건을 파일로 남겨 재현 가능하게 만든다
# [설명] 어떤 설정으로 학습했는지 기록하는 것은 필수 작업입니다.

import json

config = {
    "experiment": "exp_003",
    "model": "yolov8n",
    "train": {"img_size": 640, "batch": 16, "epochs": 100, "lr": 0.001},
    "classes": {"1": "나뭇잎류", "2": "플라스틱류", "3": "나뭇가지류",
                "5": "병해·갈변", "6": "파·고추"},
    "result": {"mAP50": 0.7821, "precision": 0.85, "recall": 0.89},
}

with open("exp_003.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

# 다시 읽어 리포트 출력
with open("exp_003.json", "r", encoding="utf-8") as f:
    cfg = json.load(f)

print(f"=== {cfg['experiment']} 결과 ===")
print(f"모델    : {cfg['model']}")
print(f"학습설정: batch {cfg['train']['batch']}, epochs {cfg['train']['epochs']}")
print(f"클래스수: {len(cfg['classes'])}종")
print(f"mAP50   : {cfg['result']['mAP50']:.4f}")
print(f"목표 달성: {'예' if cfg['result']['mAP50'] >= 0.7 else '아니오'}")

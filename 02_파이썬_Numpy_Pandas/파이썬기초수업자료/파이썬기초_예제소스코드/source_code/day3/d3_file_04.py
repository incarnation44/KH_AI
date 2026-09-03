# [목적] 딕셔너리를 파일로 저장하고 그대로 복원한다
# [설명] 중첩 구조를 그대로 보존할 수 있는 것이 JSON의 장점입니다.

import json

config = {
    "model": "yolov8n",
    "img_size": 640,
    "classes": {"1": "나뭇잎류", "2": "플라스틱류"},
    "augment": True,
}

with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)

print("=== 저장된 파일 ===")
with open("config.json", "r", encoding="utf-8") as f:
    print(f.read())

with open("config.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print("복원 확인:", loaded["model"], "/", loaded["classes"]["1"])
print("자료형 유지:", type(loaded["img_size"]), type(loaded["augment"]))

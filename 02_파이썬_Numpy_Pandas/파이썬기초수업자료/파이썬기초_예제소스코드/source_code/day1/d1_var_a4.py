# [목적] 딥러닝 학습에 필요한 하이퍼파라미터를 변수로 모아 관리한다
# [설명] 값을 코드 여기저기 흩어두지 않고 맨 위에 모으는 것이 실무 관례입니다.

MODEL_NAME = "yolov8n"            # 대문자 = 바꾸지 않을 설정값이라는 표시
IMAGE_SIZE = 640                  # 입력 이미지 크기
BATCH_SIZE = 16                   # 한 번에 학습할 이미지 수
EPOCHS = 100                      # 전체 데이터를 반복 학습할 횟수
LEARNING_RATE = 0.001

total_images = 500
steps_per_epoch = total_images // BATCH_SIZE   # 몫만 취하기
total_steps = steps_per_epoch * EPOCHS

print("모델:", MODEL_NAME, "/ 입력크기:", IMAGE_SIZE)
print("1 epoch당 반복:", steps_per_epoch, "회")
print("전체 학습 반복:", total_steps, "회")

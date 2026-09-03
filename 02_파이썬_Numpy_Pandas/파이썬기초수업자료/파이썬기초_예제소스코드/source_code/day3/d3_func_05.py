# [목적] 개수가 정해지지 않은 인자를 받는 방법
# [설명] *는 튜플로, **는 딕셔너리로 모아줍니다.

def total_sum(*numbers):
    print("받은 값들:", numbers, type(numbers))
    return sum(numbers)

print("합계:", total_sum(1, 2, 3))
print("합계:", total_sum(10, 20, 30, 40, 50))

def show_config(**options):
    print("설정 항목:", options)
    for key, value in options.items():
        print(f"  {key} = {value}")

show_config(model="yolov8n", epochs=100, lr=0.001)

# [목적] 인스턴스의 상태가 시간에 따라 변하는 것을 표현한다
# [설명] 메서드가 self.속성을 바꾸는 형태입니다.

class Counter:
    def __init__(self):
        self.count = 0
        self.history = []

    def increase(self, step=1):
        self.count += step
        self.history.append(self.count)

    def reset(self):
        self.count = 0
        self.history.append(0)

c = Counter()
c.increase()
c.increase()
c.increase(5)
print("현재 값:", c.count)
print("변화 기록:", c.history)

c.reset()
print("리셋 후:", c.count, c.history)

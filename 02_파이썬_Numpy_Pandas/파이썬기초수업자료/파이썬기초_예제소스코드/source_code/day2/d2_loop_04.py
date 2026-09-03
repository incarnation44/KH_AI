# [목적] 반복을 중간에 멈추거나 건너뛰는 방법
# [설명] break는 완전 종료, continue는 이번 회차만 건너뜀

# break : 찾으면 즉시 종료
for i in range(1, 11):
    if i == 4:
        print("4를 찾아서 중단")
        break
    print("검사 중:", i)

print("=== continue ===")

# continue : 짝수는 건너뛰기
for i in range(1, 7):
    if i % 2 == 0:
        continue
    print("홀수:", i)

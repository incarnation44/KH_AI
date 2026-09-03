# [목적] 변수는 언제든 새 값으로 덮어쓸 수 있다는 것을 확인한다
# [설명] count = count + 1 은 "현재 값에 1을 더해 다시 넣기"입니다.

count = 0
print("시작:", count)

count = count + 1
print("한 번 더한 뒤:", count)

count += 1          # count = count + 1 의 줄임 표현
count += 1
print("세 번 더한 뒤:", count)

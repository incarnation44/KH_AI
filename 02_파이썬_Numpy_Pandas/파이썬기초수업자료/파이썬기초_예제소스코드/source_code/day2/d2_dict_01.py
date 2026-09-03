# [목적] key로 값을 저장하고 조회하는 기본 동작
# [설명] 리스트의 [0] 대신 ["이름"]으로 접근합니다.

person = {"name": "홍길동", "age": 25, "city": "서울"}

print(person)
print("이름:", person["name"])
print("나이:", person["age"])
print("항목 수:", len(person))

# 값 수정 / 새 항목 추가
person["age"] = 26
person["job"] = "데이터 분석가"
print("수정 후:", person)

# [목적] 파일 목록에서 중복 등록된 항목을 찾는다
# [설명] 여러 조가 촬영한 데이터를 합칠 때 필요합니다.

team_a = ["img_001.jpg", "img_002.jpg", "img_003.jpg"]
team_b = ["img_003.jpg", "img_004.jpg", "img_001.jpg", "img_005.jpg"]

set_a, set_b = set(team_a), set(team_b)

duplicated = set_a & set_b
all_files = set_a | set_b

print(f"A조: {len(team_a)}장 / B조: {len(team_b)}장")
print(f"단순 합계: {len(team_a) + len(team_b)}장")
print(f"실제 고유 파일: {len(all_files)}장")
print(f"중복된 파일 {len(duplicated)}건: {sorted(duplicated)}")
print(f"\n중복 제거로 절약: {len(team_a) + len(team_b) - len(all_files)}장")

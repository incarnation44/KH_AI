# [목적] 이미 처리한 파일을 집합에 기록해 중복 작업을 막는다
# [설명] 대용량 데이터를 나눠서 처리할 때 필수적인 패턴입니다.

all_files = ["img_001.jpg", "img_002.jpg", "img_003.jpg",
             "img_004.jpg", "img_005.jpg"]

processed = {"img_001.jpg", "img_003.jpg"}    # 이전 실행에서 완료

remaining = [f for f in all_files if f not in processed]

print(f"전체 {len(all_files)}건 / 완료 {len(processed)}건 / 남음 {len(remaining)}건")
print(f"진행률: {len(processed)/len(all_files):.0%}")
print("\n=== 이어서 처리 ===")

for f in remaining:
    print(f"처리 중: {f}")
    processed.add(f)

print(f"\n최종 완료: {len(processed)}건 / 진행률 100%")

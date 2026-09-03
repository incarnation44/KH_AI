# [목적] 파일 목록과 비율을 받아 세 그룹으로 나눈다
# [설명] 비율을 인자로 받게 만들어 어떤 프로젝트에도 재사용 가능합니다.

def split_dataset(files, train_ratio=0.7, val_ratio=0.15):
    total = len(files)
    train_end = int(total * train_ratio)
    val_end = train_end + int(total * val_ratio)
    return {
        "train": files[:train_end],
        "val": files[train_end:val_end],
        "test": files[val_end:],
    }

def print_split_info(splits):
    total = sum(len(v) for v in splits.values())
    print(f"{'구분':<8}{'장수':>6}{'비율':>9}")
    print("-" * 24)
    for name, items in splits.items():
        print(f"{name:<8}{len(items):>6}{len(items)/total:>9.1%}")
    print("-" * 24)
    print(f"{'합계':<8}{total:>6}")

files = [f"img_{i:03d}.jpg" for i in range(1, 101)]
result = split_dataset(files)
print_split_info(result)

print("\nTrain 첫 3개:", result["train"][:3])
print("Test 마지막 3개:", result["test"][-3:])

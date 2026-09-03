# [목적] 파일이 없거나 형식이 틀려도 프로그램이 멈추지 않게 한다
# [설명] 이미지는 있는데 라벨이 없는 경우가 실제로 자주 발생합니다.

def read_label(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = [ln.strip() for ln in f if ln.strip()]
    except FileNotFoundError:
        print(f"  [경고] 라벨 파일 없음: {path}")
        return []
    except UnicodeDecodeError:
        print(f"  [경고] 인코딩 오류: {path}")
        return []

    boxes = []
    for i, line in enumerate(lines, 1):
        try:
            parts = line.split()
            if len(parts) != 5:
                raise ValueError(f"컬럼이 5개가 아님({len(parts)}개)")
            boxes.append({
                "class_id": int(parts[0]),
                "coords": [float(v) for v in parts[1:5]],
            })
        except (ValueError, IndexError) as e:
            print(f"  [경고] {path} {i}번째 줄 형식 오류: {e}")
    return boxes

# 실습용 파일 생성
with open("good.txt", "w", encoding="utf-8") as f:
    f.write("1 0.42 0.35 0.10 0.08\n6 0.71 0.60 0.15 0.12\n")
with open("bad.txt", "w", encoding="utf-8") as f:
    f.write("1 0.42 0.35 0.10 0.08\nabc 0.1 0.1 0.1 0.1\n3 0.5\n")

for path in ["good.txt", "bad.txt", "missing.txt"]:
    print(f"{path}:")
    result = read_label(path)
    print(f"  -> 유효한 박스 {len(result)}개\n")

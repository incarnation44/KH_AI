# [목적] 데이터셋의 파일 목록과 분할, 통계를 한 곳에서 관리한다
# [설명] 실무에서 가장 흔히 만드는 형태의 관리 클래스입니다.

class Dataset:
    def __init__(self, name):
        self.name = name
        self.items = []        # (파일명, 클래스ID) 목록

    def add(self, file_name, class_id):
        self.items.append((file_name, class_id))

    def size(self):
        return len(self.items)

    def class_counts(self):
        counts = {}
        for _, cid in self.items:
            counts[cid] = counts.get(cid, 0) + 1
        return counts

    def split(self, train=0.7, val=0.15):
        n = self.size()
        a, b = int(n * train), int(n * train) + int(n * val)
        return {"train": self.items[:a], "val": self.items[a:b],
                "test": self.items[b:]}

    def summary(self):
        print(f"=== {self.name} ===")
        print(f"전체: {self.size()}건")
        counts = self.class_counts()
        for cid in sorted(counts):
            n = counts[cid]
            bar = "█" * int(n / self.size() * 20)
            print(f"  클래스 {cid}: {n:>3}건 {bar} {n/self.size():.0%}")
        s = self.split()
        print(f"분할: train {len(s['train'])} / val {len(s['val'])} / test {len(s['test'])}")
        if len(counts) < 5:
            print(f"[주의] 클래스가 {len(counts)}종입니다 (요구: 5종 이상)")

ds = Dataset("conveyor_2026")
pattern = [1, 1, 2, 1, 6, 3, 1, 6, 2, 1, 3, 6, 1, 2, 1, 6, 1, 3, 1, 2]
for i, cid in enumerate(pattern, 1):
    ds.add(f"img_{i:03d}.jpg", cid)

ds.summary()

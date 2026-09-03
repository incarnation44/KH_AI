import os, glob, csv

VALID_CLASSES = [1, 2, 3, 5, 6]
CLASS_NAMES = {1: "나뭇잎류", 2: "플라스틱류", 3: "나뭇가지류",
               5: "병해·갈변", 6: "파·고추"}


class DatasetValidator:
    def __init__(self, image_dir, label_dir):
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.errors = []
        self.class_counts = {}
        self.total_lines = 0

    def check_line(self, file_name, line_no, line):
        self.total_lines += 1
        parts = line.split()
        if len(parts) != 5:
            return self._error(file_name, line_no, f"컬럼 {len(parts)}개 (5개여야 함)")
        try:
            class_id = int(parts[0])
        except ValueError:
            return self._error(file_name, line_no, f"클래스ID가 숫자 아님: '{parts[0]}'")
        if class_id not in VALID_CLASSES:
            return self._error(file_name, line_no, f"미등록 클래스: {class_id}")
        try:
            coords = [float(v) for v in parts[1:]]
        except ValueError:
            return self._error(file_name, line_no, "좌표가 숫자 아님")
        if min(coords) < 0 or max(coords) > 1:
            return self._error(file_name, line_no, "좌표가 0~1 범위 초과")
        if coords[2] == 0 or coords[3] == 0:
            return self._error(file_name, line_no, "너비 또는 높이가 0")
        self.class_counts[class_id] = self.class_counts.get(class_id, 0) + 1
        return True

    def _error(self, file_name, line_no, message):
        self.errors.append({"file": file_name, "line": line_no, "error": message})
        return False

    def check_file(self, path):
        name = os.path.basename(path)
        try:
            with open(path, "r", encoding="utf-8") as f:
                lines = [ln.strip() for ln in f if ln.strip()]
        except FileNotFoundError:
            return self._error(name, 0, "파일을 열 수 없음")
        if not lines:
            return self._error(name, 0, "빈 라벨 파일 (객체 없음)")
        for i, line in enumerate(lines, start=1):
            self.check_line(name, i, line)

    def check_pairs(self):
        images = {os.path.splitext(f)[0] for f in os.listdir(self.image_dir) if f.endswith(".jpg")}
        labels = {os.path.splitext(f)[0] for f in os.listdir(self.label_dir) if f.endswith(".txt")}
        return {"matched": sorted(images & labels), "no_label": sorted(images - labels),
                "no_image": sorted(labels - images)}

    def run(self):
        files = sorted(glob.glob(os.path.join(self.label_dir, "*.txt")))
        for path in files:
            self.check_file(path)
        return len(files)

    def print_report(self, file_count, pairs):
        print("=" * 52)
        print("          데이터셋 검증 리포트")
        print("=" * 52)
        print(f"\n[1] 파일 현황")
        print(f"  라벨 파일   : {file_count}개")
        print(f"  검사한 줄   : {self.total_lines}줄")
        print(f"  정상 짝     : {len(pairs['matched'])}건")
        print(f"  라벨 누락   : {len(pairs['no_label'])}건 {pairs['no_label']}")
        print(f"  이미지 누락 : {len(pairs['no_image'])}건 {pairs['no_image']}")
        print(f"\n[2] 오류 현황 : 총 {len(self.errors)}건")
        for e in self.errors:
            print(f"  {e['file']:<16} {e['line']:>3}행  {e['error']}")
        print(f"\n[3] 클래스 분포")
        total = sum(self.class_counts.values())
        if total > 0:
            for cid in sorted(self.class_counts):
                n = self.class_counts[cid]
                bar = "█" * int(n / total * 20)
                name = CLASS_NAMES.get(cid, "?")
                print(f"  {name:<10} {n:>3}개 {bar} {n/total:.0%}")
            missing = set(VALID_CLASSES) - set(self.class_counts)
            if missing:
                print(f"  [주의] 한 번도 등장하지 않은 클래스: {sorted(missing)}")
        ok_rate = (self.total_lines - len(self.errors)) / self.total_lines if self.total_lines else 0
        print(f"\n[4] 종합 : 정상률 {ok_rate:.1%}")
        print("=" * 52)

    def save_csv(self, path="validation_report.csv"):
        if not self.errors:
            print("오류가 없어 리포트를 생성하지 않았습니다.")
            return
        with open(path, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=["file", "line", "error"])
            w.writeheader()
            w.writerows(self.errors)
        print(f"오류 {len(self.errors)}건을 {path}에 저장했습니다.")


if __name__ == "__main__":
    os.makedirs("dataset/images", exist_ok=True)
    os.makedirs("dataset/labels", exist_ok=True)
    samples = {
        "img_001": ["1 0.42 0.35 0.10 0.08", "6 0.71 0.60 0.15 0.12"],
        "img_002": ["2 0.30 0.25 0.09 0.07"],
        "img_003": ["3 1.20 0.40 0.10 0.10", "abc 0.3 0.3 0.1 0.1"],
        "img_004": ["9 0.50 0.50 0.10 0.10", "2 0.30 0.30"],
        "img_005": ["1 0.20 0.20 0.00 0.05"],
    }
    for name, lines in samples.items():
        open(f"dataset/images/{name}.jpg", "w").close()
        with open(f"dataset/labels/{name}.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(lines) + "\n")
    open("dataset/images/img_006.jpg", "w").close()

    v = DatasetValidator("dataset/images", "dataset/labels")
    count = v.run()
    pairs = v.check_pairs()
    v.print_report(count, pairs)
    v.save_csv()

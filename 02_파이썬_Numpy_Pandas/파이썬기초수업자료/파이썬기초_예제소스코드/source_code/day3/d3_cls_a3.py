# [목적] 검증 규칙과 결과 집계를 하나의 클래스로 관리한다
# [설명] 설정과 상태를 함께 가지는 도구형 클래스입니다.

class LabelValidator:
    def __init__(self, valid_classes=None):
        self.valid_classes = valid_classes or [1, 2, 3, 5, 6]
        self.errors = []
        self.checked = 0

    def check_line(self, file_name, line_no, line):
        self.checked += 1
        parts = line.split()

        if len(parts) != 5:
            return self._add(file_name, line_no, "컬럼 개수 오류")
        try:
            cid = int(parts[0])
        except ValueError:
            return self._add(file_name, line_no, "클래스ID가 숫자 아님")
        if cid not in self.valid_classes:
            return self._add(file_name, line_no, f"미등록 클래스 {cid}")
        try:
            coords = [float(v) for v in parts[1:]]
        except ValueError:
            return self._add(file_name, line_no, "좌표가 숫자 아님")
        if min(coords) < 0 or max(coords) > 1:
            return self._add(file_name, line_no, "좌표 범위 초과")
        return True

    def _add(self, file_name, line_no, msg):
        self.errors.append({"file": file_name, "line": line_no, "error": msg})
        return False

    def report(self):
        print(f"검사 {self.checked}줄 / 오류 {len(self.errors)}건")
        for e in self.errors:
            print(f"  {e['file']} {e['line']}행: {e['error']}")
        rate = (self.checked - len(self.errors)) / self.checked
        print(f"정상률: {rate:.1%}")

data = {
    "img_001.txt": ["1 0.42 0.35 0.10 0.08", "6 0.71 0.60 0.15 0.12"],
    "img_002.txt": ["3 1.20 0.40 0.10 0.10", "abc 0.3 0.3 0.1 0.1"],
    "img_003.txt": ["9 0.50 0.50 0.10 0.10", "2 0.30 0.30"],
}

v = LabelValidator()
for fname, lines in data.items():
    for i, line in enumerate(lines, 1):
        v.check_line(fname, i, line)

v.report()

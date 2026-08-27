# Day 2 — 권한 · 아카이브 · 텍스트 스트림 (8H)
## 핵심 학습 내용
- rwx 권한 체계 (755, 644, 444, 555) 및 디렉토리 x(진입/접근) 권한의 의미
- raw 데이터셋 읽기 전용 잠금 (`chmod 444 raw/* && chmod 555 raw`)
- 심볼릭 링크 (`ln -s`) 를 활용한 디스크 용량 절약형 7:1.5:1.5 분할
- 표준 스트림 (stdin, stdout, stderr) 및 `2>&1`, `2>/dev/null` 리다이렉션
- 파이프라인 집계: `cat *.txt | cut -d' ' -f1 | sort | uniq -c | sort -rn`
- `tar -czvf` / `tar -xzvf` / `tar -tzvf` 아카이브 및 `--exclude` 규칙

## 산출물
- `dataset/kimchi/meta/class_distribution.txt`
- `dataset/kimchi/meta/dataset_report.txt`
- `dataset/kimchi/backup/` 메타데이터 백업 아카이브

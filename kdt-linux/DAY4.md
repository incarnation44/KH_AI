# Day 4 — 셸 스크립트 · 프로세스 · 자동화 (8H)
## 핵심 학습 내용
- `set -euo pipefail` (셸 스크립트 3중 안전벨트)
- 함수화, `local` 변수, 표준 사용법 `usage()` 및 종료 코드 (0: 성공, 1: 실패, 2: 사용법 오류)
- 백그라운드 작업 제어 (`&`, `jobs`, `fg`, `kill`, `pkill`)
- `nohup` 과 `tail -f` 를 통한 로그 모니터링
- `tmux` 세션 분할 (`%`, `"`) 및 Detach (`Ctrl+b d`) 로 무중단 학습 세션 운영
- `cron` 반복 작업 스케줄링 및 절대경로/PATH 함정 극복

## 산출물
- `scripts/dataset_check.sh` (정합성 검증 CLI)
- `scripts/auto_backup.sh` (cron 백업 스크립트)
- `scripts/run_pipeline.sh` (통합 파이프라인)

# Day 3 — 편집기와 텍스트 처리 (8H)
## 핵심 학습 내용
- Vim 3대 모드 (Normal, Insert, Command) 및 기본 조작법 (`:wq`, `:q!`)
- `.vimrc` 생산성 설정 (syntax on, number, tabstop=4, shiftwidth=4, expandtab)
- `grep` 패턴 매칭, `-v`(반전), `-c`(카운트), `-n`(줄번호), `-E`(확장 정규식)
- `sed` 스트림 편집: 치환(`s/old/new/g`), 백업 옵션(`sed -i.bak`)
- `awk` 필드/레코드 처리: `NF`(필드 수), `NR`(레코드 수), 조건문, 배열 활용
- 조각김치 라벨 클래스 재매핑 (6종 -> 5종 재편성)

## 산출물
- `~/.vimrc` 개인화 설정 파일
- `scripts/remap_classes.sh`

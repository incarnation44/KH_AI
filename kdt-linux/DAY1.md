# Day 1 — 리눅스 시작과 파일 시스템 (8H)
## 핵심 학습 내용
- FHS (Filesystem Hierarchy Standard): `/dev/video0`, `/var/log`, `/mnt`, `/etc`
- 절대 경로 vs 상대 경로
- `ls -l` 출력 7개 필드 해독 (권한, 링크, 소유자, 그룹, 크기, 수정일시, 이름)
- `mkdir -p {images,labels}/{train,val,test}` 중괄호 확장으로 YOLO 표준 디렉토리 일괄 생성
- `find` 와 `comm` 을 활용한 이미지-라벨 1차 정합성 검사
- `rsync --dry-run` 및 `scp` 원격 파일 전송

## 산출물
- `dataset/kimchi/` 표준 디렉토리 계층
- `dataset/kimchi/meta/classes.txt`
- `make_sample_dataset.sh`

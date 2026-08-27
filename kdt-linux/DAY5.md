# Day 5 — Anaconda 환경과 데이터셋 구조화 (8H)
## 핵심 학습 내용
- 패키지 관리 3층 구조: ① apt(시스템 라이브러리) > ② conda(파이썬 인터프리터) > ③ pip(패키지)
- OpenCV 실행 시 `libGL.so.1` 의존성 문제 해결
- Conda 황금 규칙: conda 먼저, pip 나중에, sudo pip 절대 금지
- 대용량 데이터셋 설계 5원칙: 원본 불변, 링크 분할, 메타데이터 동봉, 명명 규칙 통일, VCS 분리
- `split_dataset.sh` 시드 고정 70:15:15 분할

## 산출물
- `env/environment.yml` (Conda 환경 정의서)
- `env/requirements.txt`
- `scripts/split_dataset.sh`
- `dataset/kimchi/meta/data.yaml` & `meta/DATASET.md`

# Foundation (기초 설계 및 시스템 청사진)

## 1. 과정 및 프로젝트 개요
* **과정명**: KH 정보교육원 KDT AI / Vision AI 개발자 양성과정
* **핵심 로드맵**:
  1. `01_리눅스` : 셸 스크립트, 리눅스 명령어, Git 버전 관리 및 브랜치/사고 복구 (완료)
  2. `02_파이썬_Numpy_Pandas` : 파이썬 기초 3일 완성 ➡ 데이터 분석(Numpy, Pandas) (현재 진행 중)
  3. `머신러닝 & 딥러닝` : 분류/회귀 알고리즘, 모델 최적화 및 텐서 연산
  4. `Vision AI 프로젝트` : 영상 처리, 컴퓨터 비전 실무 애플리케이션 구축

---

## 2. 하드웨어 및 3대 기기 인프라 매핑 (절대 혼동 금지)
* **1. 학원 컴퓨터 (Academy PC)**:
  * 계정 / 경로: `user1` / `D:\KH_AI` (수업 및 강사 예제 작업)
  * 환경: 윈도우 Anaconda `pytest (Python 3.11)` + WSL Ubuntu
* **2. 메인 데스크톱 (Ildo 본체)**:
  * CPU/GPU/RAM: AMD Ryzen 5 5600X / AMD Radeon RX 6600 (8GB VRAM 외장) / 32GB DDR4
  * 저장소: C: (OS/도구), D: (미디어/보조 SSD), E: (데이터)
* **3. 💻 서브 노트북 (Ildo-Laptop / Dell Latitude 7440 - 현재 작업 기기)**:
  * CPU/GPU/RAM: Intel Core i5-1345U (10C/12T) / Intel Iris Xe Graphics (내장) / 32GB LPDDR5
  * 저장소 경로: **`C:\KH_AI`** (단일 고속 NVMe C 드라이브)
  * 환경: 윈도우 Miniconda `pytest (Python 3.11.16)` + WSL Ubuntu 24.04 (`~/kdt-linux` 연동)
* **작업 환경 이원화 원칙**:
  * **윈도우 (`C:\KH_AI` / `D:\KH_AI`)**: 정규 교재, 강의 예제 파일, 통합 상태 문서.
  * **우분투 (WSL: `~/kdt-linux`)**: 리눅스 커맨드라인 실습 전용 샌드박스.

---

## 3. AI 튜터 불변의 헌법 (Constitutional Rules)
1. **임의 실행 절대 금지**: 임의 이메일 발송, 결제/과금, 파일/데이터 삭제(`rm`, `Remove-Item` 등) 일체 금지.
2. **바탕화면 오염 방지**: `C:\Users\user1\Desktop`에 어떠한 임시 파일이나 로그도 생성하지 않는다.
3. **설명 및 대화 스타일**: 감탄사/추임새 배제, 기호/공백 단위의 토큰 분해 설명, 직관적 비유(상자, 영수증, 책갈피) 적용.

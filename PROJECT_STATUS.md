# PROJECT STATUS (KH_AI)

> **프로젝트 작업 연속성 상태판 (3-PC 공통 기준점)**  
> 노트북 ↔ 본체 ↔ 학원 PC 간 작업 인계 시 이 문서를 최우선 참조합니다.  
> *주의: 이 문서의 머신 정보는 참고용(히스토리)이며, 현재 실행 환경 판정은 각 PC 로컬의 `MACHINE_ID`가 기준입니다.*

---

## 1. Project Metadata
* **저장소**: `https://github.com/incarnation44/KH_AI.git`
* **기본 브랜치**: `main`
* **마지막 작업 머신 (참고용)**: `laptop`
* **마지막 업데이트 일시**: 2026-09-05 16:42
* **마지막 커밋**: `34c8968 refactor: 01_리눅스 loose 파일 정리 및 02_파이썬 기초 수업자료·예제코드 Git 추적 완료`

---

## 2. Current Task
* **진행 과제**: `02_파이썬_Numpy_Pandas` 기초 실습 예제 코드 분석 및 입출력/문자열 실습 준비
* **작업 디렉터리**: `C:\KH_AI\02_파이썬_Numpy_Pandas\파이썬기초수업자료\파이썬기초_예제소스코드\source_code\day1\`

---

## 3. Completed
* [x] KH_AI 저장소 구조화 및 Git 동기화 (`main` 브랜치 일치)
* [x] 01_리눅스 loose 파일 아카이빙 및 정리
* [x] 02_파이썬 기초 수업자료 및 예제코드 Git 추적 완료
* [x] Conda `pytest` 환경 (Python 3.11.16, OpenCV 5.0.0, PyTorch 2.14.0 CPU, NumPy 2.4.6, Pandas 3.0.5) 검증 완료
* [x] `.gitignore` 보안 항목 보강 (API 키, 자격증명, 개인 파일 차단)

---

## 4. In Progress
* [ ] 3-PC 통합 작업환경 연동 및 Git 동기화 검증
* [ ] `day1` 파이썬 기초 실습 (`d1_str_01.py` ~ `d1_str_05.py`, `d1_io_01.py` ~ `d1_io_05.py`) 코드 분석

---

## 5. Next Steps
1. 노트북에서 작업한 변경사항을 GitHub `main`에 push
2. 본체(Desktop)에서 `git pull origin main` 수신 후 `PROJECT_STATUS.md` 확인하여 작업 연속성 검증
3. 학원 PC(Academy)에서 `git pull origin main` 수신 후 개인 정보 격리 상태에서 파이썬 실습 수행

---

## 6. Known Issues
* Conda 환경이 활성화되지 않은 상태에서 `python.exe`를 직접 호출할 경우 pandas/C-extension DLL 누락 오류가 발생할 수 있음.
* 반드시 `conda activate pytest` 환경에서 실행하거나 VS Code 터미널 프로필을 활용할 것.

---

## 7. Test Results
* **2026-09-05 환경 검증**:
  * Conda `pytest` 환경 인터프리터 (`C:\Users\ildoc\miniconda3\envs\pytest\python.exe`) 동작 확인: **PASS**
  * OpenCV, Torch, NumPy, Pandas, PyTest 5개 핵심 라이브러리 로드: **ALL PASS**

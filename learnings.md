# Learnings (오답 노트 및 시행착오 해결책)

이 문서는 실습 중 발생했던 에러, 오타 패턴, 시스템 특이사항을 기록하여 향후 동일한 실수를 반복하지 않도록 방지합니다.

---

### 1. Conda 가상환경 생성 시 문법 규칙
* **문제 상황**: `conda create -n pytest python 3.11 -y` 입력 시 `PackagesNotFoundError: - 3.11` 발생.
* **원인**: `python`과 `3.11` 사이에 공백이 들어가면 컴퓨터가 `3.11`이라는 이름의 독립 패키지를 찾으려고 시도함.
* **해결책**: 버전을 지정할 때는 반드시 **등호(`=`)**를 붙여 `python=3.11` 형태로 작성해야 함.

---

### 2. 파워셸 스크립트 실행 보안 정책 (PSSecurityException)
* **문제 상황**: VS Code PowerShell 터미널에서 conda 활성화 시 붉은색 `PSSecurityException` 오류 발생.
* **원인**: 윈도우 파워셸의 기본 실행 정책(ExecutionPolicy)이 외부 스크립트 실행을 차단(Restricted)하고 있음.
* **해결책**: 파워셸에서 `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`를 실행하여 스크립트 실행 권한을 부여함.

---

### 3. VS Code의 WSL 리눅스 vs 윈도우 모드 구분
* **문제 상황**: 윈도우 아나콘다에 `pytest`를 만들었으나, VS Code의 `Select Interpreter` 및 `Open Folder`에 리눅스(`/home/ildoc/`) 경로만 표시됨.
* **원인**: VS Code 좌측 하단에 `WSL: Ubuntu-24.04` 원격 모드가 켜져 있어 리눅스 시스템만 탐색하고 있었음.
* **해결책**: 좌측 하단 파란색 WSL 버튼 클릭 ➡ `Close Remote Connection`을 선택하여 순수 윈도우 모드로 복귀함.

---

### 4. 바탕화면 파일 오염 방지
* **문제 상황**: 세션 대화 백업 파일이 바탕화면(`C:\Users\user1\Desktop\AI_Chat_Logs.md`)에 생성됨.
* **원칙**: 바탕화면에는 어떠한 로그나 임시 파일도 생성하지 않으며, 모든 저장물은 오직 `D:\KH_AI` 내부로만 격리함.

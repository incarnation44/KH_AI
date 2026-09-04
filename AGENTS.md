# 💻 KH_AI Vision AI Workspace (Project Rules)

> **상위 헌법 상속**: 본 프로젝트는 전역 헌법 `GEMINI.md`를 100% 상속하며, 파일 삭제 금지, PII 보호, 결제 금지 규칙을 동일하게 적용받습니다.

## 1. 프로젝트 정체성 (Workspace Identity)
- **목적**: Python, OpenCV, YOLO, ROS2 기반 Vision AI 실습 및 개발 전용 워크스페이스
- **위치**: `D:\KH_AI` (실제 코드, 데이터셋, 모델 가중치, 실행 파일)
- **Obsidian(`C:\전일도`)과의 관계**: **절대 분리 (Strict Separation)**
  - `KH_AI` 내부의 코드/데이터셋을 `Obsidian` Vault로 복사하지 않습니다.
  - 개념 정리, 에러 트러블슈팅, 수업 기록 등 "지식(Knowledge)"은 `Obsidian`에 작성합니다.
  - `Obsidian`에서 프로젝트를 참조할 때는 `D:\KH_AI\...` 경로 링크(Link) 방식을 사용합니다.

## 2. 3대 기기(DESKTOP, LAPTOP, ACADEMY) 동기화 원칙
- **식별**: 각 기기는 `.local/machine.json`에 정의된 `machine_id` (`DESKTOP`, `LAPTOP`, `ACADEMY`)를 갖습니다.
- **Git 리포지토리**: `github.com/incarnation44/KH_AI` (Obsidian-vault와 별도 관리)
- **동기화(`/업데이트`) 철칙**:
  1. 명시적인 `/업데이트` 호출 시 AI는 임의로 `git pull/push/commit/reset` 등 Git 명령어를 조합하여 타이핑하지 않고, **오직 `scripts\sync_safe_update.ps1` 스크립트를 실행**하여 안전하게 동기화하고 그 결과를 보고합니다.
  2. 스크립트 내부에서 덮어쓰기 금지(No Auto-Overwrite), 충돌 보호(Conflict Protection), 기기명 자동 삽입(`[DESKTOP] ...`)을 완벽히 수행하며, 충돌 시엔 작업을 중지(STOP)합니다.

## 3. 형상 관리 (Git) 및 제외 대상 (.gitignore)
- `dataset/`, `models/`, `weights/`, `*.pt`, `*.pth` 등 대용량 파일은 원격에 푸시하지 않습니다.
- `.local/` (기기 식별자)는 Git 추적 대상에서 제외하여 기기 고유성을 유지합니다.

## 4. Antigravity AI 협업 프로토콜
- AI가 `KH_AI` 코드 오류를 해결할 때, `Obsidian`의 수업 정리/개념 노트를 RAG로 참조하여 코딩을 수행할 수 있습니다.
- 단, 파일 물리적 위치는 항상 "코드 = `KH_AI`", "지식 = `Obsidian`" 으로 이원화 상태를 유지합니다.

# KDT Vision AI — Linux & Dataset Ops Toolkit (`visionops`)

> KDT AI Campus [비솔] 현장 데이터 기반 Vision AI & 산업분야 Vertical AI 융합 전문가 양성 과정  
> 교과 1 · 리눅스 (60H) 핵심 산출물 및 자동화 툴킷

[![CI](https://github.com/incarnation44/visionops/actions/workflows/ci.yml/badge.svg)](actions)

---

## 1. 개요 (Overview)

`visionops`는 Vision AI 프로젝트(교과 8 조각김치 이물검출, 교과 14 컨베이어 제조검사, 교과 15 모션인식)에서 대용량 데이터셋 준비, 품질 검수, 무손실 분할, 통계 산출, 메타 백업을 자동화하는 CLI 툴킷입니다.

---

## 2. 주요 기능 (Key Features)

| 명령어 | 기능 설명 |
| :--- | :--- |
| `init <name>` | YOLO 표준 디렉토리 계층(`raw/`, `images/`, `labels/`, `meta/`) 및 메타 문서 생성 |
| `check <dir>` | 이미지-라벨 짝 검증, 포맷 검사, 좌표 범위(0~1), 클래스 불균형 검증 |
| `split <dir>` | 고정 난수 시드(기본: 42) 기반 70:15:15 재현 가능 분할 |
| `report <dir>` | 클래스별 Bounding Box 분포 및 통계 리포트 생성 (`meta/dataset_report.txt`) |
| `backup <dir>` | 메타데이터 자동 아카이브 압축 및 보존 주기(30일) 초과 백업 자동 정리 |
| `run <dir>` | **검증 ➔ 분할 ➔ 리포트 ➔ 백업** 원클릭 통합 파이프라인 |

---

## 3. 요구 환경 및 설치 (Installation)

### 시스템 요구 사항
- OS: Windows 11 (PowerShell / Git Bash) 또는 Ubuntu 22.04 LTS
- CPU: Intel i5-12400 이상 / RAM 16GB 이상 (CPU 최적화 빌드 지원)
- Git: Git for Windows 2.x 이상

### 환경 설정 및 훅 등록
```bash
# 1. 저장소 클론 및 이동
cd C:\Users\user1\.gemini\antigravity\scratch\visionops

# 2. Git 보안 훅 설치 (데이터 유출 방지)
# [Linux / Git Bash]
./hooks/install_hooks.sh
# [PowerShell]
.\hooks\install_hooks.ps1
```

---

## 4. 사용 예시 (Usage Examples)

### ① Bash / Linux / Git Bash 환경
```bash
# 1. 새 데이터셋 구조 생성
./visionops init kimchi --classes 6

# 2. 데이터셋 정합성 검사 (--fix 로 공백/빈라벨 자동 수정)
./visionops check dataset/kimchi --min 500 --fix

# 3. 데이터셋 분할 (70:15:15 고정 시드)
./visionops split dataset/kimchi --ratio 70:15:15 --seed 42 --clean

# 4. 통계 리포트 생성
./visionops report dataset/kimchi

# 5. 전체 파이프라인 실행
./visionops run dataset/kimchi
```

### ② Windows PowerShell 환경
```powershell
# 1. 새 데이터셋 구조 생성
.\visionops.ps1 init kimchi --classes 6

# 2. 데이터셋 정합성 검사
.\visionops.ps1 check dataset\kimchi --min 500 --fix

# 3. 데이터셋 분할
.\visionops.ps1 split dataset\kimchi --ratio 70:15:15 --seed 42 --clean

# 4. 전체 파이프라인 실행
.\visionops.ps1 run dataset\kimchi
```

---

## 5. ⚠️ 데이터 보안 규정 준수 (Security)

- **㈜비솔 제공 데이터(조각김치·이물 이미지 및 라벨)**는 **원내 폐쇄망 전용**이며, GitHub 및 외부 클라우드 업로드가 엄격히 금지됩니다. (안내서 6.2절 · 7장)
- 본 저장소의 `hooks/pre-commit` 및 `.gitignore`는 이미지/영상, 모델 가중치(`.pt`), 자격증명 파일의 커밋을 원천 차단합니다.

---

## 6. 라이선스 (License)

본 프로젝트는 KDT AI Campus 교육 및 실무 프로젝트를 위한 목적으로 제작되었습니다.

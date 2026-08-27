# 🚀 KH_AI — Vision AI & 리눅스 실습 저장소

> **교육 과정**: [비솔] 현장 데이터 기반 Vision AI & 산업분야 Vertical AI 융합 전문가 양성  
> **교육 기관**: KH정보교육원 (강남)  
> **작업 공간**: `D:\KH_AI` (`/mnt/d/KH_AI`)  
> **작성자**: ildo (`incarnation44`)

---

## 📂 카테고리별 디렉토리 구조

```text
D:\KH_AI/
├── 📁 docs/                   # 시스템 사양서 및 환경 문서
│   └── system_spec.md        # 학원 PC (DESKTOP-HHAIR2K) 상세 사양서
├── 📁 OT/                     # 교육원 오리엔테이션 및 행정 규정 문서
│   ├── AI 캠퍼스 - 개강 OT (8).pdf
│   ├── 규정안내문_[비솔]...pdf
│   ├── 260827 [비솔]...pdf
│   └── 개강OT(행정).mp4
├── 📁 리눅스/                  # 교과 1 리눅스 & ROS2 공식 교재
│   ├── 00.html ~ 08.html     # 교과 1 리눅스 60H 정규 교재 (D1~D8)
│   ├── 2일차.pdf              # 로보틱스 센서/액추에이터 & ROS2 교재
│   └── 99.html / index.html  # 치트시트 및 전체 목차
├── 📁 kdt-linux/              # Vision AI 실습 워크스페이스 & 데이터셋
│   ├── dataset/kimchi/       # YOLO 표준 데이터셋 (raw, train, val, test, meta)
│   ├── scripts/              # 데이터셋 검증, 분할, 리포트, 백업 스크립트
│   ├── hooks/                # 보안 감사 및 커밋 컨벤션 Git Hooks
│   ├── visionops             # Vision AI 운영 자동화 CLI 툴킷
│   └── DAY1.md ~ DAY8.md     # 일차별 학습 정리 및 체크포인트
└── ⚙️ sync_github.sh          # 원클릭 GitHub 자동 동기화 (Pull + Commit + Push)
```

---

## 🖥️ 개발 및 실행 환경 요약

* **PC 고유 호스트명**: **`DESKTOP-HHAIR2K`**
* **CPU / RAM**: Intel Core i5-12400 (6C/12T) / 16.0 GB RAM
* **OS / 플랫폼**: Windows 11 Pro + WSL2 (Ubuntu 22.04.5 LTS)
* **로보틱스 미들웨어**: ROS2 Humble Hawksbill (Desktop)
* **상세 사양 문서**: [docs/system_spec.md](docs/system_spec.md)

---

## 🔄 GitHub 자동 동기화 명령어
수업 및 실습 후 아래 명령어 한 줄로 자동 Pull / Commit / Push 동기화:
```bash
./sync_github.sh "커밋 메시지"
```

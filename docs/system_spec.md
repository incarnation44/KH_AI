# 🖥️ KH정보교육원 교육장 PC 시스템 사양서

> **수강 과정**: [비솔] 현장 데이터 기반 Vision AI & 산업분야 Vertical AI 융합 전문가 양성  
> **기록 일시**: 2026-08-27  
> **사용자 계정**: ildo (chunildo44@gmail.com)

---

## 1. 하드웨어 사양 (Hardware Specifications)

| 항목 | 상세 규격 | 비고 |
| :--- | :--- | :--- |
| **PC 고유 호스트명** | **`DESKTOP-HHAIR2K`** | Windows / WSL 네트워크 식별자 |
| **CPU (프로세서)** | **12th Gen Intel(R) Core(TM) i5-12400** | 6 코어 / 12 스레드 (최대 4.40 GHz) |
| **RAM (메모리)** | **16.0 GB** | DDR4/DDR5 (교재 권장 사양 충족) |
| **GPU (그래픽)** | **Intel(R) UHD Graphics 730** | 인텔 12세대 내장 그래픽 |
| **저장장치 (C:)** | **475.9 GB SSD** (가용 공간: **411.3 GB**) | Windows 11 OS 및 핵심 시스템 |
| **저장장치 (D:)** | **931.5 GB (~1TB)** (가용 공간: **931.3 GB**) | **`D:\KH_AI` 전용 실습 & 백업 파티션** |

---

## 2. 운영체제 및 가상화 환경 (OS & Virtualization)

| 구분 | 환경 | 세부 버전 및 정보 |
| :--- | :--- | :--- |
| **호스트 OS** | **Windows 11 Pro** | 빌드 번호: `26200` (64-bit) |
| **가상화 플랫폼** | **WSL 2 (Hyper-V)** | WSL 버전 2 (Linux 커널 6.18) |
| **리눅스 배포판** | **Ubuntu 22.04.5 LTS** | 코드명: `jammy` (장기 지원 정식 버전) |
| **기본 셸 (Shell)** | **GNU Bash 5.1.16** | 프롬프트: `ildo@DESKTOP-HHAIR2K:~$` |

---

## 3. 개발 도구 및 런타임 (Development Tools & Runtime)

| 도구 / 패키지 | 버전 | 역할 및 설치 경로 |
| :--- | :--- | :--- |
| **ROS2** | **Humble Hawksbill (LTS)** | `/opt/ros/humble` (Desktop 풀버전) |
| **ROS 빌드 도구** | **`ros-dev-tools`** | `colcon`, `rosdep`, `vcstool` 등 |
| **Python** | **Python 3.10.12** | `/usr/bin/python3` (리눅스 표준 인터프리터) |
| **코드 에디터** | **Visual Studio Code** | WSL Ubuntu-22.04 원격 확장 연동 |
| **버전 관리** | **Git 2.34.1** | `ildo` (`chunildo44@gmail.com`) / SSH 키 연동 |
| **GUI 창 시스템** | **X11 / WSLg** | `x11-apps`, `gnome-text-editor`, `nautilus` |

---

## 4. 디렉토리 매핑 규격 (Directory Mapping)

* **Windows 탐색기 경로**: `D:\KH_AI\`
* **Linux (WSL) 마운트 경로**: `/mnt/d/KH_AI/`
* **GitHub 원격 저장소**: `git@github.com:incarnation44/KH_AI.git`

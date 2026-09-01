# Day 9 — WSL과 Anaconda를 활용한 Vision AI 환경 구성 (8H)
## 핵심 학습 내용
- Windows 11 환경에서 WSL2 및 Ubuntu 24.04 LTS 설치 및 연동
- 리눅스용 Anaconda 설치 및 `conda init` 환경 변수 초기화
- `conda create -n vision-ai python=3.10` 가상환경 구축
- OpenCV, PyTorch(CPU), Numpy, Pandas 필수 패키지 세팅
- VS Code WSL 원격 접속(`code .`) 및 Python Interpreter 직접 지정(`/home/ildoc/anaconda3/envs/vision-ai/bin/python`)

## 산출물
- `Ildo-Laptop` WSL Ubuntu 24.04 인스턴스
- `vision-ai` Conda 가상환경
- `test.py` (패키지 구동 확인용 검증 스크립트)

# visionops 설계 및 아키텍처 문서 (DESIGN.md)

## 1. 개요 및 목적
`visionops`는 Vision AI 및 산업용 제조/모션 데이터셋 구축 전 과정을 자동화하고, 엄격한 데이터 보안 규정을 준수하기 위한 CLI 운영 툴킷입니다.

## 2. 모듈 구조
```
visionops (Entrypoint)
├── lib/common.sh / common.ps1      : 로깅, 색상, 유틸리티
├── lib/cmd_init.sh / .ps1          : 데이터셋 구조 생성
├── lib/cmd_check.sh / .ps1         : 정합성 및 포맷 검증
├── lib/cmd_split.sh / .ps1         : 70:15:15 시드 고정 분할
├── lib/cmd_report.sh / .ps1        : 통계 및 클래스 분포 리포트
├── lib/cmd_backup.sh / .ps1        : 메타데이터 아카이브 백업
└── lib/cmd_run.sh / .ps1           : 파이프라인 통합 실행
```

## 3. 보안 3중 방어선
1. **`.gitignore`**: 원본/가공 데이터, 미디어, 모델 가중치 배제
2. **`hooks/pre-commit`**: 커밋 시점에 차단 (이미지, 가중치, 자격증명)
3. **`GitHub Actions CI`**: push/PR 시 원격 서버에서 자동 스캔

## 4. 재현성 보장
- `split_seed.txt`에 난수 시드, 비율, 총 수량, 실행 명령어를 영구 기록하여 동일 조건 시 완벽한 재현성을 보장합니다.

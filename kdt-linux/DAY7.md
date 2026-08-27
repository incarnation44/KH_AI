# Day 7 — GitHub 협업과 데이터 보안 (8H)
## 핵심 학습 내용
- SSH 키 (`~/.ssh/id_ed25519`) 및 PAT 기반 GitHub 인증
- GitHub Flow (branch -> push -> PR -> code review -> merge)
- 코드 리뷰 코멘트 접두사 규칙: `[must]`, `[should]`, `[nit]`, `[q]`, `[praise]`
- ㈜비솔 데이터 보안 규정(안내서 6.2절·7장) 준수를 위한 3중 방어선
  - 1차: `.gitignore`
  - 2차: `hooks/pre-commit` (이미지, 모델가중치, 자격증명 차단)
  - 3차: GitHub Actions CI 스캔
- 포트폴리오용 README 작성

## 산출물
- `hooks/pre-commit` 및 `hooks/commit-msg`
- `.github/workflows/ci.yml`
- GitHub 원격 저장소 및 PR/리뷰 이력

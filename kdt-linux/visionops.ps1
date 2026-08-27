# ===============================================================
# visionops.ps1 — Vision AI 데이터셋 운영 툴킷 (PowerShell 버전)
# ===============================================================

$VERSION = "1.0.0"
$SCRIPT_DIR = Split-Path -Parent $MyInvocation.MyCommand.Path
$LIB_DIR = Join-Path $SCRIPT_DIR "lib"

. (Join-Path $LIB_DIR "common.ps1")
. (Join-Path $LIB_DIR "cmd_init.ps1")
. (Join-Path $LIB_DIR "cmd_check.ps1")
. (Join-Path $LIB_DIR "cmd_split.ps1")
. (Join-Path $LIB_DIR "cmd_report.ps1")
. (Join-Path $LIB_DIR "cmd_backup.ps1")
. (Join-Path $LIB_DIR "cmd_run.ps1")

function Show-MainUsage {
    Write-Host @"
visionops v$VERSION — Vision AI 데이터셋 운영 툴킷

사용법:
  .\visionops.ps1 <command> [args] [options]

명령:
  init <name>          표준 YOLO 데이터셋 구조 및 메타 문서 생성
  check <dir>          데이터셋 정합성 및 포맷 검증
  split <dir>          train/val/test 70:15:15 시드 고정 분할
  report <dir>         클래스 분포 및 바운딩 박스 통계 리포트 생성
  backup <dir>         메타데이터 아카이브 백업
  run <dir>            검증 → 분할 → 리포트 → 백업 통합 파이프라인

전역 옵션:
  -h, --help           도움말 출력
  -v, --version        버전 정보 출력

예시:
  .\visionops.ps1 init kimchi --classes 5
  .\visionops.ps1 check dataset\kimchi --min 500
  .\visionops.ps1 split dataset\kimchi --ratio 70:15:15 --seed 42
  .\visionops.ps1 run dataset\kimchi
"@
}

if ($args.Count -eq 0) {
    Show-MainUsage
    exit 2
}

$cmd = $args[0]
$cmdArgs = if ($args.Count -gt 1) { $args[1..($args.Count - 1)] } else { @() }

switch ($cmd) {
    "-h" { Show-MainUsage; exit 0 }
    "--help" { Show-MainUsage; exit 0 }
    "-v" { Write-Host "visionops v$VERSION"; exit 0 }
    "--version" { Write-Host "visionops v$VERSION"; exit 0 }
    "init"   { Invoke-CmdInit -Arguments $cmdArgs }
    "check"  { Invoke-CmdCheck -Arguments $cmdArgs }
    "split"  { Invoke-CmdSplit -Arguments $cmdArgs }
    "report" { Invoke-CmdReport -Arguments $cmdArgs }
    "backup" { Invoke-CmdBackup -Arguments $cmdArgs }
    "run"    { Invoke-CmdRun -Arguments $cmdArgs }
    default  {
        Write-Host "알 수 없는 명령: $cmd" -ForegroundColor Red
        Show-MainUsage
        exit 2
    }
}

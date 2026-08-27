# ===============================================================
# hooks/install_hooks.ps1 — Git 훅 자동 설치 스크립트 (PowerShell)
# ===============================================================

$hookSrc = Split-Path -Parent $MyInvocation.MyCommand.Path
$gitDir = ".git"
$hookDst = Join-Path $gitDir "hooks"

if (!(Test-Path $hookDst)) {
    New-Item -ItemType Directory -Path $hookDst -Force | Out-Null
}

foreach ($h in @("pre-commit", "commit-msg")) {
    $srcPath = Join-Path $hookSrc $h
    if (Test-Path $srcPath) {
        $dstPath = Join-Path $hookDst $h
        Copy-Item -Path $srcPath -Destination $dstPath -Force
        Write-Host "[OK] $h 훅이 설치되었습니다." -ForegroundColor Green
    }
}

Write-Host "전체 Git 훅 설치 완료 ($hookDst)" -ForegroundColor Cyan

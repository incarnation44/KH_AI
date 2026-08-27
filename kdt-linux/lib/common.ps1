# ===============================================================
# lib/common.ps1 — visionops 공통 라이브러리 (PowerShell 버전)
# ===============================================================

$script:LOG_DIR = if ($env:LOG_DIR) { $env:LOG_DIR } else { ".\logs" }
$script:QUIET = if ($env:QUIET -eq "1") { 1 } else { 0 }

function Get-TimeStamp {
    return (Get-Date -Format "yyyy-MM-dd HH:mm:ss")
}

function Write-OpsLog {
    param([string]$Message)
    if (!(Test-Path $script:LOG_DIR)) {
        New-Item -ItemType Directory -Path $script:LOG_DIR -Force | Out-Null
    }
    $entry = "[$([Get-TimeStamp])] $Message"
    Add-Content -Path (Join-Path $script:LOG_DIR "visionops.log") -Value $entry
}

function Log-Info {
    param([string]$Message)
    if ($script:QUIET -ne 1) { Write-Host "  $Message" }
    Write-OpsLog "INFO  $Message"
}

function Log-Ok {
    param([string]$Message)
    if ($script:QUIET -ne 1) {
        Write-Host "  [OK]   $Message" -ForegroundColor Green
    }
    Write-OpsLog "OK    $Message"
}

function Log-Warn {
    param([string]$Message)
    Write-Host "  [WARN] $Message" -ForegroundColor Yellow
    Write-OpsLog "WARN  $Message"
}

function Log-Fail {
    param([string]$Message)
    Write-Host "  [FAIL] $Message" -ForegroundColor Red
    Write-OpsLog "FAIL  $Message"
}

function Die {
    param([string]$Message)
    Log-Fail $Message
    exit 1
}

function Log-Section {
    param([int]$Step, [string]$Title)
    if ($script:QUIET -ne 1) {
        Write-Host ""
        Write-Host "[$Step] $Title" -ForegroundColor Cyan
    }
}

function Log-Banner {
    param([string]$Title)
    if ($script:QUIET -ne 1) {
        Write-Host "==============================================" -ForegroundColor DarkCyan
        Write-Host "  $Title"
        Write-Host "  $(Get-TimeStamp)"
        Write-Host "==============================================" -ForegroundColor DarkCyan
    }
}

function Require-Directory {
    param([string]$Path)
    if (!(Test-Path -Path $Path -PathType Container)) {
        Die "디렉토리 없음: $Path"
    }
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location "$scriptDir\.."

$pass = 0
$fail = 0

function Test-Check {
    param([string]$Name, [scriptblock]$Action)
    try {
        & $Action | Out-Null
        Write-Host "  [PASS] $Name" -ForegroundColor Green
        $script:pass++
    } catch {
        Write-Host "  [FAIL] $Name ($_)" -ForegroundColor Red
        $script:fail++
    }
}

Write-Host "==============================================" -ForegroundColor Cyan
Write-Host " visionops Test Suite (PowerShell)" -ForegroundColor Cyan
Write-Host "==============================================" -ForegroundColor Cyan

Test-Check "1. --help flag" { & powershell -ExecutionPolicy Bypass -File .\visionops.ps1 --help }
Test-Check "2. --version flag" { & powershell -ExecutionPolicy Bypass -File .\visionops.ps1 --version }

$testDir = ".\dataset\_test_ps_unit"
if (Test-Path $testDir) { Remove-Item $testDir -Recurse -Force }

Test-Check "3. visionops init" { & powershell -ExecutionPolicy Bypass -File .\visionops.ps1 init _test_ps_unit --classes 3 }

$testImg = Join-Path $testDir "raw\images"
$testLbl = Join-Path $testDir "raw\labels"
New-Item -ItemType Directory -Path $testImg, $testLbl -Force | Out-Null
1..5 | ForEach-Object {
    $n = $_.ToString("D2")
    $b = [byte[]](0xFF, 0xD8, 0xFF, 0xE0)
    [System.IO.File]::WriteAllBytes((Join-Path $testImg "sample_${n}.jpg"), $b)
    "0 0.5 0.5 0.2 0.2" | Set-Content (Join-Path $testLbl "sample_${n}.txt")
}

Test-Check "4. visionops check" { & powershell -ExecutionPolicy Bypass -File .\visionops.ps1 check $testDir --min 5 }
Test-Check "5. visionops split" { & powershell -ExecutionPolicy Bypass -File .\visionops.ps1 split $testDir --ratio 60:20:20 --seed 42 --clean }
Test-Check "6. visionops report" { & powershell -ExecutionPolicy Bypass -File .\visionops.ps1 report $testDir }
Test-Check "7. visionops backup" { & powershell -ExecutionPolicy Bypass -File .\visionops.ps1 backup $testDir }

if (Test-Path $testDir) { Remove-Item $testDir -Recurse -Force }

Write-Host "----------------------------------------------"
Write-Host "  Result: Pass $pass / Fail $fail"
Write-Host "=============================================="

if ($fail -ne 0) { exit 1 } else { exit 0 }

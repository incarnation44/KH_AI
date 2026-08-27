# ===============================================================
# lib/cmd_split.ps1 — visionops split 서브커맨드 (PowerShell)
# ===============================================================

function Show-SplitUsage {
    Write-Host @"
사용법: visionops split <dataset_dir> [옵션]

인자:
  dataset_dir       분할할 데이터셋 루트 디렉토리

옵션:
  --ratio <T:V:S>   분할 비율 (기본: 70:15:15)
  --seed <N>        난수 고정 시드 (기본: 42)
  --copy            파일 복사 모드 (Windows 기본 권장)
  --clean           기존 분할 디렉토리 초기화 후 재분할
  -h, --help        도움말
"@
}

function Invoke-CmdSplit {
    param([string[]]$Arguments)

    if ($Arguments.Count -eq 0) {
        Show-SplitUsage
        exit 2
    }

    $ds = $Arguments[0]
    $trainR = 70; $valR = 15; $testR = 15
    $seed = 42
    $mode = "copy"
    $clean = $false
    $i = 1

    while ($i -lt $Arguments.Count) {
        switch ($Arguments[$i]) {
            "--ratio" {
                $parts = $Arguments[++$i] -split ':'
                $trainR = [int]$parts[0]
                $valR = [int]$parts[1]
                $testR = [int]$parts[2]
            }
            "--seed" { $seed = [int]$Arguments[++$i] }
            "--copy" { $mode = "copy" }
            "--clean" { $clean = $true }
            "-h" { Show-SplitUsage; exit 0 }
            "--help" { Show-SplitUsage; exit 0 }
            default { Die "알 수 없는 옵션: $($Arguments[$i])" }
        }
        $i++
    }

    if (!(Test-Path $ds -PathType Container)) {
        Die "경로 없음: $ds"
    }

    $rawImg = Join-Path $ds "raw\images"
    $rawLbl = Join-Path $ds "raw\labels"
    if (!(Test-Path $rawImg)) {
        $rawImg = Join-Path $ds "raw"
        $rawLbl = Join-Path $ds "raw"
    }

    $sum = $trainR + $valR + $testR
    if ($sum -ne 100) { Die "분할 비율 합이 100이 아닙니다 (입력: $sum)" }

    Log-Banner "visionops split :: $(Split-Path $ds -Leaf)"

    if ($clean) {
        Log-Info "기존 분할 디렉토리 정리 중..."
        Remove-Item -Path "$ds\images\train", "$ds\images\val", "$ds\images\test", "$ds\labels\train", "$ds\labels\val", "$ds\labels\test" -Recurse -Force -ErrorAction SilentlyContinue
    }

    $imgFiles = Get-ChildItem -Path $rawImg -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -match '^\.(jpg|jpeg|png)$' }
    $validPairs = @()

    foreach ($img in $imgFiles) {
        $lblPath = Join-Path $rawLbl "$($img.BaseName).txt"
        if ((Test-Path $lblPath) -and ((Get-Item $lblPath).Length -gt 0)) {
            $validPairs += $img
        }
    }

    $total = $validPairs.Count
    Log-Info "유효 샘플 쌍(이미지+라벨 모두 존재): ${total}개"
    if ($total -eq 0) { Die "분할할 유효 데이터가 없습니다." }

    # 고정 시드 기반 결정론적 셔플
    $rand = [System.Random]::new($seed)
    $shuffled = $validPairs | Sort-Object { $rand.NextDouble() }

    $nTrain = [int]($total * $trainR / 100)
    $nVal = [int]($total * $valR / 100)
    $nTest = $total - $nTrain - $nVal

    Log-Info "분할 계획: Train=$nTrain / Val=$nVal / Test=$nTest (시드=$seed, 모드=$mode)"

    $splits = @{
        "train" = $shuffled[0..($nTrain - 1)]
        "val"   = if ($nVal -gt 0) { $shuffled[$nTrain..($nTrain + $nVal - 1)] } else { @() }
        "test"  = if ($nTest -gt 0) { $shuffled[($nTrain + $nVal)..($total - 1)] } else { @() }
    }

    foreach ($sName in @("train", "val", "test")) {
        $targetImgDir = Join-Path $ds "images\$sName"
        $targetLblDir = Join-Path $ds "labels\$sName"
        New-Item -ItemType Directory -Path $targetImgDir, $targetLblDir -Force | Out-Null

        foreach ($item in $splits[$sName]) {
            if ($null -eq $item) { continue }
            Copy-Item -Path $item.FullName -Destination $targetImgDir -Force
            $srcLbl = Join-Path $rawLbl "$($item.BaseName).txt"
            if (Test-Path $srcLbl) {
                Copy-Item -Path $srcLbl -Destination $targetLblDir -Force
            }
        }
    }

    # split_seed.txt 기록
    $metaDir = Join-Path $ds "meta"
    New-Item -ItemType Directory -Path $metaDir -Force | Out-Null
    $seedFile = Join-Path $metaDir "split_seed.txt"
    $seedInfo = @"
seed=$seed
ratio=${trainR}:${valR}:${testR}
mode=$mode
total=$total
train=$nTrain
val=$nVal
test=$nTest
generated=$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')
command=visionops split $ds --ratio ${trainR}:${valR}:${testR} --seed $seed
"@
    Set-Content -Path $seedFile -Value $seedInfo

    Write-Host ""
    Write-Host "=============================================="
    Write-Host ("  {0,-8} {1,10} {2,10}" -f "SPLIT", "IMAGES", "LABELS")
    Write-Host ("  {0,-8} {1,10} {2,10}" -f "-------", "------", "------")
    foreach ($s in @("train", "val", "test")) {
        $ic = (Get-ChildItem -Path "$ds\images\$s" -File -ErrorAction SilentlyContinue).Count
        $lc = (Get-ChildItem -Path "$ds\labels\$s" -File -ErrorAction SilentlyContinue).Count
        Write-Host ("  {0,-8} {1,10} {2,10}" -f $s, $ic, $lc)
    }
    Write-Host "  --------------------------------------------"
    Log-Ok "분할 완료 및 시드 기록 ($seedFile)"
    Write-Host "=============================================="
    return 0
}

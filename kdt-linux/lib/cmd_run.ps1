# ===============================================================
# lib/cmd_run.ps1 — visionops run 서브커맨드 (PowerShell)
# ===============================================================

function Show-RunUsage {
    Write-Host @"
사용법: visionops run <dataset_dir> [옵션]

인자:
  dataset_dir       파이프라인을 실행할 데이터셋 루트 디렉토리

옵션:
  --min <N>         최소 요구 이미지 장수 (기본: 500)
  --ratio <T:V:S>   분할 비율 (기본: 70:15:15)
  --seed <N>        분할 시드 (기본: 42)
  --fix             검증 단계에서 단순 문제 자동 수정
  -h, --help        도움말
"@
}

function Invoke-CmdRun {
    param([string[]]$Arguments)

    if ($Arguments.Count -eq 0) {
        Show-RunUsage
        exit 2
    }

    $ds = $Arguments[0]
    $minImages = 500
    $ratio = "70:15:15"
    $seed = 42
    $fixArgs = @()
    $i = 1

    while ($i -lt $Arguments.Count) {
        switch ($Arguments[$i]) {
            "--min" { $minImages = [int]$Arguments[++$i] }
            "--ratio" { $ratio = $Arguments[++$i] }
            "--seed" { $seed = [int]$Arguments[++$i] }
            "--fix" { $fixArgs = @("--fix") }
            "-h" { Show-RunUsage; exit 0 }
            "--help" { Show-RunUsage; exit 0 }
            default { Die "알 수 없는 옵션: $($Arguments[$i])" }
        }
        $i++
    }

    if (!(Test-Path $ds -PathType Container)) {
        Die "경로 없음: $ds"
    }

    $stopwatch = [System.Diagnostics.Stopwatch]::StartNew()
    Log-Banner "visionops run :: 통합 파이프라인 ($(Split-Path $ds -Leaf))"

    # 1. 검증
    Log-Section 1 "파이프라인 1단계: 정합성 검증"
    $checkArgs = @($ds, "--min", "$minImages") + $fixArgs
    $checkRes = Invoke-CmdCheck -Arguments $checkArgs
    if ($checkRes -ne 0) {
        Die "검증 단계 실패로 파이프라인이 중단되었습니다."
    }

    # 2. 분할
    Log-Section 2 "파이프라인 2단계: 데이터셋 분할 (70:15:15)"
    $splitArgs = @($ds, "--ratio", $ratio, "--seed", "$seed", "--clean")
    Invoke-CmdSplit -Arguments $splitArgs | Out-Null

    # 3. 리포트
    Log-Section 3 "파이프라인 3단계: 통계 리포트 생성"
    Invoke-CmdReport -Arguments @($ds) | Out-Null

    # 4. 백업
    Log-Section 4 "파이프라인 4단계: 메타데이터 아카이브 백업"
    Invoke-CmdBackup -Arguments @($ds) | Out-Null

    $stopwatch.Stop()
    $sec = [math]::Round($stopwatch.Elapsed.TotalSeconds, 2)

    Write-Host ""
    Write-Host "══════════════════════════════════════════════" -ForegroundColor Green
    Write-Host "  ✔ 파이프라인 전체 완료! (소요 시간: ${sec}초)" -ForegroundColor Green
    Write-Host "══════════════════════════════════════════════" -ForegroundColor Green
    return 0
}

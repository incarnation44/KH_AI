# ===============================================================
# lib/cmd_check.ps1 — visionops check 서브커맨드 (PowerShell)
# ===============================================================

function Show-CheckUsage {
    Write-Host @"
사용법: visionops check <dataset_dir> [옵션]

인자:
  dataset_dir       검사할 데이터셋 루트 디렉토리

옵션:
  --fix             발견된 단순 문제(빈 라벨 파일 삭제, 공백 파일명 변경) 자동 수정
  --min <N>         최소 요구 이미지 장수 (기본: 500)
  --balance-ratio <R> 클래스 최대/최소 비율 허용치 (기본: 5)
  -h, --help        도움말
"@
}

function Invoke-CmdCheck {
    param([string[]]$Arguments)

    if ($Arguments.Count -eq 0) {
        Show-CheckUsage
        exit 2
    }

    $dsDir = $Arguments[0]
    $minImages = 500
    $balanceRatio = 5.0
    $doFix = $false
    $errors = 0
    $warnings = 0
    $i = 1

    while ($i -lt $Arguments.Count) {
        switch ($Arguments[$i]) {
            "--fix" { $doFix = $true }
            "--min" { $minImages = [int]$Arguments[++$i] }
            "--balance-ratio" { $balanceRatio = [double]$Arguments[++$i] }
            "-h" { Show-CheckUsage; exit 0 }
            "--help" { Show-CheckUsage; exit 0 }
            default { Die "알 수 없는 옵션: $($Arguments[$i])" }
        }
        $i++
    }

    if (!(Test-Path $dsDir -PathType Container)) {
        Die "데이터셋 디렉토리가 존재하지 않습니다: $dsDir"
    }

    Log-Banner "visionops check :: $(Split-Path $dsDir -Leaf)"

    # [1] 구조 검증
    Log-Section 1 "디렉토리 구조 검증"
    $rawDir = Join-Path $dsDir "raw"
    $imgRaw = Join-Path $dsDir "raw\images"
    $lblRaw = Join-Path $dsDir "raw\labels"

    if (!(Test-Path $imgRaw) -and (Test-Path $rawDir)) {
        $imgRaw = $rawDir
        $lblRaw = $rawDir
    }

    if (Test-Path $rawDir) {
        Log-Ok "raw/ 디렉토리 존재"
    } else {
        Log-Fail "raw/ 디렉토리 누락"; $errors++
    }

    $classesFile = Join-Path $dsDir "meta\classes.txt"
    $numClasses = 0
    if (Test-Path $classesFile) {
        $lines = Get-Content $classesFile | Where-Object { $_.Trim().Length -gt 0 }
        $numClasses = $lines.Count
        Log-Ok "meta\classes.txt 존재 (${numClasses}종 정의됨)"
    } else {
        Log-Warn "meta\classes.txt 없음"; $warnings++
    }

    # [2] 이미지-라벨 짝 검증
    Log-Section 2 "이미지-라벨 짝(Pairing) 검증"
    $imgFiles = Get-ChildItem -Path $imgRaw -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -match '^\.(jpg|jpeg|png)$' }
    $lblFiles = Get-ChildItem -Path $lblRaw -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -eq '.txt' }
    $imgCount = $imgFiles.Count
    $lblCount = $lblFiles.Count

    Log-Info "발견: 이미지 ${imgCount}장 / 라벨 ${lblCount}개"

    $imgBases = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $lblBases = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)

    foreach ($f in $imgFiles) { [void]$imgBases.Add($f.BaseName) }
    foreach ($f in $lblFiles) { [void]$lblBases.Add($f.BaseName) }

    $noLbl = ($imgBases | Where-Object { -not $lblBases.Contains($_) }).Count
    $noImg = ($lblBases | Where-Object { -not $imgBases.Contains($_) }).Count

    if ($noLbl -eq 0) {
        Log-Ok "라벨 누락 이미지 없음"
    } else {
        Log-Warn "라벨 없는 이미지 ${noLbl}건 발견 (배경 학습 유의)"; $warnings++
    }

    if ($noImg -eq 0) {
        Log-Ok "이미지 누락 라벨 없음"
    } else {
        Log-Fail "이미지 없는 고아 라벨 ${noImg}건 발견"; $errors++
    }

    # [3] 라벨 포맷 검증
    Log-Section 3 "라벨 포맷 및 데이터 정합성 검증"
    $emptyCount = 0
    $badNfCount = 0
    $badRangeCount = 0
    $badClsCount = 0
    $classCounts = @{}

    foreach ($lf in $lblFiles) {
        if ($lf.Length -eq 0) {
            $emptyCount++
            if ($doFix) { Remove-Item $lf.FullName -Force }
            continue
        }

        $lines = Get-Content $lf.FullName
        foreach ($line in $lines) {
            $trimmed = $line.Trim()
            if ($trimmed.Length -eq 0) { continue }
            $parts = $trimmed -split '\s+'
            if ($parts.Count -ne 5) {
                $badNfCount++
                continue
            }

            $cid = 0
            if ([int]::TryParse($parts[0], [ref]$cid)) {
                if ($numClasses -gt 0 -and ($cid -lt 0 -or $cid -ge $numClasses)) {
                    $badClsCount++
                }
                if ($classCounts.ContainsKey($cid)) { $classCounts[$cid]++ } else { $classCounts[$cid] = 1 }
            } else {
                $badClsCount++
            }

            for ($idx = 1; $idx -le 4; $idx++) {
                $val = 0.0
                if ([double]::TryParse($parts[$idx], [ref]$val)) {
                    if ($val -lt 0.0 -or $val -gt 1.0) {
                        $badRangeCount++
                        break
                    }
                } else {
                    $badRangeCount++
                    break
                }
            }
        }
    }

    if ($emptyCount -eq 0) { Log-Ok "빈 라벨 파일 없음" }
    else {
        Log-Warn "빈 라벨 파일 ${emptyCount}건 발견"
        if ($doFix) { Log-Info "     → [--fix] 빈 라벨 파일 삭제 완료" }
        $warnings++
    }

    if ($badNfCount -eq 0) { Log-Ok "YOLO 필드 개수 (5개) 정상" }
    else { Log-Fail "필드 개수 오류 ${badNfCount}건 발견"; $errors++ }

    if ($badRangeCount -eq 0) { Log-Ok "바운딩 박스 좌표 정규화 범위 (0.0 ~ 1.0) 정상" }
    else { Log-Fail "좌표 범위 초과 ${badRangeCount}건 발견"; $errors++ }

    if ($numClasses -gt 0) {
        if ($badClsCount -eq 0) { Log-Ok "클래스 ID 범위 (0 ~ $($numClasses-1)) 정상" }
        else { Log-Fail "미정의 클래스 ID 사용 ${badClsCount}건 발견"; $errors++ }
    }

    # [4] 파일명 공백 검사
    Log-Section 4 "파일명 규칙 검증"
    $allFiles = (Get-ChildItem -Path $imgRaw, $lblRaw -File -ErrorAction SilentlyContinue)
    $spaced = $allFiles | Where-Object { $_.Name -match '\s' }
    if ($spaced.Count -eq 0) {
        Log-Ok "공백 포함 비표준 파일명 없음"
    } else {
        Log-Warn "공백 포함 파일명 $($spaced.Count)건 발견"; $warnings++
        if ($doFix) {
            foreach ($sf in $spaced) {
                $newName = $sf.Name -replace '\s+', '_'
                Rename-Item -Path $sf.FullName -NewName $newName -Force
            }
            Log-Info "     → [--fix] 파일명 공백 치환 완료"
        }
    }

    # [5] 데이터 규모 검사
    Log-Section 5 "데이터 규모 요건 검증"
    Log-Info "요구 요건: 최소 ${minImages}장"
    if ($imgCount -ge $minImages) {
        Log-Ok "데이터 규모 충족 (${imgCount}장 >= ${minImages}장)"
    } else {
        Log-Fail "데이터 규모 미달 (${imgCount}장 / 최소 요구 ${minImages}장)"; $errors++
    }

    # [6] 클래스 불균형 검사
    Log-Section 6 "클래스 불균형 검증"
    if ($classCounts.Keys.Count -gt 0) {
        $cVals = $classCounts.Values | Measure-Object -Minimum -Maximum
        $minVal = $cVals.Minimum
        $maxVal = $cVals.Maximum
        if ($minVal -gt 0) {
            $rat = [math]::Round(($maxVal / $minVal), 1)
            Log-Info "최다/최소 클래스 비율: ${rat}:1 (최대 $maxVal, 최소 $minVal)"
            if ($rat -gt $balanceRatio) {
                Log-Warn "클래스 불균형 감지 (${rat}:1 > ${balanceRatio}:1) — 데이터 증강 권장"; $warnings++
            } else {
                Log-Ok "클래스 분포 균형 양호"
            }
        }
    }

    # [7] 종합 판정
    Write-Host ""
    Write-Host "=============================================="
    Write-Host "  결과 요약: 오류 $errors 건 / 경고 $warnings 건"
    if ($errors -eq 0) {
        Write-Host "  최종 판정: PASS ✔" -ForegroundColor Green
        Write-Host "=============================================="
        return 0
    } else {
        Write-Host "  최종 판정: FAIL ✘" -ForegroundColor Red
        Write-Host "=============================================="
        return 1
    }
}

# ===============================================================
# lib/cmd_report.ps1 — visionops report 서브커맨드 (PowerShell)
# ===============================================================

function Show-ReportUsage {
    Write-Host @"
사용법: visionops report <dataset_dir> [옵션]

인자:
  dataset_dir       통계를 산출할 데이터셋 루트 디렉토리

옵션:
  -o, --output <f>  리포트 저장 경로 (기본: <dataset_dir>\meta\dataset_report.txt)
  -h, --help        도움말
"@
}

function Invoke-CmdReport {
    param([string[]]$Arguments)

    if ($Arguments.Count -eq 0) {
        Show-ReportUsage
        exit 2
    }

    $ds = $Arguments[0]
    $out = ""
    $i = 1

    while ($i -lt $Arguments.Count) {
        switch ($Arguments[$i]) {
            "-o" { $out = $Arguments[++$i] }
            "--output" { $out = $Arguments[++$i] }
            "-h" { Show-ReportUsage; exit 0 }
            "--help" { Show-ReportUsage; exit 0 }
            default { Die "알 수 없는 옵션: $($Arguments[$i])" }
        }
        $i++
    }

    if (!(Test-Path $ds -PathType Container)) {
        Die "경로 없음: $ds"
    }

    if ([string]::IsNullOrWhiteSpace($out)) {
        $out = Join-Path $ds "meta\dataset_report.txt"
    }

    Log-Banner "visionops report :: $(Split-Path $ds -Leaf)"

    $rawImg = Join-Path $ds "raw\images"
    $rawLbl = Join-Path $ds "raw\labels"
    if (!(Test-Path $rawImg)) {
        $rawImg = Join-Path $ds "raw"
        $rawLbl = Join-Path $ds "raw"
    }

    $imgFiles = Get-ChildItem -Path $rawImg -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -match '^\.(jpg|jpeg|png)$' }
    $lblFiles = Get-ChildItem -Path $rawLbl -File -ErrorAction SilentlyContinue | Where-Object { $_.Extension -eq '.txt' }

    $totalImg = $imgFiles.Count
    $totalLbl = $lblFiles.Count
    $totalBox = 0
    $classCounts = @{}

    $classesFile = Join-Path $ds "meta\classes.txt"
    $classNames = @{}
    if (Test-Path $classesFile) {
        Get-Content $classesFile | ForEach-Object {
            $t = $_.Trim()
            if ($t.Length -gt 0) {
                $p = $t -split '\s+', 2
                $classNames[[int]$p[0]] = $p[1]
                $classCounts[[int]$p[0]] = 0
            }
        }
    }

    foreach ($lf in $lblFiles) {
        $lines = Get-Content $lf.FullName -ErrorAction SilentlyContinue
        foreach ($line in $lines) {
            $t = $line.Trim()
            if ($t.Length -eq 0) { continue }
            $p = $t -split '\s+'
            if ($p.Count -eq 5) {
                $totalBox++
                $cid = 0
                if ([int]::TryParse($p[0], [ref]$cid)) {
                    if ($classCounts.ContainsKey($cid)) { $classCounts[$cid]++ } else { $classCounts[$cid] = 1 }
                }
            }
        }
    }

    $avg = if ($totalImg -gt 0) { [math]::Round(($totalBox / $totalImg), 2) } else { 0 }

    $reportLines = @()
    $reportLines += "=============================================="
    $reportLines += "  Vision AI Dataset Report :: $(Split-Path $ds -Leaf)"
    $reportLines += "  일시: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
    $reportLines += "=============================================="
    $reportLines += ""
    $reportLines += ("  {0,-20} {1,10} 장" -f "총 이미지 수:", $totalImg)
    $reportLines += ("  {0,-20} {1,10} 개" -f "총 라벨 파일 수:", $totalLbl)
    $reportLines += ("  {0,-20} {1,10} 개" -f "총 바운딩 박스:", $totalBox)
    $reportLines += ("  {0,-20} {1,10} 개/장" -f "이미지당 평균 객체:", $avg)
    $reportLines += ""
    $reportLines += "  [클래스별 Bounding Box 분포]"
    $reportLines += ("  {0,-6} {1,-24} {2,8}" -f "ID", "CLASS NAME", "COUNT")
    $reportLines += ("  {0,-6} {1,-24} {2,8}" -f "----", "------------------------", "--------")

    foreach ($cid in ($classCounts.Keys | Sort-Object)) {
        $cname = if ($classNames.ContainsKey($cid)) { $classNames[$cid] } else { "class_$cid" }
        $reportLines += ("  {0,-6} {1,-24} {2,8}" -f $cid, $cname, $classCounts[$cid])
    }
    $reportLines += "=============================================="

    $outDir = Split-Path $out -Parent
    if (!(Test-Path $outDir)) { New-Item -ItemType Directory -Path $outDir -Force | Out-Null }
    Set-Content -Path $out -Value $reportLines

    foreach ($l in $reportLines) { Write-Host $l }
    Log-Ok "리포트가 생성되어 저장되었습니다 ($out)"
    return 0
}

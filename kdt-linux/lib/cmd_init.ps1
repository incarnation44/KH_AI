# ===============================================================
# lib/cmd_init.ps1 — visionops init 서브커맨드 (PowerShell)
# ===============================================================

function Show-InitUsage {
    Write-Host @"
사용법: visionops init <name> [옵션]

인자:
  name              데이터셋 이름 (예: kimchi, conveyor)

옵션:
  --root <path>     데이터셋 생성 상위 디렉토리 (기본: .\dataset)
  --classes <n>     초기 클래스 수 (기본: 5)
  -h, --help        도움말
"@
}

function Invoke-CmdInit {
    param([string[]]$Arguments)

    if ($Arguments.Count -eq 0) {
        Show-InitUsage
        exit 2
    }

    $name = $Arguments[0]
    $root = ".\dataset"
    $ncls = 5
    $i = 1

    while ($i -lt $Arguments.Count) {
        switch ($Arguments[$i]) {
            "--root" { $root = $Arguments[++$i] }
            "--classes" { $ncls = [int]$Arguments[++$i] }
            "-h" { Show-InitUsage; exit 0 }
            "--help" { Show-InitUsage; exit 0 }
            default { Die "알 수 없는 옵션: $($Arguments[$i])" }
        }
        $i++
    }

    $ds = Join-Path $root $name
    Log-Banner "visionops init :: $name"

    if (Test-Path $ds) {
        Die "데이터셋 디렉토리가 이미 존재합니다: $ds"
    }

    Log-Section 1 "표준 디렉토리 계층 생성"
    $dirs = @(
        "$ds\raw\images", "$ds\raw\labels",
        "$ds\images\train", "$ds\images\val", "$ds\images\test",
        "$ds\labels\train", "$ds\labels\val", "$ds\labels\test",
        "$ds\processed", "$ds\meta", "$ds\backup"
    )
    foreach ($d in $dirs) {
        New-Item -ItemType Directory -Path $d -Force | Out-Null
    }
    Log-Ok "표준 디렉토리 생성 완료 ($ds)"

    Log-Section 2 "메타데이터 및 클래스 정의서 생성"
    $classesFile = Join-Path $ds "meta\classes.txt"
    $classesContent = @()
    for ($c = 0; $c -lt $ncls; $c++) {
        $classesContent += "$c class_$c"
    }
    Set-Content -Path $classesFile -Value $classesContent
    Log-Ok "meta\classes.txt 생성 (${ncls}종)"

    $yamlFile = Join-Path $ds "meta\data.yaml"
    $yamlContent = @"
# Vision AI YOLO Dataset Config
path: $(Resolve-Path $ds)
train: images/train
val: images/val
test: images/test

nc: $ncls
names:
"@
    for ($c = 0; $c -lt $ncls; $c++) {
        $yamlContent += "`n  $c: class_$c"
    }
    Set-Content -Path $yamlFile -Value $yamlContent
    Log-Ok "meta\data.yaml 생성"

    $docFile = Join-Path $ds "meta\DATASET.md"
    $docContent = @"
# $name Dataset

## 개요
| 항목 | 내용 |
|---|---|
| 데이터셋명 | $name |
| 생성일자 | $(Get-Date -Format 'yyyy-MM-dd') |
| 클래스 수 | $ncls |
| 라벨 포맷 | YOLO (class x_center y_center width height, 0~1 정규화) |
| 분할 비율 | train : val : test = 70 : 15 : 15 |

## 보안 및 사용 제한 ⚠️
- ㈜비솔 제공 데이터는 **원내 폐쇄망 전용**이며 GitHub 및 외부 클라우드 업로드가 금지됩니다.
- 원본 raw/ 디렉토리는 읽기 전용으로 관리하십시오.
"@
    Set-Content -Path $docFile -Value $docContent
    Log-Ok "meta\DATASET.md 생성"

    Log-Section 3 "초기화 완료 안내"
    Log-Info "생성 위치: $ds"
    Log-Info "다음 단계: $ds\raw\images 및 $ds\raw\labels 에 원본 데이터를 배치한 후"
    Log-Info "           visionops check $ds 를 실행하여 검증하십시오."
    return 0
}

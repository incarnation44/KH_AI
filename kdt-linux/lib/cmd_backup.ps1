# ===============================================================
# lib/cmd_backup.ps1 — visionops backup 서브커맨드 (PowerShell)
# ===============================================================

function Show-BackupUsage {
    Write-Host @"
사용법: visionops backup <dataset_dir> [옵션]

인자:
  dataset_dir       백업할 데이터셋 루트 디렉토리

옵션:
  --keep-days <N>   백업 파일 보존 일수 (기본: 30일)
  -h, --help        도움말
"@
}

function Invoke-CmdBackup {
    param([string[]]$Arguments)

    if ($Arguments.Count -eq 0) {
        Show-BackupUsage
        exit 2
    }

    $ds = $Arguments[0]
    $keepDays = 30
    $i = 1

    while ($i -lt $Arguments.Count) {
        switch ($Arguments[$i]) {
            "--keep-days" { $keepDays = [int]$Arguments[++$i] }
            "-h" { Show-BackupUsage; exit 0 }
            "--help" { Show-BackupUsage; exit 0 }
            default { Die "알 수 없는 옵션: $($Arguments[$i])" }
        }
        $i++
    }

    if (!(Test-Path $ds -PathType Container)) {
        Die "경로 없음: $ds"
    }

    Log-Banner "visionops backup :: $(Split-Path $ds -Leaf)"

    $name = Split-Path $ds -Leaf
    $stamp = Get-Date -Format 'yyyyMMdd_HHmmss'
    $backupDir = Join-Path $ds "backup"
    New-Item -ItemType Directory -Path $backupDir -Force | Out-Null
    $outFile = Join-Path $backupDir "${name}_meta_${stamp}.zip"

    $metaDir = Join-Path $ds "meta"
    if (Test-Path $metaDir) {
        Compress-Archive -Path "$metaDir\*" -DestinationPath $outFile -Force
        $sz = [math]::Round(((Get-Item $outFile).Length / 1KB), 1)
        Log-Ok "메타데이터 아카이브 생성 완료: $(Split-Path $outFile -Leaf) (${sz} KB)"
    } else {
        Die "백업 대상 meta/ 디렉토리가 없습니다."
    }

    # 오래된 백업 정리
    $threshold = (Get-Date).AddDays(-$keepDays)
    $oldBackups = Get-ChildItem -Path $backupDir -Filter "*_meta_*.zip" | Where-Object { $_.LastWriteTime -lt $threshold }
    foreach ($ob in $oldBackups) {
        Remove-Item $ob.FullName -Force
    }
    if ($oldBackups.Count -gt 0) {
        Log-Info "${keepDays}일 초과된 오래된 백업 $($oldBackups.Count)건 정리 완료"
    }

    return 0
}

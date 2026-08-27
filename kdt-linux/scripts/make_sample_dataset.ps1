# ===============================================================
# scripts/make_sample_dataset.ps1
# 교과 8/14 실데이터와 동일한 구조의 더미 데이터셋 생성 (PowerShell)
# ===============================================================
param(
    [string]$DatasetName = "kimchi",
    [string]$RootDir = ".\dataset",
    [int]$Count = 1000
)

$ds = Join-Path $RootDir $DatasetName
$rawImg = Join-Path $ds "raw\images"
$rawLbl = Join-Path $ds "raw\labels"
$metaDir = Join-Path $ds "meta"
$backupDir = Join-Path $ds "backup"

New-Item -ItemType Directory -Path $rawImg, $rawLbl, $metaDir, $backupDir -Force | Out-Null

Write-Host "[1/4] 이미지 ${Count}장 생성 중 ($DatasetName)..."
$rand = [System.Random]::new(42)

for ($i = 1; $i -le $Count; $i++) {
    $numStr = $i.ToString("D4")
    $imgPath = Join-Path $rawImg "${DatasetName}_${numStr}.jpg"
    $bytes = [byte[]](0xFF, 0xD8, 0xFF, 0xE0, 0x00, 0x10, 0x4A, 0x46, 0x49, 0x46)
    [System.IO.File]::WriteAllBytes($imgPath, $bytes)
}

Write-Host "[2/4] 라벨 TXT 생성 중..."
for ($i = 1; $i -le $Count; $i++) {
    $numStr = $i.ToString("D4")
    $lblPath = Join-Path $rawLbl "${DatasetName}_${numStr}.txt"
    $cls = $rand.Next(0, 6)
    $x = [math]::Round(($rand.NextDouble() * 0.6 + 0.2), 6)
    $y = [math]::Round(($rand.NextDouble() * 0.6 + 0.2), 6)
    $w = [math]::Round(($rand.NextDouble() * 0.2 + 0.05), 6)
    $h = [math]::Round(($rand.NextDouble() * 0.2 + 0.05), 6)
    "$cls $x $y $w $h" | Set-Content -Path $lblPath
}

Write-Host "[3/4] classes.txt 및 메타 문서 생성..."
$classesContent = @"
0 leaf
1 plastic_stone_metal
2 branch
3 rubber_glove
4 disease_browning
5 green_onion_pepper
"@
Set-Content -Path (Join-Path $metaDir "classes.txt") -Value $classesContent

$yamlContent = @"
path: $(Resolve-Path $ds)
train: images/train
val: images/val
test: images/test
nc: 6
names:
  0: leaf
  1: plastic_stone_metal
  2: branch
  3: rubber_glove
  4: disease_browning
  5: green_onion_pepper
"@
Set-Content -Path (Join-Path $metaDir "data.yaml") -Value $yamlContent

Write-Host "[4/4] 의도적 검증 결함 데이터 주입..."
# 1. 라벨 누락
Remove-Item -Path (Join-Path $rawLbl "${DatasetName}_0007.txt") -Force -ErrorAction SilentlyContinue
# 2. 이미지 누락
Remove-Item -Path (Join-Path $rawImg "${DatasetName}_0123.jpg") -Force -ErrorAction SilentlyContinue
# 3. 범위 초과 + 없는 클래스
"9 1.500000 0.400000 0.200000 0.200000" | Set-Content -Path (Join-Path $rawLbl "${DatasetName}_0456.txt")
# 4. 빈 파일
Set-Content -Path (Join-Path $rawLbl "${DatasetName}_0789.txt") -Value $null
# 5. 파일명 공백
New-Item -ItemType File -Path (Join-Path $rawImg "${DatasetName} 0999.jpg") -Force | Out-Null

$finalImgs = (Get-ChildItem -Path $rawImg -Filter "*.jpg").Count
$finalLbls = (Get-ChildItem -Path $rawLbl -Filter "*.txt").Count
Write-Host "생성 완료: 이미지 $finalImgs 장 / 라벨 $finalLbls 개" -ForegroundColor Green

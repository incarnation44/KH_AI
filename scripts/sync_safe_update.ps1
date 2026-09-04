$ErrorActionPreference = "Stop"

# 1. Read machine.json
$machineJsonPath = Join-Path $PSScriptRoot "..\.local\machine.json"
if (-not (Test-Path $machineJsonPath)) {
    Write-Host "CRITICAL: machine.json not found at $machineJsonPath. Aborting." -ForegroundColor Red
    exit 1
}

$machineData = Get-Content $machineJsonPath -Raw | ConvertFrom-Json
$machineId = $machineData.machine_id

if ([string]::IsNullOrWhiteSpace($machineId)) {
    Write-Host "CRITICAL: machine_id is empty in machine.json. Aborting." -ForegroundColor Red
    exit 1
}

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Starting Safe Sync for Machine: [$machineId]" -ForegroundColor Cyan
Write-Host "Workspace: $((Get-Item $PSScriptRoot).Parent.FullName)" -ForegroundColor Cyan
Write-Host "=========================================" -ForegroundColor Cyan

Push-Location (Join-Path $PSScriptRoot "..")

try {
    # 2. Fetch remote state safely without merging
    Write-Host "[1/4] Fetching remote state..."
    git fetch origin master
    
    # 3. Check local changes
    $localChanges = git status --porcelain
    $hasLocalChanges = -not [string]::IsNullOrWhiteSpace($localChanges)
    
    # 4. Check remote changes (commits on origin/master not in HEAD)
    $remoteChanges = git log HEAD..origin/master --oneline 2>$null
    $hasRemoteChanges = -not [string]::IsNullOrWhiteSpace($remoteChanges)
    
    # 5. Check unpushed local commits
    $unpushedCommits = git log origin/master..HEAD --oneline 2>$null
    $hasUnpushedCommits = -not [string]::IsNullOrWhiteSpace($unpushedCommits)
    
    Write-Host "[2/4] Analyzing Sync State:"
    Write-Host "  - Uncommitted Local Changes : $hasLocalChanges"
    Write-Host "  - New Remote Commits        : $hasRemoteChanges"
    Write-Host "  - Unpushed Local Commits    : $hasUnpushedCommits"
    
    # 6. Conflict Protection Logic
    if ($hasLocalChanges -and $hasRemoteChanges) {
        Write-Host ""
        Write-Host "⚠️  SYNC CONFLICT DANGER ⚠️" -ForegroundColor Red
        Write-Host "Both local changes AND remote commits exist." -ForegroundColor Yellow
        Write-Host "Auto-merge is disabled to protect your files." -ForegroundColor Yellow
        Write-Host "ACTION REQUIRED: Please commit your changes manually, then pull and resolve conflicts." -ForegroundColor Yellow
        Write-Host "ABORTING SYNC." -ForegroundColor Red
        exit 1
    }
    
    # 7. Safe Pull
    if ($hasRemoteChanges) {
        Write-Host "[3/4] Safe Pulling from remote..."
        git pull origin master --no-rebase
    } else {
        Write-Host "[3/4] No remote changes to pull. Up to date."
    }
    
    # 8. Safe Commit & Push
    if ($hasLocalChanges) {
        Write-Host "[4/4] Committing local changes..."
        git add .
        $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm"
        git commit -m "[$machineId] Automated Sync Update - $timestamp"
        
        Write-Host "Pushing to remote..."
        git push origin master
    } elseif ($hasUnpushedCommits) {
        Write-Host "[4/4] Pushing existing local commits to remote..."
        git push origin master
    } else {
        Write-Host "[4/4] Nothing to commit or push."
    }
    
    Write-Host "=========================================" -ForegroundColor Green
    Write-Host "✅ Sync Completed Safely!" -ForegroundColor Green
    Write-Host "=========================================" -ForegroundColor Green
}
catch {
    Write-Host "An error occurred during sync: $_" -ForegroundColor Red
    exit 1
}
finally {
    Pop-Location
}

param(
    [string]$Message = "Update machine learning progress"
)

git add .

$changes = git diff --cached --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "No changes to commit."
    exit 0
}

git commit -m $Message

if ($LASTEXITCODE -ne 0) {
    exit 1
}

git push origin main

param(
    [Parameter(Mandatory = $true)]
    [string]$Message
)

$ErrorActionPreference = "Stop"

git add .

git diff --cached --quiet

if ($LASTEXITCODE -eq 0) {
    Write-Host "No changes to commit."
    exit 0
}

git commit -m $Message

if ($LASTEXITCODE -ne 0) {
    throw "Commit failed."
}

git push origin main

if ($LASTEXITCODE -ne 0) {
    throw "Push failed."
}

Write-Host "Successfully published your changes!"

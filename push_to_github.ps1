# ==============================================================
# Helper Script: Connect & Push Cloud Reel Factory to GitHub
# ==============================================================

param(
    [string]$RepoUrl = "https://github.com/amareshdas3-eng/Agentic-AI.git"
)

Write-Host "--- Linking ProEngineering Reel Factory to GitHub ---" -ForegroundColor Cyan

# Check existing remote
$existingRemote = git remote get-url origin 2>$null
if (-not $existingRemote) {
    git remote add origin $RepoUrl
    Write-Host "[SUCCESS] Added git remote 'origin': $RepoUrl" -ForegroundColor Green
} else {
    git remote set-url origin $RepoUrl
    Write-Host "[INFO] Remote 'origin' already configured as: $existingRemote" -ForegroundColor Yellow
}

# Add and commit all cloud factory files
git add .github/ cloud_reel_factory.py generate_pop_sfx.py assets/
git commit -m "Deploy ProEngineering Autonomous Cloud Reel Factory (11:00 AM IST)"

Write-Host ""
Write-Host "==========================================================" -ForegroundColor Green
Write-Host "To push to GitHub, run:" -ForegroundColor White
Write-Host "  git push -u origin master" -ForegroundColor Yellow
Write-Host "==========================================================" -ForegroundColor Green


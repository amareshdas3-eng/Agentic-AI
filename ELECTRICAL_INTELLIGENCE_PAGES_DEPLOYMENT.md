# Electrical Intelligence RC2 — isolated Pages deployment

## Safety and scope
- Deployment branch: `deploy/electrical-intelligence-rc2`
- Target folder: `electrical-intelligence/`
- The workflow publishes only that folder as the GitHub Pages artifact.
- `main` is not changed by this branch setup. The live `proengineering.in` website is not touched.
- This is a preliminary demonstration only, not a production SaaS, compliance certificate, or design approval. Do not upload confidential customer/project files.

## Current state
The Pages workflow is prepared. It deliberately skips deployment until both `electrical-intelligence/index.html` and `electrical-intelligence/sample_verification_report.html` exist. The RC2 package itself still needs to be copied into that folder and pushed to this branch.

## Windows PowerShell — finish staging the RC2 package
1. Download `ProEngineering_Electrical_Intelligence_Suite_v1.0.0-rc2-preview.zip` from the ChatGPT conversation and note its actual download location.
2. Open PowerShell and run the commands below, changing the ZIP path if needed:

```powershell
git clone https://github.com/amareshdas3-eng/Agentic-AI.git
Set-Location Agentic-AI
git checkout deploy/electrical-intelligence-rc2
New-Item -ItemType Directory -Force electrical-intelligence | Out-Null
Expand-Archive -LiteralPath "$env:USERPROFILE\Downloads\ProEngineering_Electrical_Intelligence_Suite_v1.0.0-rc2-preview.zip" -DestinationPath ".\electrical-intelligence" -Force
Test-Path ".\electrical-intelligence\index.html"
Test-Path ".\electrical-intelligence\sample_verification_report.html"
git status --short
git add electrical-intelligence
git commit -m "feat(pages): stage electrical intelligence RC2 preview"
git push origin deploy/electrical-intelligence-rc2
```

3. Open the repository's **Actions** tab and inspect **Deploy ProEngineering Electrical Intelligence Preview**. Confirm the run succeeds before using any Pages URL.
4. If GitHub asks to enable Pages or the workflow fails due to repository permissions, do not change `main` or website hosting settings. Share the exact workflow error so the next step can be chosen safely.

## Release gates before wider customer use
- Independent, line-by-line engineering review of formulas, constants, assumptions, and supported configurations.
- Traceable worked examples and boundary/regression tests.
- Browser end-to-end checks on desktop and mobile.
- Security, privacy, terms, professional-liability and data-handling review.
- Pilot feedback using synthetic data only until confidentiality and processing terms are agreed.

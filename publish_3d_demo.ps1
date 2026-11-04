# ========================================================
# ProEngineering 1-Click Publishing Assistant: 3D Demo Reel
# ========================================================

$videoPath = "d:\instagram\reels\reel_3d_live_person_demo.mp4"
$caption = @"
Watching 33kV transformer differential protection in 3D changes how you commission substations forever! ⚡ In this 3D live demonstration, we step into the substation digital twin:

1️⃣ Real-Time 3D Transformer Flux Density: Tracking nominal 1.72 Tesla core saturation
2️⃣ 3D Dynamic Polar Phasor Engine: Compensating Dyn11 30° vector lag in numerical relays
3️⃣ Inrush Cross-Blocking: Suppressing magnetizing harmonics on the 87T differential loop
4️⃣ Millisecond Arc Quenching: Verifying 38ms VCB trip speed with zero pole discrepancy

👇 Comment 3D below and I'll DM you the complete 3D Substation Twin & Relay Protocol PDF! (Or explore tools at proengineering.in)

#SubstationCommissioning #DigitalTwin #PowerSystems #ElectricalEngineering #3DAnimation #RelayProtection #HighVoltage #IndustrialAI #ProEngineering
"@

# 1. Load system clipboard
Set-Clipboard -Value $caption
Write-Host "[SUCCESS] 3D Demo Caption copied to clipboard!" -ForegroundColor Green

# 2. Highlight video file in Explorer
Start-Process "explorer.exe" "/select,$videoPath"
Write-Host "[SUCCESS] Highlighted 3D video in Explorer: $videoPath" -ForegroundColor Cyan

# 3. Launch Instagram Create in Google Chrome
Start-Process "chrome.exe" "https://www.instagram.com"
Write-Host "[SUCCESS] Opened Instagram in Chrome. Ready to drag and drop!" -ForegroundColor Yellow

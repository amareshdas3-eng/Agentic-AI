# ==========================================
# ProEngineering 1-Click Publishing Assistant
# ==========================================

$videoPath = "d:\instagram\reels\reel_human_touch_spec_trap.mp4"
$caption = @"
Most `$400K+ switchgear change orders hide inside contradictions between Division 26 Specs, the SLD, and the BOQ (31.5 kA vs 40 kA fault levels & IEC 61850 gateways). ⚡

Here are the 4 pre-bid traps every Project Director, EPC Lead, and Electrical Engineer must audit before signing off:
1️⃣ Order-of-precedence conflicts between BOQ line items and spec clauses
2️⃣ 33 kV / 11 kV switchgear fault-level mismatches (31.5 kA vs. 40 kA for 3s)
3️⃣ Proprietary IEC 61850 / SCADA gateway traps on numerical relays
4️⃣ Two-way cable takeoff gaps between feeder schedules and trench routing

👇 Comment SPEC below and I'll DM you my printable 33 kV Substation & EPC Pre-Bid Diagnostic Checklist (or grab the tools directly at proengineering.in).

#ElectricalEngineering #PowerSystems #Substation #EPC #ProjectManagement #PrimaveraP6 #ProtectionRelays #IndustrialAI #ProEngineering
"@

# 1. Load system clipboard
Set-Clipboard -Value $caption
Write-Host "[SUCCESS] Caption copied to clipboard!" -ForegroundColor Green

# 2. Highlight video file in Explorer
Start-Process "explorer.exe" "/select,$videoPath"
Write-Host "[SUCCESS] Highlighted video in Explorer: $videoPath" -ForegroundColor Cyan

# 3. Launch Instagram Create in Google Chrome
Start-Process "chrome.exe" "https://www.instagram.com"
Write-Host "[SUCCESS] Opened Instagram in Chrome. Ready to drag and drop!" -ForegroundColor Yellow

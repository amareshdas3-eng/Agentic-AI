import os
import fitz  # PyMuPDF

PDF_PATH = "d:/instagram/ProEngineering_Instagram_Brand_and_Checklist_Kit.pdf"

def create_lead_magnet_pdf():
    doc = fitz.open()
    
    # ---------------- PAGE 1: Brand & Launch Architecture ----------------
    page1 = doc.new_page(width=595, height=842) # A4 Portrait
    
    # Header Background Banner (Dark Charcoal)
    page1.draw_rect(fitz.Rect(0, 0, 595, 120), color=None, fill=(0.05, 0.07, 0.10))
    # Electric Cyan Accent Bar
    page1.draw_rect(fitz.Rect(0, 120, 595, 124), color=None, fill=(0.0, 0.95, 1.0))
    
    # Header Text
    page1.insert_text(fitz.Point(40, 48), "PROENGINEERING | INDUSTRIAL AI & MEGACAPEX", fontsize=20, fontname="helv", color=(0.0, 0.95, 1.0))
    page1.insert_text(fitz.Point(40, 72), "The Category-of-One Engineering Brand Playbook & Commissioning Kit", fontsize=12, fontname="helv", color=(1.0, 1.0, 1.0))
    page1.insert_text(fitz.Point(40, 95), "Author: Senior Power Systems & Industrial AI Architect (23+ Yrs L&T / ABB Megaprojects, PMP)", fontsize=9, fontname="helv", color=(1.0, 0.72, 0.0))
    
    # Section 1: Brand Positioning & Identity
    y = 150
    page1.insert_text(fitz.Point(40, y), "1. BRAND FOUNDATION: THE CATEGORY-OF-ONE POSITIONING", fontsize=13, fontname="helv", color=(0.05, 0.15, 0.3))
    page1.draw_line(fitz.Point(40, y+4), fitz.Point(555, y+4), color=(0.0, 0.6, 0.8), width=1.5)
    
    # Bio Box
    y += 20
    page1.draw_rect(fitz.Rect(40, y, 555, y+65), color=(0.0, 0.7, 0.9), fill=(0.95, 0.98, 1.0), width=1)
    page1.insert_text(fitz.Point(50, y+18), "OFFICIAL INSTAGRAM BIO FORMULA (PASTE DIRECTLY):", fontsize=9, fontname="helv", color=(0.0, 0.4, 0.6))
    page1.insert_text(fitz.Point(50, y+34), "⚡ 23+ Yrs Commissioning 33kV Substations & Megaprojects (L&T, ABB, PMP)", fontsize=10, fontname="helv", color=(0.1, 0.1, 0.1))
    page1.insert_text(fitz.Point(50, y+48), "🤖 Agentic AI for Primavera P6 Controls, Relay Testing & Reliability", fontsize=10, fontname="helv", color=(0.1, 0.1, 0.1))
    page1.insert_text(fitz.Point(50, y+60), "👇 Free Pre-Bid Checklists, SLD Audits & Tools: proengineering.in", fontsize=10, fontname="helv", color=(0.0, 0.3, 0.8))
    
    # Section 2: 5-Day Viral Sequence & Reel Formats
    y += 85
    page1.insert_text(fitz.Point(40, y), "2. 5-DAY VIRAL LAUNCH SEQUENCE & HIGH-RETENTION FORMATS", fontsize=13, fontname="helv", color=(0.05, 0.15, 0.3))
    page1.draw_line(fitz.Point(40, y+4), fitz.Point(555, y+4), color=(0.0, 0.6, 0.8), width=1.5)
    
    rows_p1 = [
        ("Day 1: Forensic Teardown", "Reel #1: 4-Step Animated AI Spec Trap", "Comment SPEC for Checklist", "Targets EPC Directors losing margin on Division 26 spec traps."),
        ("Day 2: Field Commissioning", "Reel #2: 33kV Substation Zero-Trip Protocol", "Comment SLD for Matrix", "High-save checklist: OLTC, CT knee-points, OMICRON injection."),
        ("Day 3: Project Controls AI", "Reel #3: Primavera P6 Float Trap Audit", "Comment P6 for Playbook", "Demonstrates AI detecting hidden lags on critical path milestones."),
        ("Day 4: Pattern-Interrupt", "Reel #4: 2-Character Site Manager vs Architect", "Comment RELAY for Protocol", "Pattern interrupt: Day-1 soak trip & 2nd harmonic inrush fix."),
        ("Day 5: Visual Cheat Sheet", "Carousel: Generator Protection on 1 Page", "Comment GEN for High-Res", "High share potential: ANSI 87G, 40, 46, 64R relay matrix."),
    ]
    
    y += 20
    # Table Header
    page1.draw_rect(fitz.Rect(40, y, 555, y+20), color=None, fill=(0.1, 0.15, 0.25))
    page1.insert_text(fitz.Point(45, y+14), "Day & Pillar", fontsize=9, fontname="helv", color=(1.0, 1.0, 1.0))
    page1.insert_text(fitz.Point(160, y+14), "Format & Production Asset", fontsize=9, fontname="helv", color=(1.0, 1.0, 1.0))
    page1.insert_text(fitz.Point(340, y+14), "Keyword Trigger", fontsize=9, fontname="helv", color=(1.0, 1.0, 1.0))
    page1.insert_text(fitz.Point(450, y+14), "Strategic Value", fontsize=9, fontname="helv", color=(1.0, 1.0, 1.0))
    y += 20
    
    for day, fmt, cta, strat in rows_p1:
        page1.draw_rect(fitz.Rect(40, y, 555, y+32), color=(0.8, 0.85, 0.9), fill=(0.98, 0.99, 1.0) if ((y//32)%2==0) else (1.0, 1.0, 1.0), width=0.5)
        page1.insert_text(fitz.Point(45, y+18), day, fontsize=8, fontname="helv", color=(0.1, 0.1, 0.1))
        page1.insert_text(fitz.Point(160, y+18), fmt, fontsize=8, fontname="helv", color=(0.0, 0.3, 0.7))
        page1.insert_text(fitz.Point(340, y+18), cta, fontsize=8, fontname="helv", color=(0.8, 0.4, 0.0))
        page1.insert_text(fitz.Point(450, y+14), strat[:26], fontsize=7, fontname="helv", color=(0.3, 0.3, 0.3))
        page1.insert_text(fitz.Point(450, y+24), strat[26:], fontsize=7, fontname="helv", color=(0.3, 0.3, 0.3))
        y += 32
        
    # Section 3: The 3-Step Comment-to-Client Funnel
    y += 25
    page1.insert_text(fitz.Point(40, y), "3. THE AUTOMATED COMMENT-TO-CLIENT FUNNEL", fontsize=13, fontname="helv", color=(0.05, 0.15, 0.3))
    page1.draw_line(fitz.Point(40, y+4), fitz.Point(555, y+4), color=(0.0, 0.6, 0.8), width=1.5)
    
    steps = [
        ("Step 1: Algorithmic Velocity", "Every Reel asks for a specific 1-word comment (SPEC, SLD, P6, RELAY). This spikes comment velocity within the first 60 minutes, signaling high engagement to the Instagram algorithm."),
        ("Step 2: Instant Technical Asset DM", "Commenters instantly receive a direct link to download this high-density engineering PDF checklist, establishing unquestioned technical authority in under 30 seconds."),
        ("Step 3: Executive Advisory Bridge", "The final page of every tool invites EPC Project Directors and Plant VPs to book a 30-minute Pre-Bid Spec Audit or Substation RCA Advisory session at proengineering.in."),
    ]
    y += 18
    for s_title, s_desc in steps:
        page1.insert_text(fitz.Point(45, y), s_title, fontsize=9.5, fontname="helv", color=(0.0, 0.45, 0.75))
        page1.insert_text(fitz.Point(45, y+13), s_desc[:115], fontsize=8, fontname="helv", color=(0.2, 0.2, 0.2))
        page1.insert_text(fitz.Point(45, y+24), s_desc[115:], fontsize=8, fontname="helv", color=(0.2, 0.2, 0.2))
        y += 38
        
    # Footer
    page1.draw_line(fitz.Point(40, 810), fitz.Point(555, 810), color=(0.7, 0.7, 0.7), width=0.5)
    page1.insert_text(fitz.Point(40, 825), "ProEngineering © 2026 | Category-of-One Industrial AI & Megaproject Authority | Page 1 of 2", fontsize=8, fontname="helv", color=(0.5, 0.5, 0.5))

    # ---------------- PAGE 2: The 33 kV Substation & EPC Pre-Bid Checklist ----------------
    page2 = doc.new_page(width=595, height=842) # A4 Portrait
    
    # Header Banner
    page2.draw_rect(fitz.Rect(0, 0, 595, 90), color=None, fill=(0.05, 0.07, 0.10))
    page2.draw_rect(fitz.Rect(0, 90, 595, 93), color=None, fill=(1.0, 0.72, 0.0)) # Gold bar
    page2.insert_text(fitz.Point(40, 38), "THE 33 kV SUBSTATION & EPC PRE-BID DIAGNOSTIC CHECKLIST", fontsize=15, fontname="helv", color=(1.0, 0.72, 0.0))
    page2.insert_text(fitz.Point(40, 58), "Field-Tested Across 23+ Years of Megaproject Execution & Commissioning Sign-Offs", fontsize=10, fontname="helv", color=(1.0, 1.0, 1.0))
    page2.insert_text(fitz.Point(40, 75), "Confidential Field Checklist | ProEngineering Technical Practice Document", fontsize=8, fontname="helv", color=(0.0, 0.95, 1.0))
    
    # Part 1: Pre-Bid Specification & BOQ Audit
    y = 115
    page2.insert_text(fitz.Point(40, y), "PART 1: PRE-BID SPECIFICATION & DRAWING AUDIT (STOP THE $400K CHANGE ORDERS)", fontsize=11, fontname="helv", color=(0.8, 0.15, 0.15))
    page2.draw_line(fitz.Point(40, y+3), fitz.Point(555, y+3), color=(0.8, 0.2, 0.2), width=1.5)
    
    chk_part1 = [
        ("[ ] Order of Precedence Clause Audit", "Identify contradictions between Division 26 spec clauses, BOQ line items, and Tender SLD. Ensure spec supersedes BOQ or submit formal pre-bid RFI."),
        ("[ ] 33kV & 11kV Fault Level Withstand Duration", "Verify 31.5 kA vs 40 kA fault ratings for 3 seconds across busbars, CTs, and VCBs. Standard commercial switchgear is rated 1 sec; 3s requires heavy surcharge."),
        ("[ ] CT Class PS Knee-Point (Vk) Calculation", "Audit differential 87T CT specifications: Vk >= 2 * If * (Rct + 2*RL + Rr). Reject ambiguous 'standard class' designations before vendor procurement."),
        ("[ ] SCADA Gateway & IEC 61850 Protocol Interoperability", "Verify whether client requires PRP/HSR redundant ring protocols or proprietary vendor relays (MiCOM / ABB Relion / Siemens SIPROTEC) with license costs."),
        ("[ ] Two-Way Cable Takeoff & Trench Derating", "Cross-check route length from SLD vs Site Plot Plan. Factor in 15% routing slack plus depth/thermal resistivity derating factors to prevent undersized runs."),
    ]
    
    y += 18
    for item_title, item_desc in chk_part1:
        page2.draw_rect(fitz.Rect(40, y, 555, y+36), color=(0.85, 0.85, 0.85), fill=(0.99, 0.97, 0.97), width=0.5)
        page2.insert_text(fitz.Point(48, y+14), item_title, fontsize=9, fontname="helv", color=(0.7, 0.1, 0.1))
        page2.insert_text(fitz.Point(48, y+27), item_desc[:125], fontsize=7.5, fontname="helv", color=(0.2, 0.2, 0.2))
        y += 40
        
    # Part 2: 33 kV Substation Zero-Trip Commissioning Protocol
    y += 15
    page2.insert_text(fitz.Point(40, y), "PART 2: ZERO-TRIP 33 kV ENERGIZATION & COMMISSIONING PROTOCOL", fontsize=11, fontname="helv", color=(0.0, 0.45, 0.75))
    page2.draw_line(fitz.Point(40, y+3), fitz.Point(555, y+3), color=(0.0, 0.5, 0.8), width=1.5)
    
    chk_part2 = [
        ("[ ] Dyn11 Vector Group & CT Secondary Loop Polarity", "Confirm primary-to-secondary phase displacement (30° lag) and secondary star-point orientation to eliminate false 87T differential zero-sequence spill current."),
        ("[ ] 15% 2nd-Harmonic Inrush Restraint Setting", "Activate 2nd-harmonic restraint threshold (12-15%) on MiCOM P643/ABB RET670 to prevent nuisance tripping during initial transformer core magnetization soak."),
        ("[ ] Secondary Injection with OMICRON CMC 356", "Perform 3-phase ramp test to verify pick-up, dual-slope characteristic (Slope 1 @ 20-30%, Slope 2 @ 70-80%), and high-set instantaneous element tripping time (< 30ms)."),
        ("[ ] Vacuum Circuit Breaker (VCB) Timing & Contact Resistance", "Measure breaker closing time (< 60ms), opening time (< 45ms), and pole-to-pole contact resistance (< 35 micro-ohms) using 100A DC micro-ohmmeter."),
        ("[ ] 24-Hour No-Load Soak & Online DGA Oil Sample", "Maintain 33kV energization for 24 hours under continuous vibration and acoustic inspection. Pull post-soak transformer oil sample for dissolved gas chromatography."),
    ]
    
    y += 18
    for item_title, item_desc in chk_part2:
        page2.draw_rect(fitz.Rect(40, y, 555, y+36), color=(0.85, 0.85, 0.85), fill=(0.96, 0.98, 1.0), width=0.5)
        page2.insert_text(fitz.Point(48, y+14), item_title, fontsize=9, fontname="helv", color=(0.0, 0.35, 0.65))
        page2.insert_text(fitz.Point(48, y+27), item_desc[:125], fontsize=7.5, fontname="helv", color=(0.2, 0.2, 0.2))
        y += 40
        
    # High-Value Advisory Callout Box at Bottom
    y += 12
    page2.draw_rect(fitz.Rect(40, y, 555, y+70), color=(0.0, 0.95, 1.0), fill=(0.07, 0.10, 0.15), width=1.5)
    page2.insert_text(fitz.Point(55, y+20), "NEED AN EXPERT PRE-BID SPEC AUDIT OR COMMISSIONING RCA?", fontsize=10.5, fontname="helv", color=(0.0, 0.95, 1.0))
    page2.insert_text(fitz.Point(55, y+36), "ProEngineering partners with EPC Contractors, Project Directors, and Industrial Plant Heads", fontsize=8.5, fontname="helv", color=(1.0, 1.0, 1.0))
    page2.insert_text(fitz.Point(55, y+48), "to eliminate multi-crore change orders and optimize Primavera P6 project execution via Industrial AI.", fontsize=8.5, fontname="helv", color=(1.0, 1.0, 1.0))
    page2.insert_text(fitz.Point(55, y+62), "Book a Confidential Advisory Diagnostic: https://proengineering.in | contact@proengineering.in", fontsize=9, fontname="helv", color=(1.0, 0.72, 0.0))
    
    # Footer
    page2.draw_line(fitz.Point(40, 810), fitz.Point(555, 810), color=(0.7, 0.7, 0.7), width=0.5)
    page2.insert_text(fitz.Point(40, 825), "ProEngineering © 2026 | 33 kV Substation & EPC Diagnostic Checklist | Page 2 of 2", fontsize=8, fontname="helv", color=(0.5, 0.5, 0.5))
    
    doc.save(PDF_PATH)
    print("Lead Magnet PDF generated at:", PDF_PATH)
    doc.close()

if __name__ == "__main__":
    create_lead_magnet_pdf()


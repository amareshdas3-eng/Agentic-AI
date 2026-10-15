# ProEngineering Industrial Power Systems Suite — 15-Minute Pilot Client Interview Script

**Release Target:** v1.0.0-rc1  
**Distribution Package:** `ProEngineering_Customer_Demo_v1.0.0-rc1.zip`  
**Target Audience:** Industrial EPC Engineering Leads, Switchgear / MCC Panel Builders, Plant Electrical Managers

---

## 1. Objectives of the Pilot Interview
1. Demonstrate the speed and accuracy of automated deterministic sizing and cross-document discrepancy checking.
2. Validate whether automated discrepancy detection (e.g., $I_b > I_n$, cable overload, excessive voltage drop) saves real engineering hours.
3. Secure qualitative feedback and identify must-have standards / features before presenting a commercial subscription offer.

---

## 2. 15-Minute Structured Interview Flow

### Step 1: Context & Problem Setup (3 Minutes)
> *"Hello [Client Name], thank you for your time. As electrical engineers, we know that during fast-track industrial projects, discrepancies between the Load Schedule, Cable Schedule, and Switchgear Breaker ratings often slip through until the factory acceptance test (FAT) or site commissioning—causing costly rework, cable repulls, or nuisance tripping.*
> 
> *At ProEngineering.in, we built a deterministic verification suite that performs instant cross-document audits against IEC and IEEE standards without sending your plant data to the cloud."*

### Step 2: Live Screen-Share Demonstration (6 Minutes)
1. **Launch Dashboard:**
   - Double-click `launch_demo.bat` (or open `index.html`).
   - Highlight: *"Notice this runs 100% locally and offline in the browser—zero cloud storage or security risk for your plant designs."*
2. **Showcase Modules:**
   - **Tab 01 (Voltage Drop & Inrush):** Show $R_{90}$ temperature correction and motor starting inrush dip calculation.
   - **Tab 02 (Transformer Sizing):** Show standard IEC kVA series matching and bolted secondary fault calculation.
   - **Tab 03 (Adiabatic Withstand):** Demonstrate how an undersized cable ($S_{min} = 188\text{ mm}^2$ vs $95\text{ mm}^2$) is instantly caught as a fire hazard.
   - **Tab 05 (Design Assurance Audit):** Run the multi-module consistency check. Show the 4 detected findings, pointing out:
     - Finding 1: Breaker undersized for mill motor continuous current ($I_b = 333\text{ A} > I_n = 315\text{ A}$).
     - Finding 2: Adiabatic failure on 16 mm² cable under 25 kA fault.
3. **Showcase Deliverable:**
   - Click *"Open Watermarked Engineering Report"*.
   - Point out the complete equations, input snapshots, and active findings register ready for management review.

### Step 3: Discovery & Validation Questions (4 Minutes)
Ask these specific questions to validate the commercial proposition:
1. *"In your current design reviews, how do you cross-check cable schedules against breaker ratings? Is it manual in Excel, or do you run it through specialized software?"*
2. *"If an automated tool like this pre-audited your feeder schedules and produced this watermarked report in 30 seconds, how much engineering review time would that save per project?"*
3. *"Looking at this report, what additional checks would your lead engineer require before relying on this for client submittals? (e.g., harmonics, short-circuit curves, arc-flash)?"*

### Step 4: Closing & Controlled Pilot Offer (2 Minutes)
> *"We are currently running a closed, zero-cost engineering pilot with 3 selected industrial firms. We can provide you this standalone offline package to run against your synthetic or sanitized feeder lists for 30 days in exchange for your candid feedback on feature priorities.*
> 
> *Can I send you the ZIP package and a 1-page feedback sheet to test with your design team?"*

---

## 3. Key Feedback Scoring Matrix (Log in `docs/release/PILOT_FEEDBACK_TRACKER.csv`)

| Client Name | Organization Type | Primary Value Identified | Missing Feature Requested | Willingness to Pay ($/₹ / mo) | Next Follow-Up Date |
| :--- | :--- | :--- | :--- | :--- | :--- |
| *Example EPC 1* | Industrial EPC | Cross-check $I_b \le I_n \le I_z$ | Support for $60\text{ Hz}$ & NEC tables | ₹15,000 / month | +7 Days |

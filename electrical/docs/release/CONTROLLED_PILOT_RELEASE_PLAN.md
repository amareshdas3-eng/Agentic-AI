# ProEngineering Electrical Intelligence Suite — Controlled Pilot Release Plan

**Target Release:** v1.0.0-rc1  
**Document ID:** PRO-ENG-PILOT-PLAN-001  
**Author:** Agent 0 (Chief Architect) & Agent 13 (Commercial Lead)  
**Objective:** Enable safe commercial testing and high-credibility demonstrations of the ProEngineering Suite without touching or risking the live `proengineering.in` WordPress/Elementor business.

---

## 1. Release Strategy & Staged Deployment Options

To satisfy the Owner Priority Rules ("Budget: zero by default", "Preserve the existing live WordPress website"), the rollout is structured into three progressive tiers:

```
[Tier 1: Offline Pilot Package] ──> [Tier 2: Isolated Subdomain] ──> [Tier 3: Commercial SaaS]
  (Standalone Desktop/HTML)          (app.proengineering.in)             (Licensed Web App)
  Zero Hosting / Zero Risk            Air-Gapped from WordPress           Full Client Onboarding
  STATUS: READY NOW (RC-1)            STATUS: PROVISIONING READY          STATUS: FUTURE GATE 5
```

### Tier Comparison & Recommendation

| Rollout Tier | Technical Architecture | Live Site Risk | Cost | Primary Use Case | Readiness |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Tier 1: Standalone Portable Demo** *(Recommended Now)* | Double-clickable local HTML/JS bundle with synthetic data & launcher scripts. | **Zero Risk** (Offline) | $0.00 | Direct consulting client demos, EPC executive reviews, offline workshops. | **IMMEDIATELY READY** |
| **Tier 2: Isolated Subdomain (`app.proengineering.in`)** | Static cloud storage bucket (e.g. Firebase Hosting, GitHub Pages, or cPanel subfolder) mapped to `app` CNAME. | **Zero Risk** (Separate vhost/DNS) | $0.00 | Gated pilot access, link-based interactive demos for prospective clients. | **AWAITING DNS SETUP** |
| **Tier 3: Embedded WordPress Integration** | iFrame or API integration directly inside `proengineering.in`. | **HIGH RISK** | Varies | Mass customer checkout and automated report delivery. | **STRICTLY BLOCKED** |

---

## 2. Tier 1 Execution: Standalone Portable Demo Package

The portable demonstration package is prepared in directory `portable_customer_demo/`:
- **`index.html`:** The fully self-contained visual engineering laboratory (all 5 modules embedded).
- **`launch_demo.bat`:** One-click launcher for Windows clients that opens the dashboard in the default browser.
- **`sample_verification_report.html`:** The official watermarked engineering audit deliverable.
- **`sample_load_schedule.csv` & `sample_cable_schedule.csv`:** Synthetic 33kV/11kV/415V plant datasets for client testing.
- **`README_PILOT.txt`:** Step-by-step instructions and technical limitations notice.

---

## 3. Tier 2 Execution Plan: Dedicated Subdomain (`app.proengineering.in`)

When the Owner is ready to enable web-based link access:

### Step 1: DNS & Subdomain Configuration (Hostinger / cPanel / Cloudflare)
1. In the domain DNS manager, add a dedicated record:
   - **Type:** `CNAME` or `A`
   - **Host:** `app`
   - **Target / IP:** Pointing to an isolated static host (e.g. GitHub Pages `amaresh.github.io` or Firebase Hosting).
2. **DO NOT** point `app.proengineering.in` to the main WordPress root directory (`/public_html`).
3. If using cPanel/Hostinger subdomains:
   - Document Root must be strictly `/public_html/app_subdomain_isolated/` (or outside `/public_html`).

### Step 2: Deployment of Static Release Artifact
- Copy all files from `portable_customer_demo/` into the isolated root.
- The site will serve pure client-side HTML/JS with zero server-side PHP or database execution, ensuring it cannot interfere with WordPress plugins or WooCommerce checkout.

### Step 3: Gated Access & Pilot Security
- Enable basic HTTP authentication or access token parameters in the URL (`?pilot_key=PE-2026-ALPHA`) to restrict public indexing.
- Include robots meta tag: `<meta name="robots" content="noindex, nofollow">`.

---

## 4. Controlled Pilot Protocol (3–5 Target Industrial Clients)

### Candidate Profile
- Industrial EPC engineering consultants, switchgear panel builders (MCC/PCC), and plant electrical managers.

### Engagement Process
1. **Pilot Briefing:** Share the offline demo package or `app.proengineering.in` link with `KNOWN_LIMITATIONS.md`.
2. **Data Intake:** Clients test their own radial feeder schedules using the standardized CSV format.
3. **Assurance Run:** Engine identifies discrepancy findings (cable overload, breaker mismatch, excessive voltage drop).
4. **Structured Feedback Collection:**
   - Did the automated findings catch real design discrepancies?
   - Was the watermarked verification report accepted by engineering management?
   - What additional standards or equipment types are required for commercial subscription?

---

## 5. Summary Timeline & Milestones

| Milestone | Target Date | Deliverable | Owner Action Required |
| :--- | :--- | :--- | :--- |
| **M1: Freeze & Security Clearance** | Today | `FINAL_RELEASE_AUDIT.md`, `PRODUCTION_SECURITY_REVIEW.md` | Accept Tier 1 local release. |
| **M2: Pilot Package Packaging** | Today | `portable_customer_demo/` distribution bundle | Distribute to initial friendly clients. |
| **M3: Subdomain Activation** | Next Sprint | `app.proengineering.in` live static preview | Add DNS CNAME record for `app`. |
| **M4: Pilot Feedback Synthesis** | 30 Days | `PILOT_FEEDBACK_SYNTHESIS.md` | Review conversion hypotheses and commercial pricing. |

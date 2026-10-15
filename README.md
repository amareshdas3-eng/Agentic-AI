# Agentic-AI

A multi-project repository of production-grade Agentic AI engineering tools, autonomous verification engines, and industrial intelligence workflows.

---

## ⚡ Active Projects in this Repository

### 1. [ProEngineering Electrical Intelligence Suite](electrical/)
A multi-agent, deterministic engineering suite for industrial power systems, radial distribution networks, and switchgear design assurance.
- **Governing Standards:** IEC 60364, IEC 60076, IEC 60947, IEC 60865-1, IEEE Std 80, IEEE Std 141, IS 732, IS 3043.
- **Status:** Release Candidate `v1.0.0-rc1` (56/56 Verified Automated Assertions).
- **Core Modules:**
  - `01_SLD_Engineering_Pro`: Single Line Diagrams & Interlocking Logic.
  - `02_LoadFlow_VoltageDrop_Pro`: Radial Feeder Flow, $R_{90}$ Temperature Resistance & Motor Inrush.
  - `03_Equipment_Sizing_Pro`: Transformer Capacity & Adiabatic Short-Circuit Withstand ($S_{min} = I_{sc}\sqrt{t}/k$).
  - `04_MCC_PCC_Architect_Pro`: Switchboard Architecture & Parameterized Starter Decision Matrix.
  - `05_Integrated_Power_Design_Assurance_Pro`: Deterministic Cross-Document Discrepancy Matrix.
- **Interactive Laboratory:** [`electrical/demo_dashboard.html`](electrical/demo_dashboard.html)
- **Turnkey Customer Pilot Package:** [`electrical/portable_customer_demo/`](electrical/portable_customer_demo/) (ZIP: [`electrical/ProEngineering_Customer_Demo_v1.0.0-rc1.zip`](electrical/ProEngineering_Customer_Demo_v1.0.0-rc1.zip)).

---

### 2. [IFIA (Industrial Facility Intelligence Assistant)](ifia/)
Autonomous intelligence assistant for industrial facilities and remediation verification workflows.

---

## 🚀 Quickstart for ProEngineering Electrical Suite

1. **Run the Automated Test Suite (Node.js):**
   ```bash
   node electrical/00_Universal_Master_Framework/src/test_runner.js
   ```
2. **Launch the Offline Interactive Engineering Dashboard:**
   - Double-click [`electrical/portable_customer_demo/launch_demo.bat`](electrical/portable_customer_demo/launch_demo.bat) on Windows.
   - Or open [`electrical/demo_dashboard.html`](electrical/demo_dashboard.html) in any modern browser.
3. **Inspect the Verification Dossier:**
   - [Verification Report](electrical/00_Universal_Master_Framework/sample_verification_report.html)
   - [Mathematical Proofs Dossier](electrical/docs/release/INDEPENDENT_ENGINEERING_VALIDATION.md)
   - [Final Release Audit](electrical/docs/release/FINAL_RELEASE_AUDIT.md)

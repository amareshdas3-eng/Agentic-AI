# ProEngineering 8-Stage Execution Playbook
### Turnkey Step-by-Step Prompting System for Antigravity & AI Coding Agents
**Framework:** ProEngineering Industrial Power Systems Suite

---

## Overview

Use these 8 execution prompts sequentially when building or updating any product in the suite. **Never run all stages in a single unmonitored prompt.** Always verify the output of each stage before invoking the next.

```
Stage 01 ──> Stage 02 ──> Stage 03 ──> Stage 04 ──> Stage 05 ──> Stage 06 ──> Stage 07 ──> Stage 08
(Inspect)    (Freeze)     (Engine)     (UI/UX)      (Verify)     (Reports)    (Commerce)   (Release)
```

---

## Stage 01: Inspect Existing Files & Dependencies

```markdown
PROENGINEERING EXECUTION PROMPT — STAGE 01: DISCOVERY & INSPECTION

Product Target: [INSERT PRODUCT NAME, e.g., LoadFlow & VoltageDrop Pro]
Location: [INSERT TARGET DIRECTORY]

Instructions for Agent:
1. Thoroughly inspect the designated directory and its subdirectories.
2. Catalog all existing source code files, data schemas, calculation modules, test suites, and documentation.
3. Identify all runtime dependencies, calculation libraries, or formatting packages.
4. Verify whether any existing code contains hardcoded values, hallucinated standards clauses, or unverified arithmetic.
5. Produce a comprehensive "Discovery and Inspection Report" covering:
   - File manifest with line counts and purpose.
   - Identified calculation routines vs. missing mathematical modules.
   - Reusable components vs. components that require re-architecture.
   - Technical debt, safety risks, and missing test coverage.
6. AWAIT MY APPROVAL BEFORE PROCEEDING TO STAGE 02. DO NOT WRITE OR OVERWRITE APPLICATION CODE YET.
```

---

## Stage 02: Freeze Requirements & Design Basis

```markdown
PROENGINEERING EXECUTION PROMPT — STAGE 02: REQUIREMENTS & STANDARDS FREEZE

Product Target: [INSERT PRODUCT NAME]

Instructions for Agent:
1. Create or update the formal Product Requirements Specification (PRS) in `PRODUCT_SPECIFICATION.md`.
2. Define:
   - Target User Personas (Consulting Engineers, Industrial EPC, Electrical Contractors, Plant Facility Managers).
   - Core Scope vs. Explicit Exclusions (e.g., balanced radial flow included; transient stability excluded).
   - Mandatory vs. Optional Project Inputs (with units and allowed numerical ranges).
   - Applicable Engineering Standards (cite exact year and relevant chapters/tables: IEC 60364, IEC 60909, IS 732, IEEE 141).
   - Canonical Data Schema (JSON structure for buses, cables, loads, transformers, switchgear).
   - Edge Cases and Failure Modes (e.g., zero impedance, negative length, leading power factors).
3. Generate a "Design Basis Register" outlining all assumed constants (copper/aluminum resistivity at 20°C and 70°C/90°C, reactance per km, standard breaker frame sizes).
4. Present the frozen specification for review. DO NOT BEGIN CALCULATION CODE UNTIL SIGNED OFF.
```

---

## Stage 03: Implement Deterministic Calculation Engine

```markdown
PROENGINEERING EXECUTION PROMPT — STAGE 03: DETERMINISTIC CALCULATION ENGINE

Product Target: [INSERT PRODUCT NAME]

Instructions for Agent:
1. Implement the computational core in clean, modular TypeScript/JavaScript or Python.
2. Adhere strictly to these rules:
   - ZERO LLM ARITHMETIC: All physics, circuit laws, and equations must be executed by pure deterministic functions.
   - Every function must have complete TypeScript interfaces / Python type hints, JSDoc/docstrings, formula citations, and unit documentation.
   - Implement base SI unit calculations internally, with explicit conversion helpers for user display.
   - Handle edge cases gracefully: throw typed domain errors for divide-by-zero, ungrounded sources, or floating buses.
3. Implement the dual-calculation verification path:
   - Method A (Primary): Direct circuit impedance method.
   - Method B (Verification): Symmetrical components / per-unit complex power formulation.
4. Output intermediate calculation results (e.g., resistance at operating temp, reactance, active current, reactive current, voltage drop volts, voltage drop percentage).
5. Provide isolated unit tests proving 100% test pass on basic mathematical functions.
```

---

## Stage 04: Build Interactive User Experience & Visualizer

```markdown
PROENGINEERING EXECUTION PROMPT — STAGE 04: USER EXPERIENCE & INPUT WORKFLOW

Product Target: [INSERT PRODUCT NAME]

Instructions for Agent:
1. Build a modern, high-aesthetic web interface (Vanilla HTML5/CSS3/ES Modules or React/Vite depending on project architecture).
2. Follow ProEngineering visual standards:
   - Theme: Sleek engineering dark/light theme (Slate/Obsidian dark `#0f172a`, Blueprint Blue `#2563eb`, Safety Amber `#f59e0b`, Pass Green `#10b981`, Alert Red `#ef4444`).
   - Typography: Clean monospace/sans-serif engineering font hierarchy (Inter, JetBrains Mono, or Outfit).
   - Responsiveness: Flawless layout across desktop 4K/1080p, tablet, and mobile.
3. Include:
   - Project Metadata & Design Basis intake panel.
   - Dynamic, tabular load/feeder/equipment entry with real-time field validation.
   - Visual calculation summary cards (Total Demand kVA, Max Feeder Voltage Drop %, Limiting Feeder Tag).
   - Real-time warning badges for code violations (e.g., voltage drop > 5.0% highlighted in flashing amber/red).
   - Interactive SVG Topology / Diagram viewer with pan/zoom and node inspection.
4. Ensure zero external paid dependencies or tracking scripts.
```

---

## Stage 05: Deploy Verification Agents & Benchmark Suite

```markdown
PROENGINEERING EXECUTION PROMPT — STAGE 05: INDEPENDENT VERIFICATION & BENCHMARKING

Product Target: [INSERT PRODUCT NAME]

Instructions for Agent:
1. Implement the comprehensive test suite in `TEST_BENCHMARKS_AND_EDGE_CASES.md`.
2. Include at least 5 industrial benchmark test cases with published hand-calculated solutions:
   - Case 1: Simple LV Radial Feeder (Balanced 3-Phase).
   - Case 2: Multi-Branch Distribution Substation (MV to LV).
   - Case 3: High-Inrush Motor Starting Feeder (Voltage Dip Analysis).
   - Case 4: Long Cable Run with High Ambient Temperature Derating.
   - Case 5: Pathological / Malformed Inputs (zero impedance, extreme power factor, negative load).
3. Run the automated test runner and output the "Verification & Tolerance Audit":
   - Compare Hand-Calculated Expected vs. Software Calculated Values.
   - Confirm tolerance is strictly $< 0.5\%$.
   - Verify that invalid inputs are rejected with clear engineering corrective guidance.
4. Do NOT fake or hardcode test passes. Record any discrepancy and resolve it.
```

---

## Stage 06: Generate Customer Deliverables & PDF/SVG Exporters

```markdown
PROENGINEERING EXECUTION PROMPT — STAGE 06: DELIVERABLE GENERATION ENGINES

Product Target: [INSERT PRODUCT NAME]

Instructions for Agent:
1. Implement the automated deliverable generation pipeline:
   - Engineering Calculation Workbook: Complete math proofs with equations, substitutions, units, and code references.
   - Equipment / Feeder Schedule: Tabular CSV/Excel/Markdown schedules ready for switchboard builder estimation.
   - Drawing-Ready Schematic: Standards-compliant SVG vector drawing with IEC 60617 / IEEE 315 symbols, tags, and ratings.
   - Design Review & Exception Register: Detailed list of compliant checks, warnings, and required physical validations.
2. Implement printable CSS `@media print` styling or PDF generation ensuring single-page and multi-page professional margins, title blocks, revision history, and confidentiality notices.
3. Automatically apply the status watermark (e.g., "PRELIMINARY DESIGN - NOT FOR CONSTRUCTION").
```

---

## Stage 07: Prepare Commercial Packaging & Marketing Copy

```markdown
PROENGINEERING EXECUTION PROMPT — STAGE 07: COMMERCIAL PACKAGING & SALES COPY

Product Target: [INSERT PRODUCT NAME]

Instructions for Agent:
1. Create the complete commercial sales assets in `COMMERCIAL_PACKAGE.md`:
   - High-converting product page headline, hook, and value proposition.
   - Core Features vs. Explicit Exclusions (protecting engineering liability).
   - Target Customer Pain Points (eliminating Excel formula errors, passing consultant submittals first time).
   - Dual Pricing Tiers: India (INR ₹) vs. International (USD $).
   - Sample Output Preview blurbs and visual asset mockups.
   - Customer Validation Questions & FAQ addressing engineering confidence.
2. Ensure copy aligns with ProEngineering.in branding: authoritative, mathematically rigorous, no generic AI fluff.
```

---

## Stage 08: Final Quality Gate & Release Readiness Audit

```markdown
PROENGINEERING EXECUTION PROMPT — STAGE 08: FINAL QUALITY GATE & AUDIT

Product Target: [INSERT PRODUCT NAME]

Instructions for Agent:
1. Conduct the final release audit across the product codebase:
   - Functional completeness against Product Requirements Specification (PRS).
   - Automated unit and benchmark test pass rate (100% mandatory).
   - Security check: Zero credential leaks, zero unvetted external scripts, zero confidential data storage.
   - Standards traceability check: Zero unreferenced engineering claims.
   - Disclaimer & liability check: Disclaimers present on all UI screens, reports, and exported files.
2. Issue the "Product Release Certificate":
   - Status: RELEASE CANDIDATE (v1.0.0).
   - Open defects by severity (Must be 0 Critical, 0 Major).
   - Known limitations and recommended roadmap enhancements.
```

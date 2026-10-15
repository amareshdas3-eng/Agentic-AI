# ProEngineering Electrical Intelligence Suite — System Architecture Specification
### Revision: 2.0.0 (Gate 0 / Gate 1 Baseline)
**Author:** Agent 0 (Integration Lead / Chief Architect) & Multi-Agent Engineering Build Team  
**Classification:** Core System Architecture & Non-Negotiable Integration Rules  
**Date:** October 15, 2026

---

## 1. Architectural Mission & Tenets

The **ProEngineering Electrical Intelligence Suite** delivers commercial-grade, multi-tenant engineering intelligence for industrial infrastructure, substations, and process power systems. The architecture enforces three non-negotiable tenets:

1. **Deterministic Calculation Integrity (Zero-Hallucination):**  
   Every voltage drop, fault duty, equipment size, and cable ampacity calculation is executed by pure mathematical functions. LLMs and agent personas are strictly prohibited from performing arithmetic or altering computed engineering values.
2. **Immutable Provenance & Traceability (`TraceableValue<T>`):**  
   Every engineering value records its origin: `USER_ENTERED`, `IMPORTED_RAW`, `ENGINEER_CONFIRMED`, `PROJECT_DEFAULT`, or `CALCULATED_DETERMINISTIC`. `AI_HYPOTHESIS` values cannot be passed into deterministic calculation routines without explicit human confirmation.
3. **Explicit Design Basis & Non-Hardcoded Thresholds:**  
   No calculation operates with hidden or universal default limits. Acceptable voltage drops, spare feeder margins, ambient temperatures, and fault clearing times are strictly driven by a versioned, project-specific `ProjectDesignBasis`. If inputs are missing, the system emits `EvaluationStatus: NOT_ASSESSED`.

---

## 2. Multi-Tier System Topology

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                       PRESENTATION & WORKSPACE TIER                             │
│  - Interactive Test Lab (demo_dashboard.html)                                  │
│  - Project Intake & Load List Mapping UI                                       │
│  - SVG Topology Viewer & Compartment Visualizer                                │
│  - Watermarked Audit Report Exporter (HTML / Print PDF)                        │
└──────────────────────────────────────┬──────────────────────────────────────────┘
                                       │ JSON / REST / Typed Events
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│                        DATA & INGESTION TIER (Agent 5)                          │
│  - Multi-Tenant Isolation (organisation_id / project_id / project_revision)    │
│  - CSV / XLSX Importer with Field Mapping Preview & Validation                 │
│  - Provenance Tracking Engine (records source document, sheet, row, col)        │
│  - Canonical Data Store (validates against CANONICAL_DATA_SCHEMA.json v2.0)     │
└──────────────────────────────────────┬──────────────────────────────────────────┘
                                       │ Canonical Entities & Criteria
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│              DETERMINISTIC COMPUTATIONAL CORE (Agent 4 & Agent 7)               │
│  - Pure, Side-Effect-Free Calculation Functions                                 │
│  - Request Contract: CalculationRequest<TInputs, TCriteria>                    │
│  - Response Contract: CalculationResult<TOutputs>                               │
│  - Intermediate Steps, Mathematical Proofs & Dimensional Check                  │
│  - Missing Input Detection -> Emits NOT_ASSESSED                                │
└──────────────────────────────────────┬──────────────────────────────────────────┘
                                       │ Calculated Feeds & Snapshots
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│               CROSS-DISCIPLINARY DESIGN ASSURANCE ENGINE (Agent 9)              │
│  - 40 Deterministic Cross-Document Rules (CROSS_MODULE_CONSISTENCY_MATRIX.md)   │
│  - SLD Topology <-> Load Schedule <-> Sizing Datasheets <-> MCC Lineup         │
│  - Four-Tier Severity Rubric: CRITICAL_SAFETY | MAJOR_ENG | MINOR | INFO        │
│  - Action Matrix & Discrepancy Closure Tracker                                 │
└──────────────────────────────────────┬──────────────────────────────────────────┘
                                       │ Audited Results & Gated State
                                       ▼
┌─────────────────────────────────────────────────────────────────────────────────┐
│               GOVERNANCE, STANDARDS & RELEASE GATES (Agent 2 & 12)              │
│  - Authorized Standards & Criteria Registry (Metadata Only)                     │
│  - Statutory Compliance Verification Claims Strictly Prohibited                │
│  - Release Gating: Open CRITICAL_SAFETY findings force QUARANTINED_DRAFT        │
│  - Peer Review Memoranda & Statutory Engineer-of-Record (EOR) Sign-Off Gate     │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Data Flow & Provenance Lifecycle

Every electrical parameter travels through five strictly governed states:

```
[Raw CSV/XLSX/Form] ──> (1) IMPORTED_RAW (Retains file, sheet, row, col coordinates)
                               │
                               ▼
                        (2) ENGINEER_CONFIRMED (User approves mapped preview)
                               │
                               ▼
                        (3) CALCULATED_DETERMINISTIC (Engine executes pure function)
                               │
                               ▼
                        (4) AUDITED_CONSISTENCY (Design Assurance Engine validates)
                               │
                               ▼
                        (5) RELEASE_CANDIDATE / APPROVED_FOR_PILOT
```

---

## 4. Tenant & Revision Isolation Rules

1. **Tenant Separation:** All entities possess a non-nullable `organisation_id` ensuring strict logical multi-tenancy.
2. **Revision Immutability:** When a calculation run or design review occurs, the `project_revision` is frozen. Any subsequent change to loads, lengths, or criteria creates a new revision (`v1.1`, `v2.0`). Historical calculation runs are immutable audit records.
3. **Deterministic Idempotency:** Running the calculation engine on the same input snapshot and criteria will produce bit-for-bit identical results at any point in time.

---

## 5. Security, Zero-Budget & Privacy Constraints

- **Local-First Execution:** Core calculations run locally in Node.js or in modern client-side browsers without mandatory external cloud infrastructure.
- **Zero Third-Party API Leakage:** No proprietary client load schedules or switchboard designs are sent to external LLMs for calculation or storage.
- **No Copyrighted Full Text:** The standards registry stores standard identifiers, edition metadata, clause numbers, and user-supplied criteria. Copyrighted standard texts from IEC, IEEE, or BIS are never stored in the repository.

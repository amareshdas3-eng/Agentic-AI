# Product 05: Integrated Power Design Assurance Pro — Specification
### Cross-Disciplinary Consistency Engine & Independent Electrical Design Review Platform
**Product Family:** ProEngineering Industrial Power Systems Suite  
**Version:** 1.0.0 (Flagship Review Gateway)  
**Standard Basis:** IEEE 141, IEC 60364, IEC 60909, IEC 61439, ISO 9001 Quality Assurance

---

## 1. Product Scope & Vision

`Integrated Power Design Assurance Pro` serves as an automated Chief Electrical Engineer and Independent Peer Reviewer. In real-world engineering projects, design packages fail client submittals because different deliverables are created in silos by different engineers or subcontractors:
- The **SLD** shows a $2000\text{A}$ incomer, but the **Load Schedule** calculates total peak demand as $2450\text{A}$.
- The **Cable Schedule** lists a $3\text{C} \times 95\text{ mm}^2$ cable, but the **Voltage Drop Workbook** calculated $3\text{C} \times 150\text{ mm}^2$ was necessary to stay below $3.0\%$.
- The **MCC Schedule** specifies a $45\text{ kW}$ DOL starter, but the **SLD** feeder shows a VFD symbol.
- The **Transformer Datasheet** lists $Z = 6.0\%$, while the downstream switchgear breaker breaking capacity was evaluated using $Z = 7.5\%$.

`Integrated Power Design Assurance Pro` ingests outputs from:
1. **Product 01:** SLD Engineering Pro (Topology, tags, bus voltages, coupler interlocking).
2. **Product 02:** LoadFlow & VoltageDrop Pro (Feeder currents, kW/kVA sums, percentage drops).
3. **Product 03:** Equipment Sizing Pro (Transformer ratings, cable adiabatic withstand, breaker $I_{cu}/I_{cs}$).
4. **Product 04:** MCC & PCC Architect Pro (Feeder types, starter ratings, column line-ups).

It maps all data into the universal **Canonical Data Schema** and executes **25+ deterministic cross-consistency validation rules**, producing an audit-ready **Discrepancy Matrix & Closure Tracker**.

---

## 2. In-Scope Checks vs. Scope Exclusions

### In-Scope Checks:
- **Rating Parity Checks:** Breaker continuous current vs. feeder full load current; busbar ampacity vs. upstream incomer trip setting.
- **Topological Integrity:** Unconnected feeders, conflicting voltage levels across connected nodes, loop/backfeed hazards.
- **Short-Circuit Duty Coordination:** Verified that switchgear $I_{cu}$ and cable adiabatic withstand $S_{min}$ meet or exceed the maximum prospective bolted fault current of connected sources.
- **Tagging & Metadata Uniqueness:** Duplicate tags across drawings, schedules, and datasheets.
- **Stale Document Revision Detection:** Flags where a downstream feeder schedule was generated from an older revision of the primary SLD.

### Scope Exclusions (Clearly Logged):
- On-site physical installation workmanship inspection.
- Factory Acceptance Testing (FAT) witness sign-off.
- Civil and structural building foundation review.

# Product 01: SLD Engineering Pro — Specification
### Single Line Diagram Design, Graph Topology & Electrical Rule Verification
**Product Family:** ProEngineering Industrial Power Systems Suite  
**Version:** 1.0.0 (Release Candidate Spec)  
**Target Delivery:** Standalone Web Application / API & Drawing Export Package

---

## 1. Product Scope & Vision

`SLD Engineering Pro` automates the generation and mathematical verification of industrial single line diagrams. Unlike generic vector drawing tools (AutoCAD, Visio, Draw.io) which treat diagrams as dumb lines and text, `SLD Engineering Pro` treats the power system as a **directed topological graph**. Every line represents a calculated bus, transformer ratio, or cable impedance, and every breaker is an auditable node.

### Primary Use Cases:
1. **Industrial 33kV/11kV Substation & 415V Plant Distribution SLD Generation:**
   - Double-circuit transmission incomers, 33kV outdoor switchyard.
   - Dual 33kV/11kV oil-immersed transformers with On-Load Tap Changers (OLTC).
   - 11kV indoor metal-clad switchgear with dual bus sections and motorized bus coupler.
   - 11kV/433V distribution transformers feeding 415V Main Power Control Centers (PCC).
   - Emergency Diesel Generator (DG) synchronization / interlocking bus.
2. **Automated Electrical Graph Validation:**
   - Detects floating buses, disconnected loads, and source loops.
   - Flags unsynchronized parallel source tie-ins (preventing bus backfeeds).
   - Verifies voltage consistency across every branch and transformer winding.
3. **Drawing-Ready Multi-Format Exports:**
   - Scalable Vector Graphics (SVG) adhering to IEC 60617 / IEEE 315 symbology.
   - DXF/DWG-ready CAD exchange metadata.
   - Tabular circuit schedules (Incomers, Couplers, Feeders).

---

## 2. In-Scope vs. Explicit Exclusions

### In-Scope:
- Multi-voltage systems: 33kV, 22kV, 11kV, 6.6kV, 3.3kV, 415V, 230V, 110V DC.
- Radial, dual-incomer with bus coupler (2-out-of-3 interlocking scheme), and ring distribution configurations.
- Source types: Utility Grid Incomers, Step-Down Transformers, Diesel Generators, Uninterruptible Power Supplies (UPS), Solar PV Inverters.
- Switchgear components: Vacuum Circuit Breakers (VCB), Air Circuit Breakers (ACB), Molded Case Circuit Breakers (MCCB), Isolators/Disconnectors, Earth Switches, Current Transformers (CT), Potential Transformers (PT), Surge Arresters (LA).
- Automated equipment tag generation based on plant hierarchy (e.g., `33-SWYD-INC-01`, `11-SWBD-BC-01`, `04-PCC-FDR-05`).

### Explicit Exclusions (Clearly Logged in User Reports):
- Substation civil/structural foundation sizing and bay clearance layout.
- Detailed protection relay coordination curves (Time-Current Curves / TCC) — logged as required downstream study.
- Dynamic transient stability and electromagnetic transient analysis (EMTP).
- 3D spatial routing and physical switchyard cable trench layout.

---

## 3. Engineering Inputs & Data Hierarchy

```
[Project Header]
  ├── Grid Supply Voltage & Frequency (e.g. 33kV, 50Hz)
  ├── Fault Level at Delivery Point (MVA or kA)
  └── Earthing Philosophy (Solidly Earthed, NGR, Ungrounded)
        │
[Primary Substation Incomers]
  ├── Incomer 1 (33kV VCB, CT/PT, Surge Arrester)
  └── Incomer 2 (33kV VCB, CT/PT, Surge Arrester)
        │
[Transformers]
  ├── TR-01 (33/11kV, 5MVA, ONAN, Dyn11, Z=7.5%)
  └── TR-02 (33/11kV, 5MVA, ONAN, Dyn11, Z=7.5%)
        │
[11kV Switchboard (Split-Bus Architecture)]
  ├── Incomer 1 (11kV 630A VCB, 25kA 3s)
  ├── Bus Section A (11kV Cu Busbar, 1250A)
  ├── Bus Coupler (11kV 1250A VCB with 2-out-of-3 Castell Interlock)
  ├── Bus Section B (11kV Cu Busbar, 1250A)
  └── Incomer 2 (11kV 630A VCB, 25kA 3s)
        │
[Downstream Distribution & 415V PCC]
  ├── Secondary Step-Down (11kV/433V 1600kVA Transformers)
  ├── 415V PCC-1 & PCC-2 with Tie Breakers
  └── Outgoing Feeders to MCC-1, MCC-2, Utility Panels & Emergency Bus
```

---

## 4. Applicable Standards & References

- **IEC 60617:** Graphical symbols for diagrams.
- **IEEE Std 315 / ANSI Y32.2:** Graphic symbols for electrical and electronics diagrams.
- **IEC 61439-1 / IEC 61439-2:** Low-voltage switchgear and controlgear assemblies.
- **IEC 62271-200:** High-voltage switchgear and controlgear (1kV to 52kV).
- **IS 10118:** Code of practice for selection, installation, and maintenance of switchgear.
- **IEEE Std 141 (Red Book):** Electric Power Distribution for Industrial Plants.

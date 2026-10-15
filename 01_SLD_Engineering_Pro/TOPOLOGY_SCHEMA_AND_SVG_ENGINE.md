# SLD Engineering Pro — Topology Schema & SVG Engine Specification
### Vector Graph Data Model, Symbol Library, and Layout Generation Logic
**Framework:** ProEngineering Industrial Power Systems Suite

---

## 1. Electrical Topology Graph Data Model

The core of `SLD Engineering Pro` is a directed acyclic hierarchy represented in JSON:

```json
{
  "diagramId": "SLD-33-11-04-SUBSTATION",
  "title": "33kV / 11kV Substation & 415V Plant Distribution Single Line Diagram",
  "drawingNumber": "PE-E-SLD-001",
  "revision": "R0",
  "standard": "IEC_60617",
  "canvas": {
    "width": 1920,
    "height": 1080,
    "theme": "DARK_SLATE",
    "gridSpacing": 20
  },
  "nodes": [
    {
      "id": "SRC-GRID-1",
      "type": "UTILITY_INCOMER",
      "tag": "33kV Transmission Grid Line 1",
      "voltageV": 33000,
      "coords": { "x": 400, "y": 80 }
    },
    {
      "id": "SRC-GRID-2",
      "type": "UTILITY_INCOMER",
      "tag": "33kV Transmission Grid Line 2",
      "voltageV": 33000,
      "coords": { "x": 1200, "y": 80 }
    },
    {
      "id": "BUS-33KV-1",
      "type": "BUSBAR",
      "tag": "33kV Main Busbar Section 1",
      "voltageV": 33000,
      "ratedCurrentA": 1250,
      "coords": { "x1": 300, "y1": 180, "x2": 650, "y2": 180 }
    },
    {
      "id": "BUS-33KV-2",
      "type": "BUSBAR",
      "tag": "33kV Main Busbar Section 2",
      "voltageV": 33000,
      "ratedCurrentA": 1250,
      "coords": { "x1": 950, "y1": 180, "x2": 1300, "y2": 180 }
    },
    {
      "id": "CB-33-BC",
      "type": "CIRCUIT_BREAKER_VCB",
      "tag": "33-SWYD-BC-01",
      "ratedCurrentA": 1250,
      "breakingKa": 25.0,
      "coords": { "x": 800, "y": 180 }
    },
    {
      "id": "TR-01",
      "type": "TRANSFORMER_2W",
      "tag": "33/11kV Power Transformer 1",
      "ratingKva": 5000,
      "primaryV": 33000,
      "secondaryV": 11000,
      "impedancePercent": 7.5,
      "vectorGroup": "Dyn11",
      "coords": { "x": 480, "y": 320 }
    },
    {
      "id": "TR-02",
      "type": "TRANSFORMER_2W",
      "tag": "33/11kV Power Transformer 2",
      "ratingKva": 5000,
      "primaryV": 33000,
      "secondaryV": 11000,
      "impedancePercent": 7.5,
      "vectorGroup": "Dyn11",
      "coords": { "x": 1120, "y": 320 }
    },
    {
      "id": "BUS-11KV-A",
      "type": "BUSBAR",
      "tag": "11kV Switchboard Bus Section A",
      "voltageV": 11000,
      "ratedCurrentA": 1250,
      "coords": { "x1": 250, "y1": 460, "x2": 750, "y2": 460 }
    },
    {
      "id": "BUS-11KV-B",
      "type": "BUSBAR",
      "tag": "11kV Switchboard Bus Section B",
      "voltageV": 11000,
      "ratedCurrentA": 1250,
      "coords": { "x1": 850, "y1": 460, "x2": 1350, "y2": 460 }
    },
    {
      "id": "CB-11-BC",
      "type": "CIRCUIT_BREAKER_VCB",
      "tag": "11-SWBD-BC-01",
      "ratedCurrentA": 1250,
      "coords": { "x": 800, "y": 460 }
    }
  ],
  "edges": [
    { "from": "SRC-GRID-1", "to": "BUS-33KV-1", "type": "OVERHEAD_LINE" },
    { "from": "SRC-GRID-2", "to": "BUS-33KV-2", "type": "OVERHEAD_LINE" },
    { "from": "BUS-33KV-1", "to": "CB-33-BC", "type": "BUS_TIE" },
    { "from": "CB-33-BC", "to": "BUS-33KV-2", "type": "BUS_TIE" },
    { "from": "BUS-33KV-1", "to": "TR-01", "type": "FEEDER_VCB" },
    { "from": "BUS-33KV-2", "to": "TR-02", "type": "FEEDER_VCB" },
    { "from": "TR-01", "to": "BUS-11KV-A", "type": "CABLE_RUN", "cableTag": "11kV 3C x 300 mm² XLPE Cu" },
    { "from": "TR-02", "to": "BUS-11KV-B", "type": "CABLE_RUN", "cableTag": "11kV 3C x 300 mm² XLPE Cu" },
    { "from": "BUS-11KV-A", "to": "CB-11-BC", "type": "BUS_TIE" },
    { "from": "CB-11-BC", "to": "BUS-11KV-B", "type": "BUS_TIE" }
  ]
}
```

---

## 2. Standard Vector Symbol Library (IEC 60617 / IEEE 315)

The SVG generator renders each electrical component using precise parametric vector snippets:

### A. Busbar (Copper / Aluminum)
```xml
<!-- Busbar: Heavy Solid Stroke with Voltage-Coded Accent -->
<line x1="250" y1="460" x2="750" y2="460" stroke="#38bdf8" stroke-width="6" stroke-linecap="round" />
<!-- Bus Tag & Voltage Text -->
<text x="260" y="445" fill="#e2e8f0" font-family="Inter, sans-serif" font-size="13" font-weight="600">11kV BUS SECTION A (1250A, 25kA 3s)</text>
```

### B. Two-Winding Transformer (IEC 60617 - Interlocking Circles)
```xml
<g class="transformer-node" transform="translate(480, 320)">
  <!-- Primary Winding -->
  <circle cx="0" cy="-18" r="22" fill="none" stroke="#e2e8f0" stroke-width="2.5" />
  <!-- Secondary Winding -->
  <circle cx="0" cy="18" r="22" fill="none" stroke="#38bdf8" stroke-width="2.5" />
  <!-- Vector Group & Rating Tag -->
  <text x="32" y="-5" fill="#f8fafc" font-size="11" font-weight="600">5 MVA, 33/11kV</text>
  <text x="32" y="10" fill="#94a3b8" font-size="10">Dyn11, Z=7.5%</text>
  <text x="32" y="24" fill="#94a3b8" font-size="10">ONAN / OLTC</text>
</g>
```

### C. Drawout Vacuum Circuit Breaker (VCB)
```xml
<g class="vcb-breaker" transform="translate(800, 460)">
  <!-- Isolation Plugs (Drawout representation) -->
  <polygon points="-12,-20 0,-28 12,-20" fill="none" stroke="#e2e8f0" stroke-width="2" />
  <!-- Breaker Square with Cross -->
  <rect x="-14" y="-14" width="28" height="28" fill="#1e293b" stroke="#e2e8f0" stroke-width="2" rx="3" />
  <line x1="-10" y1="-10" x2="10" y2="10" stroke="#22c55e" stroke-width="2.5" />
  <line x1="-10" y1="10" x2="10" y2="-10" stroke="#22c55e" stroke-width="2.5" />
  <!-- Bottom Isolation Plug -->
  <polygon points="-12,20 0,28 12,20" fill="none" stroke="#e2e8f0" stroke-width="2" />
  <!-- Device Tag & Rating -->
  <text x="22" y="5" fill="#38bdf8" font-size="11" font-weight="600">11-SWBD-BC-01 (1250A)</text>
</g>
```

### D. Current Transformer (CT) & Protection Core
```xml
<g class="ct-assembly" transform="translate(480, 260)">
  <!-- Primary Feeder Line -->
  <line x1="0" y1="-25" x2="0" y2="25" stroke="#e2e8f0" stroke-width="2.5" />
  <!-- CT Toroid Cores -->
  <circle cx="0" cy="-6" r="9" fill="none" stroke="#eab308" stroke-width="2" />
  <circle cx="0" cy="8" r="9" fill="none" stroke="#eab308" stroke-width="2" />
  <!-- Ratio & Class Annotation -->
  <text x="16" y="-3" fill="#e2e8f0" font-size="10">Core 1: 300/1A, 5P20, 15VA (Prot)</text>
  <text x="16" y="11" fill="#e2e8f0" font-size="10">Core 2: 300/1A, Cl 0.2S, 10VA (Mtr)</text>
</g>
```

---

## 3. Automated Tiered Layout Engine Algorithm

1. **Hierarchy Level Assignment:**
   - Level 0 ($Y = 80$): Transmission Grid Incomers, Overhead Lines, Lightning Arresters.
   - Level 1 ($Y = 180$): Primary Switchyard 33kV Busbar & Bus Coupler.
   - Level 2 ($Y = 320$): Primary Power Step-Down Transformers.
   - Level 3 ($Y = 460$): Secondary 11kV Distribution Switchboard.
   - Level 4 ($Y = 640$): Distribution Transformers (11/0.433kV) & DG Incomers.
   - Level 5 ($Y = 780$): 415V Main Power Control Center (PCC) Busbars.
   - Level 6 ($Y = 940$): Outgoing Motor Control Centers (MCC) & Plant Feeder Terminals.
2. **Horizontal Spacing & Collision Avoidance:**
   - Feeder spacing: Minimum $140\text{px}$ center-to-center.
   - Section spacing: Bus couplers require $120\text{px}$ clearance between adjacent bus sections.
   - Annotation offsets: Text is anchored rightward with automatic collision detection.

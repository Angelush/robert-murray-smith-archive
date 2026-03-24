## Overview
Robert Murray-Smith builds a prototype Savonius-style vertical axis wind turbine (VAWT) using a rim-driven generator design — a concept introduced in video 1867 — to demonstrate that placing the generator on the rim rather than the axle hub yields comparable or better performance at lower cost and complexity. The turbine is 3D-printed from PLA in three simple parts and successfully powers an LED by breath alone, and produces ~2V / 12–14mA against a resistive load at low wind speeds. The central message is that practical simplicity and acceptable efficiency, not theoretical perfection, is what allows a design to actually get built.

## Key Topics
- Rim-driven generator concept vs. torque-at-the-hub (axle) approach
- Savonius-style VAWT as the simplest baseline design for comparison
- Design-for-manufacture philosophy: fewest parts, lowest cost, easiest build
- Serpentine coil construction and its suitability for this generator type
- Cost analysis: prototype (~£9) vs. projected production cost (~£2–4)
- Performance demonstration: LED powered by breath, then measured against a resistive load
- Scalability concept: stacking multiple units into a "wind wall"

## Materials and Chemicals Mentioned
- **PLA plastic** — 3D-printed body (~300g, three parts); cost ~£5.40 at ~£2/kg
- **N35 neodymium magnets** — 1 cm diameter, 2 mm thick; pressed into recesses in the rotor base
- **32 gauge enamel-coated copper wire** — used to wind the serpentine coil (confirmed in comments)
- **Steel rod** — acts as the central axle/guide pin for the rotor
- **Bearing** — pressed into the rotor bottom to prevent axial displacement
- **Bridge rectifier** — converts AC output to DC for the load/LED

## Techniques and Methods
- **3D printing (FDM/PLA)** — rotor and stator housing printed in three parts to avoid support material waste; uses Elegoo printers
- **Serpentine coil winding** — single flat coil with 36 sub-coils, wound in ~15 minutes (detailed in video 1859)
- **Rim-driven generator layout** — magnets embedded in the rotating rim pass over a stationary serpentine coil below
- **Bridge rectification** — AC output from coil converted to DC via a bridge rectifier
- **Load testing** — output measured against a calibrated resistive load using a BK Precision instrument, with wind speed monitored by a handheld anemometer

## Notable Timestamps
- `[00:00]` — Introduction; references video 1867 on rim-speed vs. hub-torque concept
- `[00:28]` — Presents the completed Savonius-style turbine and describes the three-part printed design
- `[00:55]` — Describes the N35 neodymium magnets (1 cm × 2 mm) placed in the rotor base
- `[01:14]` — Design philosophy monologue: simplicity enables manufacturability
- `[03:43]` — Assembly sequence: magnets in base, bearing, steel rod, serpentine coil fitted to stator
- `[04:47]` — Cost breakdown: ~£5.40 plastic, ~£3.60 magnets, 35p wire; total ~£9 prototype
- `[06:01]` — Live demo: turbine connected to LED, powered by blowing
- `[06:34]` — Surprised reaction: turbine lights LED from breath alone
- `[07:00]` — Formal test setup: BK Precision resistive load, fan, anemometer
- `[07:37]` — Measured output: ~2V, 12–14mA at low wind speed
- `[08:01]` — Declares the rim-driven concept validated; closes with design principles summary

## Robert's Own Replies
- **Measured performance:** At 1.7 m/s (≈4 mph) wind, the turbine produced ~24mW — comparable to or slightly better than other Savonius-type turbines of similar size under the same conditions, achieved via a different design paradigm (rim-driven vs. hub-driven).
- **Scalability to a wind wall:** At 11 m/s wind, output would be ~6W per unit. A wall 2.4m × 1.8m (~167 units) could produce ~1kW at a total cost of ~£668 — he considers this competitive.
- **Wire specification:** 32 gauge enamel-coated wire was used for the serpentine coil.
- **Printer used:** Elegoo printers, used intensively; notes it's largely "horses for courses" between brands.
- **Blade material:** Suggests cloth as the simplest, most hardwearing option for blades.
- **Simplicity clarified:** Distinguishes between "simple" and "simplicity" — the design philosophy aims to reduce component count and process steps, not to be naively crude. "The best part is no part."
- **Wind energy physics:** Emphasises that wind turbines extract available power; they don't generate it. Output is fundamentally limited by wind speed and swept area.
- **Preferred styles:** Chose Savonius as the most basic baseline; personally likes the Ugrinsky design.
- **Counter-rotation:** Notes counter-rotating blades could double relative speed but would introduce brush contact issues — though certain configurations could avoid brushes.
- **Electrics potting:** Suggests the electronics can be potted (encapsulated) in the base for weatherproofing.
- **Wind wall goal:** Confirms the long-term aim is a modular wind wall; has done videos with up to 100 units.
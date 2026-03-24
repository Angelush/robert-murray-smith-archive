## Overview
Robert Murray-Smith demonstrates how to paint a flat panel radiator onto almost any surface using a heat-resistant conductive ink he developed. The process involves laying copper tape electrodes, brushing on 2–3 coats of the ink, and sealing it with a protective coating, resulting in a 2 sq ft panel drawing ~35W at 44°C. His central claim is that this technology could make traditional bulky radiators obsolete.

## Key Topics
- Construction of a painted panel heater on MDF
- Choice of substrate materials suitable for the heater
- Copper tape electrode placement and connection methods
- Voltage, current, and resistance considerations for safe operation
- Protective coating options for the finished heater
- Possibility of painting heaters directly onto walls, floors, or ceilings
- Running the heater from AC or DC power sources

## Materials and Chemicals Mentioned
- **Heat-resistant conductive/resistive ink** — the core heating element, painted onto the substrate (silicate-based, per author comments)
- **MDF (Medium Density Fibreboard)** — used as the substrate in this demo
- **Copper tape** — used as bus-bar electrodes at each end of the panel
- **Plastic film / window-frost film** — used as a protective overlay on the painted surface
- **Silicone-based paint** — recommended top coat when painting directly onto walls, in any chosen colour
- **Plasterboard** — mentioned as a suitable alternative substrate
- **Masking tape** — suggested for clean edges during painting

## Techniques and Methods
- Laying copper tape strips as electrodes along opposite edges of the substrate
- Bending copper tape tails to form connection points (also: bolt or crimp alternatives mentioned)
- Brush-applying 2–3 coats of heat-resistant ink, allowing ~1 hour drying between coats
- Resistance testing after each coat (target: just below 10 ohms) to determine readiness
- Applying protective film overlay or silicone paint topcoat
- Using a benchtop DC power supply to dial in voltage/current for temperature control
- Using a light dimmer as a low-cost current-limiting option for AC supply
- Using a K-type thermocouple + PID controller for temperature regulation (mentioned in comments, e.g. for underfloor applications)

## Notable Timestamps
- `[00:05]` — Introduction: finished panel heater shown running at 35W, 44°C
- `[00:51]` — Overview of substrate options (MDF, plastic, plasterboard, wall, floor, ceiling)
- `[01:55]` — Copper tape electrode laying demonstrated
- `[02:30]` — Voltage drop and width limit explained (~600 mm max width, ~40V safety limit per UK wiring regs)
- `[03:14]` — Ink painting demonstrated with a brush
- `[04:08]` — Drying and resistance testing explained
- `[04:30]` — Protective film overlay applied
- `[04:57]` — Power supply connection and switch-on
- `[05:48]` — Summary and wall-painting use case revisited
- `[06:42]` — AC vs DC operation and current-limiting discussed

## Robert's Own Replies
- **The ink is no longer sold commercially**, but Robert made a separate video showing how to make it yourself (available in his "ink making" playlist).
- The ink is **silicate-based**, giving it low flexibility — suitable for the flex most buildings experience, but not for cloth; he was working on a flexible cloth version at the time.
- For **underfloor heating** applications, he recommends painting it directly onto concrete and tiling over it, using a K-type thermocouple + PID controller kit (available as underfloor heating kits) to keep temperature below 60°C.
- He confirmed it could work well **under floors** and potentially as a **seed propagator**.
- He references a follow-up video ("A Painted Radiator On House Mains (A/C)") where he runs the heater at 40V on mains AC.
- Material cost for the ink is approximately **a dollar or so** per panel.
## Overview
Robert revisits his Pelton wheel-style wind turbine, upgrading from a three-blade to a six-blade design based on community feedback. Testing the new version in real wind and with a fan, he measures a tip speed ratio (TSR) of 5 — better than the expected 4 — concluding that the design has genuine promise and warrants further optimization despite being crudely built.

## Key Topics
- Iteration on the Pelton wheel wind turbine design (3-blade → 6-blade)
- Community-driven improvements: filling blade gaps and removing the top cap to allow wind exhaust
- Real-world wind testing at ~3–5 m/s
- Voltage output measurement (~1.1–1.2 V at ~4 m/s)
- RPM measurement using a tachometer and retroreflective tape (~2448–2900 RPM)
- Tip Speed Ratio (TSR) calculation and what it means for turbine efficiency
- Power available in wind vs. power extractable at small scale

## Materials and Chemicals Mentioned
- Retroreflective (retro-reflective) tape — used as a marker stripe for tachometer readings

## Techniques and Methods
- Wind turbine blade doubling (3 → 6 blades) with no-exit top removed to allow wind exhaust
- Field wind speed measurement (anemometer reading ~3–5 m/s)
- Voltage output measurement from the turbine generator
- RPM measurement using an optical tachometer (Rigol DM3058E multimeter with tachometer function) and a single retroreflective tape strip
- Tip Speed Ratio (TSR) calculation from measured RPM and wind speed
- Fan-based controlled wind simulation for bench testing

## Notable Timestamps
- `[00:00]` — Introduction; recap of the original 3-blade Pelton wheel turbine
- `[00:26]` — Reveal of the new 6-blade version; explanation of airflow and exhaust improvement
- `[00:44]` — Outdoor wind test begins at ~3 m/s
- `[02:39]` — Results reported: ~1.1–1.2 V output at ~4 m/s wind speed
- `[02:51]` — Tachometer setup explained; retroreflective tape introduced
- `[03:33]` — RPM readings: 2448 → 2600 → 2900 RPM during fan test
- `[04:06]` — Power analysis: small scale context (10 cm × 14 cm), ~9 mW available at 1 m/s, ~100 mW at 4 m/s
- `[04:42]` — TSR calculation result: **TSR = 5** (expected 4, typical good ~6, exceptional ~8)
- `[05:05]` — Conclusions: promising result despite wobble and lack of optimization; further investigation warranted

## Robert's Own Replies
Robert engaged actively in the comments, primarily to defend the tachometer methodology:
- The tachometer reads **only the single retroreflective strip**, not the individual blades — he explicitly pointed this out in the video.
- After a commenter questioned the accuracy, Robert re-ran the experiment with the strip repositioned **above the blades** and confirmed the reading was unchanged, categorically stating it is counting only the strip.
- He noted that accurately hand-counting RPM at that spin rate would be nearly impossible anyway.
- He identified the multimeter used as a **Rigol DM3058E**.
- He briefly acknowledged a suggestion about a "Waters turbine" as an interesting related concept.
- Remaining replies are brief acknowledgements (`cheers mate`, `I appreciate that`) with no additional technical content.
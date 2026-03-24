## Overview
Robert explores whether salvaged PC fans can be converted into wind generators and assembled into a "wind wall" — a flat panel of recycled fans mounted on a plywood board. After converting 100 fans to generators and mounting them with carefully spaced holes, he discovers the plywood board acts as an orifice plate (a simplified Venturi), significantly boosting power output. Outdoor testing in a Canterbury car park suggests the wall performs comparably to a commercial horizontal-axis wind turbine (HAWT) of equivalent swept area.

## Key Topics
- Converting PC fans from motors to generators by desoldering and resoldering the stator coils
- Disappointing power output of a single unconverted/unmounted fan (~microamps)
- The dramatic improvement (microamps → milliwatts, ~1000×) from mounting fans in a drilled plywood board
- Orifice plates as a cheap alternative to Venturi tubes for accelerating airflow
- Bernoulli's principle and its application to ducted/shrouded wind turbines
- Wiring 100 generators in parallel columns to combine current output
- Comparison against a Savonius-type wind wall (made from water guttering) ahead of a planned "wall-off" on a hill

## Materials and Chemicals Mentioned
- **PC case fans (80 mm and 120 mm)** — salvaged from old equipment, converted to generators
- **18 mm plywood** — used as the mounting board / orifice plate
- **Rectifiers (small diode bridges)** — one per fan to convert AC to DC
- **Filament light bulb** — used as a resistive load during outdoor testing
- **LED** — used as an indicator load during bench testing
- **Solder / tinned wire** — for reconnecting stator coil leads (L1 and L2)

## Techniques and Methods
- **Fan-to-generator conversion** — removing the stator board, identifying the three coil legs (L1, L2, L3) by resistance measurement (44 Ω each end-to-end, 88 Ω across both), then soldering output wires to L1 and L2
- **Orifice-plate wind ducting** — drilling 78 mm holes spaced 120 mm apart in 18 mm plywood to create a cheap Venturi effect that accelerates wind through each fan
- **Parallel wiring in columns** — 10 columns × 9 rows of fans wired in parallel per column, summing current while keeping voltage constant
- **Wind speed measurement** — using a handheld anemometer; cross-referencing with a HAWT online calculator (Omni Calculator) to estimate expected power
- **Power measurement** — reading voltage and current separately under resistive (light bulb) and LED loads to estimate milliwatt-level output

## Notable Timestamps
- `[00:00]` — Introduction: PC fans as wind generators, overview of the project
- `[01:00]` — Stator removal and coil identification (L1, L2, L3); resistance-based identification method
- `[01:47]` — Single fan test: measured output is only microamps at 3.5 m/s wind
- `[03:28]` — Single fan mounted in a card shroud: output jumps from microwatts to milliwatts (~1000× improvement)
- `[04:49]` — Time-lapse: converting all 100 fans (took one full day)
- `[06:32]` — Drilling plywood board and mounting all 100 fans
- `[07:38]` — Outdoor night test with blower: ~12 mA at ~3 V (~30 mW) from the single-fan prototype
- `[08:49]` — Explanation of Bernoulli's principle and Venturi tubes
- `[10:39]` — Introduction of the orifice plate concept and why the plywood board functions as one
- `[13:04]` — Wiring explanation: rectifiers, parallel columns, final output leads
- `[14:52]` — Full wind wall outdoor test in Canterbury car park: ~3.4 W at 2.4 m/s wind over 1.2 m × 1.08 m area
- `[17:54]` — Comparison with the Savonius-type wind wall; teaser for an upcoming "wall-off" on a hill

## Robert's Own Replies
- Clarified that the connecting wire from the stator leads goes directly to the rectifier (answering a likely comment about wiring).
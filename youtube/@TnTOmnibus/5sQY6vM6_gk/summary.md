## Overview
Robert Murray-Smith presents an omnibus episode covering the development of his "vortex" cylindrical wind turbine — a ring-shaped rotor with an Archimedes screw interior and integrated generator. He demonstrates how to measure static torque to evaluate wind capture device performance, shows that adding fins to a flying-gyroscope-style rotor produces roughly a fivefold increase in torque, and walks through the full electronics chain from AC coil output through rectification and capacitor smoothing to usable DC. The episode concludes with TinkerCad tutorials for producing cube and hexagonal ("wind wall") housing variants, plus weatherproofing techniques.

## Key Topics
- Measuring static torque to evaluate wind turbine rotor designs without a complete generator
- The flying gyroscope as a wind turbine concept (ring-wing / annular airfoil)
- Effect of external vs. internal airfoil bumps on torque output
- Effect of adding fins (internally and externally) to the cylindrical rotor
- Archimedes screw interior fins integrated into the cylindrical rotor
- Integrated generator design: neodymium magnets embedded in the rotor cylinder, serpentine coil in the stator
- Coil winding theory: turns, wire gauge, voltage, current, and power relationships
- Custom coil-winding machine for hair-thin wire
- AC-to-DC conversion using a bridge rectifier and electrolytic capacitor
- TinkerCad workflow for designing cube and hexagonal wind-wall housings
- Weatherproofing with potting compound or paraffin wax
- "Wind Cube" and "Wind Tube" as stackable modular turbine concepts

## Materials and Chemicals Mentioned
- **Neodymium magnets** (1 cm × 3 mm) — embedded in the rotor cylinder in a north-south alternating pattern to form the rotor of the integrated generator
- **Superglue** — used to fix magnets in place
- **32 SWG (Standard Wire Gauge) copper wire** — hair-thin magnet wire used for the 1,000-turn coil
- **Electrician's tape** — used to bind and hold the wound serpentine coil together
- **Electrolytic capacitor** (1,000 µF / 50 V) — used to smooth rectified DC output
- **Bridge rectifier module** (2 A / 1,000 V) — bought in bulk from eBay, used to convert AC to DC
- **Paraffin wax / potting compound** — mentioned for weatherproofing the electronics cavity
- **PLA or similar 3D-print filament** — implied throughout for all printed parts (not stated explicitly)
- **8 mm skate bearings** — used as radial and thrust bearings in the rotor cradle

## Techniques and Methods
- **Static torque measurement** — attaching a lever arm (150 mm) to a stalled rotor, pressing against a digital scale at a known angle (45°), measuring grams, then calculating torque via T = r·F·sin θ
- **Comparative torque benchmarking** — testing the new rotor against a standard propeller blade of equal swept area to cancel out experimental errors
- **3D modelling in TinkerCad** — using SVG Revolver to create airfoil-profile ring bodies; using boolean hole/merge ("cookie cutter") operations to produce cube and hex housings
- **SVG export/import workflow** — exporting an NACA 2414 airfoil from TinkerCad as SVG then re-importing into the SVG Revolver primitive to revolve it 360°
- **STL scaling re-import** — exporting as STL and re-importing at 10,000% to rescale without distortion
- **Serpentine coil winding** — winding a large flat circular coil on a custom-built hand-cranked winding machine; coil castellated to match magnet pitch
- **Coil sizing calculation** — coil diameter derived from (tape width + magnet pitch) × number of magnets
- **Wire gauge selection** — determined by expected power output (from Omni Calculator wind turbine tool), volts-per-turn measurement, and current-carrying capacity of the chosen wire
- **AC-to-DC rectification** — bridge rectifier followed by electrolytic capacitor for smoothing; optional DC-DC buck-boost converter for regulated output
- **Bearing assembly** — 8 mm rod with washers sandwiching skate bearings in printed cradle; separate thrust bearing to handle axial load
- **Weatherproofing** — filling the electronics bay with potting compound or paraffin wax after assembly

## Notable Timestamps
- `[00:00]` — Introduction: why measuring total turbine output can mislead; need to isolate rotor performance
- `[01:44]` — Static torque test rig described: fan, cradle, anemometer (1.8 m/s), 150 mm lever arm, digital scale
- `[03:24]` — Explanation of static vs. dynamic torque
- `[04:09]` — Warning: average multiple readings (×10); converting grams to Newtons; torque formula T = rF sin θ
- `[05:52]` — Using Omni Calculator to compare measured torque against theoretical blade torque; benchmark test with standard propeller blade
- `[07:21]` — Results: standard blade ~8 g, new vortex rotor ~1.6 g — early indication worth pursuing
- `[08:27]` — Introduction of the flying gyroscope concept as potential wind turbine
- `[09:27]` — TinkerCad workflow: NACA 2414 airfoil from Thingiverse, SVG Revolver, 360° revolution
- `[12:16]` — Two variants printed: airfoil bump on outside vs. inside; static torque comparison (1.6 g vs. 1.2 g)
- `[13:43]` — Discussion of ring-wing aerodynamics: lift-induced drag reduction vs. parasitic drag trade-off
- `[14:01]` — Adding external fins: nearly fivefold torque increase demonstrated
- `[16:29]` — Archimedes screw interior fins added; integrated magnet/coil generator concept introduced
- `[17:27]` — TinkerCad design of full rotor assembly: parabolic inlet cone, skate bearings, thrust bearing, magnet slots
- `[18:45]` — Magnet installation: 1 cm × 3 mm neodymium, north-south pattern, fixed with superglue
- `[21:22]` — First light-up test: tiny turbine lighting an LED bulb from fan airflow
- `[23:18]` — Wire selection theory: expected power from Omni Calculator, volts-per-turn, current capacity, wire gauge
- `[26:07]` — Custom coil-winding machine for 32 SWG wire; 1,000-turn coil
- `[33:38]` — Wind Cube final design: 150 × 150 × 150 mm, tighter magnet-coil tolerance, 1,000-turn SWG 32 coil
- `[35:54]` — Open-circuit voltage test of Wind Cube; voltage climbs dramatically with fan on
- `[36:44]` — AC-to-DC conversion: bridge rectifier wiring, capacitor smoothing, DC voltage demonstration
- `[40:31]` — Full DC output test with fan at 4–4.5 m/s
- `[41:55]` — Wind Tube variant (round cowl, pole-mount ready) introduced
- `[43:27]` — TinkerCad tutorial: converting Wind Tube to Wind Cube using boolean cookie-cutter method
- `[45:28]` — Hexagonal Wind Cube variant for honeycomb stacking
- `[47:04]` — Weatherproofing discussion: split-cowl pan design filled with potting compound or paraffin wax

## Robert's Own Replies
- **Connecting multiple turbines in a wind wall in series/parallel:** Robert advises wiring each turbine individually rather than in parallel, because if outputs differ, higher-output units would act as a battery driving lower-output units as motors. He notes wind uniformity across a wall would be poor and the combined system behaviour "may well be surprising."
- **Avoiding digital electronics / buck-boost converters:** He agrees with a commenter that a DC-DC buck-boost converter consumes 25–30 mA just to operate — significant for a small turbine. He suggests a capacitor-based voltage transformer (parallel-in, series-out) as an alternative, and mentions he previously built a fractal capacitor array for converting very high voltage / ultra-low current (microamps) to lower voltage / higher current output.
- **Coil geometry trade-offs (square vs. zig-zag):** He notes the square (serpentine) form wastes wire, but the zig-zag places wire at an angle to the magnetic field, reducing output per unit wire length — he is unsure which is better overall.
- **Using the design as an impeller:** Robert says he would try the cylindrical rotor as an impeller too, noting "it has promise."
- **Channel scope:** He explains the channel cannot focus exclusively on wind turbines as that would quickly become dull for both him and viewers — variety is intentional.
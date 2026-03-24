## Overview
Robert demonstrates a 3D-printed, modular wind wall based on the Ugrinsky rotor design, built as a self-contained axial flux generator unit. The goal is to create a cheap, scalable, tile-able energy harvesting system from low-grade ambient wind. He argues that cost and simplicity matter more than peak efficiency, and that injection-molded production could bring unit costs down to cents.

## Key Topics
- The Ugrinsky rotor design and its claimed efficiency (contested in literature)
- Design philosophy: prioritising low cost over maximum efficiency
- Modular, stackable 3D-printed construction for accessibility
- Axial flux generator configuration using permanent magnets
- Serpentine coil stator winding
- Scalability: stacking modules vertically and connecting multiple units in series or parallel
- Power output estimates at realistic wind speeds

## Materials and Chemicals Mentioned
- **PLA/FDM filament** — used for 3D printing all structural parts
- **N35 neodymium magnets** — 10 mm diameter, 2 mm thick, arranged N-S-N-S on rotor and base plate
- **8 mm steel bar** — central shaft/pin
- **Ball bearings** — 12 mm OD × 8 mm ID (two sets, 4 mm deep each)
- **Thrust washer** — 47 × 11 mm (25 mm gap variant)
- **Enamelled copper wire** — for the serpentine/Lenz coil wound on the stator former
- **Resin or sealant** — mentioned in comments as optional gap filler for the generator housing

## Techniques and Methods
- **3D printing (FDM)** — all structural components printed modularly to fit a wide range of printer bed sizes
- **Serpentine (Lenz) coil winding** — coil wound around a printed former and pressed onto stator uprights
- **Axial flux generator assembly** — opposing magnet plates on rotor and base create axial flux across the stator coil
- **Modular stacking** — rotor sections glued vertically to reach desired height (~70 mm per module)
- **Series/parallel electrical connection** — multiple units connected depending on desired voltage or current output
- **Live demonstration** — fan used to spin the rotor, output measured with voltmeter and connected to a light bulb

## Notable Timestamps
- `[00:00]` — Introduction: Robert explains his fascination with wind walls and lists previous build materials
- `[00:50]` — Introduces the Ugrinsky design and discusses the efficiency debate in research literature
- `[01:55]` — Explains the cost argument: cheap enough beats most efficient
- `[02:30]` — Shows the 3D model remix and explains the modular rotor design
- `[03:11]` — Rotor dimensions: 70 mm per module, 120 mm wide, ~490 mm total assembled height
- `[03:36]` — Bottom piece assembly: thrust washer, magnets, 8 mm shaft
- `[04:13]` — Rotor stacking and top bearing installation
- `[04:52]` — Stator assembly: coil former, serpentine coil, cap, and central bearing
- `[05:57]` — Second magnet plate added to complete the axial flux generator
- `[06:23]` — Module integration overview: wiring, electronics cavity, parallel/series connection options
- `[07:15]` — Live test: fan blows across rotor, light bulb lights up, voltage measured
- `[08:26]` — Power output estimates: ~17 W at 12.5 m/s for one unit; ~500 W for 10 units in a row at that wind speed
- `[08:51]` — Files uploaded to Thingiverse, link in description

## Robert's Own Replies
- Confirmed he already made a video on the core electronics/system for this type of setup (linked `https://youtu.be/r9dVWEo1ykk`).
- Clarified that the generator housing gap does not need sealing — it only contains enamelled copper wire and already has a drain hole; resin/sealant is optional.
- Addressed a flux-switching suggestion: explained it introduces **cogging** and significantly higher **start torque**, which is undesirable for a low-wind-speed harvester.
- Confirmed that doubling up rotors would **not** double output.
- Noted that adding more blades increases the **force required to turn** the rotor.
- Expressed enthusiasm for a commenter's idea of using **cloth** for blades, encouraging them to try it.
- Acknowledged that he does not test efficiency in every video, as it would make videos repetitive and excessively long.
- Agreed that a **multi-pronged energy approach** is needed (not wind alone).
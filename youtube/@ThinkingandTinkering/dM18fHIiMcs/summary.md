## Overview
Robert demonstrates the assembly and testing of video #1877 in his series: a maglev-bearing wind turbine using a squirrel cage rotor and a rim-based flat-pack pancake generator, all built primarily from 3D-printed parts. The design avoids axle connections entirely by placing magnets around the rim, and uses repelling ring magnets as a frictionless thrust bearing. In a light-wind outdoor test and a fan test at 3.4 m/s, it successfully lit an LED and produced approximately 4.5 volts.

## Key Topics
- Parts list and cross-references to prior videos (1859: coil making; 1868: rim generation; 1874: maglev with Savonius turbine)
- Maglev (magnetic levitation) thrust bearing using repelling ring magnets
- Rim-based flat-pack pancake generator design (no axle connections required)
- Squirrel cage rotor as the wind capture element
- 3D-printed two-part construction via TinkerCAD
- Outdoor wind test and fan bench test results
- Hurricane/storm protection options
- UK average wind speed context (~4–4.5 m/s) and low-wind-start design philosophy

## Materials and Chemicals Mentioned
- **0.1 mm magnet wire** — 400 turns forming the serpentine coil
- **Ceramic ring magnets** — 72 mm OD, 32 mm ID, 10 mm thick; used as the maglev thrust bearing pair
- **N35 neodymium magnets** — 1 mm × 1 cm; arranged north–south alternately around the rotor rim for generation
- **Steel bar** — 8 mm thick (from B&Q); serves as the central spike to prevent the maglev magnets from flying apart
- **Skate bearings (608)** — 22 mm OD, 8 mm ID, 7 mm thick; ceramic variant chosen for this build
- **Potting compound** — suggested for weatherproofing/sealing the stator against the environment

## Techniques and Methods
- **Serpentine coil winding** — 0.1 mm wire, 400 turns, with tape markers for alignment (detailed in video 1859)
- **3D printing** — two-part design (stator base + rotor cage) modelled in TinkerCAD
- **Rim-based generation** — magnets glued around the rotor rim pass over the stationary serpentine coil; no rotating electrical connections needed
- **Maglev thrust bearing** — two same-pole-facing ceramic ring magnets repel each other; a central steel spike prevents lateral escape
- **Coil installation** — tape marks used to orient and slot the coil around the stator
- **Potting/encapsulation** — pouring potting compound into the stator for long-term weatherproofing
- **Wind and fan testing** — outdoor test with light breeze (LED illumination), bench test with fan at 3.4 m/s measuring output voltage

## Notable Timestamps
- `[00:00]` — Introduction; Robert explains his parts-list format and references to prior videos
- `[00:22]` — Serpentine coil described (0.1 mm wire, 400 turns); reference to video 1859
- `[00:47]` — Maglev bearing system explained; reference to video 1874
- `[01:16]` — Rim-based generation concept explained; reference to video 1868
- `[01:55]` — TinkerCAD two-part design walkthrough (yellow stator base, blue squirrel cage rotor)
- `[02:14]` — N35 neodymium magnets (1 mm × 1 cm) described; bearing hole and skate bearing specs
- `[03:17]` — Assembly: ring magnets oriented to repel, steel spike, coil slotted in
- `[05:00]` — Outdoor test: turbine spins in light breeze and lights an LED
- `[05:25]` — Fan bench test: 3.4 m/s airflow → ~4.5 V output
- `[06:19]` — Hurricane protection: remove rotor or seal with potting compound
- `[06:57]` — Summary and closing remarks on the modular, experimental nature of the design

## Robert's Own Replies
- **Bearing specification:** Clarified that the bearings are standard 608 skate bearings — 22 mm OD, 8 mm ID, 7 mm thick.
- **Current output:** Confirmed output current is approximately **35 mA** at the tested wind speed.
- **Magnet upgrade (N35 → N52):** Explained that switching to N52 magnets would improve output because EMF = BLV sin θ — a stronger magnetic field (B) directly increases voltage; he encouraged viewers to try it and share results.
- **Wiring simplicity:** Clarified that each end of the coil connects directly to the positive and negative of the meter or LED — no additional circuitry needed.
- **Physics reminder:** Confirmed that higher voltage is achievable with better magnets, but power out is always less than power in — you cannot exceed what the wind provides.
- **Enclosure / PowerPod:** Noted that adding an enclosure to this design essentially makes it the "PowerPod" (a related project in his series).
- **Measuring amps:** Explained his reasoning for focusing on volts rather than amps during iterative development — since losses in the generation system are constant, voltage is a sufficient comparative metric at this stage.
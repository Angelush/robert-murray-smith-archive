## Overview
Robert Murray-Smith demonstrates how to use 3D-printed planetary gear systems to increase the output voltage of a repurposed PC fan motor acting as a generator. He explains the fundamental generator voltage equation (E = BLv sinθ) and shows that speed is the key variable when the generator is fixed. The video ties directly into his prior work at a windmill, arguing that stacked planetary gears are an elegant, modular solution for matching a slow wind turbine's torque output to the high RPM requirements of a standard generator.

## Key Topics
- Generator voltage equation: E = BLv sinθ, and why speed is the primary controllable variable
- Repurposing a PC fan motor as a small generator
- Types of gearing: magnetic gearing, straight gears, and planetary gear systems
- Planetary gear anatomy: ring gear, sun gear, planet gears, planetary carrier
- Gear ratio mathematics: stacking stages for multiplicative speed increase (3×, 9×, 27×…)
- Torque/speed trade-off and how load torque propagates back through the gearbox to the turbine
- Application to wind turbines: matching slow, high-torque rotor output to high-RPM generator input
- 3D printing gears in Tinkercad; design rationale for chunky/robust geometry

## Materials and Chemicals Mentioned
- PC fan motor (repurposed as a generator)
- 3D-printed plastic planetary gear components (ring gear, sun gear, planet gears, planetary carrier)

## Techniques and Methods
- Disassembly of a PC fan to extract the brushless motor/generator core
- CAD design of modular planetary gear stages in Tinkercad
- FDM 3D printing of gear components
- Stacking/compounding planetary gear stages to achieve multiplicative gear ratios
- Live voltage measurement with a multimeter while hand-spinning the gear assembly
- Demonstration of torque-to-speed conversion relevant to wind turbine generator coupling

## Notable Timestamps
- `[00:08]` — Recap of previous video: PC fan motor stripped down as a generator
- `[00:28]` — Explains the generator voltage equation (BLv sinθ) and why speed matters
- `[01:15]` — Overview of gearing options: magnetic, straight, and planetary
- `[01:34]` — Detailed explanation of planetary gear anatomy and gear ratio calculation
- `[02:20]` — Gear ratio of 3:1 demonstrated; concept of stacking for 3×, 9×, 27× multiplication
- `[03:50]` — Live demo: single-stage assembly tested, ~0.5 V output
- `[04:19]` — Sun-and-planet arrangement added; noticeably higher voltage achieved
- `[05:06]` — Three-stage stack (27×) assembled and spun — "Madness" result
- `[05:28]` — Fourth stage added, even higher voltage demonstrated
- `[05:54]` — Connects experiment back to wind turbine gearing problem discussed at Crabble Mill
- `[07:14]` — Closing remarks on chunky design rationale and modular planetary gear system

## Robert's Own Replies
- **Chunky design is intentional but not the only option:** Confirms that slimmer designs could work; he prefers chunky for visibility in demonstrations and mechanical robustness under load with plastic parts.
- **Torque scaling:** Clarifies that torque increases in the same ratio as speed through the gearbox, plus a small additional factor for mechanical losses.
- **Variable transmission idea:** Showed interest in the concept of a variable transmission applied to this system, responding with "like a variable transmission?" — suggesting he found it a worthwhile direction to explore.
- **General encouragement:** Several brief supportive replies ("cheers mate", "awesome", "up and coming mate") acknowledging viewer comments and ideas.
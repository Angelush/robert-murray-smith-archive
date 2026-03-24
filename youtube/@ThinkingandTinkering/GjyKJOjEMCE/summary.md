## Overview
Robert demonstrates how to convert a common PC fan into a wind generator by modifying its brushless motor stator, then uses the resulting test rig to compare the toroidal propeller against a standard PC fan blade for electrical generation efficiency. The experiment shows the toroidal propeller produces significantly less voltage (~1.8V) than the standard fan (~4–5V) under the same airflow, though Robert frames the result as a starting point for further exploration rather than a definitive verdict.

## Key Topics
- Converting PC brushless motors (OutRunner type) into generators
- Understanding brushless motor anatomy: stator, rotor, coils, magnets
- Using resistance measurement to identify coil wire endpoints
- The EMF voltage formula: V = BLv sin θ (magnetic field, wire length, velocity, angle)
- Comparative testing of toroidal propeller vs standard PC fan blade as wind turbine blades
- Philosophy of building simple test rigs to evaluate design alternatives

## Materials and Chemicals Mentioned
- PC fan (brushless OutRunner motor)
- White split clip (internal rotor retention mechanism)
- Stator with two coils (~30 ohms each, ~61 ohms in series)
- Capacitor and IC (removed from stator control board)
- Red and black hookup wires (soldered to coil endpoints)
- Toroidal propeller (previously used in DIY air conditioning units)
- Hair dryer (used as a controlled airflow source for testing)

## Techniques and Methods
- Disassembling a PC fan by peeling the label, removing the split clip, and lifting out the stator
- Desoldering and snipping components (capacitor, IC) from the stator control board
- Identifying coil endpoints via resistance measurement: single coil ≈ 30 Ω, both coils in series ≈ 60 Ω
- Soldering output wires to the two highest-resistance pin pair on the stator
- Reassembling the modified stator as a standalone generator core
- Comparative voltage measurement using a multimeter under constant hairdryer airflow

## Notable Timestamps
- `[00:06]` — Robert explains his motivation: understanding, replicating, and sharing experiments
- `[00:33]` — Introduces the PC fan; references previous "wind wall" project (100 fans converted)
- `[01:00]` — Removes label and split clip to access the stator
- `[01:33]` — Frees stator wires and removes stator from housing
- `[02:01]` — Snips and desolders capacitor and IC from stator board
- `[02:30]` — Explains brushless OutRunner motor anatomy (rotor magnet outside, stator inside)
- `[03:00]` — Describes using resistance to find coil endpoints; measures ~30 Ω and ~61 Ω
- `[04:03]` — Solders red and black output wires to the two coil endpoints
- `[04:22]` — Reassembles the fan as a generator; reads 2–3V unloaded
- `[06:07]` — Removes blades to expose bare generator core; gets ~1.3V by hand spinning
- `[07:12]` — Introduces toroidal propeller and poses the central test question
- `[07:34]` — Explains EMF formula (BLv sin θ) and why speed is the only variable in this comparison
- `[09:27]` — Tests standard PC fan blade with hair dryer: ~4–5V
- `[09:36]` — Tests toroidal propeller with hair dryer: ~1.8V
- `[09:57]` — Acknowledges test limitations; encourages viewers to explore blade count, airflow direction, and other variables

## Robert's Own Replies
No author replies found.
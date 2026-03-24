## Overview
In this video, Robert tests the DIY generator section he built for a wind turbine project (introduced in video 1931), for which updated Tinkercad STL files are now available. He demonstrates two rectification approaches and explains the trade-offs between wiring the three coil outputs in series (adding volts) versus parallel (adding amps), before measuring actual output by hand-spinning the generator. The test yields roughly 22–26V and ~100mA (~2W), confirming the unit produces real usable power.

## Key Topics
- Overview of the generator's serpentine coil and neodymium magnet arrangement
- Two rectification strategies: rectifying each coil individually vs. a single three-phase rectifier circuit
- Series vs. parallel wiring of rectified coil outputs and their electrical implications
- Live hand-spin voltage test using a multimeter
- LED demonstration (requires ~20–25V turn-on voltage)
- Precision calibrated load test to read simultaneous volts and amps
- Introduction of a 3D-printed planetary gear system as the next step for the wind turbine build

## Materials and Chemicals Mentioned
- **Neodymium magnets** — used as the magnetic field source inside the generator
- **PLA filament** — 3D-printed parts (confirmed in author comments); often reinforced with CA (cyanoacrylate/superglue)
- **Rectifier diodes / rectification circuits** — used to convert AC output from each coil to DC
- **LED** — used as a demonstration load; turn-on voltage ~20–25V
- **100 ohm resistor load** — used alongside the precision calibrated load meter (~80 ohm coil resistance noted)

## Techniques and Methods
- **Individual coil rectification** — each of three serpentine coils rectified separately, producing three positive and three negative terminals
- **Three-phase rectification** (described as alternative) — all coils combined into one rectifier circuit for a single DC output
- **Series wiring** — chaining rectified coil outputs positive-to-negative to sum voltages
- **Parallel wiring** (described as alternative) — combining all positives and negatives to sum currents
- **Hand-spin testing** — manually rotating the generator cog to demonstrate output
- **Precision calibrated load measurement** — simultaneous voltage and current reading under a defined resistive load
- **Tinkercad STL file design** — 3D-printable enclosure and components made available for community adaptation

## Notable Timestamps
- `[00:07]` — Introduction; references previous video 1931 and announces updated STL files on Tinkercad
- `[00:35]` — Description of the generator internals: three serpentine coils around neodymium magnets, six exit wires
- `[01:00]` — Explains choice between individual coil rectification vs. three-phase rectification
- `[01:54]` — Explains series (adds volts) vs. parallel (adds amps) wiring trade-offs
- `[02:22]` — Wires coils in series; prepares to test with LED (~20V turn-on threshold)
- `[03:15]` — Hand-spin test with multimeter; reads ~28V
- `[03:33]` — LED lights up, demonstrating real power output
- `[03:59]` — Precision calibrated load connected with 100 ohm resistor
- `[04:26]` — Reads 22–26V and ~100–150mA under load; estimates ~2W output from hand-spinning
- `[04:46]` — Introduces planetary gear system as the next build step

## Robert's Own Replies
- **On testing vs. demonstration:** Clarifies this video is "demonstrating it does something" rather than a rigorous test; more detailed electronics coverage is in other videos.
- **On materials:** The 3D-printed parts are PLA, often strengthened with CA (superglue); he did a dedicated video on that technique.
- **On gearing necessity:** Explains that there is a physical limit to how fast you can hand-spin, so gears are essential to reach efficient operating speed — running too slowly drops voltage and makes the machine inefficient. "Tomorrow's video" would make this clearer.
- **On planetary gear slop:** He makes the inner gear 1mm wider in diameter before subtracting to create a little intentional slop, which prevents binding.
- **On the physics:** Confirms the relevant formula is BLV sin θ.
- **On boosting voltage for mains use:** Suggests adding a transformer.
- **On archiving:** Acknowledges his videos are hard to navigate and is assembling relevant ones into omnibus playlist editions to improve accessibility.
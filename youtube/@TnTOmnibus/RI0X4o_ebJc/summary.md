## Overview
Robert demonstrates how to build a hand-powered emergency phone charger using a treadle-crank mechanism, a 3D-printed gear train, a magnet disc, and a serpentine coil generator. The device converts arm or leg motion into electricity via a 9:1 gear ratio, passes the AC output through a rectifier and voltage regulator, and feeds a USB port — successfully charging a phone during testing.

## Key Topics
- History and mechanical efficiency of crank vs. treadle mechanisms
- 3D-printed generator design using TinkerCAD (disc with magnets, gear chain, coil cradle)
- Gear ratios and compound gear chains (3:1 × 3:1 = 9:1)
- AC generation and the need for rectification
- DC voltage stabilisation using a cheap LM2596S-based buck regulator board
- Serpentine coil design and Fleming's right-hand generator rule
- Edge-generation principle (magnets placed at the disc rim for higher tip speed)
- Human power output estimates (~60 W per arm, ~120 W legs, ~500 W full cross-ski body motion)
- Compact redesign with offset gear chain and single rocker arm

## Materials and Chemicals Mentioned
- **Neodymium magnets** — 1 cm × 3 mm circular disc magnets (first design) and 1 cm × 2 mm disc magnets (second design), polarised north–south alternately on the rotor disc
- **6 mm steel bar** — used as axles throughout
- **12 mm × 6 mm × 4 mm bearings** — standard bearing size used at all shaft locations
- **4 mm bar** — used in the compact redesign's crank pivot
- **Super glue** — used to fix cranks to the 6 mm bar
- **Enamelled copper wire (hair-thin)** — wound into the serpentine coil
- **LM2596S buck converter module** — voltage regulator chip, accepts 3–40 V in, outputs 1.5–35 V, rated 3 A

## Techniques and Methods
- **3D printing** — all structural parts (disc, cradle, uprights, cogs, coil former, feet) designed in TinkerCAD and printed in PLA/similar
- **Serpentine coil winding** — wire wound around a former with two-bolt jig on a wooden board, taped with tack strips, then transferred to the coil carrier
- **Gear chain assembly** — large/small cog pairs stacked on shared 6 mm axles to achieve compound 9:1 speed multiplication
- **Bridge rectifier wiring** — four diodes in diamond arrangement to convert AC to pulsed DC
- **Voltage regulator calibration** — adjusting the brass trimmer screw on the LM2596S board while monitoring output with a multimeter against a stable bench supply
- **Heat-gun bending** — used to correct a print geometry issue with the coil bracket
- **One-way (freewheel) clutch** — incorporated into the magnet disc hub in the compact redesign to allow smooth treadle motion

## Notable Timestamps
- `[00:00]` — Introduction: crank vs. treadle history and mechanical efficiency
- `[01:15]` — Singer treadle mechanism explained; penny farthing and railway pump trolleys
- `[02:17]` — First design overview: TinkerCAD disc, magnets, cradle, bearings, and axle assembly
- `[05:13]` — Live voltage test of first design with single coil — reads 1.3–1.5 V
- `[06:00]` — Electronics overview: why all generators produce AC and need rectification
- `[07:36]` — LM2596S voltage regulator board explained and calibrated live (10 V in → 5 V out)
- `[11:10]` — Gear upgrade: 60-tooth + 20-tooth cog giving 3:1, then 9:1 compound ratio
- `[13:58]` — Live test of geared version
- `[16:55]` — Magnet disc with one-way clutch; serpentine coil winding demonstration
- `[20:49]` — Animation/explanation: motor vs. generator principle
- `[24:28]` — Phone charging demonstrated successfully with first design
- `[25:05]` — Introduction of compact redesign with offset gear chain
- `[29:18]` — Live voltage test of compact design — peaks at ~7 V

## Robert's Own Replies
No substantive technical content; Robert posted only a brief "cheers mate" in response to a comment. No author replies found with additional insights.
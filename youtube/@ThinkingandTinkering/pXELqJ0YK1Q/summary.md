## Overview
Robert Murray-Smith walks through the complete setup process for the Elegoo Orangestorm Giga, the large-format 3D printer he built in the previous video (2265). The video covers everything from rewiring the power plug to suit UK standards, through auto bed leveling and Z-offset calibration, to manual bed screw adjustment. By the end the machine is fully calibrated and ready to print, with Robert pondering what ambitious first project to attempt.

## Key Topics
- Rewiring the proprietary European power plug to a UK standard plug
- The built-in RCBO safety device (combined MCB + RCD) and its significance
- Belt tension adjustment on the X and Y carriages
- Using the touchscreen interface for the first time
- Automated 100-point bed probing / leveling routine
- Z-offset calibration using the included steel shim
- Reading and interpreting the bed height map (tolerance ≤0.51 mm)
- Leveling the base frame with adjustable feet before leveling the bed
- Manual bed screw adjustment via the platform measurement menu
- Software overview: Elegoo Cura on the included USB stick

## Materials and Chemicals Mentioned
- **PEI sheet** — the print surface sheet used during normal printing (swapped out during bed screw adjustment for holed alignment plates)
- **Steel shim (feeler gauge)** — supplied in the kit; used to set the correct Z-offset gap between nozzle and bed
- **Filament** — mentioned generically as the next step once setup is complete; specific material not yet chosen

## Techniques and Methods
- **Continuity testing** of mains wiring before rewiring the plug to UK standard
- **Automated 100-point bed probing** — machine heats bed to 60 °C and nozzle to 140 °C, then probes a 10×10 grid
- **Z-offset calibration** — iterative adjustment in 0.1 mm increments using the touchscreen until the steel shim slides with a firm but smooth resistance
- **Base leveling** — adjusting the four corner feet with a 19 mm spanner and locking nut so the heavy steel frame sits level before touching the bed
- **Manual bed screw adjustment via platform measurement menu** — moving the print head to each screw position, reading the deviation in mm, and turning the Allen-key screw until the reading reaches zero
- **Re-running full auto-level after manual adjustment** to confirm the high-low variance is within the 0.51 mm tolerance

## Notable Timestamps
- `[00:08]` — Introduction; context from build video 2265
- `[00:16]` — Proprietary power cable and European plug issue explained
- `[00:38]` — Rewiring to UK plug; continuity check of wire colour coding
- `[02:00]` — Discovery of the built-in RCBO safety device
- `[02:50]` — Belt tension adjuster mechanism on the carriages
- `[04:13]` — First power-on; touchscreen overview
- `[04:24]` — Starting the auto bed leveling / probing routine
- `[05:18]` — Z-offset calibration with steel shim, step-by-step
- `[07:44]` — Reading the bed height map; 0.51 mm tolerance explained
- `[08:03]` — Base leveling with adjustable feet and 19 mm spanner
- `[09:22]` — Manual bed screw adjustment via Settings → Advanced → Platform Measurement
- `[11:15]` — Re-running full auto-level after manual adjustment; confirming within tolerance
- `[12:15]` — Machine declared ready; Elegoo Cura software overview

## Robert's Own Replies
- **Shim is just a feeler gauge**: confirmed the included steel shim is simply a standard feeler gauge — "simplest is always best."
- **No firmware update needed** (at time of filming).
- **Glue sticks**: was considering whether to use them for adhesion; leaning toward trying without first, and if failures mount up, printing a multi-stick holder.
- **Print ideas**: repeatedly mentioned wanting to print a **life-size terracotta warrior for the garden**, and separately referenced **Maria from Metropolis** as another inspiration.
- **Power draw / RCBO rating**: acknowledged a viewer's note that 16 A is plenty — "double the draw, which is going to be at most 8 A."
- **Video cadence**: confirmed he will continue making videos but "not at the rate I used to."
- **Personal note**: in one reply Robert mentioned that Elegoo had originally offered him the printer some time ago, that **Patti had agreed to where it could be placed**, and that when Elegoo renewed the offer he accepted — adding quietly, *"wow — that hurt to think about."* This is a rare, candid moment of grief visible in the comments (Patti was his late partner).
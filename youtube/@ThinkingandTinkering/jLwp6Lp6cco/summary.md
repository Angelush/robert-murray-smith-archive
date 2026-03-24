## Overview
Robert Murray-Smith demonstrates how to build a ratcheting continuously variable transmission (CVT) using 3D-printed parts and common hardware components. The video is a follow-up to his previous video on Evans cone drives, explaining why a ratcheting CVT is superior for wind turbine applications — it avoids the efficiency losses inherent in friction-based designs. He walks through assembly step by step, showing how shifting a pivot point changes the gear ratio.

## Key Topics
- Continuously variable transmissions (CVTs) and their role in wind turbines
- Limitations of friction-based CVTs (Evans cone drive, ~80% efficiency)
- Ratcheting CVT design principle: converting circular motion to linear via a scotch yoke, applying variable throw via a moveable pivot, then converting back to rotary via a ratchet
- How varying the pivot point position changes the effective gear ratio
- Using three ratchet units offset by 120° for smoother output
- Roller clutch as an alternative to a ratchet-and-pawl mechanism

## Materials and Chemicals Mentioned
- PLA and PLA+ filament (for 3D-printed parts)
- Stainless steel shelf supports (25 mm × 6 mm)
- Bearings: 12 mm OD × 6 mm ID × 4 mm deep; 22 mm bearings
- 8 mm bolt and nut
- 22 mm × 8 mm washer / skater bearing
- 8 mm steel bar (input/output shafts)
- Glue (painted over fixings)

## Techniques and Methods
- 3D printing parts in Tinkercad (files linked in description)
- Scotch yoke mechanism: converts rotary input to linear reciprocating motion
- Moveable pivot point: adjusting pivot height changes the throw length, giving variable ratio
- Ratchet-and-pawl mechanism: converts linear motion back to one-directional rotary output
- Duplicating the ratchet assembly on the reverse side for full-rotation engagement
- Three-unit arrangement (120° offset) to sum ratchet steps and smooth output torque
- Roller clutch as an alternative one-way drive mechanism

## Notable Timestamps
- `[00:00]` — Introduction; recap of previous video (Evans cone CVT) and wind turbine context
- `[01:00]` — Efficiency problem with friction CVTs (~80%); introduction of ratcheting CVT concept
- `[01:54]` — Overview of the Tinkercad design; parts list (shelf supports, bearings, bolt/nut)
- `[03:19]` — Explanation of how the moveable pivot point changes gear ratio
- `[04:40]` — Scotch yoke assembly walkthrough
- `[06:55]` — Ratchet and carrier assembly
- `[07:19]` — How the ratchet and pivot work together to produce variable output
- `[07:48]` — Need to duplicate assembly for full-rotation drive; three-unit arrangement for best performance
- `[08:53]` — Roller clutch as an alternative to ratchet-and-pawl

## Robert's Own Replies
- **On efficiency figures:** The ~80% efficiency figure applies to all friction-based CVTs (even if NASA-machined), not just his model. A ratcheting CVT with higher efficiency can raise total wind turbine machine efficiency above what a simple gear set achieves — this is why automakers are enthusiastic about CVT technology. Most wind turbines are only ~30% efficient overall, so CVT matching of rotor-to-generator speed can recover more than the transmission losses.
- **On the teaching model:** He is explicit that this is a teaching aid to demonstrate the logic, not a final compact design. A production model would be more compact but harder to learn from. The material (plastic, wood, metal) is irrelevant — the logic is the same.
- **On ratio range:** The ratio is effectively infinite and is set by the bar length at any given pivot position; it can be set to anything in between.
- **On ratchet-and-pawl vs. roller clutch:** He acknowledges both options and notes roller clutches are already used in production ratcheting CVTs.
- **On load requirement:** Ratchets need a load on the output shaft to engage properly; under no load, engagement suffers.
- **On bristle-based ratchets:** He made one a few months prior — notes it worked well and is a "much poorly understood method with a lot going for it."
- **On Google Scholar:** Recommends searching "ratcheting CVT" on Google Scholar (not main Google) — roughly 2,000–3,000 competing designs exist.
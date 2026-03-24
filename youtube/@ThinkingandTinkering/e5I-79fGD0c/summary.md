## Overview
Robert Murray-Smith demonstrates how to build a functional mechanical clock from 3D-printed parts, breaking the seemingly complex machine down into four simple subsystems: power, escapement, gear train, and display face. The video walks through assembling each subsystem step by step — from the rubber-band-powered drum motor and pendulum escapement to the gear trains for the minute and hour hands — reinforcing his core philosophy that complexity is just layered simplicity.

## Key Topics
- The four universal subsystems of any clock: power, escapement (time control), gear train, and display
- How an escapement releases power in fixed time increments
- Rubber band motor as an interchangeable power source
- Pendulum as the timing oscillator and regulator (bob height controls speed)
- Translation gear section: converting escapement output (~20 sec/rev) to a usable base period (120 sec/rev)
- Gear ratio mathematics for the minute hand (30:1 reduction) and hour hand (12:1 reduction)
- Direction of rotation management using intermediate/idle gears
- The modular, replaceable nature of each subsystem

## Materials and Chemicals Mentioned
- **Rubber band** — used as the power source for the drum motor
- **3D-printed PLA parts** — barrel/drum, ratchet wheel, anchor, pendulum bob, gear train components, face, supports
- **Skate bearings (608-type, 22×7×8 mm)** — used throughout for free rotation
- **Thrust bearings** — used in the drum assembly
- **8 mm steel bar (38 mm length)** — used for pendulum pivot and lever arm pins (optionally printed)
- **8 mm washer** — spacer to give clearance for free movement
- **10 mm and 4 mm spacers** — for positioning components along shafts
- **Glue** — for assembling fixed joints

## Techniques and Methods
- **3D printing (Tinkercad)** — designing and printing all structural components
- **Gear ratio calculation** — multiplying ratios across compound gear stages (e.g., 6:1 × 5:1 = 30:1 for minute hand; 3:1 × 4:1 = 12:1 for hour hand)
- **Press-fitting bearings** into printed housings
- **Timing the escapement output** empirically (measured at ~21.74 sec/rev, approximated to 20 sec for calculation)
- **Pendulum regulation** — adjusting bob height to tune beat period
- **Idle/direction gear insertion** — adding an intermediate gear to reverse rotation direction without affecting ratio
- **Subsystem decomposition** — breaking a complex machine into independently understandable and buildable modules

## Notable Timestamps
- `[00:00]` — Introduction: the subsystems philosophy applied to clocks (power, escapement, gear train, display)
- `[00:42]` — Review of prior work on escapements and rubber band motors
- `[02:42]` — Assembly begins: 3D-printed drum/barrel with ratchet, pressing in skate bearing
- `[03:36]` — Back face assembly: thrust bearing, steel bar pivot, pendulum release arm, spacers
- `[05:03]` — Top and bottom faces joined; rubber band anchor glued; escapement completed
- `[05:41]` — Pendulum bob assembly and how bob height regulates timing
- `[06:39]` — Gear train overview: translation section, minute hand section, hour hand section
- `[07:26]` — Timing the escapement output (~20 sec/rev); translation gears introduced
- `[08:36]` — Translation gear math: 25T → 50T (2:1, 40 sec) → 75T (3:1, 120 sec)
- `[11:59]` — Minute hand gear train: 30:1 reduction achieved via 6:1 × 5:1 compound gears
- `[14:50]` — Hour hand gear train: 12:1 reduction achieved via 3:1 × 4:1, co-axial with minute hand
- `[15:46]` — Face glued on, hands set to midnight; clock complete
- `[16:23]` — Closing philosophy: complexity = layered simplicity; power source is fully interchangeable
- `[17:44]` — Clock wound up and demonstrated running on the wall

## Robert's Own Replies
- **Files location**: The 3D print files are on Thingiverse, and gear/part details are in the Thingiverse description.
- **On electronic oscillators**: Clarified that a quartz oscillator (e.g., HC-49/S at 16 MHz) provides a stable timing signal; electronic control is essentially switching, not fundamentally different in logic from mechanical escapements. Pointed a commenter to the Wikipedia article on oscillators in timepieces.
- **On friction/durability**: Noted the clock has very little plastic-on-plastic contact because it is "full of bearings," so friction is not a significant concern.
- **On materials**: Confirmed that plastic pins can be replaced with steel (as he did for the pendulum and lever), or the whole thing could be built from wood — the logic remains the same.
- **On pendulum**: Confirmed that pendulum length dictates the beat, and that bearings are important for smooth operation.
- **On runtime**: Estimated the clock runs for about 10 minutes on a single wound rubber band, noting he was primarily checking whether a rubber band had enough torque to drive it.
- **On print files**: Offered the files freely; suggested that people without printers use 3D printing services.
- **Prior clock builds**: Referenced two earlier videos where he built a clock: https://youtu.be/Q-HfTxC-0Iw and https://youtu.be/7aHL_ME6vwc
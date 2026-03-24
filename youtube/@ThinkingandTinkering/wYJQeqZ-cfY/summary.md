## Overview
Robert Murray-Smith demonstrates how to build a cheap, high-current DC power supply using a salvaged microwave oven transformer (MOT) for use in electrolysis experiments. By rewinding the secondary coil with heavy-gauge wire and adding a bridge rectifier, he achieves a 12V supply capable of delivering 20–60+ amps. The build is presented as a low-cost, practical alternative to expensive bench supplies.

## Key Topics
- Why commercial high-current bench supplies are expensive and impractical for DIY use
- Microwave oven transformers (MOTs) as a versatile DIY power source
- Rewinding the secondary coil to set output voltage (turns-per-volt relationship)
- Wire gauge selection and current-carrying capacity
- Adding a bridge rectifier to convert AC output to DC
- Safety considerations for both the mains (240V) side and the low-voltage high-current output side
- Fusing and basic enclosure recommendations

## Materials and Chemicals Mentioned
- **Microwave oven transformer (MOT)** — salvaged core with secondary removed, used as the main transformer
- **1.5mm² single-core wire** — capable of ~20A, mentioned as a lighter option
- **2.5mm² twin-core wire** — carries ~36A, commonly available
- **6mm² wire** — used for the secondary winding; carries ~40A, stripped from twin-core cable
- **70A bridge rectifier** — salvaged from a plasma TV, mounted on a heatsink, converts AC to DC
- **50A fuse** — recommended for the mains live line

## Techniques and Methods
- **Secondary coil removal** — prior video covers chopping out the original secondary from the MOT
- **Turns-per-volt calibration** — wind a test coil, energise briefly, measure voltage to determine volts-per-turn (~0.8V/turn), then calculate turns needed for target voltage
- **Secondary rewinding** — threading 12 turns of 6mm² wire through the transformer core window for ~12V output
- **Bridge rectification** — connecting the AC output to the AC terminals of a bridge rectifier; DC taken from the +/− terminals
- **Voltage verification** — using a multimeter on AC setting before rectifier, then adjusting turn count to hit target voltage

## Notable Timestamps
- `[00:16]` — Introduction: need for high-current DC supply for electrolysis
- `[00:47]` — MOT introduced as the solution; prior projects (spot welder, electromagnet) mentioned
- `[01:09]` — Reference to separate video on removing the secondary coil
- `[02:08]` — Explanation of turns-per-volt (~0.8V per turn)
- `[02:24]` — Wire gauge options discussed (1.5mm², 2.5mm², 6mm²)
- `[04:19]` — Bridge rectifier introduced; salvaged 70A unit from plasma TV
- `[04:50]` — Turns calibration method: wind a few turns, measure voltage
- `[05:09]` — Final build: 12 turns of 6mm² wire wound onto core
- `[06:03]` — Live mains test; voltmeter reads 11.2V AC — one turn too many
- `[06:44]` — Safety demo: touching 12V bare terminals while holding a charged car battery
- `[07:54]` — Safety explanation: low voltage won't push current through body resistance
- `[08:08]` — Bridge rectifier wiring explained
- `[09:08]` — Final summary: cheap, simple, delivers 12V at 20–60A for electrolysis

## Robert's Own Replies
- **On low-voltage safety:** Confirms 50V and below is generally considered safe; dismisses fear of 12V as a "modern myth" and notes he has been shocked and formerly worked on live 10,000V lines — advises being *cautious and sensible*, not afraid.
- **On chainmail/saltwater joke:** Acknowledges the humour and thanks a commenter for the safety tip.
- **On PC power supplies as an alternative:** Agrees they give a more stable and efficient supply, but notes cost and simplicity sometimes matter more — "it all depends on what you want really."
- **On centre-tap pigtail wiring:** Appreciates the suggestion as a simple alternative that also provides voltage options.
- **On converting back to AC (for microwave reactor use):** Advises switching DC at 50Hz using a 555 timer with power transistors or MOSFETs/IGBTs, noting IGBTs are best.
- **On overheating:** Suggests submerging a hot component in a tub of oil.
- **On electromagnetic leakage from the core:** Notes the field is mostly contained by the core; to use it as an electromagnet you need to cut the top off.
- **On wire gauge current ratings:** Confirms ratings vary by installation method but in free air, 4–6mm² should be fine for this application; admits he's "forever looking up wire gauge conversion tables."
- **On sourcing MOTs:** Gets them from skips, finds them by the road, and receives donations from neighbours who know he's into this kind of thing.
- **On a slip of the tongue in the video:** Acknowledges the error, says he put a correction in the description rather than reshoot, and notes most people hadn't read it.
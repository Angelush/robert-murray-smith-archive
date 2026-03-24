## Overview
Robert Murray-Smith provides a comprehensive guide to building a small kiln from scratch using fire bricks, ceramic fiber blanket, and high-temperature silica putty, followed by detailed instructions for winding resistance wire heating coils and wiring the control electronics. The video covers all three major components — the kiln body, the heating coils, and the control box — with the goal of producing a functional, properly rated kiln capable of reaching 800–1200°C without guesswork or complex drying procedures.

## Key Topics
- Why commercially sourced fire bricks and ceramic blanket are preferred over homemade refractory mixes for consistent high-temperature performance
- Constructing the kiln body: cutting, routing coil channels, gluing with high-temperature putty, and reinforcing with angle iron and hose clips
- Repurposing found materials (a stainless steel bathroom cabinet, perforated server shelving) for the kiln enclosure
- Calculating heating coil resistance using Ohm's Law (V = IR) for 230 V and 110 V supplies
- Winding resistance wire coils on a lathe or drill, stretching to fit channels, and fitting them into the brick
- Series vs. parallel coil connections and their effect on total resistance and current draw
- Wiring the control box: PID controller, solid state relay (SSR), thermocouple, double-pole switch, and mains supply
- Kiln reconditioning: replacing coils in second-hand kilns as a cost-effective route to kiln ownership
- Safety precautions when handling ceramic fiber blanket

## Materials and Chemicals Mentioned
- **Fire bricks** — rated to 1260°C (mid-range); higher-rated versions available to 1400°C; used for the structural kiln body
- **Ceramic fiber blanket** — rated to 1400°C; wrapped around the kiln body for insulation
- **High-temperature silica putty / sealant** — rated to 1200°C; used to glue fire brick joints and seal the door
- **Resistance wire (Kanthal-type)** — 1.2 mm diameter, 1.72 Ω/m; used to wind heating coils
- **Brass connectors** — used to join coil ends and connect supply wires at the back of the kiln
- **Stainless steel wire** — used to strap ceramic blanket wrapping in place
- **Aluminium sheet** — used to fabricate the control box enclosure
- **Rubberized heat-rated flex** — used for the mains supply cable to the control box
- **Perlite, vermiculite, water glass** — mentioned as inadequate homemade refractory alternatives at high temperatures (>1200°C)
- **Copper pipe (15 mm)** — used as a gouging tool to cut coil channels in fire bricks

## Techniques and Methods
- Cutting fire bricks in half lengthwise with a panel saw
- Routing U-shaped coil channels in bricks using a 15 mm copper pipe as a gouge, assisted by a pad saw
- Gluing the brick assembly with high-temperature silica putty; reinforcing corners with angle iron and hose clips
- Coil winding: tensioning resistance wire onto a lathe or fixed drill with a 1.2 mm mandrel bar, then stretching the coil to match the channel length
- Connecting coils in series to maintain safe current draw within plug fuse limits
- Calculating required wire length from Ohm's Law: divide target resistance (≈18 Ω at 230 V / 13 A) by wire resistance per metre (1.72 Ω/m) ≈ 10.5 m; using 12 m for safety margin
- Wrapping the assembled kiln body in two layers of 1-inch ceramic fiber blanket, secured with stainless steel wire loops
- Fabricating a door from angle iron, bolts, and fire brick offcuts with a copper-pipe hinge
- Wiring the control box: connecting thermocouple to PID terminals 9 (−) and 10 (+), PID output terminals 4 (+) and 5 (−) to SSR control input, SSR switching the live supply to the heating coils, neutral running directly to the coil, earth bonded to the metal case
- Crimping neutral wire joins (preferred over terminal blocks per UK wiring regulations)
- Using IP65-rated cable glands for mains entry and kiln cable exit on the control box

## Notable Timestamps
- `[00:00]` — Introduction: overview of the kiln build and why bought fire bricks are recommended over homemade refractories
- `[01:35]` — Temperature ratings explained: fire bricks to 1260°C, ceramic blanket to 1400°C, silica putty to 1200°C; working range 800–1200°C
- `[03:35]` — Why perlite, vermiculite, and water glass fail at high temperatures
- `[05:00]` — Cutting fire bricks and marking coil channels
- `[06:26]` — Gouging U-shaped channels with copper pipe and pad saw
- `[07:35]` — Gluing the kiln body with silica putty and fitting angle-iron reinforcement
- `[08:40]` — Basic kiln body complete; ceramic blanket insulation discussed
- `[11:55]` — Tour of Robert's second-hand 150-quid kiln with 1600°C bricks and replaced coils
- `[14:20]` — Resistance wire introduced: 1.2 mm, 1.72 Ω/m
- `[15:35]` — Ohm's Law explanation for calculating coil resistance for 230 V and 110 V supplies
- `[19:03]` — Series vs. parallel coil connections and the risk of drawing excess current in parallel
- `[21:55]` — Coil winding demonstration on a mini lathe
- `[23:40]` — Stretching the finished coil to fit the 45 cm channel
- `[25:07]` — Feeding coil into brick channel and connecting coils in series at the back
- `[29:00]` — Cosmetic case construction using repurposed perforated server shelving
- `[29:44]` — Door fabrication: angle iron frame, fire brick infill, copper-pipe hinge
- `[32:21]` — Wrapping kiln in ceramic fiber blanket and securing with stainless steel wire
- `[34:28]` — Final wired kiln overview; thermocouple mounting
- `[41:54]` — Detailed step-by-step control box wiring begins
- `[44:45]` — Wiring the PID controller terminals (thermocouple, SSR signal, mains supply)
- `[53:50]` — Wiring the solid state relay to the live supply and heating coils
- `[56:14]` — Crimping neutral wires; earthing the control box case
- `[58:10]` — Connecting mains supply flex; closing and completing the control box
- `[01:00:00]` — Closing remarks: encouragement to follow terminal markings on components rather than circuit diagrams

## Robert's Own Replies
No author replies found.
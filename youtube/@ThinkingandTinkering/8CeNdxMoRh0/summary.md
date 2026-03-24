## Overview
This video concludes Robert Murray-Smith's lab kiln build series, covering the construction of the door, outer casing, insulation wrapping, and final wiring. Robert demonstrates how to assemble a functional kiln from salvaged and minimal materials, emphasising that expensive or specialist tools are not required. The finished kiln is ready to fire, with a planned next video using it to make graphitic carbon nitride.

## Key Topics
- Building the kiln door from angle iron, fire bricks, and copper pipe hinges
- Constructing the outer casing from repurposed perforated server rack shelving
- Wrapping the kiln body in ceramic fibre blanket for insulation
- Installing and positioning the thermocouple
- Wiring the control box: double pole switch, solid state relay, and PID temperature controller
- Safety considerations for ceramic fibre handling and electrical earthing
- Design philosophy: keeping wiring uncrowded for ease of future maintenance

## Materials and Chemicals Mentioned
- **Fire bricks** — used in the door and kiln body
- **Ceramic fibre blanket (1-inch)** — two layers wrapped around the kiln for insulation
- **Stainless steel wire** — used to secure the fibre blanket wrapping and as wire ties inside the wiring compartment
- **Perforated steel server rack shelving** — repurposed as the outer casing panels
- **Copper pipe** — used as the door hinge pivot
- **Silicone sealant** — used to seal bricks in the door
- **Angle iron** — structural frame for the door
- **Threaded bar (Daniels) and cap nuts** — door handle assembly
- **Aluminium foil** — mentioned as an optional addition over the fibre blanket (Robert chose to omit it)
- **Graphitic carbon nitride** — mentioned as the intended first material to be made in the kiln

## Techniques and Methods
- Fabricating a hinged kiln door using angle iron, bolts, and a copper pipe pivot dropping into a drilled hole
- Wrapping kiln exterior with ceramic fibre blanket and securing with twisted stainless steel wire loops
- Thermocouple installation: drilling a hole near the top-centre of the kiln, bracketing the thermocouple to the steel chassis
- Wiring a PID controller (terminals 1/2 for AC supply, 4/5 for relay output, 9/10 for thermocouple)
- Wiring a solid state relay (SSR+/SSR− signal from PID; live in/out for the heating coil circuit)
- Wiring a double pole switch to isolate both live and neutral
- Earthing the metal outer case and thermocouple body via chassis bonding
- Series wiring of heating coils (neutral direct to one end, switched live to the other via SSR)

## Notable Timestamps
- `[00:15]` — Introduction: cosmetics, door construction, and casing overview; emphasis on minimal tooling
- `[01:00]` — Explanation of how server rack shelving was repurposed for the outer casing
- `[01:44]` — Door construction described: angle iron frame, bricks, silicone seal, copper pipe hinge
- `[04:24]` — Safety advice for working with ceramic fibre blanket (PPE, skin protection)
- `[05:32]` — Wrapping kiln in two layers of ceramic fibre blanket and securing with stainless wire
- `[06:29]` — Construction declared finished; overview of the completed unit
- `[07:02]` — Thermocouple installation at the back of the kiln
- `[07:46]` — Wiring of the kiln body (coils, earth, neutral, switched live, sealed cable exit)
- `[09:57]` — Detailed walkthrough of PID controller terminal connections
- `[12:22]` — Solid state relay wiring explained
- `[13:30]` — Final assembled control box shown; kiln declared ready to fire

## Robert's Own Replies
- **Earthing/safety**: Robert clarified that the copper pipe door hinge provides adequate bonding, and the thermocouple outer case is earthed via its steel mounting clip to the chassis — he felt some commenters were "over thinking" the earthing concerns.
- **Ceramic fibre blanket**: Reassured viewers that occasional use does not require extreme precautions, though working with it daily would warrant better PPE.
- **Kiln longevity**: Noted his larger kiln had been running the same setup for four years with no degradation.
- **Wire gauge**: Confirmed he used **17 AWG** wire (in response to a question).
- **Airtight container for storage**: Confirmed you only need an airtight container with a rubber seal (context likely relates to storing materials).
- **Next video**: Confirmed he was working on the firing/use video and wanted to do something more meaningful than just heating for the sake of it (referencing the graphitic carbon nitride experiment).
- **Doubling insulation bricks**: Said it "wouldn't hurt in the least" but he had ceramic wool available and didn't want to spend on extra bricks — purely a design decision.
- **Salvaging materials**: When asked how he finds parts, simply said "I just keep my eyes open — there's usually something lying around."
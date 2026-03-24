## Overview
Robert demonstrates a custom-built mechanical turn counter designed for a collaborative serpentine coil winder project, capable of counting up to 10,000 wire turns. The counter combines a rotation-to-push cam mechanism (developed in a previous video) with a ballpoint pen "babble cam" ratchet mechanism to increment digits. The result is an elegantly mechanical solution that avoids electronic counting entirely.

## Key Topics
- Serpentine coil winder project and the problem of counting 1,000–2,000+ wire turns by hand
- Reuse of a rotation-to-push cam mechanism from video 2313 to drive the counter
- The ballpoint pen "babble cam" mechanism: how a click pen's internal cam works and how it was scaled up
- Construction of a multi-digit mechanical counter (4 digits, up to 10,000)
- Carry gear design: half-size and full-size teeth to lock carry gears and advance them 1/10 per full turn
- Gear ratio design using a 50-tooth cog, a 52-tooth cog, and an idle gear to achieve a 1:1 drive ratio from the winder to the counter
- Viewing window for reading the counter display
- Collaborative project structure: Robert (counter), Peter Falcon (main frame), Gavin (central adjustable section)
- Plans for an improved push-button reset mechanism

## Materials and Chemicals Mentioned
- 3D printed parts (various components)
- Laser-cut parts (partial construction of the winder frame)
- 4 mm steel/metal pin bar (counter axle)
- Spacers
- Ballpoint pen cam mechanism (repurposed as design reference)
- Gears: 50-tooth cog, 52-tooth cog, carry gears, idle gear

## Techniques and Methods
- 3D printing of mechanical components (gears, cams, frames, number wheels)
- Laser cutting for structural frame parts
- Babble cam mechanism design: repeating the ballpoint pen cam profile 10 times around a cylinder for a 36°-per-push ratchet
- Carry gear design using alternating half-size/full-size teeth to prevent free-spinning and advance once per 10 turns of the preceding digit
- Idle gear interposition to achieve a 1:1 gear ratio between drive and counter
- Tinkercad for CAD design and assembly visualisation
- Zero-alignment procedure: pulling out the carry drum to free-spin digit wheels, then pushing it home

## Notable Timestamps
- `[00:08]` — Introduction to the serpentine coil winder and its origins (Peter / grle design)
- `[01:01]` — The counting problem stated: 1,000–2,000 turns is tedious to count manually
- `[01:46]` — Introduction of the rotation-to-push cam mechanism from video 2313
- `[02:34]` — Ballpoint pen babble cam mechanism explained and scaled up for the counter
- `[03:54]` — Tinkercad CAD drawing of the complete counter shown
- `[04:39]` — Step-by-step assembly of the counter begins (4 mm pin, spacers, carry gears, drive drums)
- `[05:59]` — Demonstration of the counter incrementing with each push
- `[06:23]` — Joining the cam push mechanism and the counter into a unified frame
- `[08:45]` — Viewing window added; live demonstration of the counter incrementing with handle rotation
- `[09:14]` — Counter integrated into the coil winder; discussion of remaining issues (reset mechanism, painting numbers black)

## Robert's Own Replies
- **Connecting the counter to Gavin's coil wheel:** Robert clarifies that the 50-tooth cog at the back of the counter must engage a same-size cog at the centre of the coil wheel, linked via an idle gear or a chain.
- **Preference for mechanisms over black boxes:** Robert explicitly states he dislikes enclosed solutions where the internal workings are hidden — understanding the mechanism is part of the point.
- **On wire calculation vs. just winding:** He notes that wire is supplied by weight and coil sizes vary enormously, so calculating required wire length upfront is far more complex than simply winding when needed. His fine wire spool is approximately 20,000 km long.
- **On the push mechanism needing a spring return:** Robert notes that because the geared arm pushes in both directions, a return spring is not necessary in this design, though he acknowledges it would be useful in other contexts.
- **Book recommendation:** He recommends an unspecified book on mechanics and mechanisms as "a treasure trove of ideas," endorsing it to anyone interested in the subject.
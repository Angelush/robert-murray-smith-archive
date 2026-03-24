## Overview
Robert demonstrates a hand-built prototype of a magnetically assisted axial flux switched reluctance motor, building on his previous video (1039) where he tested a solid steel rotor. He shows a new plastic rotor with stacked-washer metal segments that respond to pulsed C-shaped electromagnets, proving his theory that flux only needs a path through the C-shaped cores rather than the rotor itself. The video concludes with the prototype working in a manual step-wise mode, with the next step being switching electronics for continuous rotation.

## Key Topics
- Recap and evolution from video 1039's solid steel rotor experiment
- Proof-of-concept plastic rotor with stacked washer metal segments
- Axial flux switched reluctance motor topology
- Magnetic assistance: adding permanent magnets to the C-shaped electromagnets
- Comparison with the Flynn motor (2 coils/2 magnets vs. this design's 1 coil/1 magnet)
- Importance of 90-degree lamination orientation between C-cores and rotor stacks
- Next steps: designing switching electronics for continuous rotation
- Reference to open-access academic paper on axial flux switched reluctance machines

## Materials and Chemicals Mentioned
- **Plastic** — used for the rotor disc (non-ferromagnetic, acceptable for axial flux designs; aids heat dissipation)
- **Steel washers (stacked)** — used as the ferromagnetic segments on the rotor, creating reluctance targets
- **Metal laminates** — used for the C-shaped stator cores
- **Permanent magnets** — mounted on the C-shaped cores to provide magnetic assistance
- **Aluminium** — mentioned as a common rotor material in commercial axial flux motors for heat dissipation (not used here)

## Techniques and Methods
- **Axial flux motor topology** — flux travels axially (along the rotation axis) through the C-shaped cores and rotor segments
- **Switched reluctance principle** — rotor metal aligns to the midpoint of energised C-cores, driving rotation
- **Magnetic assistance** — permanent magnets added to C-cores to reduce power draw compared to pure electromagnet designs
- **Stacked laminations** — C-cores laminated in one direction; rotor stacks (washers) laminated 90 degrees to that, which Robert later confirmed is technically important
- **Manual pulse switching** — used in this prototype to demonstrate step-wise rotation before electronics are added
- **Proof-of-concept prototyping** — plastic rotor used to isolate and test the flux path theory before optimisation

## Notable Timestamps
- `[00:15]` — Introduction; references video 1039 and the transition from solid steel to plastic rotor
- `[00:39]` — Close-up of the plastic rotor with stacked-washer metal segments
- `[00:50]` — Live demonstration: pulsing a C-core causes rotor to step, then second C-core pulsed manually
- `[01:40]` — Explains switching electronics needed for continuous rotation
- `[01:54]` — Names the base topology: axial flux reluctance motor; references academic literature
- `[02:12]` — Cites open-access paper: *"Axial Flux Switch Reluctance Machines: A Comprehensive Review of Design and Topologies"*
- `[02:29]` — Introduces the magnetic assistance modification; names the full motor type
- `[02:59]` — Compares design to the Flynn motor; highlights key differences (1 coil/1 magnet vs. 2/2)
- `[04:00]` — Discusses the significance of the 90-degree lamination twist (discovered retrospectively)
- `[04:22]` — Summary of prototype status and next steps

## Robert's Own Replies
- **Proof of concept first, optimisation later:** Confirmed that relays would be used initially for switching, with optimisation to follow — "yes initially relays as really this is proof of concept later comes optimisation."
- **Not using a Raspberry Pi deliberately:** Declined a viewer's Pi offer, noting he already knows how to program it and has specific reasons for not using one at this stage.
- **Name suggestion "BORSAF":** Responded positively to what appears to be a viewer-proposed acronym for the motor — "oh I like BORSAF - it really gets it I think."
- **Lathe safety clarification:** In an unrelated exchange, defended his practice of leaving the chuck key in the chuck, explaining he has modified his lathe so the chuck key must be removed to start it — making it a safety feature rather than a hazard.
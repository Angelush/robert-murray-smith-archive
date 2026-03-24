## Overview
Robert continues his VAWT (Vertical Axis Wind Turbine) series by surveying four rotor designs derived from the Savonius rotor — the Thine, Philippini, C, and Lens rotors — and then builds and tests a hybrid 3D-printed rotor that blends the Philippini curve, conical C-rotor shell, and Pelton wheel bucket geometry. The rotor is tested outdoors on a PC fan motor converted to a generator; it spins but does not reach the turn-on voltage of an LED under light wind, which Robert attributes to torque load rather than a design failure. He concludes the design shows promise and shares the TinkerCAD files for community iteration.

## Key Topics
- Recap of the fluid-transfer concept from video 1978 and the "C rotor" family
- Four C-rotor variants: Thine rotor, Philippini rotor, C rotor, and Lens rotor
- The Savonius rotor as the baseline and how adding a flat deflector plate yields a ~36% efficiency improvement
- Evolution from flat plate (Thine) → curved plate (Philippini) → conical cup (C rotor) → edge-mounted plate (Lens rotor)
- Discussion of what "best" rotor means: cost per kWh, ease of fabrication, or peak efficiency
- Design of a hybrid rotor (Philippini curve + conical C-rotor shell + Pelton wheel bucket) modelled in TinkerCAD and 3D-printed with three blades
- Real-world outdoor test at ~2–3 m/s wind speed under electrical load
- Analysis of output: estimated 20–60 mW, insufficient to cross LED turn-on voltage (~1 V)
- TinkerCAD files (small and larger versions) made public for community use

## Materials and Chemicals Mentioned
- **Guttering / half barrel** — cited as accessible DIY materials for building a Savonius-style rotor
- **3D-printed PLA (implied)** — rotor disc printed via TinkerCAD; dimensions ~10 cm × 14 cm
- **PC fan motor** — repurposed as a generator by removing electronics and rewiring
- **LED** — used as a power-output indicator / load

## Techniques and Methods
- Converting a brushless PC fan motor into a small generator (removing onboard electronics, rewiring)
- Parametric 3D modelling in TinkerCAD to prototype rotor geometry
- FDM 3D printing of rotor blades
- Outdoor real-conditions testing with an electrical load (LED) to confirm functional operation
- Normalising rotor performance by rotor diameter, height, and wind speed for cross-design comparison (discussed in comments)

## Notable Timestamps
- `[00:07]` — Recap of video 1978: air/water as fluids and the C rotor concept
- `[00:26]` — Thine rotor introduced: flat plate added to Savonius gives 36% improvement
- `[01:01]` — Philippini rotor: curved plate replaces flat plate
- `[01:11]` — C rotor: conical section cup
- `[01:22]` — Lens rotor: flat plate moved to the outer edge
- `[01:31]` — Discussion of what "best" rotor actually means
- `[02:20]` — Pelton wheel as the conceptual origin of the hybrid design
- `[02:27]` — TinkerCAD model of the hybrid rotor shown
- `[03:00]` — PC fan motor generator assembly demonstrated
- `[03:34]` — Outdoor test begins
- `[04:00]` — Test result: rotor spins but does not light the LED
- `[04:13]` — Post-test analysis: wind speed too low for the load; design deemed functional

## Robert's Own Replies
- **Blade count and exhaust venting:** Robert notes he is rethinking the number of blades and how exhaust air is vented — suggesting active ongoing design iteration beyond what is shown in the video.
- **Torque and load:** Confirms the rotor was working but attributes the weak output to the torque demand of the attached generator load, not a fundamental design failure.
- **Stepper vs fan motors:** Mentions he uses stepper motors as generators in other videos and likes to vary the approach so viewers with different parts can follow along.
- **Normalising comparisons:** Explains that fair cross-rotor comparison is straightforward — normalise torque/power as a proportion of rotor diameter, height, and wind speed.
- **VAWT vs HAWT debate:** Delivers a detailed rebuttal to a commenter claiming only HAWTs matter, arguing that wind power is a broader domain than the large-scale industry alone, and that dismissing VAWTs reflects a narrow, self-referential perspective.
- **O wind turbine:** Briefly acknowledges the "O wind" design when prompted by a commenter.
- **General tone:** Several lighthearted replies; Robert also remarks that he finds constant criticism of his approach "quite wearing."
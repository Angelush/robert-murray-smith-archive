## Overview
In Part 6 of his budget wind turbine build, Robert demonstrates a key breakthrough: four salvaged microwave transformer coils, each connected to an individual capacitor-diode rectifier circuit, successfully power separate loads simultaneously without stalling the rotor. He explains that adding a capacitor between each coil and its load effectively "decouples" the generator from the load, allowing the turbine to spin freely in low-wind conditions — a discovery he finds genuinely surprising and exciting.

## Key Topics
- Installing four microwave transformer coils at 90-degree intervals on the rotor
- Demonstrating each coil independently powering an LED light panel
- The critical role of capacitor-diode circuits in decoupling generator from load
- Analogy of the capacitor network acting as an "automatic clutch"
- Scaling plan: 24 coils total producing ~72W at low RPM
- Comparison with commercial 1kW wind turbines (~75W average output in 12 mph UK wind)
- Weatherproofing options for coils and electronics
- Redundancy advantages of individual coil wiring vs. one large coil

## Materials and Chemicals Mentioned
- **Microwave transformer coils** — used as the generator coils (700W microwave transformers confirmed in comments)
- **50V 1000µF electrolytic capacitor** — one per coil, placed after the diode bridge as a buffer/"soothing cap"
- **1N4007 diodes** (referred to as "1N407") — four per coil, wired as a bridge rectifier
- **LED light panels** — used as test loads; turn-on voltage ~28V, ~100mA draw
- **Plastic bag / plastic box** — proposed weatherproofing for coils and electronics

## Techniques and Methods
- **Axial flux generator construction** — coils positioned at the rim rather than near the axle
- **Bridge rectifier per coil** — individual full-wave rectification for each microwave coil
- **Capacitor decoupling** — placing a large capacitor between the rectifier output and the DC load to buffer the generator from load demands
- **Parallel load connection** — all four rectified outputs combined to drive a single larger light panel
- **Blower testing** — using a constant airflow blower as a reference wind source in the absence of real wind
- **Individual coil redundancy design** — separate wiring per coil rather than one large series/parallel network

## Notable Timestamps
- `[00:15]` — Robert explains why he's sharing this update early (unexpectedly exciting result)
- `[00:33]` — Demonstrates four coils each independently powering a load
- `[01:05]` — Lights-off demonstration to show brightness of individual LEDs
- `[01:26]` — Shows all four coils combined driving one larger light panel in parallel
- `[01:37]` — Reports ~3W per coil; projects 72W from 24 coils total
- `[02:29]` — Close-up of the capacitor and diode bridge rectifier circuit per coil
- `[03:00]` — Introduces the "clutch" analogy to explain capacitor decoupling behaviour
- `[04:00]` — Explains that the generator charges the capacitors, not the load directly
- `[05:23]` — Argues this design allows as many coils as desired without stall in low wind
- `[06:05]` — Projects 72W at ~12.5 mph wind; compares favourably to commercial 1kW turbines
- `[07:50]` — Discusses weatherproofing options (plastic bag, plastic box)
- `[08:02]` — Plans to route individual coil wires to a central control unit

## Robert's Own Replies
Robert was active in the comments and added several meaningful clarifications:

- **Circuit video promised:** Multiple times he commits to making a dedicated video on the capacitor-diode circuit, acknowledging he glossed over it in this video and that many viewers asked for detail.
- **Capacitor function clarification:** He explains the cap is placed *after* the diode bridge (on the DC side), so it acts primarily as a "soothing cap" reducing ripple in the rectified output, while also buffering the load from the generator — he compares this to a **soft-start motor**.
- **"Freewheeling diodes":** He notes that diodes placed across coils to suppress back-EMF are called freewheeling diodes, and ties this concept to his circuit.
- **Output voltage:** He confirms the turbine outputs roughly **30–35V**, enough that he's been shocked by it and now wears gloves.
- **RPM:** Community members told him the blower-driven speed is around **23–26 RPM**; he's uncertain and treats it as a rough reference only.
- **End use plan:** He intends to mount the turbine on his **roof**, charge a **battery bank**, and use an **inverter for AC power**.
- **Commercial turbine critique:** He acknowledges a commenter's point that output depends heavily on wind speed — his goal is simply to match or beat a £/$2,000 commercial 1kW turbine, which he believes averages only ~75W in typical UK wind (~12 mph). Beating that for ~£100 is his benchmark.
- **Not a literal clutch:** He clarifies to one commenter: "it's not a real clutch" — the analogy was illustrative.
- **Coil placement:** He plans to add a second set of coils so that two coil blocks are joined, to be shown in a later video.
- **Redundancy preference:** He explicitly prefers redundant individual-coil systems over a single large coil for resilience.
- **Patent:** He states he has never read a patent on this approach — it occurred to him independently — and he doesn't mind if others copy the idea.
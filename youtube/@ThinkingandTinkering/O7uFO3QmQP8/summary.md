## Overview
Robert Murray-Smith explains how a push-pull inverter works — a circuit topology well-suited for home energy storage from wind or solar — breaking it down into its simplest conceptual components. He demonstrates a working prototype using a centre-tapped transformer and a relay as a mechanical switch, successfully converting 12V DC into ~80V AC. The video concludes that building such an inverter at home is within most people's capabilities, and provides a practical component list for a real MOSFET-based design.

## Key Topics
- What an inverter does (DC to AC voltage conversion and step-up)
- How a centre-tapped transformer enables push-pull operation
- The role of switching (mechanical relay, then MOSFETs) to approximate an AC waveform
- Back-EMF protection using diodes across the switches
- Output smoothing using a capacitor
- Core saturation and the role of an inductor in preventing it
- Practical component selection for a buildable design
- Applications: home energy storage, UPS units, CFL backlights

## Materials and Chemicals Mentioned
- Centre-tapped transformer (hand-wound or bought)
- Double-pole relay (used as a mechanical switch in the demo)
- MOSFETs — specifically **STP36NF06L** recommended for Q1, Q2, Q3
- Resistor R2 — 10 ohms
- Diode D1 — **MBR1035**
- Diodes D2 & D3 — **MUR120**
- Inductor L — ~100 µH
- Capacitor C — 0.1 µF
- 12V battery (power source for the demo)

## Techniques and Methods
- Centre-tap transformer switching to generate an approximated AC waveform from DC
- Using a relay as a manual timing switch to demonstrate the push-pull principle
- Placing flyback/freewheeling diodes across switches to suppress back-EMF spikes
- Adding a smoothing capacitor on the output to convert the square wave towards a sinusoidal waveform
- Using an external timing/driver circuit (e.g. 555 timer) to achieve frequency-stable switching independent of core behaviour
- Including a series inductor to prevent transformer core saturation

## Notable Timestamps
- `[00:15]` — Introduction: inverters don't have to be complicated; push-pull type introduced
- `[00:52]` — Explanation of what an inverter does (DC in, stepped-up AC out)
- `[01:16]` — Transformer basics: coil, core, step-up principle
- `[02:15]` — Centre-tap concept: two coils, switching the negative to approximate AC
- `[03:44]` — Summary of push-pull topology: two switches, diodes, smoothing cap
- `[05:48]` — Live demo begins: connecting transformer, relay, and battery
- `[09:02]` — Demo result: 12V DC converted to ~80V AC
- `[09:16]` — Real-world applications mentioned (CFL tubes, sine wave inverters)
- `[09:46]` — Practical MOSFET-based schematic walkthrough with component values
- `[11:30]` — Closing remarks: home-buildable, components freely available

## Robert's Own Replies
- **Tank circuit / waveform quality:** Robert clarifies that the capacitor and inductor together form a *tank circuit* (ringing oscillator), which produces a genuine sine wave — not a simulated stepped sine wave (which he distinguishes as a digital step-function approximation, like a low-order Fourier transform with n=2 or 3).
- **Frequency stability:** He notes that frequency drift in push-pull inverters is caused by the core influencing the oscillation; an isolated external timing signal solves this. Core saturation on current-driven inverters is the main hazard to watch.
- **Microwave oven transformer idea:** He mentions thinking about building one of these inverters using a microwave oven transformer.
- **UPS as a practical shortcut:** He agrees that grabbing a UPS is a sensible approach, and mentions he already has one planned for upcoming videos — but notes this video's purpose is to explain the underlying principles.
- **Learning electronics:** When asked how to learn, he recommends the *Babani project books* and the *US Navy basic electronics tutorial series*, and emphasises learning by doing circuits rather than pure theory.
- **Buying vs. making:** He explicitly clarifies he wasn't being condescending when commenting on whether to buy or build — he respects both approaches.
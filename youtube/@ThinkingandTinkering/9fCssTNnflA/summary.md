## Overview
Robert Murray-Smith demonstrates how to build a simple oscillator using a relay and a capacitor, as part of a series building toward a relay-based clock mechanism. He explains that oscillators are the fundamental counting unit in timekeeping—by counting oscillations, a stepper motor can be driven to tick once per second. While a relay oscillator is not ideal for long-term use, it clearly illustrates the underlying principle common to all oscillator-based timing systems.

## Key Topics
- What an oscillator is and why it is essential for timekeeping
- Building a self-oscillating relay circuit (relay coil connected to its own switch)
- Controlling oscillation frequency using capacitance and resistance
- LC oscillators (inductor-capacitor tank/ringing circuits) and named variants
- RC oscillators (resistor-capacitor) and their limitations vs. LC types
- Linking the oscillator to a counter, H-bridge, and stepper motor to form a clock mechanism
- Limitations of relay-based mechanical oscillators (rated 10,000–1,000,000 switching operations)
- Alternative implementations: discrete components or Arduino with quartz oscillator

## Materials and Chemicals Mentioned
- **Relay** — used as both the switching element and the inductor in the LC oscillator
- **3,300 µF capacitor** — connected across the relay coil to slow the oscillation; two used in parallel to further reduce frequency
- **Resistor** — discussed conceptually as a secondary means of tuning oscillation speed (higher resistance = faster switching)
- **Quartz crystal/chip** — mentioned as the oscillator inside computers, clocks, and Arduino boards

## Techniques and Methods
- **Relay self-oscillation** — connecting the coil's negative terminal to the relay's own normally-closed (NC) contact to create a feedback loop that breaks and restores power automatically
- **Capacitor across the coil** — placing a capacitor in parallel with the relay coil to form an LC tank circuit, slowing the oscillation to a usable rate
- **Parallel capacitors** — adding a second capacitor in parallel to effectively double capacitance and halve frequency
- **Resistance tuning** — varying series resistance to fine-tune switching speed
- **Counter + H-bridge integration** — conceptual method of chaining the oscillator output through a counter to drive an H-bridge and stepper motor for timekeeping

## Notable Timestamps
- `[00:08]` — Recap of previous stepper motor and H-bridge relay video; motivation for needing a controlled oscillator
- `[00:37]` — Definition of an oscillator; example of counting 60 oscillations per second to produce a 1-second pulse
- `[01:14]` — Examples of oscillators: pendulum, quartz chip, radio oscillators
- `[01:44]` — Explanation of relay internal coil as an inductor; how feedback through its own switch causes oscillation
- `[02:10]` — Introduction of capacitor to form an LC (tank/ringing) circuit for frequency control
- `[03:06]` — Live demonstration: relay oscillating uncontrolled without capacitor
- `[03:30]` — Demonstration with 3,300 µF capacitor: slower, more usable tick rate
- `[04:05]` — Two capacitors in parallel: even slower click demonstrated
- `[04:27]` — Overview of LC oscillator family: Armstrong, Hartley, Colpitts and others
- `[04:48]` — RC oscillator mentioned; noted as less well-tuned than LC types
- `[05:08]` — Limitations of relay as oscillator; restatement of the universal oscillator→counter→H-bridge→motor principle

## Robert's Own Replies
- **Duty cycle control with relays** — confirmed it is possible to change duty cycle using 5 SPDT relays wired together; mentioned he may do a dedicated video on this
- **Transistor clarification** — explicitly noted that a transistor alone cannot oscillate; it is just a switch and still requires a separate oscillator to turn it on and off at a set frequency
- **555 timer** — remarked on it being the most popular IC ever made, in the context of oscillators (likely in response to a comment linking the relay oscillator concept to the 555)
- **Kromrey converter** — acknowledged a viewer's suggestion, noting it resembles what was described but is considered a perpetual motion machine and therefore "a little iffy"
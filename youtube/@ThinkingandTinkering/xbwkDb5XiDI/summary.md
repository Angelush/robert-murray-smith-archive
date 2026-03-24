## Overview
Robert demonstrates how to fabricate a voltage divider using graphene-based conductive ink painted onto an acrylic sheet, as part of his larger "Cylon machine" project. The goal is to step down 12V signals from limit switches to 5V for an Arduino input. The finished painted divider achieves 4.9V output from 12V input — roughly 1% error — while also limiting current to ~16mA.

## Key Topics
- Voltage divider theory (R1/R2 ratio, formula, and use of online calculators)
- Practical limitations of voltage dividers (variable loads, AC/impedance concerns)
- Using conductive ink as a resistive element instead of discrete resistors or potentiometers
- Integration into a Cylon machine build (8 limit switches → Arduino)
- Priming plastic surfaces before applying conductive ink

## Materials and Chemicals Mentioned
- **Conductive graphene ink ("our ink")** — painted as resistive traces onto plastic
- **Acrylic sheet** — substrate for the voltage divider plate
- **Kapton tape** — used as masking tape due to its thin profile
- **Standard masking tape** — also used for masking lanes

## Techniques and Methods
- **Surface priming** — rubbing ink onto plastic with a cloth before painting to prevent beading; believed to spread graphene onto the surface for adhesion
- **Masked painting** — using Kapton/masking tape to define 8 parallel resistive lanes
- **Drilling and gluing connectors** — 1.5mm holes drilled at calculated ratio points; bent-pin connectors glued and painted over
- **Ratio-based tap placement** — measuring the painted line length and drilling the output tap at the position corresponding to the desired R1:R2 ratio (1.4:1 for 12V→5V)

## Notable Timestamps
- `[00:14]` — Introduction to conductive ink and project context (Cylon machine)
- `[00:39]` — Explanation of the problem: 12V limit switches need to feed a 5V Arduino
- `[01:25]` — Voltage divider theory explained with diagram
- `[02:00]` — Voltage divider schematic shown on screen
- `[03:20]` — Decision to use conductive ink instead of discrete resistors/potentiometers
- `[04:07]` — Masking and painting the acrylic substrate
- `[06:04]` — Drilling complete; device connected to 12V supply
- `[06:16]` — Measurement: 4.9V output demonstrated (~1% error)
- `[07:31]` — Current draw noted: ~16mA; device also acts as current limiter
- `[08:00]` — Re-explanation of ratio principle and how to find tap position
- `[09:02]` — Device shown fitted to the Cylon machine with wiring to switches and Arduino

## Robert's Own Replies
- **Substrate:** Confirmed the sheet used is acrylic.
- **Moisture protection:** Recommends overcoating the ink traces with varnish or a glued plastic layer to prevent resistance drift from environmental moisture — notes the ink is homogeneous and precise but vulnerable to humidity.
- **Water resistance:** Clarifies the ink is *water resistant*, not waterproof.
- **Laminating:** Endorsed laminating as a good protection idea ("I will do it").
- **Acrylic varnish:** Confirmed the ink can be overcoated with acrylic varnish, including via airbrush, without issue — carbon-based and fairly stable.
- **Current draw:** Confirmed the 16mA is being *burned off* (dissipated), not passed through to the Arduino — clarifying the current-limiting function.
- **Ink availability:** Noted they no longer sell the ink (not enough demand; costs to list), and that 10mL bottles being sold elsewhere are likely rebadged — he doesn't mind this.
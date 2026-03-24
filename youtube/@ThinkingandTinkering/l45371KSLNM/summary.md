## Overview
Robert Murray-Smith demonstrates how to design a spiral (Archimedean) gear entirely within Tinkercad's Code Blocks environment, without resorting to external CAD tools. He explains the mathematical underpinning — converting polar coordinates into Cartesian steps — and walks through the full workflow from parametric code to 3D-printed assembly. The finished gear pair achieves an 18:1 reduction ratio and is self-locking, making it suitable for applications like car jacks and table lifts.

## Key Topics
- What spiral gears are and where they appear in real life (car jacks, table lifts, snail shells, Tesla coils)
- Archimedean spirals: definition and the polar coordinate equation `r = b·θ`
- Why Tinkercad uses Cartesian coordinates and how to "trick" it into approximating polar coordinates
- Using Tinkercad's Code Blocks to build a parametric, repeating tooth object
- Choosing step count (180 iterations) to stay within Tinkercad's 300-object limit while achieving a smooth curve
- Exporting as STL and reimporting into standard Tinkercad workspace
- Gear ratio (18:1) and self-locking behaviour of worm/spiral gear pairs

## Materials and Chemicals Mentioned
None mentioned.

## Techniques and Methods
- **Parametric modelling in Tinkercad Code Blocks** — defining a reusable `tooth` object and looping 180 times with incrementing angle (2° per step) and radius (0.4 mm per step)
- **Polar-to-Cartesian coordinate conversion** — approximating a continuous spiral via discrete Cartesian steps
- **STL export and reimport** — exporting the spiral from Code Blocks as an STL, then importing it back into the standard Tinkercad editor
- **FDM 3D printing** — printing the spiral gear, spur gear, and frame, then assembling with glue

## Notable Timestamps
- `[00:08]` — Introduction to spirals in nature and engineering (Tesla coil, snail shell, car jacks)
- `[00:52]` — Problem statement: drawing a spiral gear in Tinkercad
- `[01:22]` — Explanation of polar coordinates vs. Cartesian coordinates
- `[01:30]` — Archimedean spiral equation introduced (`r = b·θ`)
- `[02:17]` — Why computers use discrete steps; link to differentiation
- `[03:03]` — Code Blocks walkthrough begins; creating the `tooth` object
- `[04:11]` — Main loop: setting rotation around Z-axis, angle increment (2°), radius increment (0.4 mm)
- `[06:27]` — Adding a centre circle to enable use as a proper gear
- `[06:51]` — Running the code and watching the spiral generate
- `[07:04]` — Exporting as STL and reimporting into Tinkercad
- `[07:16]` — Printing and assembling the spiral gear, spur gear, and frame
- `[07:40]` — Demonstration: self-locking behaviour and 18:1 gear ratio explained

## Robert's Own Replies
Several replies are substantive clarifications:

- **One tooth, all the load**: Robert acknowledges a commenter's point that the design concentrates all force on a single tooth, which is a real limitation of this configuration.
- **Starting position**: He confirms he always starts at `(0, 0, 0)` — the centre point of all axes — as his default origin in Code Blocks.
- **Logarithmic spiral extension**: When asked about a logarithmic spiral variant, he notes the polar equation is straightforward and encourages the commenter to try it themselves.
- **Metal casting suggestion**: He suggests that printed gears could be used as moulds and cast in metal for stronger results.
- **Scope of the tutorial**: He pushes back gently on a critical comment, clarifying that this is a practical "how to do it" tutorial and that spiral/worm gear systems have many real applications (e.g., lathe chucks).
- **Colour choice**: He confirms the bright colour was simply chosen so the gear was easy to see — no other reason.
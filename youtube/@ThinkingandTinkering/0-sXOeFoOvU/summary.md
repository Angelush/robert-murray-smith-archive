## Overview
Robert demonstrates the fundamentals of gear design in the context of a practical problem: stepping up a hand-crank axial flux generator from ~30 RPM to ~3000 RPM. He explains the core mathematics of gear ratios using the concept of the reference circle, then shows how to design meshing gears in Tinkercad using the module and tooth count parameters. The key takeaway is that gears with the same module will always mesh, and their speed/torque ratio equals the ratio of their tooth counts.

## Key Topics
- The problem: hand-crank generator produces ~30 RPM but needs ~3000 RPM (100:1 step-up)
- Why friction wheels slip and why teeth are added — teeth are an anti-slip add-on to reference wheels
- The reference circle: the fundamental wheel underlying any gear
- Gear ratio as a consequence of circumference differences between two meshing wheels
- Speed-torque trade-off: as speed increases by a factor, torque decreases by the same factor
- The module: the ratio of reference diameter to number of teeth
- Gears mesh only when they share the same module
- Using reference radius to correctly position gear centres in a mechanism
- Designing gears in Tinkercad using the metric gear shape

## Materials and Chemicals Mentioned
- None mentioned. (The gears are 3D printed but no filament material is specified.)

## Techniques and Methods
- 3D printing gears (via Tinkercad-designed models)
- CAD gear design in Tinkercad using the built-in metric gear component
- Calculating reference diameter: `module × number of teeth`
- Selecting module and tooth count to maintain a target reference circle size
- Determining centre-to-centre distance for two meshing gears: sum of their reference radii

## Notable Timestamps
- `[00:00]` — Introduction: hand-crank axial flux generator printed from Thingiverse; the 30 RPM vs 3000 RPM problem stated
- `[00:39]` — Problem with existing small-toothed printed gears: slipping, slop, and wear
- `[01:31]` — Conceptual explanation of gear ratios using two wheels of different sizes rolling together
- `[03:11]` — Speed-torque trade-off derived from the wheel ratio relationship
- `[04:36]` — Why teeth are added: to prevent slipping; introduction of the reference circle concept
- `[06:23]` — Tinkercad demo begins: searching for and placing the metric gear component
- `[07:04]` — Module explained: how it links reference diameter to number of teeth; effect of changing module vs changing tooth count
- `[09:44]` — Demonstration that two gears mesh only when they share the same module
- `[10:21]` — Using reference radius to set the correct centre distance between gears
- `[12:07]` — Summary and sign-off: module + tooth count + reference circle = everything needed to design and place gears

## Robert's Own Replies
Robert's comments are largely casual and social. One notable clarification stands out: he acknowledges the video is intentionally simplified — *"I have to apologise for this being so cut down — I know there is a lot more to it but I am just trying to get the basics across right now"* — indicating this is a primer aimed at getting beginners building rather than a comprehensive treatment of gear theory. He also expresses that he sees his channel as a community rather than a broadcast.
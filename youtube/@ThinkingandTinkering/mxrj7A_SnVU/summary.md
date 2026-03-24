## Overview
In this second part of his hoverboard wind turbine series, Robert Murray-Smith completes the build by attaching bamboo blades (from a previous video) to the hoverboard's brushless DC motor/wheel hub, mounts it on a pole, and tests it with a three-phase rectifier for DC output. The main takeaway is that while the neodymium-magnet hoverboard motor outperformed a ceramic-magnet car radiator fan motor, the difference was modest — reinforcing Robert's point that rotational speed matters far more than motor design for generator output.

## Key Topics
- Disassembly of a hoverboard wheel/motor hub to remove the tire and expose the generator
- Attaching an adaptation plate and bamboo blades to the motor rotor
- Mounting the assembly on a pole using angle plate and hoverboard axle grips
- Building and using a three-phase rectifier to convert AC output to DC
- Live wind testing and voltage/current readings
- Comparative analysis: hoverboard motor (neodymium magnets) vs. car radiator fan motor (ceramic magnets)
- The physics of generators: turns of wire, magnetic field strength, and rotational speed

## Materials and Chemicals Mentioned
- **Hoverboard wheel/hub motors** (Razor Hovertrax) — repurposed as brushless DC generators
- **Neodymium magnets** — inside the hoverboard motor rotor, key to its superior (though modest) output
- **Ceramic magnets** — in the comparison car radiator fan motor
- **Bamboo blades** — wind-capture blades fabricated in a prior video (video 1157)
- **Soil pipe (plastic)** — used to make an earlier set of fan blades shown briefly
- **Angle plate (steel)** — used as the axle mounting bracket
- **Y-shaped welded bracket** — adapter to bolt blades to the motor's backing plate
- **Bamboo pole** — used as the turbine mast

## Techniques and Methods
- Tire removal from a hoverboard hub motor
- Drilling and bolting an adaptation plate to the motor's backing plate (with rotor removed to avoid damage)
- Reassembly with neodymium magnet awareness (snap-down risk when replacing rotor)
- Fabricating and wiring a **6-diode, three-phase rectifier** for AC-to-DC conversion
- Resistive load testing to measure voltage and current at varying wind speeds
- Comparative testing against a legacy DC motor under identical conditions

## Notable Timestamps
- `[00:16]` — Recap of part 1: hoverboard disassembly and motor extraction
- `[00:49]` — Discussion of blade options; bamboo blades (video 1157) chosen
- `[01:24]` — Welded Y-bracket introduced as blade hub adapter
- `[01:39]` — Step-by-step tire/rotor disassembly walkthrough
- `[02:07]` — Neodymium magnet ring in the rotor explained; safety caution
- `[03:00]` — Reassembly and completed blade-to-motor mounting shown
- `[03:27]` — Three-phase rectifier explained; pole mounting described
- `[04:01]` — Live wind test: cut-in speed ~3 m/s, output ~4 V; milliamp readings taken
- `[04:54]` — Comparison with car radiator fan DC motor; results discussed
- `[05:53]` — Key conclusion: motor design is less important than rotational speed

## Robert's Own Replies
- **Rectifier spec**: It was a **6-diode, three-phase rectifier**; at the wind speeds tested he expected roughly **2–3 watts output**.
- **Why AC output**: The brushless DC motor has no brushes or commutator (which normally act as a rectifier on a standard DC motor), hence it outputs AC and requires an external rectifier.
- **Wiring configuration**: Pushed back on a commenter's wiring claim — a motor like this uses delta or Y (star) configuration, not series/parallel in the conventional sense.
- **Generator output physics**: Reiterated that output is a function of wire turns, magnetic field strength, and speed — not motor design per se.
- **Voltage drop**: Explained to a commenter that longer cables increase resistance and cause voltage drop, a serious practical issue.
- **Potential output ceiling**: If spun fast enough, the motor could produce **5–10 A at 18–30 V**; the limiting factor in this test was insufficient rotational speed.
- **Water applications**: Noted the motor's high torque makes it well-suited for water turbine use with appropriate gearing.
- **Hoverboard model**: Confirmed it was a **Razor Hovertrax** hoverboard.
- **PWM query**: Questioned a commenter's suggestion of using PWM, noting PWM is for motor speed control, not generator output regulation.
## Overview
Robert demonstrates a simple DIY method for measuring the static torque output of a wind turbine blade prototype, arguing that evaluating a design by electrical output alone risks discarding a potentially excellent blade due to a poor generator or gearbox. Using a fan, a lever arm, weighing scales, and basic trigonometry, he shows how to isolate and quantify the torque produced by the wind-capture device itself, then compares the result against a standard turbine blade of the same swept area.

## Key Topics
- Why measuring electrical output (amps) is an unreliable way to evaluate a new wind turbine blade design
- The three independent subsystems of a wind turbine: wind-capture device, gearing, and generator
- Static torque vs dynamic torque, and why static torque is a useful proxy for blade performance
- Building and calibrating a simple static torque measurement rig
- Using the torque formula **T = RF sin θ** to calculate torque from lever arm, force, and angle
- Validating results using the Omni Calculator theoretical torque model
- Comparative testing against a standard reference blade of equal swept area to cancel out systematic experimental errors

## Materials and Chemicals Mentioned
- None mentioned (no chemicals or raw materials; only test equipment and prototype blades)

## Techniques and Methods
- **Static torque measurement**: stalling the turbine against a lever arm resting on weighing scales to read the resisting force
- **Anemometer / wind speed measurement**: measuring airflow at the turbine position (1.8 m/s in the demonstration)
- **Tare zeroing on scales**: pressing tare before the fan starts so that only the wind-induced force is displayed, not the weight of the arm itself
- **Mass-to-force conversion**: multiplying mass in kilograms by gravitational acceleration (9.8 m/s²) to obtain force in Newtons
- **Torque calculation**: applying **T = RF sin θ** (R = arm length 150 mm, F = force in Newtons, θ = angle between arm and vertical = 45°)
- **Averaging repeated readings**: taking 10 measurements and averaging to reduce noise from wobble and scale instability
- **Comparative reference testing**: running the same rig with a conventional blade of identical swept area to normalise experimental errors
- **Online calculator cross-check**: using Omni Calculator's wind turbine torque model to benchmark measured results against theory

## Notable Timestamps
- `[00:08]` — Introduction: why judging a blade by amp output is misleading
- `[00:30]` — Wind turbine anatomy: capture device, gearbox, and generator as separate subsystems
- `[01:42]` — Torque identified as the correct metric to measure blade performance
- `[01:50]` — Overview of the test rig: fan, cradle, and lever arm
- `[02:05]` — Wind speed measured at test position: 1.8 m/s; arm length: 150 mm; angle: 45°
- `[03:24]` — Static vs dynamic torque explained; static torque as a stall-condition maximum
- `[04:09]` — Practical warning: wobble causes variability; take multiple readings and average
- `[04:32]` — Measurement result for new design: approximately 1.6 g on the scales
- `[04:39]` — Converting 1.6 g to force: ≈ 0.016 N
- `[05:06]` — Applying T = RF sin θ; result: ≈ 0.0017 N·m
- `[05:52]` — Cross-checking with Omni Calculator; theoretical standard-blade torque ≈ 0.00003 N·m
- `[06:35]` — Comparative test with a conventional blade of equal swept area (~8 g vs ~1.6 g readings)
- `[07:54]` — Caveat on scaling: small model errors compound at full scale; results are indicative, not definitive

## Robert's Own Replies
- **Tare button explanation**: when you tare the scale before switching the fan on, the display already has the arm's own weight zeroed out, so it shows only the wind-induced force — a counterweight is possible but unnecessary.
- **Arm placement flexibility**: the rod position does not matter as long as the angle is recorded and accounted for in the formula; 90° is perfectly valid and may be more convenient.
- **Lift vs drag directionality**: a viewer asked about reversing the rig to distinguish lift and drag components; Robert was genuinely uncertain whether the direction of rotation matters, noting that lift is effectively an upward push and drag a downward push and the net result may be the same.
- **Variable wind speed modelling**: variable wind speed can be approximated as a fixed wind speed of variable short duration — useful for getting a handle on real-world conditions.
- **Prony brake analogy**: Robert confirmed that the method is conceptually very similar to a prony brake.
- **Result interpretation caveat**: if the performance difference between designs is only a few percentage points, experimental error may swamp the signal; a large, clear difference is a more reliable indicator of a genuinely better design. Cost of construction is also a valid factor regardless of raw performance.
- **Turbine design note**: the specific turbine blade design shown is intentionally not the focus of this video — a dedicated video on the design concept and development process is planned.
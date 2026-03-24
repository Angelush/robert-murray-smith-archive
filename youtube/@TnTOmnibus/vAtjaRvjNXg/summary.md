## Overview
Robert Murray-Smith demonstrates how to extract coils from microwave oven transformers (MOTs) to build a simple hand-spun generator, then converts the setup into a Newman Motor using an electronic commutation circuit consisting of just a diode and a transistor. The core insight of the video is that this commutation circuit is identical to the Joule Thief / blocking oscillator, revealing the deeper connection between these seemingly separate DIY electronics topics, and showing that a functional brushless DC motor can be built with just three connections and two passive components.

## Key Topics
- Extracting and repurposing coils from microwave oven transformers
- Thick vs. thin MOT coils: voltage/amperage tradeoffs
- Building a simple hand-powered generator from MOT coils and neodymium magnets
- History and controversy of the Newman Motor (free energy claims, patent disputes, court cases, Congressional hearing)
- Electronic commutation of a DC motor using a diode and transistor (blocking oscillator)
- The Joule Thief circuit and its equivalence to the blocking oscillator
- The role of trigger coils in self-resonant motor circuits
- Winding and forming a serpentine coil (the "Twisted Serpent" printed motor design)
- History of the blocking oscillator: Roger Andrews (1974), Shawnee Borman, John Bedini's SSG
- Connection between Bedini's "Simple School Girl" motor and the Joule Thief/Newman circuit

## Materials and Chemicals Mentioned
- **Microwave oven transformer (MOT) coils** — thick wire coils (high amperage, low voltage) and thin wire coils (high voltage, low amperage), extracted by cutting along the weld line
- **8mm aluminium tube** — used as the rotor axle, with the center flattened to hold magnets
- **22mm skateboard bearings (22×7×8mm, 8mm inner diameter)** — universally used for axle support
- **N35/N52 neodymium magnets (10mm diameter × 2mm thick, circular)** — glued alternating N/S into the rotor
- **Ring magnet** — mentioned as an alternative for a maglev version of the motor
- **Thrust bearing** — used in the Twisted Serpent assembly (from Amazon)
- **1N4007 silicon diode** — used in the commutation/blocking oscillator circuit
- **2N3055 NPN power transistor** — used as the switching element for larger coils; any suitable NPN or PNP transistor will work
- **Blue tape** — used as a mechanical stop on the axle and as markers when winding the serpentine coil
- **M10 bolts** — used in the plywood coil-winding jig, placed 55cm apart
- **Hot glue** — used to mount coils to the baseboard

## Techniques and Methods
- **Extracting MOT coils** — cutting along the weld line of the transformer core to free the primary and secondary windings
- **Building a generator** — mounting two coils on a board at bearing-axle distance, inserting a magnet-bearing axle, and hand-spinning to produce AC output (~2V by hand)
- **Electronic commutation (blocking oscillator)** — using a 1N4007 diode across the coil and a 2N3055 transistor to create a self-resonant switching circuit that drives a brushless DC motor without a mechanical commutator
- **Serpentine coil winding** — winding 200 turns on a two-bolt plywood jig with a loop pulled out at turn 50 to create a tapped coil (50-turn trigger coil + 150-turn drive coil), then taping and folding into a flat serpentine shape
- **Coil tap identification** — marking start/end of each sub-coil before removing from the jig; measuring resistance to confirm connections
- **Trigger coil motor configuration** — one coil acts as the drive coil, the other as the trigger coil feeding the transistor base to sustain oscillation; requires a manual flick to start (non-self-starting)
- **Maglev vs. thrust-bearing mounting** — brief mention of swapping the center indent for a ring magnet to achieve magnetic levitation of the rotor

## Notable Timestamps
- `[00:06]` — Introduction: MOTs as versatile components; goal is to make a generator
- `[00:24]` — Cutting the weld line to extract coils from the MOT core
- `[01:00]` — Explanation of thick vs. thin coil tradeoffs (amperage vs. voltage)
- `[01:44]` — Assembly: gluing coils to board, inserting 8mm aluminium axle, skateboard bearings
- `[02:37]` — Adding neodymium magnets to the flat section of the axle
- `[03:03]` — Testing the generator; ~2V produced by hand-spinning
- `[04:00]` — Transition: converting the generator into a Newman Motor
- `[04:04]` — History of the Newman Motor: patent application (1979), rejection (1983), court case, NBS/NIST testing
- `[05:04]` — Congressional hearing (30 July 1986); conflict-of-interest revelation regarding Newman's assessor
- `[05:23]` — Newman's company, 2007 Alabama securities issue, and investors' loyalty
- `[05:50]` — Theoretical basis of the Newman Motor: counter-EMF build-up claim
- `[06:35]` — Circuit reveal: 1N4007 diode + 2N3055 transistor as electronic commutator
- `[07:08]` — First live demonstration of the Newman Motor running
- `[07:40]` — Discussion of Newman advocates' claims (mechanical commutation, copper-to-energy conversion)
- `[08:00]` — Robert's actual interest: the commutation technique, not free energy
- `[09:28]` — Trigger coils in context: flash camera transformers, flyback circuits
- `[10:06]` — Explanation of why DC motors need switching and how the self-resonant circuit achieves it
- `[11:12]` — Self-resonant / blocking oscillator behaviour explained; why the motor is non-self-starting
- `[12:02]` — Introduction of the Joule Thief and its internet fame
- `[12:35]` — Key insight: Joule Thief = blocking oscillator = Newman motor commutator (same circuit)
- `[12:41]` — History: Roger Andrews' 1974 patent (a runner motor), Shawnee Borman's science prize (2000), Bedini's "Simple School Girl" motor
- `[14:14]` — Introduction of the "Twisted Serpent" 3D-printed motor design; magnet specs
- `[15:15]` — Winding the serpentine coil on the plywood jig: 50-turn tap + 150 turns = 200 total
- `[16:15]` — Identifying and marking the four coil ends (start/end of 50T and 150T sub-coils)
- `[18:10]` — Folding the wound coil into its serpentine shape using tape markers
- `[19:19]` — Final motor assembly complete; transistor wiring instructions (NPN vs. PNP)
- `[21:10]` — Final demonstration: Joule Thief circuit running the brushless motor from a battery

## Robert's Own Replies
No author replies found.
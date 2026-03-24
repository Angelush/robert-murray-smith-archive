## Overview
Robert Murray-Smith explains why PC fans make disappointing generators and demonstrates how to dramatically increase their voltage output by rewinding the coils with thinner, longer wire. By replacing the original 24 AWG wire (62 turns, ~6 metres) with 30 AWG wire wound to 240 turns, he nearly doubles the measured output voltage and achieves enough power to light an LED that previously wouldn't illuminate.

## Key Topics
- The three factors governing EMF in a generator: magnetic field strength, wire length, and rotational speed
- Why PC fans (originally servo motors) are poorly optimised as generators — thick, short wire prioritises current capacity over voltage
- The trade-off between wire gauge, voltage output, and current-carrying capacity
- Rewinding coil poles with thinner wire to increase turn count and wire length
- Comparison with microwave turntable motors as high-voltage generators (very fine wire, thousands of turns)

## Materials and Chemicals Mentioned
- PC fan (brushless, used as wind generator)
- Ceramic magnets (original magnets inside the fan)
- 24 SWG (~0.5 mm) wire — original winding
- 30 gauge (~0.25 mm) wire — replacement winding
- LED (used as output indicator)

## Techniques and Methods
- Disassembly of PC fan: removing the circuit board to expose the coil poles
- Stripping original windings from the stator poles
- Rewinding coil poles by hand with thinner wire to a higher turn count (62 → 240 turns per pair of poles)
- Soldering directly to coil wire ends to form generator output leads
- Voltage measurement with a voltmeter and qualitative load testing with an LED

## Notable Timestamps
- `[00:15]` — Introduction; Robert explains the problem with PC fans as generators
- `[00:36]` — The three factors determining generator EMF are explained (field strength, wire length, speed)
- `[01:27]` — Decision to rewind with longer/thinner wire as the only practical variable to change
- `[01:55]` — Original winding specs revealed: 6 m total, 62 turns, 24 SWG
- `[03:24]` — Rewinding complete: 30 AWG wire, 240 turns (~4× the original length)
- `[03:45]` — Baseline test on unmodified fan: ~1.4 V, LED does not light
- `[04:21]` — Test on rewound fan: ~2.6 V, LED lights brightly
- `[04:42]` — Summary of the three improvement strategies and trade-offs discussed
- `[05:04]` — Aside on microwave turntable motors as an example of the same principle at scale

## Robert's Own Replies
- **On energy conservation:** Clarifies that output power is always less than input power — the generator converts energy, it does not create it. Amps depend on the load, not the generator itself.
- **On usability:** Confirms that the higher voltage makes the output easier to work with practically, which is the point of the modification.
- **On the claim of "dramatic" improvement:** Defends the video title by noting the LED went from zero output to visibly lighting — technically an infinite percentage increase, which he argues qualifies as dramatic.
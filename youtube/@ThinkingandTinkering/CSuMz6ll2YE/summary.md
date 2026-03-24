## Overview
Robert demonstrates how to build a low-cost mechanical inverter by coupling two brushless DC PC fans — one acting as a motor, the other converted into a three-phase AC generator. This is a modern take on the historical "dynamotor" concept, but using brushless motors eliminates the brush wear that made dynamotors obsolete. Feeding 12V DC in, the prototype produces 15V AC out, at very low cost compared to commercial solid-state inverters.

## Key Topics
- History of DC-to-AC inversion and the dynamotor concept
- Limitations of traditional dynamotors (brush wear)
- Brushless DC PC fans as a long-lasting alternative
- Converting a brushless PC fan into a three-phase generator
- Coupling a motor and generator to create a mechanical inverter
- Cost comparison with commercial solid-state inverters (which can cost thousands of pounds)

## Materials and Chemicals Mentioned
- Brushless DC PC fans (used both as motor and converted generator)
- Internal permanent magnets (inside the fan rotor)
- Three-phase stator coils (Y or delta configuration) — tapped for AC output
- Fan control electronics (removed during conversion)
- Plastic disc and bolts (for coupling the two fan units)
- Glue (for coupling alignment)
- Solder / hookup wires (three wires soldered to coil ends)

## Techniques and Methods
- Disassembly of a brushless PC fan: removing label, plastic washer/spring clip, and fan blade assembly
- Extracting the stator coil assembly from the central pillar (press-fit removal using grips)
- Stripping control electronics from the stator PCB
- Soldering three output wires directly to the coil ends (three-phase output)
- Trimming fan blades to the hub to eliminate windage losses
- Coupling motor and generator units using a glued plastic disc and bolts, aligned to the manufactured tolerances of the fan housings
- Measuring AC output across two phases with a multimeter

## Notable Timestamps
- `[00:16]` — Robert introduces the problem: inverters are expensive (thousands of pounds) and DC-to-AC conversion is a century-old problem
- `[00:37]` — Historical context: dynamotors (motor-generator pairs) used until the 1960s, limited by brush wear
- `[01:02]` — Key insight: brushless DC PC fans have no brushes and last decades
- `[01:15]` — Core idea presented: couple two brushless fans as motor + generator to make a brushless dynamotor/inverter
- `[01:56]` — Step-by-step disassembly of a PC fan begins
- `[02:27]` — Stator coils identified; control electronics stripped; three wires soldered to coil ends
- `[03:41]` — Generator tested by hand-spinning: 4V AC measured immediately across two phases
- `[04:00]` — Motor and generator coupled together with plastic disc and glue
- `[04:41]` — Full inverter powered: 12V DC in → 15V AC out, running quietly
- `[05:13]` — Cost summary: prototype cost nothing; even a more powerful version far cheaper than commercial inverters

## Robert's Own Replies
- **Efficiency:** Robert notes that dynamotors (which is essentially what this device is) are reportedly over 95% efficient, though he expresses some scepticism about the upper figure while believing they are genuinely quite efficient.
- **Pure sine wave output:** He believes the output is likely to be a pure sine wave — a significant advantage over digitally-based solid-state inverters, which he argues are not truly pure sine wave regardless of marketing claims.
- **Future plans:** He was considering two improvements — pairing the output with an analogue amplifier (to scale usable power while preserving sine wave quality), and potentially exploring a switched reluctance motor design.
- **Why AC at all:** He comments that AC became dominant for long-distance transmission, but with the growth of on-site micro-generation he no longer sees a fundamental need for it.
- **Motor wiring variants:** He acknowledges brushless fans come in 3-wire and 4-wire versions (sometimes UVW, sometimes plus/minus/signal), and points viewers to his other videos on brushless motor conversion for more detail — he kept this video focused on the inverter concept to avoid making it an hour long.
- **Use case vision:** He sees the primary value of this design as producing a clean, pure sine wave signal for control/analogue purposes, rather than necessarily as a high-power mains inverter in its current form.
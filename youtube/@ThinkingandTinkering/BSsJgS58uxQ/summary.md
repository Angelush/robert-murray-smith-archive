## Overview
Robert demonstrates his all-carbon supercapacitor device being charged and discharged at two different voltages — 2V and 2.4V — to compare energy storage performance. He explains the electrochemical significance of the 1.23V water dissociation threshold, how gas evolution is managed in sealed vs. open (flooded) cells, and concludes that while 2.4V yields substantially more stored energy, it requires an open/flooded cell design due to increased gassing.

## Key Topics
- Water dissociation voltage (1.23V) and its implications for energy storage devices
- Gas evolution management in sealed ("starved") vs. open ("flooded") cell configurations
- Comparison of charge/discharge performance at 2V vs. 2.4V
- Leakage current measurement and effective series resistance (ESR) as quality indicators
- The all-carbon supercapacitor device and its carbon structure

## Materials and Chemicals Mentioned
- **Carbon** — active electrode material in the supercapacitor device
- **Electrolyte** — used in both starved and flooded cell configurations; surface/composition modifications can raise the gassing voltage
- **Hydrogen and oxygen** — gases evolved above 1.23V during water dissociation
- **Lead acid battery electrolyte (water)** — referenced as a comparison case for flooded cell maintenance

## Techniques and Methods
- Charge/discharge cycling in sealed CR2032 coin cells over multiple days to assess cell integrity
- Voltage-stepping to failure ("pop the cell") to determine maximum safe charge voltage
- Electrochemical Impedance Spectroscopy (EIS) to monitor side reactions and gas evolution
- Inductive/motor load discharge test to compare energy delivery at 2V vs. 2.4V
- Leakage current measurement cross-referenced against Maxwell supercapacitor application notes
- C-rate discharge characterisation (C/20, 1C, 5C, 10C, 60–80C) referenced as proper methodology for full characterisation

## Notable Timestamps
- `[00:10]` — Introduction: overview of the three-video series plan
- `[00:43]` — Explanation of the 1.23V water dissociation voltage and gas evolution management strategies
- `[01:39]` — Description of the sealed CR2032 test methodology and voltage-stepping to failure
- `[02:00]` — EIS curves discussed as a check for side reactions
- `[03:32]` — Live discharge test at 2V with motor load; runs ~27 seconds
- `[04:36]` — Device recharged to 2.4V; leakage current (~20–40 µA) noted
- `[06:43]` — Live discharge test at 2.4V; motor runs noticeably harder and longer (~62 seconds, roughly twice as long)
- `[08:08]` — Conclusion: flooded cell at 2.4V offers impressive energy density; further investigation planned

## Robert's Own Replies
- **Units clarification:** The right axis of the display showed volts (starting at 2.000V, decreasing) and the left axis showed milliamps (starting at ~180mA, decreasing) — Robert acknowledged he should have labelled these more clearly in the video.
- **Device type:** Explicitly confirmed the device is a supercapacitor, not a battery, and noted its power density is well suited to the discharge loads shown.
- **C-rate methodology:** Explained that C-rate refers to the capacity of the active material (not resistance), derived from pourbaix diagrams and stoichiometric equations; recommended characterising at C/20, 1C, 5C, 10C, and 60–80C for full investigation. Noted he made a separate video explaining C-rates.
- **Sealing vs. gassing:** Confirmed that at 2V the cell can be sealed, but at higher voltages gassing rate increases, requiring a vented or flooded design — this is why commercial sealed lead-acid batteries always have a vented cap with a recombination catalyst.
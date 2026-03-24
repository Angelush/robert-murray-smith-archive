## Overview
Robert Murray-Smith demonstrates an electrochemical ("green") method for producing graphene that avoids the strong acids used in chemical methods. Using a block graphite electrode, a dilute sulfuric acid/sodium hydroxide electrolyte, and a simple polarity-switching DC setup, he shows that graphene flakes can be produced in about 10 minutes from common materials. The key takeaway is that voltage control (keeping close to 10 V) and polarity cycling are critical to obtaining thin, high-quality flakes.

## Key Topics
- Why a "green" electrochemical method is preferable to chemical graphene synthesis
- Requirements for the graphite electrode (block graphite, not powder; 99.9% purity; 1.5 cm × 1.5 cm submerged area)
- Electrolyte composition and pH targeting (~1.2)
- Voltage protocol: +2.5 V for 1 minute, then cycling ±10 V (2 s positive / 5 s negative)
- Current density calculation using Ohm's law and electrode area
- Practical cell setup with copper counter-electrode and fiberglass barrier
- Suggested improvements: 555 timer relay for automatic polarity switching, potassium hydroxide instead of sodium hydroxide, stabilised power supply
- Reference to his book *Graphene 101* and the Tang Lau method

## Materials and Chemicals Mentioned
- **Block graphite** (99.9% pure, sourced from Graphite Kumaris International) — used as the working electrode
- **Sulfuric acid (H₂SO₄), 98% concentrated** — 2.4 g per 100 mL water; forms the base electrolyte
- **Battery acid (35% H₂SO₄)** — practical alternative; 7.2 g used in place of the 98% grade
- **Sodium hydroxide (NaOH), 30% solution** — 11 mL added to adjust pH to ~1.2; sold as caustic soda
- **Potassium hydroxide (KOH)** — mentioned as a superior alternative to NaOH for thinner flakes
- **Copper** — used as the counter-electrode (in place of platinum)
- **Fiberglass** — used as a physical barrier between electrodes to prevent short-circuiting by graphene flakes
- **DMF (dimethylformamide)** — mentioned in comments as a solvent for dispersing/separating graphene
- **PVP / PEG** — mentioned in comments as surfactants to improve graphene dispersion in water

## Techniques and Methods
- **Electrochemical exfoliation** — polarity-cycling DC method to lift graphene flakes from a bulk graphite electrode
- **Electrode preparation** — splitting block graphite with a chisel, sawing to size, filing, and drilling a 4 mm mounting hole
- **Electrolyte formulation** — mixing dilute H₂SO₄ with NaOH solution to reach pH 1.2
- **Ohm's law / current density calculation** — measuring cell resistance to calculate and control current density (A/cm²) across the electrode face
- **Voltage protocol** — +2.5 V pre-treatment for 1 min; then manual ±10 V cycling (~2 s / 5 s) for ~10 min
- **555 timer relay circuit** — recommended for automated polarity switching
- **Spin-casting and annealing** — mentioned as a verification technique (deposit film, heat to check transparency and conductivity)
- **Vacuum filtration and gentle sonication** — mentioned for washing and dispersing the product

## Notable Timestamps
- `[00:03]` — Introduction: why a green (non-acid) method was requested
- `[00:47]` — Electrochemical method introduced; electrode size specification (1.5 cm × 1.5 cm)
- `[02:00]` — Electrolyte recipe: 100 mL water + 2.4 g H₂SO₄ + 11 mL of 30% NaOH
- `[04:22]` — Voltage protocol explained: +2.5 V for 1 min, then ±10 V cycling
- `[06:10]` — Discussion of potentiostat / reference electrode for research-grade control
- `[07:05]` — Ohm's law and current density calculation walkthrough
- `[09:02]` — Physical cell setup shown on camera; battery acid substitution explained
- `[12:43]` — Live demonstration of polarity switching and visible fizzing/flaking
- `[13:23]` — Result after 10 minutes: visible graphene film on solution surface
- `[14:02]` — Suggested improvements: 555 timer relay, KOH instead of NaOH, stabilised voltage supply

## Robert's Own Replies
- **Voltage sensitivity**: Robert emphasises that 10 V is critical — below 10 V the reaction is too slow; above (12–15 V) flakes peel off too thickly.
- **KOH vs NaOH**: He confirms KOH is a better alkali and encourages trying it, though he hasn't personally tested every combination.
- **555 timer circuit**: He provides a specific Maplin kit reference and describes building one from a 555 chip, two capacitors, and two resistors with a relay. He planned to post a follow-up video on this.
- **Verifying graphene**: Without an electron microscope or Raman spectroscope, he recommends spin-casting the dispersion onto glass, annealing at ~350 °C, and checking for a transparent, conductive film.
- **Dispersing graphene**: He notes graphene doesn't dissolve in water but forms a colloid; surfactants (PVP, PEG) help, but the substrate must withstand ~300 °C to burn off the surfactant. DMF is the most reliable solvent.
- **Electrolyte alternatives**: He suggests sulphuric acid from a car battery as the easiest source, and notes that NaOH is sold as caustic soda in hardware stores.
- **Graphene quality in uncontrolled conditions**: Likely to produce few- to many-layer flake graphite rather than true single-layer graphene without tight voltage/electrolyte control.
- **Intercalation tips**: CuCl₂ can assist intercalation of larger ions (e.g. Al); smaller ions act as intercalation assistants.
- **Flake size**: He uses 5–350 micron flakes; 5 µm is approximately the size of a blood cell.
- **Philosophy**: He repeatedly encourages readers to experiment themselves, noting that "the best answer is often just to try it and see."
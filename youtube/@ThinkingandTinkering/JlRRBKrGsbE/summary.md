## Overview
Robert Murray-Smith teardowns a Kilowatt Labs 3.5kWh "capacitor" module given to him by a friend as a potentially faulty unit to repair. Through careful physical measurements and energy density calculations, he builds a compelling case that the cells inside are not supercapacitors as advertised, but rather lithium titanate (LTO) 18650 batteries — a much cheaper technology being sold at supercapacitor price points. He concludes this is likely a deliberate misdirection and warns anyone considering purchasing Kilowatt Labs or Series products to think carefully.

## Key Topics
- Teardown of a Kilowatt Labs Series 3550 capacitor module (48V, 3.5kWh rated)
- Cell configuration analysis: 1200 cells in a 20-series × 30-parallel × 2-layer arrangement
- Voltage anomaly: 2.4V per cell, below the 2.7V minimum for any supercapacitor
- Weight anomaly: ~43g per cell vs ~30g expected for supercapacitors; matches 18650 lithium batteries (~45g)
- Size anomaly: cells measure 18mm × 65mm — exactly the 18650 battery form factor
- Energy density fraud: claimed ~63 Wh/kg vs actual supercapacitor maximum of ~10–12 Wh/kg (Skeleton Technologies top-end)
- Maximum discharge rate mismatch: rated 1.7C is consistent with LTO batteries, not supercapacitors (capable of 100–200C)
- Price comparison: supercapacitor storage costs ~£60,000–70,000/kWh vs LTO at ~£150–200/kWh
- Cycle life difference: supercapacitors ~1,000,000 cycles vs LTO ~7,000–10,000 cycles
- Risk of deep discharge damage to lithium cells (unlike true supercapacitors)
- Intended application: solar energy storage
- White-labelling: the module appears to be a Chinese-manufactured product rebranded by Kilowatt Labs (a US company)

## Materials and Chemicals Mentioned
- **Lithium titanate (LTO)** — the battery chemistry Robert suspects is inside, matching on voltage (2.4V), weight, size, and energy density
- **18650 cells** — the cylindrical battery form factor (18mm diameter × 65mm height) that the internal cells match exactly
- **Lithium hexafluorophosphate in acetonitrile** — the standard electrolyte used in conventional supercapacitors (mentioned in comments; Robert notes this makes claims of "lithium doping" as a differentiator meaningless)
- **Lithium oxide-based cathode** — component of LTO batteries (mentioned in comments)
- **Graphite, aluminium, copper** — other internal materials of LTO cells (mentioned in comments)
- **Maxwell supercapacitors** — referenced for comparison (5,000–10,000 Farad units, ~600 GBP each)
- **Skeleton Technologies supercapacitors** — referenced as the real-world top-end benchmark (~7–12 Wh/kg)

## Techniques and Methods
- Visual inspection and physical teardown of the module
- Cell counting and series/parallel topology analysis
- Gravimetric measurement: weighing each layer (~25.8 kg) and calculating grams per cell (~43g)
- Caliper measurement of individual cells to confirm 18650 form factor
- Voltage-per-cell calculation from rated pack voltage (48V ÷ 20 cells = 2.4V/cell)
- Energy density calculation: rated kWh divided by total mass to derive Wh/kg and compare against published benchmarks
- Cross-referencing manufacturer technical datasheet specifications against physical measurements
- Comparative analysis against known supercapacitor and LTO battery specifications

## Notable Timestamps
- `[00:11]` — Robert introduces the video, explaining he received the module from a friend as a potentially repairable faulty unit
- `[00:54]` — Identifies the unit as a Kilowatt Labs Series 3550 and notes he pulled the technical datasheet
- `[01:24]` — Opens the module and reveals the internal cell arrays and electronics (contactor, bus bars, BMS, display)
- `[01:52]` — Describes the 1200-cell configuration: 20 series × 30 parallel × 2 layers
- `[02:24]` — First red flag: voltage works out to 2.4V/cell; supercapacitors start at 2.7V minimum
- `[02:56]` — Second red flag: cells weigh ~43g each; supercapacitors of that size should be ~30g
- `[03:19]` — Third red flag: claimed energy density of ~63 Wh/kg is orders of magnitude above any real supercapacitor
- `[04:36]` — Notes the module appears mass-produced and white-labelled, likely from China
- `[05:00]` — Introduces an 18650 cell for physical comparison
- `[05:16]` — Caliper measurement confirms the internal cells are exactly 18mm × 65mm
- `[05:28]` — Notes 18650 lithium batteries weigh ~45g — matching the measured cells
- `[05:41]` — Identifies lithium titanate (LTO) as the specific chemistry matching all anomalies (2.4V nominal, 18650 size, ~45g)
- `[06:36]` — Price breakdown: supercapacitor storage ~£60–70k/kWh vs LTO ~£150–200/kWh; Kilowatt Labs pricing is mid-premium for a budget technology
- `[07:51]` — Discusses the practical consequence: LTO batteries can be permanently damaged by deep discharge, unlike supercapacitors
- `[09:03]` — Concludes the product is likely a scam; warns viewers considering Kilowatt Labs or Series products

## Robert's Own Replies
- **On battery chemistry diversity:** Robert clarifies that "lithium batteries" encompasses many distinct chemistries (LFP, LCO, LMO, LTO, etc.). His objection is not to LTO itself — which is a legitimate technology — but to selling it as a capacitor.
- **On "doped" electrolyte claims:** He dismisses the suggestion that "doping" makes the cells hybrid or special, noting that conventional supercapacitors already use lithium hexafluorophosphate in acetonitrile as standard. The term is a marketing trick.
- **On hybrid supercapacitors:** He states he is unaware of any commercial hybrid supercapacitor-battery cell in production and challenges anyone claiming otherwise to name a specific product (drawing a comparison to Turnigy's misleading "graphene battery" marketing).
- **On LTO cell composition:** He describes LTO batteries as containing a lithium salt electrolyte, lithium oxide-based cathode, graphite, aluminium, and copper.
- **On the people who gave him the module:** He defends the friend who donated it as genuine — he does not believe they knew what was inside, and he takes a charitable view of their motivations.
- **On next steps:** If the cells are not dead, his plan is to test them individually and replace the BMS. He is also keen to slice one cell open to confirm the internal chemistry definitively.
- **Intended use case:** Confirmed as solar energy storage.
- **On the company:** Kilowatt Labs is American; the batteries were sourced from China.
- **On pricing:** He feels even LTO at the prices being charged seems overpriced, though he acknowledges LTO is a good fit for this kind of stationary storage application — his core objection remains the mislabelling.
## Overview
Robert Murray-Smith explains how to design, wind, and install resistance heating coils for a lab kiln, covering both new builds and reconditioning old kilns. Using Ohm's law as the core framework, he walks through calculating the correct wire length for a given voltage supply and fuse rating, then demonstrates the physical winding and fitting process. The video emphasizes that kiln electrics are straightforward and that understanding coil-making is the key skill for affordable kiln ownership and maintenance.

## Key Topics
- Why kiln coil knowledge is essential for building, reconditioning, and maintaining kilns
- Buying secondhand kilns cheaply and replacing the electrics
- Using Ohm's law (V = IR) to calculate required resistance wire length
- Effect of mains voltage (230V UK vs 110V US) on coil resistance requirements
- Series vs parallel coil wiring configurations and their effect on total resistance
- Winding coils on a mini lathe (or by hand/drill)
- Stretching and fitting coils into routed channels in the kiln body
- Connecting coils at the back with brass connectors
- Solid state relays and PID controller as the complete control electronics

## Materials and Chemicals Mentioned
- **Resistance/heating wire** — the primary element; 1.2 mm diameter, 1.72 ohms/metre in this example
- **Nichrome wire** — identified in comments as the wire type (available on eBay/Amazon or kiln suppliers)
- **Kanthal wire** — Robert's preferred material (confirmed in comments); rated to ~1400 °C, suitable for a kiln body rated to 1200 °C
- **Brass connectors** — used to join coil ends and connect supply wires at the back of the kiln
- **Fire brick** — kiln body material; bricks in Robert's purchased kiln rated to 1600 °C
- **6 mm cable** — used for Robert's larger 12 kW kiln wiring

## Techniques and Methods
- **Ohm's law calculation** — determining required wire length from supply voltage and maximum amp draw (fuse rating)
- **Series and parallel resistance calculation** — choosing wiring configuration to stay within supply limits
- **Coil winding on a mini lathe** — winding wire tightly around a mandrel bar slightly smaller than the channel width, allowing the coil to spring out to fit
- **Coil stretching** — manually stretching the wound coil beyond target length to account for spring-back
- **Channel routing** — cutting a groove (round cross-section, made with a copper pipe) in the kiln's fire brick to seat the coil
- **Coil installation** — threading wire ends through pre-drilled holes and pressing the coil into the channel
- **Solid state relay switching** — using a 3–32 V DC signal from a PID controller to switch 24–380 V AC to the coils

## Notable Timestamps
- `[00:15]` — Introduction; explains why kiln build content is split across multiple videos
- `[01:05]` — Shows purchased secondhand kiln (£150); discusses reconditioning rationale
- `[02:00]` — Overview of back-of-kiln wiring: coils, solid state relays, PID controller
- `[03:32]` — Introduces resistance wire; specifies 1.2 mm / 1.72 ohms per metre
- `[04:30]` — Explains AC impedance vs pure resistance; justifies using Ohm's law only
- `[05:27]` — Worked example: 230 V / 13 A fuse → ~18 ohms → ~10.5 m of wire → ~3 kW
- `[07:35]` — Discusses 110 V supply equivalent (~13 ohms, ~1.5 kW)
- `[08:13]` — Series vs parallel coil connections; warns that parallel halves resistance and doubles amp draw
- `[11:02]` — Demonstrates coil winding on mini lathe
- `[12:49]` — Stretching the coil to fit the 45 cm channel
- `[14:14]` — Feeding coil into the channel
- `[14:55]` — Back-of-kiln connections: brass connectors, solid state relay wiring explained
- `[16:48]` — Recap and sign-off; next video will cover control electronics and case finishing

## Robert's Own Replies
- **Wire type and sourcing:** The wire is **Nichrome**; available on eBay, Amazon, or from kiln supply shops (search "kiln wire"). He personally uses **Kanthal**, which he finds gives good service life and is rated to ~1400 °C — sufficient for a 1200 °C kiln body.
- **Maximum temperature:** The kiln reaches around **1200 °C**.
- **Reactance clarification:** Robert acknowledges that the coils do technically have reactance (and capacitance), but it is completely negligible at 50/60 Hz with such high resistance and tiny inductance/capacitance — safe to ignore in this context.
- **Safety:** He dismisses concerns about electric shock risk during normal use, noting you would burn your hand from heat long before encountering an electrical hazard, and that proper safety margins (he added ~20%) are built into the design.
- **Solid state relays:** They do eventually blow but are trivial to replace; his have run in the large kiln for over two years without issue.
- **UK plug fuse context:** Explains the UK ring main system — appliances use 3, 5, or 13 A fuses in the plug, with the ring main breaker at 32 A. That is why 13 A is the working figure.
- **Wire choice advice:** Different wires suit different temperature ranges and atmospheres; a mid-range wire works fine and can always be swapped out as experience grows.
- **Intended use for this kiln:** He plans to use it to make **graphitic carbon nitride (gCN)**, which he has made and filmed before.
## Overview
This video is an update on Robert's ongoing plant battery (microbial fuel cell) project, showing the results of charging a supercapacitor from a moss-based cell over several days. He also introduces a kit for the experiment that he is making available for sale, timed alongside an upcoming live workshop event. The key takeaway is that the stored energy from the plant cell was sufficient to run a small motor for an estimated 30 minutes — a significant improvement over the original few-second runtime.

## Key Topics
- Progress update on the plant battery / microbial fuel cell project
- Introduction of a commercial kit for the experiment
- Demonstration of energy storage using a supercapacitor
- Motor runtime test to measure stored energy capacity
- Overview of kit contents and assembly instructions
- Announcement of an upcoming live workshop (end of May / beginning of June)

## Materials and Chemicals Mentioned
- **Carbon felt** — top electrode layer in the plant battery stack
- **Graphoil (graphite foil)** — bottom electrode layer
- **Zeolite clay** — used as a proton exchange barrier between electrode layers; noted to work "really really well"; also sold commercially as a clay face mask
- **Supercapacitor** — used to store harvested energy from the cell
- **Topsoil** — substrate option for growing plants in the cell
- **Moss** — primary plant material used; plants suited to waterlogged/boggy environments recommended
- **Fertilizer concentrate** — added to water (~half a litre) to sustain the system; kit includes an additive believed to improve performance
- **Soil bacteria** — the biological source of the redox reaction generating electricity (clarified in comments)

## Techniques and Methods
- **Microbial fuel cell construction** — layering graphoil, zeolite clay, and carbon felt in a tray with plant material on top
- **Energy scavenging / harvesting** — continuously trickle-charging a supercapacitor from the low-power plant cell over multiple days
- **Motor runtime test** — discharging the supercapacitor through a small induction motor while monitoring voltage drop as a proxy for stored energy
- **Voltage monitoring** — using a voltmeter connected in parallel to track cell output and capacitor discharge rate

## Notable Timestamps
- `[00:11]` — Introduction; context on the kit and upcoming live event
- `[01:17]` — Walkthrough of kit contents: carbon felt, graphoil, zeolite, fertilizer, crocodile clips, motor
- `[02:28]` — Plant selection advice: waterlogged/boggy plants perform best
- `[03:00]` — Explanation of supercapacitor use for energy storage
- `[04:24]` — Motor demonstration begins; supercapacitor discharged after several days of charging
- `[04:34]` — Motor confirmed spinning; voltage reads 1.84 V dropping to 1.61 V
- `[05:00]` — Estimates ~30-minute motor runtime from moss-charged supercapacitor

## Robert's Own Replies
- **Source of electricity:** The energy comes from the redox reaction of soil bacteria that feed on plant waste produced by photosynthesis — not directly from the plant itself.
- **Motor choice rationale:** The small induction motor (8 mm × 14 mm, sourced from toy quadcopters) is ideal because it runs down to 0.08 V and draws only 10–15 mA. An LED, by contrast, requires a higher forward voltage and will quickly exhaust a very low-power source — this is why a supercapacitor is used in the circuit.
- **System longevity:** The battery will continue to work as long as the moss continues to grow.
- **Metal ion additives:** Adding metals like zinc is not advisable — zinc is not non-toxic (he points to zinc environmental toxicity research) and introducing high concentrations of free metal ions would poison the biological system. The choice is between forcing higher output and killing the system, versus working with it to keep it alive.
- **Output voltage:** The cell produces around 0.3 V, which is sufficient to do useful work — consistent with its nature as a plant microbial fuel cell.
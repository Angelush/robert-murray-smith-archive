## Overview
Robert Murray-Smith presents an improved switchable permanent magnet device he built in his shed, based on a 2001 patent (US6229422) by Penion Taro. The device is a hybrid design drawing from Flynn, Art Porter, and Pantoro, using flux switching via a brief current pulse to permanently toggle a magnet arrangement on or off — holding a 350g steel block with no continuous power. He argues this design is simpler and cheaper than the Flynn device and that its bistable (latching) magnetic state is a practical advantage.

## Key Topics
- Flux switching principle and bistable permanent magnet states
- Comparison to Flynn device, Art Porter's gap motor, and Pantoro's patent
- Demonstration of switching a 350g steel load on and off with a brief pulse
- Energy requirements for flux switching the Alnico magnet
- Advantages of this hybrid design over the Flynn device
- Potential for motor applications using repulsion at switch-on

## Materials and Chemicals Mentioned
- **Alnico magnet** — one of the two rod magnets; used because it can be easily demagnetised and re-magnetised by a brief current pulse
- **Neodymium magnet (N42)** — the second rod magnet; provides strong permanent field opposing the Alnico
- **Steel** — used for pole pieces and the large demonstration block (350g); must be large enough to absorb the flux
- **Copper wire (24 SWG)** — used to wind the 150-turn coil

## Techniques and Methods
- **Flux switching** — brief current pulse through the coil reverses the Alnico magnet's polarity, toggling between NN (flux contained, magnet off) and NS (flux escaping through pole pieces, magnet on)
- **Pole piece construction** — steel pole pieces fitted to the ends of the coil/magnet assembly to channel or contain flux
- **Pulse energisation** — 12V battery, ~10A pulse for ~100 microseconds (~13.1 mJ) sufficient to switch the Alnico
- **Coil winding** — 150 turns of 24 SWG wire, 1.1 Ω resistance
- **FEMM simulation** — recommended (by Robert in comments) for modelling designs before building

## Notable Timestamps
- `[00:17]` — Introduces the device; credits 2001 Penion Taro patent (US6229422)
- `[00:41]` — Live demonstration: device holding 350g steel block with no power
- `[01:01]` — Switches magnet off with a single quick touch to battery terminal
- `[01:36]` — Reverses terminals and switches magnet back on
- `[02:23]` — Explains the bistable/latching nature: state is retained with no power
- `[03:07]` — Describes internal magnets: 2cm × 0.5cm rods, one Alnico, one N42 Neo, in NSNS arrangement
- `[03:43]` — Explains the flux path logic: NN orientation contains flux; NS forces it out through pole pieces
- `[04:39]` — Draws comparison to Art Porter's magnetic shielding motor concept
- `[05:46]` — Gives coil specs: 150 turns, 24 SWG, 1.1 Ω
- `[06:01]` — Energy calculation: 10A from 12V for ~100 µs ≈ 13.1 mJ input
- `[06:58]` — States key advantages: simpler, cheaper, fewer components than Flynn device

## Robert's Own Replies
- **Orientation of rod magnets**: North at the top, south at the bottom of the rods.
- **Why it only works with Neo + Alnico**: The Alnico is demagnetised and re-magnetised by the pulse; the Neo is not. Initial orientation doesn't matter — pulsing will switch it to whichever state it needs to be in.
- **Flux path explanation**: NN orientation forces flux through the pole pieces (magnet "on"); NS orientation contains flux entirely within the magnets (magnet "off"). Pole piece size matters — there must be enough steel to absorb the flux.
- **Coil design guidance**: Calculate required ampere-turns from magnet flux density; fewer turns means higher current and thicker wire; heat dissipation must be factored in.
- **Reducing switching energy**: Suggests back-EMF harvesting from the coil to recover energy, and a 555 timer-based switching circuit (as used in his gap motor replication video) to bring it closer to Art Porter's design.
- **Pull force**: Follows inverse-square law with distance. The steel block demo is just to show the effect scale; the magnet itself is tiny (2cm × 0.5cm rod).
- **Modelling recommendation**: Recommends FEMM (free software) for designing and modelling coil/magnet arrangements before building; refers users to his FEMM tutorial videos.
- **Current work**: At time of writing, was also working on MHD augmentation of water arcs (à la Graneau) in parallel with flux switching experiments; acknowledged having several failed flux switching models and offered to post videos of those.
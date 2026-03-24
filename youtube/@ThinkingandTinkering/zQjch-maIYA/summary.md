## Overview
Robert Murray-Smith demonstrates how to convert a mains-powered LED panel light to run on batteries, revealing that the conversion is simpler than expected because these panels already operate on DC internally. The key modification involves rewiring the internal LED strips from a series configuration to a parallel one, which reduces the required voltage from ~36V to ~24V, making it practical to power with two 12V car batteries.

## Key Topics
- How LED panel lights work internally (AC-to-DC conversion via transformer)
- Why battery conversion is straightforward — the panel is already a DC device
- Internal construction of a cheap LED panel (reflector, acrylic light guide, diffuser layers)
- Series vs. parallel wiring of LED strips and the trade-offs (voltage vs. current)
- Practical battery options for powering the rewired panel

## Materials and Chemicals Mentioned
- LED panel light (budget, ~£12)
- Thin pressed steel back panel
- Reflective white plastic sheet
- Acrylic light guide (pitted, Fresnel lens, or linear pattern)
- Frosted plastic diffuser
- AC-to-DC transformer (230V in, 27–42V DC out at 900mA)
- Red and black extension wire (soldered onto LED strip terminals)
- Kapton tape (used to secure wiring; original used Sellotape)
- 12V car batteries (×2, connected in series for 24V supply)

## Techniques and Methods
- Disassembly of LED panel (unscrewing or unclipping the back)
- Reading transformer and box labels to determine voltage/current specs
- Identifying LED strip polarity by wire colour (red = positive, black = negative)
- Soldering extension wires to LED strip terminals for clearer identification
- Rewiring LED strips from series to parallel (joining red-to-red, black-to-black)
- Reassembly with internal layers stacked in original order

## Notable Timestamps
- `[00:16]` — Introduction; context from previous light box video
- `[00:38]` — Contents of the box: transformer and LED panel described
- `[01:11]` — Key insight: the panel is already a DC device; conversion is simpler than people think
- `[01:51]` — Disassembly begins; internal layers explained (reflector, acrylic, diffuser)
- `[04:00]` — Reading voltage/current specs from transformer label (27–42V DC, 900mA)
- `[05:08]` — Decision to rewire from series to parallel to reduce operating voltage to ~24V
- `[05:39]` — Close-up of soldering extension wires and identifying polarity
- `[07:27]` — Rejoining wires in parallel (red-to-red, black-to-black)
- `[08:09]` — Reassembly and screw replacement
- `[09:01]` — Live demo: panel powered by two 12V car batteries — success

## Robert's Own Replies
- Confirmed that **18V might be a viable supply voltage** and acknowledged it as a good idea, though he notes the video is primarily demonstrating proof-of-concept.
- Clarified on **reassembly order of internal layers**: layers should be stacked back exactly as removed; if mixed up, there are few combinations and it's easy to trial-and-error back to correct order.
- On **current limiting**: questioned why a current-limiting circuit would be needed, suggesting the voltage limit is sufficient and noting that a simple current-limiting circuit is essentially just a diode and resistor network — which the existing circuit already approximates. He later acknowledged a commenter's explanation on this point.
- Noted that **regional availability of LED panels varies** — some places have adopted them widely, others haven't.
- One reply references a specific LED panel product link (ledkia.com), likely in response to someone asking where to buy one.
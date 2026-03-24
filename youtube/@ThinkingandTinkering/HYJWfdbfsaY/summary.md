## Overview
Robert Murray-Smith demonstrates how to repurpose an old desktop PC — specifically its ATX power supply and case — to build a functional hot wire cutter. He walks through stripping the PC, decoding ATX wire colours to extract a 12V supply, and using a cheap PWM speed controller to regulate wire temperature. The finished tool is tested cutting polystyrene foam and proves highly effective at low cost.

## Key Topics
- Selecting and stripping an old PC for its ATX power supply and enclosure
- ATX power supply wire colour coding and bundling (12V, 5V, 3.3V, ground)
- Using the green "power-on sense" wire to add a front-panel on/off switch
- Using purple (standby) and gray (power good) wires to drive LED status indicators
- Pulse width modulation (PWM) as a method for controlling current and wire temperature
- Using a PWM motor speed controller as a temperature controller for the hot wire
- Building and mounting the wire support arm using steel rod
- Using a ceramic power transistor body as an insulating hook for the hot wire
- Calculating required wire resistance using Ohm's law (V=IR)
- Cutting polystyrene foam as a demonstration

## Materials and Chemicals Mentioned
- **Old desktop PC** — donor of case and ATX power supply
- **ATX power supply** — repurposed for 12V DC output
- **PWM speed/motor controller** — ~£5, used to control wire temperature via pulse width modulation; must handle up to 6A at 12V
- **Nichrome resistance wire** — the cutting element; minimum ~2 ohms resistance required at 12V/6A
- **6mm steel rod** — bent into a support arm ("gibbet") for the wire
- **Ceramic power transistor** — repurposed as an insulating hook at the top of the arm
- **LEDs** — standby and power-good indicators
- **Resistors (200–400 ohm)** — current-limiting resistors for the LEDs
- **Single-pole single-throw (SPST) switch** — front-panel power switch wired to the green sense wire
- **Bolt, washers, and nut (ideally wing nut)** — lower wire connection point, mounted through a wood block
- **Polystyrene foam** — used in the cutting demonstration

## Techniques and Methods
- **ATX power supply repurposing** — bundling and soldering same-colour wires together to consolidate voltage rails
- **Power-on sense wire mod** — shorting the green wire to ground to allow the ATX supply to run standalone
- **PWM current control** — using a pulse width modulator to vary effective current through the resistance wire, controlling cutting temperature
- **Ohm's law wire sizing** — applying V=IR (12V ÷ 6A = 2Ω minimum) to select appropriate resistance wire
- **Ceramic insulator repurposing** — drilling and bending a power transistor to serve as an insulated wire hook
- **Steel rod bending** — forming a simple cantilever arm to suspend the wire over the cutting surface
- **LED indicator wiring** — wiring LEDs with dropping resistors to the purple and gray ATX wires for standby/power-good status

## Notable Timestamps
- `[00:15]` — Introduction: plan to build a hot wire cutter from an old PC
- `[01:16]` — PWM speed controller introduced; explanation of pulse width modulation for current/temperature control
- `[02:53]` — PC stripped; ATX power supply removed for modification
- `[03:07]` — ATX wire colour coding explained (yellow = 12V, black = ground, red = 5V, orange = 3.3V)
- `[04:57]` — Green wire (power-on sense) explained; wired to ground via front-panel switch
- `[05:52]` — Purple (standby) and gray (power good) wires used for LED indicators
- `[07:09]` — Wiring reassembled and summarised; green/black to switch, purple/gray to LEDs
- `[08:31]` — Underside of unit shown; wiring to control board and wire connection points described
- `[09:09]` — Face plate assembled with speed controller, potentiometer, switch, and LEDs
- `[10:51]` — Live demo: cutting polystyrene foam at 26% power
- `[11:46]` — Wire resistance calculation explained (V=IR, minimum 2Ω for 12V/6A)

## Robert's Own Replies
- **On expanding to a full bench power supply:** Robert acknowledges he regretted cutting off all wires except the yellow (12V) for simplicity, and confirms that collecting the orange (3.3V) and red (5V) wires onto their own binding posts would turn the unit into a multi-rail bench top power supply — something he says he'd like to do in a remake.
- **On wire resistance:** He clarifies that you need a minimum of 2 ohms resistance wire, derived from V=IR (12V, max 6A). Resistance wire is sold by resistance per metre, so you size it to your wire length.
- **On fumes/safety:** He addresses concerns about toxic fumes from burning polystyrene, saying that working in a well-ventilated space (open window, door, fan) is adequate, and that an extractor or fume hood could easily be added if desired. He also notes that cyanide is not a byproduct of burning polystyrene, though fumes are produced.
- **On the enclosure:** He emphasises that the PC case is a frequently overlooked but excellent enclosure, noting that enclosures are expensive to buy new.
- **On self-reliance:** He reflects that building tools like this is part of a broader philosophy of self-reliance, which the COVID period reinforced for him.
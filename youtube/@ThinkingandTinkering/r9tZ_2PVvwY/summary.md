## Overview
Robert Murray-Smith demonstrates how to build a large-scale radiant wall heater by painting heat-resistive (carbon-based) ink directly onto a plasterboard panel mounted on a wall. The finished unit measures 2.4 × 1.2 metres, draws approximately 3 amps at 230V (0.8 kW), and heats up to a safe maximum of ~60°C surface temperature. The video walks step-by-step through surface preparation, copper tape electrode installation, thermocouple placement, ink application, resistance testing, and controller wiring, with the aim of making this a viable DIY or small-business heating solution.

## Key Topics
- Concept of painting a radiant heater directly onto a wall or floor using conductive ink
- Surface preparation (plasterboard/drywall substrate)
- Copper tape electrode layout and electrical connections
- Thermocouple (temperature sensor) installation and embedding in wall filler
- Resistance measurement to determine power output (Ohm's law applied)
- Ink application technique — rolling in a serpentine/ladder pattern vs. solid block
- Controller options: simple rheostat PWM boards (~£1–2), PID kit controllers (~£20), and digital underfloor-heating controllers (~£60)
- Wiring to mains supply (UK colour codes: brown = live, blue = neutral, bare = earth)
- Electrical safety, UK wiring regulations, and Class II device classification
- Covering the finished heater (vinyl, tiles, carpet, skirting board)
- Potential applications: walls, floors, ceilings, bathrooms, portable roll-out panels

## Materials and Chemicals Mentioned
- **Heat-resistive / carbon-based conductive ink** — the core heating element, painted onto the substrate; Robert notes he made his own and did a separate video on how to make it
- **Copper tape** — used as electrode bus bars along the edges; approximately 5 metres long, 1 cm wide per run; must lie flat and be painted over to ensure good carbon-to-copper junction
- **Plasterboard (drywall)** — substrate for the heater panel (½ metre × 2.4 metre sheet)
- **Rockwool / insulation board** — mentioned as optional backing/insulation material
- **Wall filler (spackle/compound)** — used to embed the thermocouple sensor just below the surface
- **Masking tape** — used to define painting zones and panel geometry
- **Plastic sheeting / vinyl** — protective cover over the live heating surface
- **Earth sleeving (green/yellow)** — used to safely terminate the earth wire where no earth connection is required (Class II device)
- **Sodium silicate** — mentioned in comments as a suitable fireproof binder for making resistive ink at higher temperatures
- **Kapton film** — mentioned in comments as a high-temperature (up to 400°C) alternative covering material

## Techniques and Methods
- **Substrate preparation** — sealing an absorbent surface before painting to prevent excessive ink absorption and uneven resistance
- **Copper tape layout** — applying continuous strips (no joins) along the top and bottom edges as bus bar electrodes, folded and clamped for electrical connections
- **Thermocouple embedding** — drilling a hole in the wall/board, routing the sensor wire through a conduit or plastic box, filling over the sensor ball with wall filler, sanding flush
- **Resistance measurement** — using a multimeter across the copper bus bars before and after each coat; target range is ~50–100 Ω for the desired ~0.8 kW output at 230V
- **Ink rolling** — applying with a paint roller in a serpentine (ladder/zigzag) pattern rather than solid blocks, for more even heat distribution; ~25 mL of ink used for the full 2.4 × 1.2 m panel
- **Multi-coat application** — applying coats, allowing each to dry for a couple of hours, retesting resistance, and adding further coats until target resistance is reached
- **Mains wiring** — connecting live (brown), neutral (blue), and earth (bare) from the controller output cable to the copper tape electrodes using clamp connectors screwed into timber backing; earth terminated with sleeving (Class II, no chassis earth needed)
- **Controller wiring** — connecting supply, load (heater), and thermocouple sensor to the digital underfloor-heating controller per its labelled terminals
- **Strain relief** — fitting a cable clip to the supply plug cable so mechanical pull acts on the clip rather than the electrical connections inside the box

## Notable Timestamps
- `[00:04]` — Introduction: completed wall radiator revealed, scale demonstrated (2.4 × 1.2 m)
- `[01:06]` — Electrical specs stated: 0.8 kW, 3 A at 230V, max 60°C surface temperature
- `[01:28]` — Controller described; thermocouple explained as the temperature-sensing element
- `[04:00]` — Substrate preparation shown: plasterboard panel screwed to wall frame
- `[07:30]` — Thermocouple installation: embedding sensor in wall filler just below surface
- `[08:00]` — Copper tape application: continuous strip, 400–600 mm section spacing guidance
- `[10:35]` — Cable routing and mains wiring colour codes explained (UK: brown/live, blue/neutral, bare/earth)
- `[11:44]` — Making the copper tape electrical connection: folding, clamping, screwing into timber
- `[15:19]` — Ink application begins: rolling technique, masking tape pattern layout
- `[15:57]` — Resistance testing procedure explained: checking ohms after each coat
- `[16:22]` — Finished painted panel shown with masking tape removed
- `[17:06]` — Power calculation: ~65 Ω resistance yields ~0.8 kW at 230V; Ohm's law discussion
- `[18:17]` — Controller options reviewed: PWM rheostat board (~£1–2), PID kit (~£20), digital thermostat (~£60)
- `[21:31]` — Electrical safety warning: UK regulations, electrician's qualification, "appliance" loophole via plug
- `[23:59]` — Live test: heater switched on, temperature monitored with thermometer
- `[26:26]` — Summary of performance and covering options (tiles, vinyl, carpet, skirting board)

## Robert's Own Replies
- **Check local electrical codes** — Robert repeatedly emphasises verifying regulations for your country; he mentions UK rules are strict but notes wiring requirements differ internationally.
- **Class II device safety** — In a detailed reply, Robert explains that the heater qualifies as a Class II appliance (double insulation, no exposed metal), which does not legally require an earth connection. He cites IET Wiring Regulations BS 7671:2008(2011) 17th edition. He clarifies: use thick plastic over the surface to prevent contact with the element, not a chassis earth.
- **Ink is no longer sold; make it yourself** — Robert confirms he stopped selling the resistive ink and instead made a video on how to produce it at home. He encourages experimentation.
- **Fireproof ink variant** — For applications requiring fire-resistant ink, he suggests using **sodium silicate as a binder**; **Kapton film** is mentioned as suitable for covering up to 400°C.
- **Power calculation** — He directs people to use Ohm's law (DC resistance as an approximation for AC impedance) to calculate the power draw from the resistance measured across the electrodes.
- **Floor vs. wall** — He advises painting the floor is preferable to the wall because heat rises.
- **Business potential** — He encourages the idea of making portable "art radiators" on coloured plastic sheets with a controller and plug as a viable small business concept.
- **Running all winter** — He confirms the heater shown was run all winter without issues, though he acknowledges concern about people inexperienced with wiring attempting the project.
- **Stepping down voltage** — He notes that operating at lower voltages (e.g., 40V via a dimmer, as done in another video) removes concerns about high-voltage safety while still producing useful heat.
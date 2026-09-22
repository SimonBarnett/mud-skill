---
name: discworld-travel-transport
description: >
  Discworld MUD travel: carriages, ferries, guild travel, portals, arcane NPC
  travel. Use when the user says DW carriage, intercontinental express, get to
  Lancre, or /discworld-travel-transport.
  Does not stamp ready for human UAT.
---

# Discworld MUD — travel and transport

Companion to `mud-skill`, `discworld-city-*`, and `discworld-mud`.

**Sources (link-out):**

- [Travel concept](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ftravel)
- [Carriages concept](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Fcarriages)
- [Carriages (wiki)](https://dwwiki.mooo.com/wiki/Carriages)
- [Travel overview (wiki)](https://dwwiki.mooo.com/wiki/Travel)
- [Jogloran's Portal (wiki)](https://dwwiki.mooo.com/wiki/Portal)
- FAQ transport list on [concepts/faq](https://discworld.starturtle.net/lpc/playing/documentation.c?path=%2Fconcepts%2Ffaq)

## LOCKED — On foot

- Default: read **exits from game text only** (`mud-skill` navigate procedure).
- Long wilderness legs: human approves supplies, wimpy, and corpse recovery plan
  (`discworld-death-recovery`).

## LOCKED — Carriages (everyone, free, slow)

1. Find a **carriage stop** — coloured **note** on a pole lists route stops.
2. When carriage arrives, **`enter carriage`** (exit name appears in room).
3. Driver **calls stops** — **`leave carriage`** at destination (some routes
   support `leave carriage at <stop>` per wiki).
4. Routes loop; you may need to **transfer** between lines (public carriages help).
5. Generally **safer** through dangerous terrain than walking; rare NPC aggro at stops.

Named inter-city examples (wiki — not exhaustive): **Intercontinental Express**,
**Mail Carriage**, **Djelibeybi**, **Istanzia River**, **Lancre Kingdom**, **Uberwald**,
**Steppes**, **Ankh River** circuit, plus **five AM city carriage** routes.

## LOCKED — Ferries and water

- River **ferries** at bridge crossings (wiki travel page) — use game exits;
  corpses may not drag through water (`discworld-death-recovery`).

## LOCKED — Guild / magic travel (gated)

| Method | Who (public docs) | Agent note |
|--------|-------------------|------------|
| Broom flight | Witches (skill + fuel) | Human OK before long flight while fragile |
| Divine Hand | Priests | Patron/faith dependent — read help |
| Teleport / portal spells | Wizards (blorple + JPCT) | `look enter portal` before use; misportals possible |
| JPCT scrolls | Non-wizards with magic skill | One-way; door may wobble/burn |

## LOCKED — Arcane transport NPCs

- Some NPCs offer **`list`** then **`travel to <destination>`** — destinations
  depend on NPC (wiki travel). Human confirms cost and one-way rules in room text.

## UNKNOWN

- Current carriage timetable lag — wait in room or check player maps (wiki maps by
  community; do not treat as LOCKED coordinates).

## Do not

- Memorise speedwalk strings as LOCKED without in-game verification.
- Stamp ready for human UAT.

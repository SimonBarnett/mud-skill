---
name: mud-character-creation
description: >
  Umbrella character-creation playbooks for text MUDs: what to decide before
  connect, race/species vs nationality, stats, guild/class timing. Use when the
  user says character creation, new char, roll a character, or /mud-character-creation.
  Does not stamp ready for human UAT.
---

# Character creation (umbrella)

Companion to `mud-skill`. Each game has its own rules — load the matching
leaflet when the human names the MUD:

| MUD | Skill |
|-----|--------|
| Discworld MUD | `discworld-character-creation` |
| Achaea | `achaea-character-creation` |

## LOCKED — Before you connect

1. Confirm **which MUD instance** and client path with the human (umbrella
   `mud-skill` **Procedure: connect**). Never invent host, port, or credentials.
2. Capture the human's **intent**: guild/class, roleplay tone, solo vs group,
   and whether this is a throwaway newbie or a long-term character.
3. Read **only** public help/wiki for that game; mark gaps **UNKNOWN** — do not
   invent room names, ENAMEs, or recruiter locations.

## LOCKED — Common decision order (pattern)

Most class-based MUDs follow a similar arc (details differ per game):

1. Account / character name (operator supplies login secrets).
2. **Body choices** — race/species, gender gates, nationality/starting region.
3. **Starting location** — often tied to nationality or tutorial zone.
4. **Stats** — may be fixed, rolled once, or rearranged later; read help before
   spending one-time `rearrange`-style commands.
5. **Tutorial / newbie area** — complete orientation before open-world travel.
6. **Guild / class / house** — major fork; confirm with human before join.

## Do

- Link to world-specific skills for numbered steps and cited URLs.
- Log choices the human made (no passwords).

## Do not

- Stamp ready for human UAT (Bob only).
- Treat wiki speedwalks as LOCKED room names without in-game verification.

---
name: mud-skill
description: >
  Umbrella agent skill for playing MUDs (connect, navigate, combat, quest,
  economy playbooks). Discworld MUD details live in companion discworld-mud.
  Use when the user says MUD, MUD playbook, telnet mud, DW MUD, Discworld,
  or /mud-skill. Does not stamp ready for human UAT.
---

# MUD skill (umbrella)

Playbooks for agents in text MUDs. Prefer world-specific companions when
the game is named (start with `discworld-mud`).

When connected to **Discworld MUD** and room text or the human indicates
**Ankh-Morpork** (AM), load companion **`discworld-ankh-survival`** before
generic navigation — especially for newbies (“dead in 10 minutes” in AM).

## GATES (stub)

| Gate | Status | Entry |
|------|--------|--------|
| connect | LOCKED stub | **Procedure: connect (stub)** below |
| navigate | LOCKED stub | **Procedure: navigate (stub)** below |
| combat | UNKNOWN stub | **Procedure: combat (stub)** below (U4) |

## Procedure: connect (stub)

1. LOCKED — Ask the human which MUD instance and which client or telnet path
   to use; never invent host, port, TLS, or credentials.
2. LOCKED — Connect only with operator-supplied details; do not echo passwords
   into logs, commits, or issue comments.
3. UNKNOWN — Wire format (plain telnet vs TLS vs existing fleet tool) stays
   U1 until the human or harvest doc names one.
4. LOCKED — After login, capture prompt/character name from game text; if
   login fails, stop and report verbatim errors (no credential guessing).

## Procedure: navigate (stub)

1. LOCKED — Read the current room description and listed exits from game output
   only; do not invent room names or directions.
2. LOCKED — Maintain a short session log: room label (as shown), exits, and
   notable NPCs/items; no passwords.
3. UNKNOWN — Automap or client scripts (U1) — defer until human approves a tool.
4. LOCKED — Before `go`/`enter` into risky or one-way areas, confirm with the
   human when the skill or companion marks the action irreversible.

## Procedure: combat (stub)

1. LOCKED — Confirm with the human whether to engage; default human-in-the-loop
   for lethal or loot-heavy fights (U4).
2. LOCKED — Parse target name and health cues from game text; issue only commands
   the game accepts (e.g. kill/flee) as shown in help or human instruction.
3. UNKNOWN — Optimal rotations, guild combos, and XP grinding routes — harvest
   later; use companion class playbooks when present.
4. LOCKED — Stop and ask before `pkill`, looting unique items, or continuing
   after a death message.

## Do

1. Confirm which MUD (never invent host/port/login).
2. Load the matching companion skill if present (Discworld + AM →
   `discworld-ankh-survival`; other Discworld → `discworld-mud`).
3. Keep a short session log (room, exits, HP/GP if shown) — no passwords.
4. Ask before irreversible actions (pkill, drop unique, guild resign).

## Do not

- Store or commit credentials.
- Stamp ready for human UAT (Bob only).
- Confuse this with `MUD-AI` (separate product).
## CAST IRON harvest (Simon 2026-09-22)

This repo must keep a harvest foundation like `agentic_build`. When you
learn a MUD / Discworld playbook, harvest it into `.grok/skills/` here
and note `docs/skill-harvest-log.md`. Do not leave it only in `~/.grok`.
Empty harvest: no commit. See `SimonBarnett/agentic_build` skill
`harvest-agent-skills`.

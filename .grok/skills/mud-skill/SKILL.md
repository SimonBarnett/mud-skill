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

## Do

1. Confirm which MUD (never invent host/port/login).
2. Load the matching companion skill if present.
3. Keep a short session log (room, exits, HP/GP if shown) â€” no passwords.
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

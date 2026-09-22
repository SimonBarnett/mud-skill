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
the game is named (start with `discworld-mud`; **57+** leaflets under
`.grok/skills/discworld-*` and topic skills — issues #23, #26).

## Topic playbooks (#26)

| Topic | Skill |
|-------|--------|
| Character creation (umbrella) | `mud-character-creation` |
| Discworld char create | `discworld-character-creation` |
| Achaea char create | `achaea-character-creation` |
| Death / corpses | `discworld-death-recovery`, lore: `discworld-lore-death` |
| Money / currency | `discworld-money-currency` |
| Shops (where + workflow) | `discworld-shop-*` |
| Travel | `discworld-travel-transport` |
| Skills / XP | `discworld-skills-experience` |

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
3. LOCKED — Discworld plain TCP on port 4242 answered (playtest 2026-09-22).
   TLS port 4245 and any fleet wire client stay UNKNOWN.
4. LOCKED — After login, capture prompt/character name from game text; if
   login fails, stop and report verbatim errors (no credential guessing).

### Discworld front door (playtest 2026-09-22)

Source: [Getting Started](https://discworld.starturtle.net/lpc/playing/getting_started.html). Observed on plain TCP `discworld.starturtle.net` port 4242. Banner: `LPmud version : DW OS v1.02 on port 4242.`

1. LOCKED — That page names ports 23 and 4242, and TLS port 4245. This session used 4242 only. Treat 23 and 4245 as cited, not re-tested.
2. LOCKED — The first screen is a menu, not a room:

```
Q - Quit
M - Print this menu again
D - Delete your character
R - Request a temporary password
U - Short list of who is on-line
L - Short list of liaisons on-line
P - Uptime
F - Finger someone
N - New character
G - Guest character
Or, enter your current character's name
Your choice:
```

3. LOCKED — Do not send `look`, `score`, `inventory`, or `quit` until game text shows a room and exits. At the name prompt those words are names. Reply seen: `Sorry the player name look has been banished.` Same for `score` and `inventory`.
4. LOCKED — Guest creation is menu `G`, then the prompt list in `discworld-character-creation`.
5. LOCKED — Terms include the line `Use of robot scripts or triggers is not permitted.` Stop. Do not accept. Do not send play commands. Show the terms to the human. The human plays, or the session ends.
6. LOCKED — After the terms list the game says it will be back in 30 seconds. Send nothing during that wait.
7. UNKNOWN — Wording of the accept prompt after the wait. Do not invent a yes/no command.
8. LOCKED — No passwords in logs, commits, or issues.

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

When you learn a MUD / Discworld playbook, load and follow
`harvest-mud-skill` (this repo). Do not leave playbooks only in
`~/.grok/skills`.

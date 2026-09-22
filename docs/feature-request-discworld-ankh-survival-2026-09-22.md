# Feature request: Discworld Ankh survival details

**Repo:** `SimonBarnett/mud-skill`  
**Date:** 2026-09-22  
**Source:** Simon via https://github.com/SimonBarnett/mud-skill/issues/3 — "MUCH more details". Agent with the P0 stub is dead inside of 10 minutes in Ankh-Morpork. Harvest loads of play information so the seat has a fighting chance.

## Intent / critique

| | |
|--|--|
| **Intent** | P1 harvest: enough Discworld / Ankh-Morpork playbook detail that an agent survives the first minutes (streets, NPCs, combat, newbie path). |
| **Good** | P0 already separated umbrella `mud-skill` from companion `discworld-mud`. |
| **Bad** | Companion is UNKNOWN stubs only (guild table + three-line newbie path). No street, combat, or class playbook a seat can follow. |
| **Ugly** | Issue #3 had no intake doc and no `feature-request` label until this park. |

## Gap vs current tree

At P0 seed (`docs/feature-request-mud-skill-2026-09-22.md` / L1–L10):

- `.grok/skills/discworld-mud/SKILL.md` names Warrior / Thief / Witch / Wizard as UNKNOWN and defers guild choice.
- Umbrella skill has no connect / navigate / combat GATES beyond a four-line Do list.
- `docs/skill-harvest-log.md` is seed-only (no harvested Ankh procedure).

This FR is **not** a re-ask of P0 file presence. It is the harvest Simon named on #3.

## Ask (MUST)

1. Harvest operator-approved Discworld / Ankh-Morpork procedures into `.grok/skills/discworld-mud/` (or a companion), not only `~/.grok`.
2. Cover at stub-or-better: newbie streets, combat survival, and at least one class playbook a seat can follow without dying in ten minutes.
3. Log the harvest in `docs/skill-harvest-log.md` (what / from where). Prefer companions over one mega-file (L4).
4. Keep U2: lore is stubs or cited operator-approved sources — do not invent canon.

## LOCKED

| ID | Requirement |
|----|-------------|
| S1 | No invented Discworld host/port or player login. Confirm connection details from the human. |
| S2 | No secrets in git. No `password=` / API key assignments. |
| S3 | Workers do not stamp ready for human UAT (Bob only). |
| S4 | Do not break P0 paths: `.grok/skills/mud-skill/SKILL.md`, `discworld-mud`, BT0 validate/install. |

## UNKNOWN

| ID | Item |
|----|------|
| U2 | How much Discworld lore is fair-use in-repo vs link-out only (same as functional spec). |
| U4 | Automation vs human-in-the-loop for combat. |
| U5 | Which class playbook to expand first (Warrior / Thief / Witch / Wizard / other). |

## Out of scope

- Full telnet client product (functional spec U1).
- Replacing `SimonBarnett/MUD-AI`.
- Real credentials.
- Re-doing P0 file seed (that is issue #1).

## Acceptance

| ID | Criterion |
|----|-----------|
| B1 | Discworld companion has followable Ankh / newbie-street steps (not only "orient: whoami"). |
| B2 | Combat survival playbook stub or better (flee / look / when to ask the human). No invented host. |
| B3 | At least one named class playbook with steps, UNKNOWN marked where unharvested. |
| B4 | Harvest log names sources (or operator-approved link-out). Empty harvest: no commit. |
| B5 | BT0 still exits 0. S1–S4 honored. |

## Bob-job

Dispatch `bob-job-loop` on the parked issue after this markdown is on git. Do not implement inside an MRB job for issue #1.

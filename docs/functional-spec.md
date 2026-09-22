# Functional spec: mud-skill (LOCKED)

**Product:** `SimonBarnett/mud-skill` — agent skill pack for MUD play.  
**First world:** Discworld MUD (classes, guilds, combat/rituals, navigation).  
**Source ask:** Simon `#bobiverse` 2026-09-22 — harvest MUD-relevant skills; Discworld in particular; new public repo; functional spec; bob-job it.

## Intent

Give Bob / fleet seats a single skill home that:

1. Collects **repeatable MUD play playbooks** (connect, navigate, combat, quest, economy).
2. Specialises for **Discworld MUD** class/guild knowledge and game-specific rituals.
3. Stays **skill-shaped** (`.grok/skills/*/SKILL.md`) — not a second MUD client, not a secret store.

Related but separate: `SimonBarnett/MUD-AI` (game/sim product). This repo is **skills for agents playing MUDs**, not the AI-MUD game itself.

## LOCKED

| ID | Requirement |
|----|-------------|
| L1 | Skill path: `.grok/skills/mud-skill/SKILL.md` with YAML `name: mud-skill`. |
| L2 | Triggers include: MUD, Discworld MUD, DW MUD, mud playbook, /mud-skill. |
| L3 | Docs: this file, `docs/feature-request-mud-skill-2026-09-22.md`, `docs/build-and-test-plan.md`. |
| L4 | Harvest: inventory MUD-relevant procedures into skills (general MUD + Discworld-specific). Prefer companions under `.grok/skills/` rather than one mega-file. |
| L5 | Discworld focus P0: classes/guilds overview, newbie path, and at least one class playbook stub. |
| L6 | No secrets in git. No `password=` / API key assignments. No invented instance URLs or player credentials. |
| L7 | Workers do not stamp ready for human UAT (Bob only). |
| L8 | `tools/Validate-MudSkill.ps1` (BT0) exits 0 when structure checks pass. |
| L9 | `tools/Install-MudSkill.ps1` copies skills into `~/.grok/skills`. |
| L10 | BT0 CI workflow optional but preferred (`.github/workflows/bt0.yml`). |

## MUST NOT

| ID | Rule |
|----|------|
| N1 | Push `main` or merge own PR (workers). |
| N2 | Post ready for human UAT / final PASS-UAT (Bob only). |
| N3 | Commit real player passwords, auth tokens, or private Discord/IRC secrets. |
| N4 | Replace `MUD-AI` product scope; do not vend a full client as the P0 deliverable. |

## UNKNOWN

| ID | Item |
|----|------|
| U1 | Preferred MUD wire client (telnet / TLS / existing `irc-skill` / `agentic_irc` compose). |
| U2 | How much Discworld lore is fair-use in-repo vs link-out only. |
| U3 | Multi-MUD packs beyond Discworld (Phase 2+). |
| U4 | Automation vs human-in-the-loop for combat. |

## Acceptance

| ID | Criterion |
|----|-----------|
| A1 | `mud-skill` SKILL.md exists with L2 triggers and L7 UAT rule. |
| A2 | Functional spec + FR + build plan present. |
| A3 | Validator BT0 exits 0; install copies at least `mud-skill`. |
| A4 | At least one Discworld companion skill stub (e.g. `discworld-mud` or class pack) with clear triggers. |
| A5 | Harvest log section lists what was promoted and from where (or "seed only"). |
| A6 | No secrets; no invented host/login. |

## Phase order

| Phase | Deliverable |
|-------|-------------|
| P0 | Repo, docs, `mud-skill` + Discworld stub, BT0 validate/install, CI optional |
| P1 | Expand class/guild playbooks; connect/nav rituals |
| P2 | Additional MUDs / deeper automation (U3/U4) |
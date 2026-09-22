# FR: Mud playbooks MUCH deeper (issue #23)

**Issue:** https://github.com/SimonBarnett/mud-skill/issues/23  
**Ask (Simon):** No. MUCH deeper. Location guides, shop guides, lore,
fighting guides, weapon guides, more details on the guilds, the
different cities. Really put **50+ skills** in here.

## Summary

#20 (PASS-nits #22 / PR #21) added depth on a few playbooks. That is
not enough. This FR requires a **skill pack**: at least **50** agent
skills (each a `.grok/skills/<name>/SKILL.md`) covering Discworld
locations, shops, lore, fighting, weapons, guilds, and cities.

Harvest public Discworld MUD help / wiki facts only. Mark LOCKED vs
UNKNOWN. Do not invent host, port, credentials, or procedure ENAMEs.

## Gap vs main (`d95f6b4`)

Four skills only: `mud-skill`, `discworld-mud`, `discworld-ankh-survival`,
`harvest-mud-skill`. Guild tables and Ankh survival exist. No 50-skill
pack. No dedicated location / shop / lore / weapon / city skill files
at that count.

## LOCKED

1. At least **50** `SKILL.md` files under `.grok/skills/` after the
   implement PR (count = directories with `SKILL.md`).
2. Cover all named surfaces: locations, shops, lore, fighting, weapons,
   guilds, cities. One skill may own one surface slice; do not dump
   everything into `discworld-mud`.
3. No invented credentials, instance URLs, or ENAMEs.
4. `tools/Validate-MudSkill.ps1` (BT0) stays green.
5. Workers do not stamp ready for human UAT. Bob chairs.

## UNKNOWN

- Exact skill names and split (one city vs one street) — implementer
  locks in the plan and the tree.
- Whether a skill is Discworld-only or generic MUD — prefer Discworld
  companions unless the fact is game-agnostic.

## Acceptance

- A1: `Get-ChildItem .grok/skills/*/SKILL.md` count >= 50 on the PR
  head.
- A2: Named surfaces from the issue appear as skill `name` or
  description (location, shop, lore, fight/combat, weapon, guild, city).
- A3: No invented host/login/secrets.
- A4: Validate-MudSkill / BT0 green.
- A5: harvest-mud-skill note if new harvest patterns.

Workers do not stamp UAT.

# FR: MORE — fill stubs from search (issue #26)

**Issue:** https://github.com/SimonBarnett/mud-skill/issues/26  
**Ask (Simon):** Pages are mostly stubs. For each page use an internet
search for that topic and fill these in. Also need sections for
character creation of the main MUDs, death, money, actual shop details
(which shops where), travel, skills, experience. Each needs a serious
search and completion.

## Summary

#23 landed 50 skill files (PASS-nits #25 / PR #24). Simon UAT: they
are still stubs. This FR requires **filled** playbooks, not more empty
leaflets.

Use a web search for each topic. Prefer public Discworld MUD help /
wiki / well-known MUD docs. Mark LOCKED vs UNKNOWN. Do not invent
host, port, credentials, or procedure ENAMEs.

## Gap vs main (`f3b8724`)

50 `SKILL.md` files exist. Many are short stubs. Missing dedicated
filled sections (or skills) for: character creation (main MUDs),
death, money, shop locations/details, travel, skills, experience.

## LOCKED

1. Existing stub skills that are still "TODO / stub / TBD" must be
   filled from search, or explicitly UNKNOWN with a cited gap.
2. New or expanded skills/sections cover: character creation (at least
   Discworld + one other named main MUD if public docs exist), death,
   money, shops (which shops where), travel, skills, experience.
3. Each filled skill cites a public source (help page / wiki URL) or
   marks UNKNOWN.
4. No invented credentials, instance URLs, or ENAMEs.
5. `tools/Validate-MudSkill.ps1` stays green.
6. Workers do not stamp UAT. Bob chairs.

## UNKNOWN

- Exact shop names / city streets — search then lock; do not invent.
- Non-Discworld "main MUDs" list — lock only names the human or
  public docs already use.

## Acceptance

- A1: Named surfaces exist as skills or clearly headed sections:
  character-creation, death, money, shops, travel, skills, experience.
- A2: Those pages are not stub-only (numbered steps or tables from
  search; UNKNOWN allowed if search found nothing).
- A3: No invented host/login/secrets.
- A4: Validate-MudSkill / BT0 green.

Workers do not stamp UAT.

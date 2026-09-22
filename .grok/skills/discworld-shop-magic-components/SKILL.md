---
name: discworld-shop-magic-components
description: >
  Discworld MUD magic component and herb shops for wizards and witches.
  Use when the user says DW components, herb shop, witch supplies, or
  /discworld-shop-magic-components.
  Does not stamp ready for human UAT.
---

# Magic and component shops

Companion to `discworld-guild-wizard`, `discworld-guild-witch`, and `discworld-mud`.
Surfaces: **shop, guild, lore** (#23, #26).

**Sources (link-out):**

- Guild newbie docs on [witches](http://discworld.atuin.net/lpc/playing/documentation.c?path=%2Fnewbie%2Fwitches_guild) and wizard library material (wiki)
- [Discworld MUD wiki](https://discworld.starturtle.net/) — component/herb pages
- [Kefka item DB](https://dw.daftjunk.com/items/index.php) — search herbs/components

## LOCKED — Wizards

- Spells and rituals consume **components** listed in spell help — buy from
  appropriate **magic shops** and UU-adjacent vendors when game text directs
  (`discworld-location-am-unseen-university`).
- Human OK before bulk purchases or stealing components.

## LOCKED — Witches

- Herbs support **brew**, **imbue**, and healing commands (witch playbook in
  `discworld-mud`).
- **`gather`** may supplement shops (in-game help) — human approves wilderness
  gathering in dangerous zones.

## LOCKED — Workflow

1. Read spell/recipe help for required component names **from game**.
2. Buy only what the room lists; check regional currency.
3. Store components in secure containers — do not sell via pawn by mistake
   (`discworld-shop-pawn-trade`).

## UNKNOWN

- Complete per-city herb shop map — harvest per trip; wiki partial.
- Rare quest components — spoiler-sensitive.

## Do not

- Invent component ENAMEs for casting.
- Stamp ready for human UAT.

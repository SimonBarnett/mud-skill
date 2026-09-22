# Build/test plan: Discworld front door (#34, harvest #35)

1. Read issues #33 #34 #35 + this FR on pulled main.
2. Paste the LOCKED sections from #35 into the five owner skills and
   `docs/skill-harvest-log.md`. Do not invent rooms, accept-prompt syntax,
   or a client. Leave UNKNOWN as UNKNOWN.
3. Run `tools/Validate-MudSkill.ps1` (BT0). Must exit 0.
4. Open PR linking #34 (also #33 #35). Do not stamp UAT.

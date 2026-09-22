# Build/test plan: mud playbooks MUCH deeper (#23)

1. Read issue #23 + this FR + current `.grok/skills/**` on pulled main.
2. Add skills until A1 (>=50 SKILL.md). Cover A2 surfaces. Public facts
   only. LOCKED vs UNKNOWN in each leaflet.
3. Update `tools/Validate-MudSkill.ps1` / Test-Pack if the pack lists
   skill names.
4. Run `tools/Validate-MudSkill.ps1` (BT0).
5. Open PR linking #23. Do not stamp UAT.

# TODO — ellmos-ai `.github`

Diese Datei ist die TASKWRITER-Erfassung zum Bundle vom 2026-09-05. Die
kanonischen Aufgaben stehen im TASKPLAN-Register; hier bleiben IDs, Quellen und
der Review-Nachweis.

## Offene TASKPLAN-Aufgaben

- [ ] #375 Live-Repository-Index auf 66 aktive und 1 archiviertes Repo
  aktualisieren.
- [ ] #376 Reproduzierbaren Freshness- und Paritätscheck für den
  Organisationsindex ergänzen.
- [x] #377 Community-Action-Referenzen auf verifizierte SHAs pinnen.

## TASKWRITER-Review — 2026-09-05

- Bundle: `fb19ee0e-419b-4ddc-82d1-a5c7caf92387` · selector review
  `sha256-v1:af60b3a78313a3222612cc1d07e0d074b2da495b84eae03b00b32503934f731c`
- Projekt/Stand: `C:\_Local_DEV\repos\dotgithub`, Branch `master`,
  `e1db881`, `master...origin/master`, Arbeitsbaum vor dem TASKWRITER-
  Schreiben sauber; Remote `ellmos-ai/.github`.
- Gelesene Kontrollen: Root-README, englische und deutsche Profilseite,
  `llms.txt`, `CHANGELOG.md`, `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, Issue-/PR-Templates, `FUNDING.yml`, beide Workflows,
  alle Profil-Assets und die Render-/MCP-Hilfsskripte.
- Live-Befund: GitHub API am 2026-09-05 liefert public=67, active=66,
  archived=1 (`recludos-legacy`). Die Dokumentation behauptet public=57,
  active=56, archived=1 und last checked 2026-08-16. Vollständig fehlende
  aktive Namen: `cowork-protocol`, `ellmos-voice-io`, `FolderHome`,
  `grounding-seed`, `NemoFold`, `rechtsabteilung`, `sentinel-fleet`,
  `source-resolver`, `swarm_ai`.
- Workflow-Befund: `stale.yml` nutzt `actions/stale@v10`, `welcome.yml`
  `actions/first-interaction@v3`; beide Workflows haben Issue-/PR-
  Schreibrechte.
- Konsistenz: `pasta-press` ist bereits in den vier Indexen vorhanden;
  die neue Drift betrifft die neun genannten Repositories und die Zähler.
- Keine Aufgaben ausgeführt und keine öffentliche Profiländerung, kein Push,
  kein Release. Der eigene Lock wird vor dem Review entfernt.

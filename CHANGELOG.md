# Changelog

All notable changes to the `ellmos-ai/.github` organization profile repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.7] - 2026-09-23

### Added & Reconciled
- Turnusgemäßer Health- und Paritäts-Audit für die `ellmos-ai`-Startseite (`.github`) durchgeführt.
- `hook-master` (lokales Zeiger-Register und Materialisierung für Agent-Hooks, Geschwistermodul zu `policy-registry`) in allen Kerndokumenten (`profile/README.md`, `profile/README_de.md`, `README.md`, `llms.txt`) indiziert.
- Vollständige Parität mit 73 aktiven öffentlichen Repositories und 1 archivierten Legacy-Repo (`recludos-legacy`), 74 Repositories gesamt.
- `profile/README.md` und `profile/README_de.md`: Banner-Galerie in der "Memory and Control"-Sektion um `hook-master` (pinker Rahmen `#ec4899`, Standardbreite 560px) sowie die Rollenbeschreibung in der Tabelle ergänzt.
- Vertragstest-Suite in `tests/test_profile_parity.py` erweitert:
  - `hook-master` in `PUBLIC_REPOS` überführt und aus `PRIVATE_REPOS` entfernt.
  - Leak-Schutz in der Test-Suite gegen alle 33 privaten Repositories aktualisiert.
  - Neuen Test `test_hook_master_indexing` zur Verifikation der lückenlosen Indizierung über alle 4 Kerndateien implementiert.
  - Timestamp-Parität auf `2026-09-23` und Repo-Zählung auf 73/74 synchronisiert.
- `TODO.md` bereinigt und anstehende Aufgaben aktualisiert.

## [1.0.6] - 2026-09-14

### Added & Reconciled
- Turnusgemäßer Health- und Discoverability-Audit für `ellmos-ai` (.github) durchgeführt.
- `clip-storyboard-director` (lokaler KI-Storyboard-Director und Szenen-Kontinuitäts-Orchestrator) in den öffentlichen Index über alle Kerndokumente (`README.md`, `profile/README.md`, `profile/README_de.md`, `llms.txt`) aufgenommen.
- Vollständige Parität mit 68 aktiven öffentlichen Repositories und 1 archivierten Legacy-Repo (`recludos-legacy`), 69 Repositories gesamt.
- Deutsche Profilseite `profile/README_de.md` harmonisiert und um 4 zuvor fehlende Hackathon-Beiträge (`cowork-protocol`, `FolderHome`, `NemoFold`, `sentinel-fleet`) sowie `clip-storyboard-director` ergänzt.
- Vollständige 11-Organisationen-Ökosystem-Tabelle in `profile/README.md` und `profile/README_de.md` integriert (inklusive `um-bruch` und `lukisch`).
- `SECURITY.md` zweisprachig modernisiert mit verbindlicher 48h Response SLA, 7-14 Tage Triage, Sicherheitsinvarianten (Zero-Egress, Non-Elevation, Integrity) und offiziellen Kontaktstellen.
- Automatisierte Vertragstest-Suite in `tests/test_profile_parity.py` mit 9 Pruefungen und striktem Privacy-Leak-Schutz gegen alle 37 privaten Repositories implementiert.
- `.gitignore` gegen Caches, Locks und Multi-Host-Konfliktkopien gehärtet.

## [1.0.5] - 2026-08-16

### Added & Reconciled
- `system-auditor` indexed across all 4 files (`README.md`, `profile/README.md`,
  `profile/README_de.md`, `llms.txt`) under "Agent operations tooling" —
  evidence-based system audits across machines, extracted from
  `ticket-master`'s TICKET-WRITER role (commit `50451fd`).
- Repository count corrected: 55/56 -> 56/57 (56 active public repositories,
  1 archived, 57 total) — verified live against `gh api orgs/ellmos-ai/repos`.
  `50451fd` added the `system-auditor` entry but left the summary line at the
  pre-addition count.

## [1.0.4] - 2026-08-14

### Added & Reconciled
- 100% full repository parity verified against live GitHub API (55 active public repositories including `.github`, 1 archived legacy repository `recludos-legacy`, 56 repositories total).
- Indexed newly public core infrastructure and governance modules across `profile/README.md`, `profile/README_de.md`, `README.md` and `llms.txt`:
  - `ellmos-scheduler`: Standalone local-first task scheduler and run recorder for modular ellmos stacks.
  - `policy-registry`: Local-first registry for policies, rules and governance decisions with metadata pointers to canonical sources.
  - `system-explorer`: Evidence-based topology mapping, capability bounds and communication edge discovery.
  - `bundles`: Recipe layer of the ellmos ecosystem (bundle manifests, catalogs and composition knowledge).
- Updated `Last-checked` timestamps and repository counts across all profile documents (`profile/README.md`, `profile/README_de.md`, `README.md`, `llms.txt`) to `2026-08-14`.
- Enhanced search phrases and LLM discoverability index in `llms.txt`.

### Added — 2026-08-05

- New **Competition Entries** section (German: *Wettbewerbsbeiträge*) in `profile/README.md`, `profile/README_de.md`, `README.md` and `llms.txt`: the three CALL-E entries, roshambo and roshambo-starmap (CockroachDB x AWS Hackathon 2026-07), build-your-users-mind and bach. Listed as entries only; no placements claimed.
- New **Agents** section describing the three CALL-E telephone agents transferred into the organization: `hungrycall` (sequential calling cascade for delivery, reservation and pickup), `ringedingeding` (multi-recipient response aggregator) and `researchcall` (standardized telephone survey runner).

### Fixed — 2026-08-05

- Live index reconciliation against the GitHub API: removed seven non-public repository entries to uphold strict public-only catalog boundaries.
- Corrected stale cross-org links: `ticket-master`, `lock-master` and `companion-for-agy` now resolve inside `ellmos-ai`, and `dev-bricks/sync-master` is `ellmos-ai/system-gap-master`. Removed them from "Related Projects in Other Orgs" and added an "Agent operations tooling" row.
- Synchronized repository counts and `Last-checked` timestamps to 50 active public repositories plus one archived (51 total), verified 2026-08-05.

### Added
- Created colorful Stacks Umbrella Banner (`stacks-umbrella-banner.png` / `.svg`) with true 32-bit alpha transparency, featuring a vibrant canopy (green → blue → purple) with white typography, rain details, and a translucent rainbow protection shelter. (Ref: T-20260801-13)
- Restructured Stacks section in `profile/README.md` and `profile/README_de.md` paritatively, placing the Umbrella Banner at the top and sheltering `ellmos-stack` and `agent-ops-stack` tiles below with neon glow frames. (Ref: T-20260801-13)

## [1.0.3] - 2026-08-01

### Fixed
- Corrected creation date labels on MCP tree diagram (`mcp-tree.png`) and HTML image map tooltips in `profile/README.md` & `profile/README_de.md` to verified repository creation dates (2026-02 to 2026-07). (Ref: T-20260801-13)

## [1.0.2] - 2026-07-30

### Maintenance & Hygiene
- Synchronized repository index: updated `taskplan` links to renamed `task-master` repository across `profile/README.md`, `profile/README_de.md`, `README.md`, `llms.txt`, and diagrams.
- Verified 38 active public repositories in the `ellmos-ai` organization profile.

## [1.0.1] - 2026-07-26

### Maintenance & Hygiene
- Synchronized organization repository index timestamps to `2026-07-26` across `README.md`, `profile/README.md`, `profile/README_de.md` and `llms.txt`.
- Added standard `CHANGELOG.md` for tracking profile maintenance and ecosystem updates.

## [1.0.0] - 2026-07-25

### Initial Profile Release
- Established canonical organization profile repository for `ellmos-ai`.
- Published `profile/README.md` and German translation `profile/README_de.md`.
- Added machine-readable ecosystem discovery index `llms.txt`.

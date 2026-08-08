# Changelog

All notable changes to the `ellmos-ai/.github` organization profile repository will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed — 2026-08-08

- Re-read the public `ellmos-ai` organization through the GitHub API: 54 active and one archived repository were visible. Added the now-public, documented modules `ellmos-scheduler`, `policy-registry` and `system-explorer` to every index surface, bringing the released index to 53 active plus one archived entry. The public `bundles` repository remains excluded because its upstream README explicitly describes a private, wave-by-wave build rather than a released project.
- Recorded the live verification date and preserved `recludos-legacy` as the sole explicitly archived reference; no push or other public write was performed.

### Added — 2026-08-05

- New **Competition Entries** section (German: *Wettbewerbsbeiträge*) in `profile/README.md`, `profile/README_de.md`, `README.md` and `llms.txt`: the three CALL-E entries, roshambo and roshambo-starmap (CockroachDB x AWS Hackathon 2026-07), build-your-users-mind and bach. Listed as entries only; no placements claimed.
- New **Agents** section describing the three CALL-E telephone agents transferred into the organization: `hungrycall` (sequential calling cascade for delivery, reservation and pickup), `ringedingeding` (multi-recipient response aggregator) and `researchcall` (standardized telephone survey runner).

### Fixed — 2026-08-05

- Live index reconciliation against the GitHub API at that snapshot: removed seven entries that were not public repositories (`memoryhooker-provenance`, `workflowhooker-provenance`, `prompt-evidence-collector`, `ellmos-core`, `ellmos-development-system`, `policy-registry`, `system-explorer`). The current 2026-08-08 readback re-adds the latter two after they became public.
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

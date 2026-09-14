# Security Policy / Sicherheitsrichtlinie

## Reporting a Vulnerability / Sicherheitslücke melden

If you discover a security vulnerability or security concern within any repository in the `ellmos-ai` organization, please report it responsibly:

1. **Do NOT open a public issue** or disclose vulnerability details publicly before a fix is available.
2. Use [GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories) on the affected repository to create a private draft advisory.
3. Or contact the maintainers directly via email:
   - `security@ellmos.ai`
   - `security@open-bricks.org`
   - `lukas@open-bricks.org`
   - `support@lukasgeiger.com`

---

## Response Timeline / Reaktionszeit

- **Acknowledgment:** Within 48 hours (best effort, guaranteed within 7 days)
- **Initial Assessment & Triage:** Within 7 to 14 days
- **Fix & Disclosure Coordination:** Best effort, typically within 30 days depending on severity

---

## Supported Versions / Unterstützte Versionen

| Repository / Tool | Supported Release | Security Updates |
|---|---|---|
| Organization profile (`ellmos-ai/.github`) | Latest commit on `master` | :white_check_mark: Supported |
| Active public repositories (`bach`, `rinnsal`, `open-ocean`, `usmc`, `gardener`, `skills`, MCP servers, agent operations tooling, domain tools, media workflows) | Latest commit or latest stable tag on default branch (`master`/`main`) | :white_check_mark: Supported |
| Archived legacy repositories (`recludos-legacy`) | Archived read-only | :x: No active updates |

---

## Security Invariants / Sicherheitsinvarianten

- **Zero-Egress & Local-First:** All LLM operating system components, memory stores, MCP servers, and agent coordination tools are engineered to operate 100% locally with zero unconsented telemetry, analytics, or cloud data egress.
- **Unprivileged User Mode (Non-Elevation):** Tools operate within standard user privileges and never require administrative elevation for normal agent, CLI, or GUI operation.
- **Integrity & Sandboxing:** File operations, database transactions, process lifecycle calls, and hook integrations fail closed and adhere to strict local authorization and boundary checks.

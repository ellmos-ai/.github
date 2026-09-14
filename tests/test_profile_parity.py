# -*- coding: utf-8 -*-
"""Contract tests for ellmos-ai organization profile parity, privacy, and integrity."""

import os
import re
import pytest

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PUBLIC_REPOS = [
    ".github",
    "FolderHome",
    "GARDENER",
    "NemoFold",
    "WORKFLOWHOOKER",
    "agent-ops-stack",
    "ai-media-editor",
    "anonymizer",
    "bach",
    "build-your-users-mind",
    "bundles",
    "clip-storyboard-director",
    "clirec",
    "clutch",
    "coma",
    "companion-for-agy",
    "compare-race",
    "connectors",
    "cowork-protocol",
    "ellmos",
    "ellmos-ai.github.io",
    "ellmos-blender-use-mcp",
    "ellmos-clatcher-mcp",
    "ellmos-codecommander-mcp",
    "ellmos-controlcenter-mcp",
    "ellmos-filecommander-mcp",
    "ellmos-homebase-mcp",
    "ellmos-scheduler",
    "ellmos-servercommander-mcp",
    "ellmos-stack",
    "ellmos-tests",
    "ellmos-voice-io",
    "grounding-seed",
    "hungrycall",
    "lock-master",
    "marblerun",
    "memoryhooker",
    "n8n-manager-mcp",
    "n8n-workflow-manager",
    "open-compute",
    "open-compute-mcp",
    "open-ocean",
    "pasta-press",
    "policy-registry",
    "project-docs-template",
    "prompt-listener",
    "rechtsabteilung",
    "recludos-legacy",
    "report-forge",
    "researchcall",
    "ringedingeding",
    "rinnsal",
    "roshambo",
    "roshambo-starmap",
    "sentinel-fleet",
    "skills",
    "source-resolver",
    "sqlite-transit-sync",
    "stacks",
    "steuer-assistent",
    "swarm_ai",
    "system-auditor",
    "system-explorer",
    "system-gap-master",
    "task-master",
    "ticket-master",
    "usmc",
    "web-scraper",
    "worksheet-generator",
]

PRIVATE_REPOS = [
    "AnliegenPilot",
    "accounts-core",
    "agent-launcher",
    "assistant-core",
    "claude-bridge",
    "condition-gates",
    "convergence-reconciler",
    "decimalai-skill-eval-monitor",
    "decision-clicker",
    "doc-services",
    "ellmos-agent-bridge",
    "ellmos-chat",
    "ellmos-code-tools",
    "ellmos-core",
    "ellmos-delegation-authority",
    "ellmos-development-system",
    "ellmos-installer",
    "ellmos-market-data",
    "ellmos-unified-gui",
    "file-collect-sort-action",
    "foerderplaner",
    "githubbot",
    "hook-master",
    "mac-backup",
    "mail-connector",
    "mediplaner",
    "memoryhooker-provenance",
    "paveman",
    "prompt-evidence-collector",
    "roblox-studio-core",
    "routinika",
    "session-checkpoint",
    "steuer-suite",
    "store-packager",
    "umbruch-social-media-runner",
    "versicherungsmanager",
    "workflowhooker-provenance",
]

SISTER_ORGS = [
    "open-bricks",
    "ellmos-ai",
    "file-bricks",
    "doc-bricks",
    "dev-bricks",
    "research-line",
    "biotec-line",
    "entertain-and-more",
    "assistassets-ai",
    "um-bruch",
    "lukisch",
]


def get_file_content(relative_path: str) -> str:
    path = os.path.join(REPO_ROOT, relative_path)
    assert os.path.exists(path), f"File not found: {path}"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def test_markdown_fence_balance():
    """Verify all markdown files have balanced code fences."""
    md_files = [
        "README.md",
        "profile/README.md",
        "profile/README_de.md",
        "CHANGELOG.md",
        "SECURITY.md",
    ]
    for rel_path in md_files:
        content = get_file_content(rel_path)
        fence_count = len(re.findall(r"^```", content, flags=re.MULTILINE))
        assert fence_count % 2 == 0, f"Unbalanced code fences in {rel_path} (found {fence_count})"


def test_public_repo_inventory():
    """Verify all 69 public repos are cataloged in core profile documents."""
    target_files = [
        "profile/README.md",
        "profile/README_de.md",
        "llms.txt",
    ]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for repo in PUBLIC_REPOS:
            # Check case-insensitively or with canonical name
            assert repo.lower() in content.lower(), f'Public repo "{repo}" missing from {rel_path}'


def test_private_repo_leak_guard():
    """Verify 0 private/internal repos are leaked into public profile documents."""
    target_files = [
        "profile/README.md",
        "profile/README_de.md",
        "README.md",
        "llms.txt",
        "SECURITY.md",
        "CHANGELOG.md",
    ]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for priv in PRIVATE_REPOS:
            assert priv.lower() not in content.lower(), f'Privacy leak violation: private repo "{priv}" found in {rel_path}'


def test_check_timestamp_parity():
    """Verify verification date 2026-09-14 across profile files."""
    expected_iso = "2026-09-14"

    en_content = get_file_content("profile/README.md")
    assert expected_iso in en_content, f"Date {expected_iso} missing from profile/README.md"

    de_content = get_file_content("profile/README_de.md")
    assert expected_iso in de_content, f"Date {expected_iso} missing from profile/README_de.md"

    root_content = get_file_content("README.md")
    assert expected_iso in root_content, f"Date {expected_iso} missing from README.md"

    llms_content = get_file_content("llms.txt")
    assert expected_iso in llms_content, f"Date {expected_iso} missing from llms.txt"


def test_repo_counts_parity():
    """Verify repository count assertions (68 active, 69 total) across documents."""
    en_content = get_file_content("profile/README.md")
    assert "68 active" in en_content
    assert "69 total" in en_content

    de_content = get_file_content("profile/README_de.md")
    assert "68 aktive" in de_content
    assert "69 gesamt" in de_content

    root_content = get_file_content("README.md")
    assert "68 active" in root_content
    assert "69 repos total" in root_content

    llms_content = get_file_content("llms.txt")
    assert "68 active" in llms_content
    assert "69 total" in llms_content


def test_clip_storyboard_director_indexing():
    """Verify clip-storyboard-director is indexed in all primary files."""
    target_files = [
        "README.md",
        "profile/README.md",
        "profile/README_de.md",
        "llms.txt",
    ]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        assert "clip-storyboard-director" in content, f"clip-storyboard-director missing from {rel_path}"


def test_ecosystem_cross_linking():
    """Verify sister organization references are complete across profile READMEs."""
    target_files = ["profile/README.md", "profile/README_de.md"]
    for rel_path in target_files:
        content = get_file_content(rel_path)
        for org in SISTER_ORGS:
            assert org in content, f'Sister org "{org}" missing from {rel_path}'


def test_utf8_encoding_and_umlauts():
    """Verify clean UTF-8 encoding and genuine German umlauts."""
    de_content = get_file_content("profile/README_de.md")
    assert "\ufffd" not in de_content, "Unicode replacement character (mojibake) in profile/README_de.md"
    assert "Öffentliches" in de_content
    assert "Dachorganisation" in de_content
    assert "Gedächtnis" in de_content


def test_security_policy_parity():
    """Verify 48h Response SLA and official contacts in SECURITY.md."""
    security_content = get_file_content("SECURITY.md")
    assert "48 hours" in security_content
    assert "security@open-bricks.org" in security_content
    assert "security@ellmos.ai" in security_content
    assert "Zero-Egress" in security_content

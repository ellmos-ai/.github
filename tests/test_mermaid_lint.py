"""Unit tests for mermaid syntax linter."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))

from lint_mermaid import (
    check_mermaid_block,
    fix_mermaid_block,
    lint_markdown_file,
)


def test_clean_flowchart():
    clean = """flowchart TD
    A["Node A (Info)"] -->|"label (ok)"| B
    B --> C
"""
    issues = check_mermaid_block(clean)
    assert len(issues) == 0


def test_unquoted_parens_in_node():
    unquoted = """flowchart TD
    A[Node A (Info)] --> B
"""
    issues = check_mermaid_block(unquoted)
    assert len(issues) == 1
    assert issues[0]["type"] == "unquoted_node_parens"

    fixed = fix_mermaid_block(unquoted)
    assert 'A["Node A (Info)"]' in fixed
    assert len(check_mermaid_block(fixed)) == 0


def test_unquoted_parens_in_edge():
    unquoted = """flowchart TD
    A -->|dry_run: true (default)| B
"""
    issues = check_mermaid_block(unquoted)
    assert len(issues) == 1
    assert issues[0]["type"] == "unquoted_edge_special_chars"

    fixed = fix_mermaid_block(unquoted)
    assert '-->|"dry_run: true (default)"|' in fixed
    assert len(check_mermaid_block(fixed)) == 0


def test_sequence_diagram_semicolon():
    seq = """sequenceDiagram
    Alice->>Bob: Hello; world
"""
    issues = check_mermaid_block(seq)
    assert len(issues) == 1
    assert issues[0]["type"] == "sequence_message_semicolon"

    fixed = fix_mermaid_block(seq)
    assert "Hello - world" in fixed
    assert len(check_mermaid_block(fixed)) == 0


def test_repo_markdown_files_clean():
    """Prueft alle Markdown-Dateien im ellmos-ai/.github Repository."""
    for md_file in REPO_ROOT.glob("*.md"):
        issues, _ = lint_markdown_file(md_file)
        assert len(issues) == 0, f"Fehler in {md_file.name}: {issues}"

    profile_dir = REPO_ROOT / "profile"
    if profile_dir.exists():
        for md_file in profile_dir.glob("*.md"):
            issues, _ = lint_markdown_file(md_file)
            assert len(issues) == 0, f"Fehler in profile/{md_file.name}: {issues}"

#!/usr/bin/env python3
"""lint_mermaid.py — Mermaid Diagramm-Linter und Syntax-Wächter.

Prüft und repariert typische Mermaid-Syntaxfehler in Markdown-Dateien:
1. Unquotierte Sonderzeichen in Kantenbeschriftungen:
   -->|dry_run: true (default)|  =>  -->|"dry_run: true (default)"|
   (Runde Klammern werden vom Mermaid-Lexer als 'PS' / Parenthesis Start interpretiert)
2. Unquotierte Klammern in Rechteck-Knoten:
   Node[Label (Zusatz)]  =>  Node["Label (Zusatz)"]
3. Unquotierte Vergleichsoperatoren & Entities in Kanten:
   -->|p_C > p_C*|  =>  -->|"p_C > p_C*"|

Verwendung:
    python _tools/lint_mermaid.py <pfad-zu-datei-oder-repo>
    python _tools/lint_mermaid.py C:\\_Local_DEV\\repos\\ellmos-clatcher-mcp
    python _tools/lint_mermaid.py --all-repos
    python _tools/lint_mermaid.py <pfad> --fix
"""

import argparse
import re
import sys
from pathlib import Path
from typing import Any

# Regex für Mermaid Code-Blöcke
MERMAID_BLOCK_RE = re.compile(r"(```mermaid\s*\n)(.*?)(\n```)", re.DOTALL)

# Regex für Kantenbeschriftungen: -->|...| oder <--+>|...| oder -.->|...| oder ==+>|...|
EDGE_LABEL_RE = re.compile(r"((?:--+>|<-+>|-\.-+>|==+>)\|)([^|\r\n]+)(\|)")

# Regex für Knoten mit eckigen Klammern: NodeID[Inhalt]
# Verhindert Fehlalarm bei Stadium ([ ... ]) oder bereits quotierten [" ... "]
NODE_SQUARE_RE = re.compile(r'(\b\w+\s*\[)([^"\[\]\r\n]+)(\])')

# Regex für Sequence Diagram Nachrichten: A->>B: message
SEQ_MSG_RE = re.compile(r'^(\s*(?:actor|participant)?[^:\r\n]*(?:->>|-->>|->|-->)\s*(?:[^:\r\n]+:\s*))(.*)$')

# Regex für HTML-Entities (z.B. &amp;, &lt;, &#39;)
ENTITY_RE = re.compile(r'&[a-zA-Z0-9#]+;')

# Sonderzeichen, die in unquotierten Kantenbeschriftungen Syntaxfehler erzeugen
ILLEGAL_EDGE_CHARS = set("()[]{}<>;")


def fix_seq_message(msg: str) -> str:
    """Ersetzt Semikolons außerhalb von HTML-Entities durch ' - '."""
    parts = []
    last_idx = 0
    for entity_m in ENTITY_RE.finditer(msg):
        pre_text = msg[last_idx:entity_m.start()]
        parts.append(re.sub(r';\s*', ' - ', pre_text))
        parts.append(entity_m.group(0))
        last_idx = entity_m.end()
    tail = msg[last_idx:]
    parts.append(re.sub(r';\s*', ' - ', tail))
    return ''.join(parts)


def check_mermaid_block(block_text: str) -> list[dict[str, Any]]:
    """Analysiert einen einzelnen Mermaid-Block auf Syntaxprobleme."""
    issues = []
    lines = block_text.splitlines()
    is_sequence = any("sequenceDiagram" in l for l in lines)
    block_depth = 0

    for idx, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped or stripped.startswith("%%"):
            continue

        if is_sequence:
            # 1. Sequence Diagram: Block-Verschachtelung tracken
            if re.match(r'^(?:alt|opt|loop|par|critical|rect)\b', stripped):
                block_depth += 1
            elif re.match(r'^end\b', stripped):
                block_depth -= 1

            # 2. Sequence Diagram: Semikolon in Nachrichten prüfen
            msg_match = SEQ_MSG_RE.match(line)
            if msg_match:
                prefix, msg = msg_match.groups()
                clean_msg = ENTITY_RE.sub('', msg)
                if ';' in clean_msg:
                    suggested_msg = fix_seq_message(msg)
                    issues.append({
                        "line": idx,
                        "type": "sequence_message_semicolon",
                        "raw": line,
                        "label": msg,
                        "suggested": f'{prefix}{suggested_msg}',
                        "detail": f"Semikolon im Sequenzdiagramm-Nachrichtentext bricht GitHub-Rendering (Statement-Terminator): |{msg.strip()}|"
                    })
        else:
            # Flowchart / Graph: Subgraph-Verschachtelung tracken
            if re.match(r'^subgraph\b', stripped):
                block_depth += 1
            elif re.match(r'^end\b', stripped):
                block_depth -= 1

            # 1. Kantenbeschriftungen prüfen
            for match in EDGE_LABEL_RE.finditer(line):
                prefix, label, suffix = match.groups()
                label_trimmed = label.strip()
                # Wenn nicht in doppelten Anführungszeichen eingeschlossen
                if not (label_trimmed.startswith('"') and label_trimmed.endswith('"')):
                    has_illegal = any(c in label_trimmed for c in ILLEGAL_EDGE_CHARS) or "&le;" in label_trimmed or "&tau;" in label_trimmed
                    if has_illegal:
                        issues.append({
                            "line": idx,
                            "type": "unquoted_edge_special_chars",
                            "raw": match.group(0),
                            "label": label,
                            "suggested": f'{prefix}"{label_trimmed}"{suffix}',
                            "detail": f"Unquotierte Sonderzeichen in Kante: |{label}|"
                        })

            # 2. Rechteckige Knotenbeschriftungen prüfen
            for match in NODE_SQUARE_RE.finditer(line):
                prefix, inner, suffix = match.groups()
                inner_trimmed = inner.strip()
                # Falls nicht Stadium-Syntax ([ ... ]) und nicht bereits quotiert
                if inner_trimmed.startswith("(") and inner_trimmed.endswith(")"):
                    continue  # Gültige Stadium-Syntax ([ ... ])
                if not (inner_trimmed.startswith('"') and inner_trimmed.endswith('"')) and (
                    "(" in inner_trimmed or ")" in inner_trimmed or ";" in inner_trimmed
                ):
                    issues.append({
                        "line": idx,
                        "type": "unquoted_node_parens",
                        "raw": match.group(0),
                        "label": inner,
                        "suggested": f'{prefix}"{inner_trimmed}"{suffix}',
                        "detail": f"Unquotierte Klammern oder Semikolons in Knoten: [{inner}]"
                    })

    if block_depth != 0:
        issues.append({
            "line": len(lines),
            "type": "unbalanced_block_statements",
            "raw": "",
            "label": "",
            "suggested": "",
            "detail": f"Unbalancierte Kontrollblöcke/Subgraphs im Diagramm (Verschachtelungstiefe: {block_depth})"
        })

    return issues


def fix_mermaid_block(block_text: str) -> str:
    """Repariert bekannte Mermaid-Syntaxfehler in einem Block."""
    lines = block_text.splitlines()
    fixed_lines = []
    is_sequence = any("sequenceDiagram" in l for l in lines)

    for line in lines:
        new_line = line

        if is_sequence:
            msg_match = SEQ_MSG_RE.match(new_line)
            if msg_match:
                prefix, msg = msg_match.groups()
                clean_msg = ENTITY_RE.sub('', msg)
                if ';' in clean_msg:
                    new_line = prefix + fix_seq_message(msg)
        else:
            # Kantenbeschriftungen reparieren
            def replace_edge(m):
                prefix, label, suffix = m.groups()
                label_trimmed = label.strip()
                if not (label_trimmed.startswith('"') and label_trimmed.endswith('"')) and (
                    any(c in label_trimmed for c in ILLEGAL_EDGE_CHARS) or "&le;" in label_trimmed or "&tau;" in label_trimmed
                ):
                    return f'{prefix}"{label_trimmed}"{suffix}'
                return m.group(0)

            new_line = EDGE_LABEL_RE.sub(replace_edge, new_line)

            # Knotenbeschriftungen reparieren
            def replace_node(m):
                prefix, inner, suffix = m.groups()
                inner_trimmed = inner.strip()
                if inner_trimmed.startswith("(") and inner_trimmed.endswith(")"):
                    return m.group(0)
                if not (inner_trimmed.startswith('"') and inner_trimmed.endswith('"')) and (
                    "(" in inner_trimmed or ")" in inner_trimmed or ";" in inner_trimmed
                ):
                    return f'{prefix}"{inner_trimmed}"{suffix}'
                return m.group(0)

            new_line = NODE_SQUARE_RE.sub(replace_node, new_line)

        fixed_lines.append(new_line)

    return "\n".join(fixed_lines)


def lint_markdown_file(file_path: Path, auto_fix: bool = False) -> tuple[list[dict[str, Any]], bool]:
    """Prüft eine Markdown-Datei und repariert sie bei Bedarf."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as e:
        return [{"line": 0, "type": "io_error", "detail": f"Fehler beim Lesen: {e}"}], False

    all_issues = []
    modified = False

    def replace_block(m):
        nonlocal modified
        start_tag, body, end_tag = m.groups()
        issues = check_mermaid_block(body)
        if issues:
            for iss in issues:
                all_issues.append({
                    "file": str(file_path),
                    "line": iss["line"],
                    "detail": iss["detail"],
                    "raw": iss.get("raw", ""),
                    "suggested": iss.get("suggested", "")
                })
            if auto_fix:
                fixed_body = fix_mermaid_block(body)
                if fixed_body != body:
                    modified = True
                    return f"{start_tag}{fixed_body}{end_tag}"
        return m.group(0)

    new_content = MERMAID_BLOCK_RE.sub(replace_block, content)

    if auto_fix and modified:
        file_path.write_text(new_content, encoding="utf-8")

    return all_issues, modified


def main():
    parser = argparse.ArgumentParser(description="Mermaid Diagramm-Linter & Syntax-Wächter")
    parser.add_argument("target", nargs="?", default="", help="Pfad zu Markdown-Datei oder Verzeichnis")
    parser.add_argument("--all-repos", action="store_true", help="Scannt alle Repositories unter C:\\_Local_DEV\\repos")
    parser.add_argument("--fix", action="store_true", help="Repariert erkannte Syntaxprobleme automatisch")
    args = parser.parse_args()

    files_to_check: list[Path] = []

    IGNORE_DIRS = {".git", "node_modules", "dist", "build", ".venv", "venv", "__pycache__"}

    if args.all_repos or (not args.target and not args.all_repos):
        repos_dir = Path(r"C:\_Local_DEV\repos")
        if repos_dir.exists():
            for p in repos_dir.glob("*/README*.md"):
                if not any(part in IGNORE_DIRS for part in p.parts):
                    files_to_check.append(p)
    elif args.target:
        target_path = Path(args.target)
        if target_path.is_file():
            files_to_check.append(target_path)
        elif target_path.is_dir():
            for p in target_path.rglob("README*.md"):
                if not any(part in IGNORE_DIRS for part in p.parts):
                    files_to_check.append(p)
            for p in target_path.glob("*.md"):
                if p not in files_to_check and not any(part in IGNORE_DIRS for part in p.parts):
                    files_to_check.append(p)

    if not files_to_check:
        print("Keine zu prüfenden Markdown-Dateien gefunden.")
        return 0

    total_issues = 0
    total_fixed = 0

    print(f"=== Mermaid Diagram Linter === (Prüfe {len(files_to_check)} Dateien)")

    for f in files_to_check:
        issues, fixed = lint_markdown_file(f, auto_fix=args.fix)
        if issues:
            total_issues += len(issues)
            print(f"\n[FAIL] {f}:")
            for iss in issues:
                print(f"  - Zeile {iss['line']}: {iss['detail']}")
                if iss.get("suggested"):
                    print(f"    Vorschlag: {iss['suggested']}")
            if fixed:
                total_fixed += 1
                print("  -> [AUTO-FIX] Datei erfolgreich repariert.")

    print("\n" + "=" * 40)
    print(f"Ergebnis: {total_issues} Syntax-Probleme in {len(files_to_check)} Dateien gefunden.")
    if args.fix:
        print(f"Repariert: {total_fixed} Dateien aktualisiert.")

    return 1 if (total_issues > 0 and not args.fix) else 0


if __name__ == "__main__":
    sys.exit(main())

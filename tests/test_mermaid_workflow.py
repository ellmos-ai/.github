"""Execute the Mermaid workflow's Bash step with inert adversarial path inputs."""

import os
from pathlib import Path
import shutil
import subprocess
import textwrap

import pytest


WORKFLOW = Path(__file__).resolve().parents[1] / ".github/workflows/mermaid-lint.yml"
INPUT_EXPRESSION = "${{ inputs.target_path || '.' }}"


def _bash():
    if os.name == "nt":
        # Avoid the Windows system32 WSL launcher: Git Bash is the native shell.
        candidate = Path(os.environ.get("ProgramFiles", "C:/Program Files")) / "Git/bin/bash.exe"
        if candidate.is_file():
            return str(candidate)
    executable = shutil.which("bash")
    assert executable, "Bash is required to verify the workflow's shell contract"
    return executable


def _run_lint_step(target_path):
    step = WORKFLOW.read_text(encoding="utf-8").split("      - name: Run Mermaid Linter\n", 1)[1]
    script = textwrap.dedent(step.split("        run: |\n", 1)[1])
    # Emulate Actions expression expansion, including the pre-fix vulnerable form.
    value = target_path or "."
    script = script.replace(INPUT_EXPRESSION, value)
    env = os.environ.copy()
    if f"          TARGET_PARAM: {INPUT_EXPRESSION}\n" in step:
        env["TARGET_PARAM"] = value
    else:
        env.pop("TARGET_PARAM", None)
    # Stub the linter command to capture its actual argument vector without I/O.
    capture = "python() { printf '%s\\0' \"$@\"; }\n"
    result = subprocess.run(
        [_bash(), "--noprofile", "--norc", "-e", "-c", capture + script],
        env=env,
        capture_output=True,
        timeout=10,
        check=True,
    )
    return result.stdout.decode("utf-8").split("\0")[:-1]


@pytest.mark.parametrize("target_path", [
    "",
    ".",
    "profile",
    "profile with spaces/README.md",
    "$(printf command-substitution)",
    "`printf backtick-substitution`",
    '\"; printf quote-breakout; #',
    "line one\nline two",
])
def test_target_path_is_one_literal_argument(target_path):
    expected = "target-repo" if target_path in ("", ".") else f"target-repo/{target_path}"
    assert _run_lint_step(target_path) == ["org-tools/tools/lint_mermaid.py", expected]

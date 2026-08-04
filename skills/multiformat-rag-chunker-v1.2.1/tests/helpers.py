from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
FIXTURES = Path(__file__).resolve().parent / "fixtures"


def run_cli(source: Path, output: Path, *extra: str) -> tuple[int, dict]:
    command = [
        sys.executable,
        str(SCRIPTS / "rag_chunker.py"),
        str(source),
        "-o",
        str(output),
        "--json",
        *extra,
    ]
    env = os.environ.copy()
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=False,
        timeout=180,
    )
    if not completed.stdout.strip():
        raise AssertionError(f"CLI produced no JSON. code={completed.returncode} stderr={completed.stderr}")
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise AssertionError(f"Invalid CLI JSON: {completed.stdout}\nstderr={completed.stderr}") from exc
    return completed.returncode, payload


def only_source_dir(output: Path) -> Path:
    directories = [path for path in output.iterdir() if path.is_dir()]
    if len(directories) != 1:
        raise AssertionError(f"Expected one source directory, found {directories}")
    return directories[0]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict]:
    records = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records

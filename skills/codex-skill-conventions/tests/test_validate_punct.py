#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regression tests for codex-skill-conventions.

These tests are pytest-compatible and directly executable with：

    python tests/test_validate_punct.py
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
VP = SCRIPTS / "validate_punct.py"
sys.path.insert(0, str(SCRIPTS))

_spec = importlib.util.spec_from_file_location("validate_punct", VP)
_validator = importlib.util.module_from_spec(_spec)
assert _spec is not None and _spec.loader is not None
_spec.loader.exec_module(_validator)


def run_vp(target: Path) -> tuple[int, str]:
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = _validator.check(str(target))
    return code, buf.getvalue()


def yaml_value(raw: str, key: str) -> str:
    m = re.search(rf"^\s*{re.escape(key)}:\s*(.*?)\s*$", raw, re.M)
    if not m:
        return ""
    value = m.group(1).strip()
    if (value.startswith('"') and value.endswith('"')) or (value.startswith("'") and value.endswith("'")):
        value = value[1:-1]
    return value


def scan_targets() -> list[Path]:
    targets = [
        VP,
        ROOT / "SKILL.md",
        ROOT / "FROZEN.md",
        ROOT / "LESSONS.md",
        ROOT / "agents" / "openai.yaml",
    ]
    for sub in ("references", "scripts"):
        folder = ROOT / sub
        if folder.is_dir():
            targets.extend(
                sorted(
                    p for p in folder.iterdir()
                    if p.is_file() and p.suffix in {".md", ".py", ".yaml", ".yml", ".txt"}
                )
            )
    return targets


def test_validator_scans_main_package_files_successfully():
    failures = []
    for target in scan_targets():
        code, out = run_vp(target)
        if code != 0:
            failures.append(f"{target.relative_to(ROOT)}\n{out}")
    assert not failures, "\n\n".join(failures)


def test_dirty_sample_is_rejected_and_reports_expected_tokens():
    with tempfile.TemporaryDirectory(prefix="codex-skill-test-") as td:
        bad = Path(td) / "bad.html"
        bad.write_text(
            "這句用半形句號.繼續\n"
            "連字號--當破折號\n"
            "他說\"引號\"包中文\n"
            "再用'單引號'包中文\n"
            "破折號—在此\n",
            encoding="utf-8",
        )
        code, out = run_vp(bad)
    assert code == 1, out
    assert "「.」" in out
    assert '「\"」' in out
    assert "「'」" in out
    assert "「--」" in out
    assert "「—」" in out


def test_clean_sample_allows_command_flags_decimals_and_urls():
    with tempfile.TemporaryDirectory(prefix="codex-skill-test-") as td:
        ok = Path(td) / "ok.html"
        ok.write_text(
            "全形標點，正常。安裝時請帶 --break-system-packages 參數，"
            "小數 3.14 與網址 example.com 不受影響。\n",
            encoding="utf-8",
        )
        code, out = run_vp(ok)
    assert code == 0, out


def test_sync_validator_auto_discovers_and_synchronizes_sibling_packages():
    with tempfile.TemporaryDirectory(prefix="codex-skill-test-") as td:
        base = Path(td)
        for name in ("pkg-a", "pkg-b"):
            scripts_dir = base / name / "scripts"
            scripts_dir.mkdir(parents=True)
            (scripts_dir / "validate_punct.py").write_text("OLD\n", encoding="utf-8")

        me = base / "codex-skill-conventions"
        ignore = shutil.ignore_patterns("__pycache__", ".pytest_cache", "pytest-cache-files-*")
        shutil.copytree(ROOT, me, ignore=ignore)
        sync = me / "scripts" / "sync_validator.py"

        first = subprocess.run([sys.executable, str(sync), "--check"], capture_output=True, text=True)
        assert first.returncode == 1, first.stdout + first.stderr
        assert "2 個包" in first.stdout

        subprocess.run([sys.executable, str(sync)], capture_output=True, text=True, check=False)
        second = subprocess.run([sys.executable, str(sync), "--check"], capture_output=True, text=True)
        assert second.returncode == 0, second.stdout + second.stderr


def test_bootstrap_flag_logic_without_real_installation():
    import bootstrap

    calls: list[list[str]] = []
    original_run = bootstrap.subprocess.run
    original_external = bootstrap._is_externally_managed
    original_venv = bootstrap._in_virtualenv

    def fake_run(cmd, *args, **kwargs):
        calls.append(list(cmd))

        class Result:
            returncode = 0

        return Result()

    bootstrap.subprocess.run = fake_run
    try:
        assert bootstrap.ensure("json") is True
        assert calls == []

        bootstrap._is_externally_managed = lambda: True
        bootstrap._in_virtualenv = lambda: False
        assert bootstrap.ensure("this_module_never_exists_xyz", log=lambda *a: None) is True
        assert "--break-system-packages" in calls[-1]

        calls.clear()
        bootstrap._is_externally_managed = lambda: False
        assert bootstrap.ensure("this_module_never_exists_xyz", log=lambda *a: None) is True
        assert "--break-system-packages" not in calls[-1]

        calls.clear()
        bootstrap._is_externally_managed = lambda: True
        bootstrap._in_virtualenv = lambda: True
        assert bootstrap.ensure("this_module_never_exists_xyz", log=lambda *a: None) is True
        assert "--break-system-packages" not in calls[-1]

        calls.clear()
        bootstrap._is_externally_managed = lambda: False
        bootstrap._in_virtualenv = lambda: False
        assert bootstrap.ensure(
            "this_module_never_exists_xyz",
            pip_names={"this_module_never_exists_xyz": "pillow"},
            log=lambda *a: None,
        ) is True
        assert "pillow" in calls[-1]
    finally:
        bootstrap.subprocess.run = original_run
        bootstrap._is_externally_managed = original_external
        bootstrap._in_virtualenv = original_venv


def test_converter_frontmatter_and_metadata_helpers():
    import convert_from_claude_skill as conv

    assert conv.validate_frontmatter({"name": "good-name", "description": "x" * 30}) == []
    assert any("不符合" in p for p in conv.validate_frontmatter({"name": "BadName", "description": "x"}))
    assert any("連續連字號" in p or "不可開頭結尾" in p for p in conv.validate_frontmatter({"name": "a--b", "description": "x"}))
    assert any("超過" in p for p in conv.validate_frontmatter({"name": "ok", "description": "x" * 1025}))
    assert any("不接受" in p for p in conv.validate_frontmatter({"name": "ok", "description": "x", "metadata": {}}))

    short = conv.guess_short_description("這是一段夠長的描述句，用來測試截取邏輯是否落在合理長度之內，並且不會超過上限。後面還有第二句。")
    assert 25 <= len(short) <= 64
    yaml = conv.build_openai_yaml("my-skill", "描述文字，測試用的一段夠長的描述文字，超過二十五個字以便通過檢查。")
    assert "$my-skill" in yaml


def test_skill_frontmatter_and_agents_metadata_contract():
    skill_text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    front = re.match(r"^---\n(.*?)\n---", skill_text, re.S).group(1)
    keys = [
        re.match(r"^([A-Za-z0-9_-]+):", line).group(1)
        for line in front.splitlines()
        if re.match(r"^([A-Za-z0-9_-]+):", line)
    ]
    assert set(keys) == {"name", "description"} and len(keys) == 2
    assert "gpt-to-codex" in front and "claude-to-codex" in front
    assert "gpt-skill-conventions v1.6.1" in front

    agents = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
    short = yaml_value(agents, "short_description")
    prompt = yaml_value(agents, "default_prompt")
    assert 10 <= len(short) <= 64
    assert "$codex-skill-conventions" in prompt
    assert re.search(r"allow_implicit_invocation:\s*true", agents)


def _run_direct() -> int:
    tests = [
        test_validator_scans_main_package_files_successfully,
        test_dirty_sample_is_rejected_and_reports_expected_tokens,
        test_clean_sample_allows_command_flags_decimals_and_urls,
        test_sync_validator_auto_discovers_and_synchronizes_sibling_packages,
        test_bootstrap_flag_logic_without_real_installation,
        test_converter_frontmatter_and_metadata_helpers,
        test_skill_frontmatter_and_agents_metadata_contract,
    ]
    failures = []
    for test in tests:
        try:
            test()
            print(f"[PASS] {test.__name__}")
        except Exception as exc:
            failures.append((test.__name__, exc))
            print(f"[FAIL] {test.__name__}: {exc}")
    print(f"結果：{len(tests) - len(failures)} passed, {len(failures)} failed")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(_run_direct())

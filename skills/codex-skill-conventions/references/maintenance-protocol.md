# Maintenance Protocol

This protocol governs future updates to this skill and to skills created under Codex Skill Conventions.

## Edits allowed without prior user approval

These edits are allowed only when all tests and validators pass afterward：

- Add a new skin, layout, prompt pattern, validator example, or reference section without changing frozen behavior.
- Append a new lesson to `LESSONS.md`.
- Add regression tests that tighten coverage.
- Fix typos or wording that does not alter rule meaning.
- Improve Codex-specific phrasing without weakening a house rule.
- Add traceability entries that document an existing migration decision.

## Edits requiring user approval first

Ask before changing any of these：

- Any value listed in `FROZEN.md`.
- The meaning of house rules 1 through 9.
- The detection logic in `scripts/validate_punct.py`.
- Any test assertion that weakens or removes coverage.
- Any validator gate that becomes optional.
- Any named GPT v1.6.1 validator pattern：`check_pages.py`、`check_math.py`、`verify_math.py`、`check_katex.py`、`verify_structures.py`、or `measure_bands.py`.
- Any pytest or direct runner contract.
- Any major version bump.
- Any deletion of a previously supported workflow, output format, or maintenance rule.
- Any replacement of a concrete hard gate with generic wording such as「domain validation」or「rendering checks」without also preserving the named source pattern.

## Lessons ledger format

Append one entry to `LESSONS.md` after validation failures, three-round stops, packaging mistakes, or user-reported defects.

```markdown
## YYYY-MM-DD｜<one-line title>
- 現象：<key validator line or user-reported issue>
- 根因：<one sentence>
- 對策：<file and rule changed, or test added>
- 已固化：<test file or rule number；write 否 if not yet hardened>
```

Keep each entry under four bullet lines. If a lesson can be converted into a test, add the test. Use `LESSONS.md` mainly for lessons not yet hard-coded into tests.

## Ledger compaction

When `LESSONS.md` exceeds 30 entries, or hardened entries exceed half of all entries, compact hardened entries into a one-line index at the end and keep unresolved entries in the main body. Run acceptance read-back before compaction to avoid deleting unresolved lessons.

## Installed skill update rule

An installed or mounted Codex Skill should be treated as immutable for the current task. To update it, create a complete revised package and give the user a new `skill.zip` or versioned release ZIP. Do not claim that the installed skill has been changed in place.

Correct delivery wording：

```text
已產出完整新版 skill.zip。重新安裝後才會生效。
```

Incorrect delivery wording：

```text
我已直接更新你已安裝的 skill。
```

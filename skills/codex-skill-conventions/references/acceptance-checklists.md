# Acceptance Checklists

Use these checklists when creating, migrating, validating, or delivering Codex Skills under Codex Skill Conventions.

## New skill focus gate

Before building a new skill, answer these items. Ask the user only for missing information that changes the output or validation contract.

| Item | Required answer |
|---|---|
| Position | What task does this skill own, and which existing skill should it not duplicate？ |
| Input | What will the user provide？ Text, files, folders, URLs, connectors, examples, or data？ |
| Output | What must the skill return？ A zip, document, analysis, transformed file, code patch, or message？ |
| Connectors | Which connectors, APIs, or tools may be used？ Which are forbidden？ |
| Contract | What values, schemas, layouts, prompts, or behaviors should be frozen？ |
| Validation | Which validators and tests define done？ |
| Boundary | What must the skill refuse, defer, or degrade？ |
| Delivery | What files must be packaged, and what should never be a manual patch？ |
| Maintenance | What lessons, versioning, and approval rules must be preserved？ |

## GPT to Codex migration checklist

1. Locate the source `SKILL.md` and confirm there is exactly one skill unless the user explicitly requested a multi-skill split.
2. Preserve source behavior, terminology, validators, tests, references, and maintenance rules unless a Codex runtime difference requires a change.
3. Rewrite the YAML frontmatter description for Codex triggering. Keep it under the validator limit and include task triggers.
4. Add `agents/openai.yaml`.
5. Move executable code into `scripts/` unless it is truly an asset for output production.
6. Convert ChatGPT-specific commands, file-presentation language, and environment paths into Codex-compatible language.
7. Document Codex runtime differences and any non-equivalent capability in `references/migration-notes.md`.
8. Add or update `FROZEN.md` for the migrated contract.
9. Run source tests first, then migrated tests, then package validation.
10. Deliver the full `skill.zip` and report what was preserved, changed, validated, and not fully enforceable.

## Pre-delivery validation checklist

| Gate | Required result |
|---|---|
| Structure | `SKILL.md` exists, frontmatter parses, and `agents/openai.yaml` exists. |
| Packaging | Official packager creates `skill.zip` without validation errors. |
| Punctuation | `scripts/validate_punct.py` exits 0 on Chinese-facing Markdown and text files. |
| Regression | `tests/test_*.py` exit 0 through both pytest and direct execution. |
| Contract tests | `tests/test_skill_contract.py` confirms named GPT v1.6.1 gates are present. |
| Frozen contract | No frozen value or rule changed without approval. |
| References | Long rules are in `references/`, and `SKILL.md` remains a control plane. |
| Scripts | Executable scripts are in `scripts/`, tested, and have clear command usage. |
| Delivery | User receives a complete installable package, not a patch. |
| Acceptance | Fresh-context acceptance is performed or a limitation is disclosed. |
| Runtime | Codex-Desktop（Windows）、codex-cli（Windows）、and codex-cli（Linux）differences are handled when commands or file paths matter. |

## v1.6.1 named gate acceptance

These checks are required for any GPT to Codex migration of this skill family.

| Gate | Required evidence |
|---|---|
| Page truncation | `SKILL.md`, `FROZEN.md`, and traceability mention print-mode page-by-page measurement, overflow greater than 2px, and `check_pages.py`. |
| Math correctness | `SKILL.md`, `FROZEN.md`, and traceability mention SymPy recomputation, mismatch as a hard block, `check_math.py`, and `verify_math.py`. |
| KaTeX rendering | `SKILL.md`, `FROZEN.md`, and traceability mention no placeholder tokens, no unrendered `$$` or `\(`, no `katex-error`, and `check_katex.py`. |
| Domain structures | `SKILL.md`, `FROZEN.md`, and traceability mention validate before rendering and `verify_structures.py`. |
| Bootstrap tests | `SKILL.md`, `FROZEN.md`, and tests mention intercepting `_pip` or `subprocess` without real installation. |
| Layout measurement | `SKILL.md`, `FROZEN.md`, and traceability mention band width difference less than one card and `measure_bands.py`. |
| Runner contract | `scripts/skill_gate.py` supports `--test-runner auto`、`--test-runner pytest`、and `--test-runner direct`. |
| Pytest compatibility | `python -m pytest tests -q` passes. |
| Direct compatibility | Direct execution of every `tests/test_*.py` file passes. |

## Fresh-context acceptance prompt template

Use this template with a separate context when possible. If a separate context is unavailable, use it as a local read-back checklist and disclose the limitation.

```text
You are validating a Codex Skill. You have not seen the generation process.

Files to inspect：
<attach or paste file list and contents>

Acceptance criteria：
1. The skill preserves the nine house rules.
2. The skill clearly explains Codex-specific migration limits.
3. Named GPT v1.6.1 validator patterns are present without abstraction：`check_pages.py`、`check_math.py`、`verify_math.py`、`check_katex.py`、`verify_structures.py`、`measure_bands.py`.
4. Executable checks are present and referenced correctly.
5. Frozen-contract and maintenance rules are present.
6. CLI interaction is a decision table plus explicit option input, with a recommended default when evidence supports one.
7. No delivery claim says an installed skill was modified in place.
8. The package can be validated and installed as a complete skill.
9. The standard Codex Skill workflow does not require a local external validator or separate application.

Return a table：criterion, pass or fail, evidence, required fix.
Do not infer from missing files. Mark missing evidence as fail.
```

## Three-round failure report template

```text
三輪重試已停止。

驗證器：<name>
完整輸出：
<output>

第 1 輪修改：<summary>
第 2 輪修改：<summary>
第 3 輪修改：<summary>

推測根因：<root cause>
建議裁決：<what the user should decide>
```

## v1.5.2 interactive acceptance review

Use this supplement when the change affects decision flow, acceptance behavior, or governance wording.

| Review point | Required evidence |
|---|---|
| Interactive options | The Skill tells the assistant to offer 2 to 4 feasible options when direction is unclear. |
| Tradeoff disclosure | Each option includes fit, risk, validation impact, and delivery impact. |
| Recommended default | The Skill marks one default only when the available constraints justify it. |
| Frozen choice handling | The Skill separates reversible choices from frozen-contract choices. |
| Acceptance template | The main file contains a reusable acceptance prompt template, not only this reference file. |
| Independent review boundary | The Skill distinguishes true separate-context acceptance from best-effort local read-back. |
| CLI option input | The Skill tells CLI users to type an option letter or type their own requirement. |

## v1.5.2 acceptance prompt short form

Use the short form only for small wording-only changes where all validators still pass.

```text
Role：Independent Skill acceptance reviewer.

Review inputs：
1. File contents：<paste changed files>
2. Requested change：<paste request>
3. Frozen rules：<paste relevant frozen rules>

Check：
1. Requested change is present.
2. No frozen rule is weakened.
3. Main-file execution-critical rules remain visible.
4. Validation and delivery gates remain enforceable.
5. Platform limitations are disclosed instead of hidden.

Return：
| Check | Pass or fail | Evidence | Required fix |
|---|---|---|---|
```

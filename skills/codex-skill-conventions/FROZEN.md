# Frozen Contract

## v1.6.1-codex｜2026-07-07｜locked

This Codex migration freezes the following contract items. v1.6.1-codex preserves the full `gpt-skill-conventions v1.6.1` contract and keeps the Codex runtime governance added in v1.5.2. These items must not be deleted, weakened, generalized, or moved out of `SKILL.md` without explicit user approval.

| Frozen item | Contract |
|---|---|
| Package identity | The skill identity remains `codex-skill-conventions`; the display name remains `Codex Skill Conventions`. Release artifacts may be versioned, but the installed skill name stays stable. |
| Canonical source | `gpt-skill-conventions v1.6.1` is the migration source for this version, with Joan v1.2 lineage preserved through the GPT package. |
| Single-skill operating model | Normal Codex Skill use remains self-contained and does not require an unrelated external validator CLI, local app, GitHub Action, or separate CI product. |
| Codex runtime governance | Codex-Desktop（Windows）、codex-cli（Windows）、and codex-cli（Linux）runtime differences remain visible in `SKILL.md`. |
| Immediate triggers | The main file and description keep the Chinese and English triggers for skill creation, update, inspection, refactor, validation, packaging, frozen contracts, regression tests, GPT to Codex migration, and Claude to Codex migration. |
| Joan lineage and ecology | The Joan v1.2 lineage and original ecology section remain visible in `SKILL.md`. |
| Nine house rules | House rules one through nine keep their order, meaning, and hard-gate strength. |
| No-abstraction rule | Concrete GPT v1.6.1 and Joan v1.2 validator rules, numeric thresholds, examples, anti-patterns, script names, and provenance names must not be replaced by generic wording. |
| Standard validation layers | Page truncation, SymPy math checks, KaTeX rendering checks, domain validation, regression self-tests, bootstrap tests, engine-change gates, and layout measurement must remain concrete, not abstract categories. |
| `scripts/validate_punct.py` gate | Fullwidth Chinese punctuation and no dash punctuation remain a baseline hard gate. |
| Page truncation gate | Print-mode page-by-page measurement remains required for fixed-page outputs; overflow greater than 2px is a hard block. Reference pattern：constructivist `check_pages.py`. |
| Math correctness gate | Every generated problem and claimed answer must be recomputed with SymPy and compared against the claim; mismatch is a hard block. Reference patterns：constructivist `check_math.py` and cornell `verify_math.py`. |
| KaTeX gate | Outputs must have no leftover placeholder tokens, no unrendered `$$` or `\(`, and no `katex-error`. Reference pattern：`check_katex.py`. |
| Domain gate | Chemistry and similar domain structures must validate before rendering. Reference pattern：cornell `verify_structures.py`. |
| Bootstrap gate | `ensure_*` happens before imports that need dependencies; tests intercept `_pip` or `subprocess` and do not perform real installation. |
| Layout measurement gate | Knowledge-wall or band-based visuals preserve explicit measurement thresholds, such as band width difference less than one card. Reference pattern：kmap `measure_bands.py`. |
| Regression test contract | `tests/test_*.py` files must be pytest-compatible and directly executable unless a future version explicitly freezes a different runner contract. |
| Skill gate runner | `scripts/skill_gate.py` supports `--test-runner auto`、`--test-runner pytest`、and `--test-runner direct`. |
| Contract tests | `tests/test_skill_contract.py` protects named GPT v1.6.1 and Joan v1.2 terms in `SKILL.md`, `FROZEN.md`, and traceability. |
| Interactive recommendation | Directional ambiguity requires 2 to 4 options, risk, validation impact, delivery impact, and a recommended default when evidence supports one. |
| CLI interaction | codex-cli interaction is a decision table plus explicit instruction to type an option letter or type the user's own requirement. Do not claim a CLI modal UI exists. |
| Acceptance template | The acceptance prompt template remains in `SKILL.md` main file and includes named validator pattern checks. |
| Main-file priority | Triggers, runtime matrix, nine house rules, named validator patterns, checklists, multi-format rules, maintenance protocol, and acceptance template remain visible in `SKILL.md`, not only in references. |
| Traceability | `references/migration-traceability.md` remains present and maps GPT v1.6.1 contract units to Codex v1.6.1 handling. |
| Complete ZIP delivery | Skill creation or update delivers a complete installable Codex Skill ZIP, not a patch-only update, unless the user explicitly asks for analysis or diff only. |
| Installed skill update rule | A mounted or installed Skill is treated as read-only; updates produce a complete new package and require reinstall. |
| `agents/openai.yaml` | `display_name`, `short_description`, `default_prompt`, and `policy.allow_implicit_invocation: true` remain present. `default_prompt` must include `$codex-skill-conventions`. |
| Helper scripts | `scripts/bootstrap.py` and `scripts/convert_from_claude_skill.py` remain bundled and regression-covered. |
| Execution priority block | The priority block remains near the top of `SKILL.md` as the first operational control plane. |

## Change Policy

Allowed without prior user approval, after validation passes：

- Add a non-frozen skin, layout, preset, registry entry, validator example, or reference section without changing frozen behavior.
- Add regression tests that tighten coverage.
- Add a lesson to `LESSONS.md`.
- Fix typos or examples without changing rule semantics.
- Improve wording that makes existing rules clearer but not weaker.
- Add traceability entries that document an existing migration decision.

Require explicit user approval before editing：

- Any item listed in this file.
- Any frozen registry, token, coordinate, schema, validator rule, runner contract, or delivery contract.
- Detection logic in `scripts/validate_punct.py`.
- Deleting or weakening any validator, test assertion, named validator pattern, or standard validation layer.
- Changing the meaning or order of the nine house rules.
- Removing main-file trigger words, checklists, standard validation layers, named validator patterns, multi-format rules, acceptance template, or maintenance protocol.
- Replacing a GPT v1.6.1 or Joan v1.2 concrete hard gate with a generic phrase.
- Any major-version semantic change.

## Validation Hooks

- `tests/test_validate_punct.py` protects the punctuation validator, sync behavior, metadata contract, bootstrap behavior, and conversion helper.
- `tests/test_skill_contract.py` protects GPT v1.6.1 and Joan v1.2 named gate terms.
- `scripts/skill_gate.py` checks structure, metadata, text hygiene, contract terms, and regression tests.
- `scripts/bootstrap.py` provides idempotent setup helpers for generated Skill scripts.
- `scripts/convert_from_claude_skill.py` provides source-to-Codex skeleton conversion and review reporting.
- The Codex package validation confirms frontmatter and creates the installable archive.

## Optional Future Infrastructure

External validator tools, repository automation, or CI workflows may be designed later only as optional infrastructure. They must not be described as required for the standard Codex Skill experience.

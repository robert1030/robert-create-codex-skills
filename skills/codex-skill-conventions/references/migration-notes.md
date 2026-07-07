# GPT and Claude to Codex Migration Notes

This file records semantic changes made while migrating `gpt-skill-conventions v1.6.1` into `codex-skill-conventions v1.6.1`, while preserving the Codex runtime governance and helper scripts from `codex-skill-conventions v1.5.2`.

## Preserved behavior

- The nine house rules remain the governing contract.
- The punctuation validator and its regression coverage remain central gates.
- Frozen contracts, `FROZEN.md`, `LESSONS.md`, maintenance rules, three-round retry limits, interactive recommendation flow, and fresh-context acceptance remain required concepts.
- The skill remains a governance overlay, not a replacement for Codex `skill-creator`.
- Chinese trigger strength remains explicit in the frontmatter and main file.
- Joan v1.2 ecology remains visible in `SKILL.md` as the design provenance.
- The earlier Claude-to-Codex helper pattern remains available through `scripts/convert_from_claude_skill.py`, but the generated output still requires human review before delivery.
- GPT v1.6.1 concrete validator names and patterns remain visible：`check_pages.py`、`check_math.py`、`verify_math.py`、`check_katex.py`、`verify_structures.py`、`measure_bands.py`.
- v1.6.1 test runner behavior remains preserved：`python -m pytest tests -q` and direct runner execution both need to work.

## Codex-specific changes

| GPT-oriented concept | Codex migration |
|---|---|
| ChatGPT Web Skill as the default surface | Codex Skill governance across Codex-Desktop（Windows）、codex-cli（Windows）、and codex-cli（Linux）。 |
| ChatGPT packager language | Generic Codex package validation plus canonical `skill.zip` handoff when required by the toolchain. |
| ChatGPT sandbox link delivery wording | Codex workspace or generated-file handoff wording, with runtime assumptions disclosed. |
| Generic command examples | Runtime-aware command style：PowerShell or `cmd` for Windows；POSIX shell for Linux. |
| Claude-era or GPT-era Skill skeletons | Use `scripts/convert_from_claude_skill.py` only as a review helper；do not treat its generated skeleton as final until `skill_gate.py` and acceptance pass. |
| Fresh-context child task | Use a separate context when available；otherwise perform best-effort local read-back and disclose the limitation. |
| Hard validation gate | Use bundled scripts and tests first；do not require external CI for the normal Codex Skill workflow. |
| ChatGPT-style interactive recommendation | Codex CLI uses a decision table plus instruction to type A, B, C, or a free-form requirement；Codex-Desktop may use a short-question UI only when available. |
| ChatGPT v1.6.1 named gates | Preserve names and semantics in `SKILL.md`, `FROZEN.md`, traceability, and contract tests；do not reduce to generic domain validation. |

## Non-equivalent capabilities

Codex Skills can instruct and bundle scripts, but they cannot guarantee these actions by themselves：

- Prevent a user or model from skipping validation in every environment.
- Open a truly independent fresh context without a separate context.
- Modify an installed skill package in place.
- Enforce repository-wide CI or pull-request blocking without separate infrastructure.
- Guarantee that Codex-Desktop plugins, browser use, or remote control are enabled in the user's workspace.

The normal migration target is still a single self-contained Codex Skill. If the user later asks for team-level automation, repository blocking, non-bypassable CI, marketplace repair, or plugin troubleshooting, treat that as a separate optional project, not part of this Skill mainline.

## Migration validation expectations

A migrated package should pass all of these before delivery：

1. Original source tests, when still applicable.
2. Migrated `tests/test_validate_punct.py`.
3. Migrated `tests/test_skill_contract.py`.
4. `scripts/skill_gate.py --test-runner pytest`.
5. `scripts/skill_gate.py --test-runner direct`.
6. `scripts/skill_gate.py --test-runner auto`.
7. `python -m pytest tests -q`.
8. Direct execution of every `tests/test_*.py` file.
9. Codex-compatible frontmatter and `agents/openai.yaml` validation.
10. `scripts/bootstrap.py` and `scripts/convert_from_claude_skill.py` regression coverage when those helpers are bundled.
11. Manual or fresh-context acceptance against the migration checklist.

## v1.6.1 remigration note

`v1.6.1-codex` treats `gpt-skill-conventions v1.6.1` as the canonical migration source for this release. The earlier `codex-skill-conventions v1.5.2` remains the Codex runtime and metadata base, but it is not allowed to abstract GPT v1.6.1 concrete gates. Platform conversion is allowed only when explicitly documented：ChatGPT artifact links become Codex workspace or generated-file handoff, ChatGPT Web Skill wording becomes Codex Skill runtime wording, installed Skills are treated as read-only, and fresh-context acceptance is best-effort when true isolation is unavailable.

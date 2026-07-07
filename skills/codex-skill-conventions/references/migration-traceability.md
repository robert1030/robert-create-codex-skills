# Migration Traceability：GPT v1.6.1 to Codex v1.6.1

This file prevents `gpt-skill-conventions v1.6.1` from being summarized into generic Codex guidance. `SKILL.md` remains the execution entrypoint. This file is evidence and review support.

| GPT v1.6.1 contract unit | Codex v1.6.1 handling | Evidence location | Notes |
|---|---|---|---|
| Governance overlay on `skill-creator` | Preserved and Codex-converted | Core contract | Compose with Codex `skill-creator`; do not replace it. |
| Chinese and English triggers | Preserved | Description and immediate trigger list | Includes 開新、升級、檢視、重構、驗證器、凍結契約、回歸測試、交付前檢查，plus GPT to Codex and Claude to Codex migration. |
| Joan v1.2 lineage and ecology | Preserved | Joan lineage and ecology | Keeps cornell, constructivist, kmap, kcg, dex, and course handout provenance. |
| House rule 1：freeze contracts | Preserved | House rule 1, `FROZEN.md` | Keeps registry, `FROZEN.md`, frozen assertions, and versioning. |
| House rule 2：validation is hard gate | Preserved and strengthened | House rule 2, `tests/test_skill_contract.py` | Concrete named gate terms remain main-file visible. |
| `validate_punct.py` | Preserved and Codex-converted | House rule 2, house rule 3, scripts | Executable copy lives in `scripts/validate_punct.py`. |
| Page truncation | Preserved | House rule 2, pre-delivery checklist, `FROZEN.md` | Print-mode page-by-page measurement; overflow greater than 2px blocked; reference pattern `check_pages.py`. |
| Math correctness | Preserved | House rule 2, pre-delivery checklist, `FROZEN.md` | SymPy recomputation for every claimed answer; reference patterns `check_math.py` and `verify_math.py`. |
| KaTeX rendering | Preserved | House rule 2, pre-delivery checklist, `FROZEN.md` | No placeholder tokens, no unrendered `$$` or `\(`, no `katex-error`; reference pattern `check_katex.py`. |
| Domain correctness | Preserved | House rule 2, pre-delivery checklist, `FROZEN.md` | Validate before rendering; reference pattern `verify_structures.py`. |
| Regression self-tests | Preserved and Codex-runner-aware | House rule 2, script map, `FROZEN.md` | `tests/test_*.py` must be pytest-compatible and directly executable. |
| Bootstrap tests | Preserved | House rule 2, house rule 6, `FROZEN.md` | Intercept `_pip` or `subprocess`; do not perform real installation. |
| Engine-change gate | Preserved | House rule 2 | Changing an engine requires all relevant tests before claiming preserved contract. |
| Layout measurement | Preserved | House rule 2, pre-delivery checklist, `FROZEN.md` | `measure_bands.py` pattern; threshold such as band width difference less than one card. |
| House rule 3：fullwidth punctuation and no dash punctuation | Preserved | House rule 3, `scripts/validate_punct.py` | Baseline validator remains a hard gate. |
| House rule 4：engine／skin／content | Preserved | House rule 4 | Keeps skeleton × skin × layout × content. |
| House rule 5：capability boundaries and graceful degradation | Preserved | House rule 5 | No fake data, hidden tool access, unsupported rendering, fake citation, or fake numeric certainty. |
| House rule 6：transparent setup and offline capability | Preserved and Codex-converted | House rule 6, `scripts/bootstrap.py` | Codex helper detects `--break-system-packages` need instead of hard-coding one runtime. |
| House rule 7：focus gate before generation | Preserved and CLI-converted | House rule 7, interactive recommendation flow | CLI uses decision table plus typed option or free-form requirement. |
| House rule 8：three-round retry | Preserved | House rule 8 | Same failure category stops after three attempts. |
| House rule 9：acceptance must not self-certify | Preserved and Codex-converted | House rule 9, acceptance prompt template | Separate context when possible; best-effort local read-back when not. |
| Three working modes | Preserved | Three working modes | Apply, Explore, Imitate. |
| Satisfaction loop | Preserved | Satisfaction loop | Ask whether the user is satisfied after delivery. |
| Multi-format delivery | Codex-converted | Multi-format delivery rules | Claude `present_files` becomes Codex workspace or generated-file handoff. |
| New Skill intake checklist | Preserved and strengthened | New skill intake checklist | Named validators and acceptance item added. |
| Pre-delivery validation checklist | Preserved and strengthened | Pre-delivery validation checklist | Concrete named validators and runner modes remain listed. |
| Maintenance protocol | Preserved and Codex-converted | Maintenance protocol | Installed Skill treated as read-only; update via complete new ZIP. |
| Delegation prompt rule | Preserved | Delegation prompt rule | Delegated prompts need acceptance criteria, fixed report format, retry limit. |
| Delivery note template | Preserved | Delivery note template | Actual checks, limitations, package link or path, satisfaction question. |
| v1.6.1 pytest compatibility | Preserved and Codex-converted | `tests/test_*.py`, `scripts/skill_gate.py` | Tests support both `python -m pytest tests -q` and direct runner. |
| `agents/openai.yaml` | Codex-specific addition | `agents/openai.yaml`, `FROZEN.md` | Codex metadata includes `default_prompt` and implicit invocation. |
| Codex runtime matrix | Codex-specific addition | Codex runtime matrix | Covers Codex-Desktop（Windows）、codex-cli（Windows）、codex-cli（Linux）。 |

## Non-equivalent or Platform-Converted Items

| GPT v1.6.1 meaning | Codex v1.6.1 handling | Reason |
|---|---|---|
| ChatGPT Web Skill surface | Codex Skill across Desktop and CLI surfaces | Codex has local workspace, CLI, and Desktop runtime differences. |
| ChatGPT artifact links | Codex workspace or generated-file handoff | Codex deliverables live in the active workspace or app handoff. |
| ChatGPT packager wording | Codex package validation and `skill-packager` zip output | Codex package structure requires folder name equals `SKILL.md` name. |
| Truly fresh-context child task | Separate context when available; otherwise best-effort read-back | A single skill cannot guarantee an independent context. |
| Direct update of installed Web Skill | Produce complete new Codex Skill ZIP and ask for reinstall | Installed or mounted skills are treated as read-only. |
| Fixed ChatGPT runtime | Runtime matrix and focus gate | Codex-Desktop Windows, codex-cli Windows, and codex-cli Linux differ in path, shell, and UI behavior。 |

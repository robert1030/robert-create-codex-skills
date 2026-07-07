---
name: codex-skill-conventions
description: "govern OpenAI Codex skill creation, GPT to Codex migration, Claude to Codex migration, validation, packaging, review, and maintenance across Codex-Desktop Windows, codex-cli Windows, and codex-cli Linux. Use when the user says or implies：開新 skill、做一個 skill、寫一支 skill、升級 skill、檢視 skill、重構 skill、skill 房規、skill 規範、驗證器、凍結契約、回歸測試、交付前檢查、create a skill、update a skill、refactor a skill、validate a skill、package a skill、gpt-to-codex skill migration、claude-to-codex skill migration. Apply with Codex skill-creator as a strict governance overlay and preserve the full gpt-skill-conventions v1.6.1 contract without abstracting validators, house rules, workflows, frozen contracts, acceptance, or delivery gates."
---
# Codex Skill Conventions

> **v1.6.1-codex｜2026-07-07**：Codex 移植版。以 `gpt-skill-conventions v1.6.1` 為契約來源，保留 `codex-skill-conventions v1.5.2` 的 Codex-Desktop（Windows）、codex-cli（Windows）、codex-cli（Linux）runtime governance。完整搬移 GPT 版房規、流程、驗證、具名 validator pattern、凍結契約、contract tests、acceptance prompt template、maintenance protocol 與 delivery gates；只做 Codex 平台轉換，不做語意抽象或縮水。

## Execution priority block

Apply these priorities before reading later details：

1. Protect frozen contracts first. Do not weaken `FROZEN.md`, validator behavior, delivery contract, or house-rule order without explicit user approval.
2. Run validators before delivery. At minimum use `scripts/skill_gate.py`, punctuation validation, contract tests, and regression tests when execution is available.
3. Deliver a complete installable package. Do not return a patch-only update unless the user explicitly requested analysis or diff only.
4. Use the focus gate when direction is unclear. Present 2 to 4 options with fit, risk, validation impact, delivery impact, and a recommended default when evidence supports one. In CLI, tell the user to type an option letter or type their own requirement.
5. Resolve Codex runtime when it affects commands, files, validation, packaging, connectors, or handoff：Codex-Desktop（Windows）、codex-cli（Windows）、or codex-cli（Linux）。
6. Keep critical governance visible in `SKILL.md`：triggers、runtime matrix、nine house rules、named validator patterns、hard gate、delivery rules、checklists、maintenance protocol、acceptance template.
7. If a required check cannot run, disclose the missing check and do not call the package fully verified.
8. Do not abstract GPT contract terms. Preserve concrete names such as `check_pages.py`、`check_math.py`、`verify_math.py`、`check_katex.py`、`verify_structures.py`、`measure_bands.py` in main-file rules, frozen contracts, traceability, and tests.

## Core contract

Use this skill as a governance overlay on top of Codex `skill-creator` whenever building, migrating, validating, packaging, reviewing, or maintaining Codex Skills. `skill-creator` provides the generic draft、test、iterate、package process. This skill adds the full `gpt-skill-conventions v1.6.1` contract：frozen contracts, hard validation gates, fullwidth punctuation, engine／skin／content separation, capability boundaries, transparent bootstrap, focus gates, three-round retry limit, fresh-context acceptance, multi-format delivery, maintenance discipline, runtime-aware questioning, and non-abstracted validator traceability.

Do not replace `skill-creator`. Compose both workflows.

Hard default：every delivered skill must be a complete installable ZIP package, not a patch set, unless the user explicitly asks for analysis only. When the surrounding toolchain expects `skill.zip`, keep that filename. When a repository or release process expects a versioned file, produce the versioned copy only after the canonical package passes validation.

Self-contained default：normal Codex Skill use must not require the user to install a separate validator product, run unrelated applications, or use repository CI. Use bundled instructions, references, scripts, and tests first. Mention external tooling only as optional infrastructure when the user explicitly asks for repository-level automation or non-bypassable CI.

Runtime-aware default：Codex has different execution surfaces. Always identify whether the user is using Codex-Desktop（Windows）、codex-cli（Windows）、or codex-cli（Linux）when that affects paths, commands, shell syntax, packaging, connectors, remote control, browser access, or file handoff. Do not ask this when the task is pure text review and the runtime cannot affect the answer.

Main-file priority：do not hide the critical governance contract only in references. The trigger list, Codex runtime matrix, nine house rules, standard validation layers, named validator patterns, interactive recommendation flow, acceptance template, multi-format delivery rules, new skill checklist, pre-delivery checklist, and maintenance protocol must remain directly visible in this file because they are execution-critical.

No-abstraction default：when migrating from GPT or Joan lineage, concrete validation rules, numeric thresholds, examples, anti-patterns, script names, and provenance names must be preserved unless a Codex runtime difference forces a documented conversion. Do not replace a concrete hard gate with a generic phrase such as「domain validation」or「rendering checks」unless the named source patterns are still listed beside it.

## Immediate trigger list

When the user says or implies these triggers, read and apply this skill before generating or modifying any Skill artifact：

- Chinese triggers：`開新 skill`、`做一個 skill`、`寫一支 skill`、`升級 skill`、`檢視 skill`、`重構 skill`、`skill 房規`、`skill 規範`、`驗證器`、`凍結契約`、`回歸測試`、`交付前檢查`。
- English triggers：`create a skill`、`update a skill`、`refactor a skill`、`inspect a skill`、`validate a skill`、`package a skill`、`migrate a GPT skill to Codex`、`migrate a Claude skill to Codex`.

Even if the user only says「幫我做一個 XXX 的 skill」，first apply this governance skill and `skill-creator` together.

## Codex runtime matrix

Use this table before asking interactive questions or giving commands. The goal is not to make the user answer needless setup questions. The goal is to avoid giving a command, path, or workflow that only works on another Codex surface.

| Runtime | Ask when it matters | Command style | Path style | Interaction and delivery impact |
|---|---|---|---|---|
| Codex-Desktop（Windows） | Ask when the task touches local files, plugins, browser/computer-use, remote pairing, sandbox paths, marketplace data, or generated ZIP handoff. | Prefer PowerShell-compatible commands unless the current session exposes a Unix shell. | Windows paths may appear, but generated artifacts usually live in the workspace or sandbox chosen by Codex. | Keep prompts short and decision-table based. State when an action changes local files. Do not assume shell profile or WSL. |
| codex-cli（Windows） | Ask when commands, quoting, environment variables, executable discovery, or package scripts are involved. | Prefer PowerShell or `cmd` examples when the user is in Windows. Give Bash only if the user says they use Git Bash, MSYS2, or WSL. | Use `C:\...` examples for user paths and avoid Linux-only assumptions. | Make validators runnable with `python scripts\...` or `py scripts\...` when needed. |
| codex-cli（Linux） | Ask when shell commands, permissions, package scripts, or executable bits matter. | Prefer POSIX shell commands. | Use `/home/...` or repository-relative paths. | It is safer to rely on executable shebangs, `chmod`, and standard shell pipelines. |

Runtime focus gate：

1. If the runtime is unknown and the answer needs commands or filesystem edits, ask one compact question with the three choices above.
2. If the user already provided OS evidence, infer the runtime and proceed. Examples：Windows paths imply Windows；Linux shell paths imply Linux；Codex-Desktop plugin or remote-pairing issues imply Codex-Desktop.
3. If a choice only affects command syntax, provide both Windows and Linux command forms instead of delaying.
4. If a choice affects validation integrity, packaging, or file locations, ask before editing frozen contracts or finalizing delivery.
5. Record runtime assumptions in the delivery report so the next session can reproduce the result.

## Joan v1.2 lineage and ecology

This Codex Skill inherits the Joan Skill Conventions v1.2 lineage through `gpt-skill-conventions v1.6.1`. Preserve the substance of the original house rules rather than flattening them into generic advice.

Original ecology to keep in mind when designing new Skills：

- `cornell-notes-generator`：Cornell notes, math verification, chemistry structure checks, and print-ready study material patterns.
- `constructivist-lesson-builder`：lesson generation, multi-question focus gate, page overflow checks, KaTeX checks, and SymPy answer verification.
- `knowledge-map-generator`：knowledge wall, band measurement, visual density checks, and reusable layout presets.
- `knowledge-card-generator`：skin registry, frozen palette contracts, card templates, and subject-agnostic rendering.
- `dex-card-generator`：subject defaults, visual fallback ladder, glyph fallback, and non-fake visual degradation.
- `course-handout-generator`：apply、explore、imitate mode discipline and satisfaction loop.

These examples are not mandatory dependencies. They are the design provenance behind the rules. Use them to preserve the original level of strictness.

## Workflow

1. Classify the task：new skill、existing skill update、GPT to Codex migration、validator work、pre-delivery review、or maintenance.
2. For provided ZIPs or folders, inspect first, count `SKILL.md` entrypoints, and preserve behavior unless Codex runtime differences require migration.
3. Run the focus gate before large generation, define input、output、connectors、frozen values、delivery formats、validation gates、fallback behavior、and acceptance criteria.
4. For GPT or Joan migration, build or update traceability：preserved、Codex-converted、moved to reference with main-file hard rule retained、or impossible to equalize.
5. Plan reusable files, implement edits, and keep critical gates in `SKILL.md` instead of moving them only to references.
6. Run machine checks before delivery：`scripts/skill_gate.py` when present, punctuation validation, `tests/test_skill_contract.py`, and all `tests/test_*.py`. Stop or label as unverified if a required check fails or cannot run.
7. If the same validation failure recurs three times, stop editing and report the validator output, three attempted fixes, likely root cause, and next decision needed.
8. Respect the three-failure stop rule, perform fresh-context acceptance when possible, disclose local-only acceptance limits, package the complete Codex Skill ZIP, and ask whether the user is satisfied.

## Interactive recommendation flow

Use this flow when the user wants to create, upgrade, inspect, or refactor a Skill, but the target behavior, validation strategy, delivery format, or maintenance direction is not fully defined.

Do not respond with a large questionnaire first. Provide a small decision table that lets the user choose a direction.

Required flow：

1. Restate the unresolved decision in one sentence.
2. Offer 2 to 4 feasible options with best fit, risk, validation impact, and delivery impact.
3. Mark one recommended default when evidence supports it；otherwise state that no default should be chosen yet.
4. Separate reversible choices from frozen-contract choices, and get explicit approval before changing frozen-contract choices.
5. Proceed with the recommended default only when user constraints are sufficient and no frozen rule is weakened.
6. After the user chooses, update the contract, affected files, validators, and tests before packaging.

Decision table format：

| Decision | Option | Best fit | Risk | Validation impact | Delivery impact | Recommendation |
|---|---|---|---|---|---|---|
| <decision> | A | <when to use> | <risk> | <validator or test change> | <file or package change> | <default or not> |

CLI prompt format：

```text
請輸入 A、B、C，或直接輸入你的需求。
建議選 A：<one concrete reason tied to evidence, validation, or delivery risk>。
```

For codex-cli（Windows）and codex-cli（Linux），the decision table and prompt text are the interactive UI. Do not imply a modal dialog, dropdown, or graphical widget exists. If Codex-Desktop exposes a short-question UI, it may be used, but the same options, recommendation, validation impact, delivery impact, and risk must remain visible in plain text.

Use this flow for ambiguity. Do not use it to delay obvious repairs, typo fixes, validator failures, or user-explicit changes.

## Acceptance prompt template

Use this main-file template for fresh-context acceptance of `SKILL.md`, `FROZEN.md`, long policy files, or full Skill packages. Use a truly separate context when available. If no separate context is available, perform a best-effort local read-back and label it as not equivalent to independent acceptance. Load `references/acceptance-checklists.md` when the review needs the expanded checklist.

```text
Role：Independent Codex Skill reviewer. You have not seen the authoring process.

Inputs：
1. Skill package or changed files：<attach or paste>
2. Intended version：<version>
3. Requested change：<request>
4. Frozen rules：<FROZEN.md or locked items>

Criteria：
1. Exactly one Skill unless explicitly requested otherwise.
2. `SKILL.md` frontmatter contains only `name` and `description`, and the description has real triggers.
3. Requested changes are present without weakening frozen rules, validator behavior, delivery contract, house-rule order, or main-file critical rules.
4. GPT v1.6.1 named validator patterns are present without abstraction：`check_pages.py`、`check_math.py`、`verify_math.py`、`check_katex.py`、`verify_structures.py`、`measure_bands.py`.
5. Required validators, scripts, tests, references, capability boundaries, fallback behavior, runtime handling, delivery format, and acceptance criteria are present.
6. CLI interaction is represented as a decision table plus explicit option input, including a recommended default when evidence supports one.
7. The package does not require unrelated external validator products, local apps, or repository CI for normal Codex Skill use.
8. The final deliverable can be packaged as a complete installable Codex Skill ZIP.

Report：
| Criterion | Pass or fail | Evidence | Required fix |
|---|---|---|---|

Rules：do not infer missing evidence；mark missing files、validators、triggers、or unclear runtime handling as fail；distinguish platform limits from defects；delivery stops on any fail.
```

Minimum acceptance evidence to report in final delivery：separate-context status, reviewed files, validators and tests executed, criteria pass or fail, and remaining limitations.

## Nine house rules

### 1. Freeze contracts and create new versions

Once a layout, coordinate set, color palette, skin, schema, validator behavior, or delivery contract is finalized, mark it as frozen. Do not mutate frozen values in place.

Implementation requirements：

- Put frozen values in named constants, registries, or tables.
- Maintain `FROZEN.md` with version, locked items, owner, and change policy.
- Write regression assertions for frozen values wherever possible.
- Add new versions or registry entries instead of editing frozen ones.
- Preserve backward compatibility：unspecified values should keep using defaults or old behavior.

Anti-pattern：silently changing a fixed palette, coordinate, validator rule, or output schema because it seems better.

### 2. Validation is the hard gate, never visual inspection

Every serious Skill deliverable needs required validators. Exit code nonzero means not ready for final delivery. Correctness belongs to executable checks, not subjective visual inspection.

Standard validation layers, stacked as each Skill requires：

- `scripts/validate_punct.py`：fullwidth Chinese punctuation and no dash punctuation. This is the shared baseline validator.
- Page truncation：for print or fixed-page outputs, measure overflow page by page in print mode. Screenshot review is insufficient because hidden cropping is easy to miss. Overflow greater than 2px is a hard block. Reference pattern：constructivist `check_pages.py`.
- Math correctness：for generated problems and claimed answers, recompute every item with SymPy and compare against the claimed answer. Mismatch is a hard block. Answer correctness must never rely on eyesight. Reference patterns：constructivist `check_math.py` and cornell `verify_math.py`.
- KaTeX rendering：there must be no leftover placeholder tokens, no unrendered `$$` or `\(`, and no `katex-error`. Reference pattern：`check_katex.py`.
- Domain correctness：domain structures must be validated before rendering. Examples include chemical carbon skeleton counts, reaction balancing, and label alignment. Reference pattern：cornell `verify_structures.py`.
- Regression self-tests：each Skill should include `tests/test_*.py` for parts that can run without heavy dependencies, including pure logic functions, frozen contract assertions for palettes, coordinates, registries, missing-input fallback branches, and automatic installation logic. Tests should be pytest-compatible and directly executable unless the user explicitly freezes a different runner contract.
- Bootstrap tests：when testing automatic installation, intercept `_pip` or `subprocess` so the test verifies that already-installed dependencies are skipped and missing dependencies trigger an install attempt without performing real installation.
- Engine-change gate：after changing an engine, run all relevant tests. All PASS is required before claiming the existing contract is preserved.
- Layout measurement：for knowledge-wall or band-based visuals, measure band widths and fill cards until the difference is less than one card. Reference pattern：kmap `measure_bands.py`.

Hard-gate rules：

- If a required validator fails, do not deliver as final.
- If a required validator cannot run in the current environment, do not mark the artifact as verified.
- If the user asks for speed, still run the minimum gate. Speed does not waive required validation.
- If only text-level review is possible, label the result as a draft or best-effort review, not a fully verified final package.
- Do not convert a failed machine gate into a subjective statement such as「看起來沒問題」。

Anti-pattern：「看起來對就交付」。This is especially dangerous for numeric answers and page truncation.

### 3. Fullwidth Chinese punctuation and no dash punctuation

Chinese text must use fullwidth punctuation. Use halfwidth punctuation only inside English, numbers, code, file paths, URLs, command flags, and machine-readable formats.

Required punctuation style：

- Use：`，`、`。`、`、`、`：`、`；`、`？`、`！`、`「」`、`『』`、`（）`。
- Do not use em dash, en dash, or double hyphen as punctuation near Chinese text.
- Use fullwidth commas, periods, colons, semicolons, or shorter sentences instead of dash punctuation.

Run `scripts/validate_punct.py` on Chinese-facing Markdown, HTML, and text outputs before delivery.

### 4. Keep engine, skin, and content orthogonal

Separate the rendering engine, visual skin, and subject content. The engine should support multiple domains without hard-coding one subject.

Implementation requirements：

- Put skins, palettes, layouts, and presets in named registries.
- Keep content data separate from rendering code.
- Provide defaults that preserve backward compatibility.
- Add new subjects through mappings or presets, not engine rewrites.
- For visual skills, design as skeleton × skin × layout × content, not as one-off hard-coded output.

### 5. Be honest about capability boundaries and degrade cleanly

State what the skill cannot reliably do. Do not fake missing data, hidden tool access, image provenance, mathematical certainty, legal certainty, connector access, or unsupported rendering.

Implementation requirements：

- Add a capability boundary section to skills that produce domain outputs.
- Define a fallback ladder for missing dependencies or missing inputs.
- Mark uncertain facts as requiring verification instead of inventing them.
- Prefer dignified text, glyph, icon, template, or placeholder fallback over empty holes or fake specificity.
- For visuals, do not copy protected illustration or proprietary design elements. Extract only non-copyrighted structural traits when using references.

### 6. Make setup transparent and delivery offline-capable

Avoid asking the user to manually install dependencies when a script can do it safely in the current execution environment. For heavy dependencies, use idempotent bootstrap helpers and call them before imports that need those dependencies.

Implementation requirements：

- Put setup helpers in `scripts/bootstrap.py` when needed.
- Provide granular `ensure_*` functions such as `ensure_export` for Playwright and Chromium, `ensure_katex` for npm KaTeX, `ensure_math` for SymPy, and `ensure_font_tools` for fonttools and brotli.
- Keep setup idempotent：installed dependencies should be skipped quickly.
- Call `ensure_*` before the corresponding import. A top-level import can fail before the helper has a chance to install the dependency.
- pip installs in constrained environments may need `--break-system-packages`; Codex helpers must detect whether this is needed instead of hard-coding one runtime.
- Test bootstrap logic without doing real installs by intercepting `_pip` or `subprocess`.
- For generated HTML or print outputs, embed fonts and rendering assets when offline use is required.
- For KaTeX or math rendering, prefer pre-rendered and embedded assets when the deliverable promises offline use.
- Deliver self-contained files when the skill promises offline or print use.

### 7. Use a focus gate before generation

Do not generate a large skill, deck, report, template, or artifact immediately from a vague topic. First align on the few parameters that affect correctness.

Ask only about material missing values：expected input and output, connectors or tools, target users and level, required formats, frozen contract or versioning needs, validation requirements, and acceptance criteria. Infer obvious values from context and avoid questionnaire overload.

When the missing information is directional rather than factual, do not ask an open-ended question only. Present feasible options with tradeoffs, risks, validation impact, and a recommended default. Let the user decide before changing frozen contracts, weakening validation, removing delivery formats, or redefining the Skill scope.

### 8. Retry the same failure at most three times

For a fix-and-rerun loop, the same validation failure category may be retried at most three times. On the third failure, stop modifying and report：

- Validator name and full output.
- What changed in each attempt.
- Likely root cause.
- Recommended next decision for the user.

User-directed redesigns are requirement changes, not retry-loop failures.

### 9. Acceptance must not self-certify

The author must not be the only judge. Code and scripts must be checked by executable validators when possible. Text deliverables should receive fresh-context acceptance when possible.

For Codex Skill work：

- Run executable tests and validators as independent checks when code execution is available.
- For `SKILL.md`, `FROZEN.md`, and long policy text, use the acceptance prompt template in this main file. Give only the file contents, user-requested changes, frozen rules, and checklist.
- If the environment cannot create a truly separate context, perform a best-effort read-back and explicitly label it as not equivalent to external acceptance.
- For high-risk changes, get user confirmation before changing frozen rules, deleting validation, relaxing tests, or removing features.

## Three working modes

- **Apply**：use an existing frozen pattern, validator, or template for stable repeated production.
- **Explore**：try variants in skin, layout, density, or workflow until the user chooses one to freeze.
- **Imitate**：extract non-copyrighted structural traits from a user-provided reference, such as layout rhythm, field set, tone, or palette. Do not copy protected illustration or proprietary design elements.

## Satisfaction loop

Every delivery must ask whether the user is satisfied. Visual issues such as color, font, density, or layout should lead to parameter changes and regenerated output. Content issues should lead to content fixes and rerun validation. This loop is separate from the three-failure retry limit because user-directed redesign is a requirement change.

## Multi-format delivery rules

For Skill creation and Skill updates, the primary deliverable is always a complete installable `skill.zip`.

For artifact-producing skills, preserve Joan v1.2 multi-format discipline unless the target task clearly does not need it：

- HTML：single self-contained file when feasible.
- PDF：print-ready output when the deliverable is meant to be printed or reviewed offline.
- PNG：multi-page visual outputs should be exported and packaged as a zip when useful.
- DOCX：instructional handouts, long-form documents, or editable office deliverables should include DOCX when the user needs editing.
- Spreadsheet or slides：use the appropriate artifact skill and preserve source data or layout templates.

Codex replacement for Claude `present_files`：provide generated files through the active workspace or generated-file handoff. The rule is still「multi-format deliverables must all be provided」，not merely described.

## New skill intake checklist

Before creating a new skill, answer or infer the following. Ask only for missing items that materially affect correctness：

1. **Positioning**：What existing skill or workflow does this overlap with？ Upgrade an existing skill instead of creating a duplicate when appropriate.
2. **Input**：What files, text, URLs, connectors, or user prompts will the skill receive？
3. **Output**：What exact artifact, answer, report, transformed text, code, or package should it produce？
4. **Connectors and tools**：Which tools must be used, and which are optional？
5. **Engine, skin, content**：What is the reusable engine？ What are the skins or presets？ What content is data？
6. **Capability boundary**：What must the skill refuse, verify externally, or degrade gracefully？
7. **Focus gate**：What must be clarified before generation？ What can be inferred without asking？ Which unclear directions require an interactive recommendation table？
8. **Frozen contract**：Which values, schemas, palettes, coordinates, prompts, or validators must be frozen？
9. **Validation layers**：Which concrete validators and hard gates apply？ Fullwidth punctuation is baseline. Math uses SymPy with `check_math.py` or `verify_math.py` style recomputation. Fixed pages use print-mode overflow measurement like `check_pages.py`. KaTeX uses `check_katex.py` style placeholder, delimiter, and `katex-error` checks. Domain visuals validate before rendering with patterns such as `verify_structures.py`. Layout measurement keeps patterns such as `measure_bands.py`.
10. **Dependencies**：Which heavy dependencies need bootstrap helpers？ Can output remain offline-capable？ How will bootstrap be tested without real installation？
11. **Delivery formats**：Which formats must be delivered？ For Skill work, include complete `skill.zip`.
12. **Regression tests**：Which pure logic, frozen values, fallback behavior, bootstrap behavior, and validator behavior must be covered under `tests/`？
13. **Acceptance**：What fresh-context or best-effort acceptance prompt will be used？

## Pre-delivery validation checklist

Use this checklist before delivering a Skill or artifact. Do not reduce it to a hidden reference.

1. [ ] `scripts/validate_punct.py` passes for Chinese-facing Markdown, HTML, YAML, and text outputs.
2. [ ] Required structure exists：`SKILL.md`、`agents/openai.yaml`、needed `scripts/`、needed `references/`、needed `tests/`、`FROZEN.md` when frozen contracts exist、`LESSONS.md` when maintaining conventions.
3. [ ] `SKILL.md` frontmatter has only `name` and `description`, and the description contains real trigger conditions.
4. [ ] Frozen contracts are unchanged or intentionally versioned.
5. [ ] Regression tests pass under `tests/test_*.py`. For this Skill family, tests must pass through both `python -m pytest tests -q` and direct execution through `scripts/skill_gate.py --test-runner direct`.
6. [ ] Contract tests pass and preserve the exact GPT v1.6.1 named gate terms：`check_pages.py`、`check_math.py`、`verify_math.py`、`check_katex.py`、`verify_structures.py`、`measure_bands.py`.
7. [ ] Math outputs, if present, pass SymPy recomputation for every claimed answer.
8. [ ] KaTeX outputs, if present, have no leftover placeholder tokens, no unrendered `$$` or `\(`, and no `katex-error`.
9. [ ] Fixed-page outputs, if present, pass print-mode page overflow measurement. Overflow greater than 2px is blocked.
10. [ ] Domain structures, if present, validate before rendering. Examples：chemistry structures, reaction balancing, and label alignment.
11. [ ] Layout measurement, if present, satisfies the Skill-specific threshold, such as band width difference less than one card.
12. [ ] Dependencies are handled by bootstrap helpers when practical, and `ensure_*` happens before imports that need the dependency.
13. [ ] Bootstrap behavior is tested without real installation when applicable by intercepting `_pip` or `subprocess`.
14. [ ] Offline or print promises are honored with embedded assets, fonts, and print settings where relevant.
15. [ ] Multi-format deliverables are all created and linked, not only listed.
16. [ ] Fresh-context acceptance uses the main-file acceptance prompt template when possible, or is clearly labeled as best-effort when true isolation is unavailable.
17. [ ] Three-failure limit was respected.
18. [ ] The final delivery states actual checks run, checks not run, limitations, and gives the complete `skill.zip` when applicable.
19. [ ] The final response asks whether the user is satisfied.

## Maintenance protocol

### Changes allowed without prior user approval

These still require validation before delivery：add a new non-frozen skin、layout、preset、or registry entry；add a new lesson to `LESSONS.md`；add regression tests；fix typos or examples without changing semantics；improve wording without weakening rules；or add traceability entries that document an existing migration decision.

### Changes requiring user approval before editing

- Any value listed in `FROZEN.md`, any frozen registry、token、coordinate、schema、validator rule、or delivery contract.
- The detection logic of `scripts/validate_punct.py`, or any deletion or weakening of a validator or test assertion.
- Changing the meaning or order of the nine house rules, removing main-file triggers、checklists、standard validation layers、named validator patterns、multi-format rules、acceptance template、or maintenance protocol, or making any major-version semantic change.
- Replacing a GPT v1.6.1 or Joan v1.2 concrete hard gate with a generic phrase.

### LESSONS.md update format

After a validator catches a real issue, after a three-failure stop, or after the user identifies a migration flaw, append one concise lesson：

```markdown
## YYYY-MM-DD｜<一句話標題>
- 現象：<驗證器輸出的關鍵一行，或使用者指出的錯>
- 根因：<一句話>
- 對策：<改了哪個檔的哪條規則，或加了哪個測試>
- 已固化：<測試檔名或房規條號；寫「否」表示尚未固化，下次優先處理>
```

If a lesson can become a test, write the test. `LESSONS.md` is not a substitute for regression protection.

### Compaction rule

When `LESSONS.md` exceeds 30 entries, compact only lessons already marked as solidified. Keep unsolved or untested lessons visible. Before compaction, perform a fresh read-back check to avoid deleting unresolved problems.

### Installed Skill update rule

A mounted or installed Skill should be treated as read-only. To update it, produce a complete new package and ask the user to reinstall it. Do not claim that an already installed Web Skill has been modified in place.

## Delegation prompt rule

Any delegated task prompt must contain three fields：

- Acceptance criteria that can be checked.
- Fixed report format.
- Retry limit, defaulting to three rounds.

If any field is missing, the delegation prompt is incomplete.

## Delivery note template

Use this minimum delivery note：

```text
已完成：<一句話>
驗證：<列出實際跑過的檢查與結果>
限制：<未能完成、未能實跑、或未真正隔離驗收的項目>
下載：<skill.zip 或其他檔案連結>
是否滿意目前版本？
```

## Reference map

Load these files when the task needs deeper templates or supporting detail. They supplement this main file; they do not replace the visible rules above.

- `references/canonical-snippets.md`：copyable patterns for version stamps, frozen contracts, bootstrap, focus gates, capability boundaries, tests, and registries.
- `references/acceptance-checklists.md`：extended migration and validation checklists.
- `references/maintenance-protocol.md`：expanded maintenance rules.
- `references/migration-notes.md`：GPT to Codex semantic mapping and known limits.
- `references/migration-traceability.md`：GPT v1.6.1 to Codex v1.6.1 traceability matrix.
- `FROZEN.md`：frozen contract for this Codex migration.
- `LESSONS.md`：maintenance lessons and historical failures.

## Script map

Use these scripts through the execution environment when relevant：

- `scripts/validate_punct.py <file>`：check Chinese-facing text for halfwidth punctuation near CJK and banned dash punctuation.
- `scripts/sync_validator.py [--check] <skill-dir> ...`：copy or compare the canonical punctuation validator across sibling skill packages.
- `scripts/bootstrap.py`：provide idempotent dependency setup helpers for generated Skill scripts when heavy dependencies are needed.
- `scripts/convert_from_claude_skill.py <source-skill-dir> <output-dir>`：create a Codex-compatible Skill skeleton from a Claude-era Skill and report frontmatter、Claude-specific wording、environment-flag、and `agents/openai.yaml` issues for manual review.
- `scripts/skill_gate.py <skill-root> [--test-runner auto|pytest|direct]`：run structural checks, metadata checks, punctuation checks, contract-term checks, and regression tests for this skill.
- `tests/test_validate_punct.py`：pytest-compatible and directly executable regression tests for the punctuation validator、validator-sync behavior、metadata contract、bootstrap behavior、and conversion helper.
- `tests/test_skill_contract.py`：pytest-compatible and directly executable contract tests that prevent GPT v1.6.1 and Joan v1.2 hard gates from being abstracted again.

## Codex migration constraints

A Codex Skill can strongly instruct, bundle scripts, and require checks. It cannot by itself mutate an already installed skill in place or guarantee a truly fresh independent model session.

Normal use must remain single-skill and self-contained. Do not make an external validator CLI, local installation, GitHub Action, or separate application part of the required Codex Skill workflow. Mention those only as optional future infrastructure when the user explicitly asks for team-level automation, repository-level blocking, or non-bypassable CI.

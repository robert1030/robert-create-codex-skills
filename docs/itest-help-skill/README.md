# itest-help-skill Docs

This folder documents the `itest-help-skill` package for Spirent iTest Help 26.2.0.

## Files

- `SPEC.md`: the contract for the skill, source data, frozen values, and verification rules.
- `itest-help-skill-runbook.md`: Windows PowerShell build, validation, and packaging steps.
- `itest-help-skill-runbook.htm`: HTML version of the same runbook.

## Current Environment

These paths are examples from the current machine. Replace them on other computers.

- Workspace: `F:\MyCode\robert-create-codex-skills`
- Skill folder: `F:\MyCode\robert-create-codex-skills\skills\itest-help-skill`
- Package: `F:\MyCode\robert-create-codex-skills\dist\itest-help-skill.zip`
- Bundled extracted RAG inside skill: `references/rag`

## Contract Summary

The skill must search local iTest Help 26.2.0 RAG chunks first. It must cite `chunk_id` and `source_original_path` when answering from local help. If local search has no useful result, it must use external lookup when available and label those facts as `External source`.

Required trigger terms:

- `itest help`
- `itest gui`
- `itest tcl`
- `itest python`
- `itest analysis`

## Verification Summary

Run these checks from `F:\MyCode\robert-create-codex-skills\skills\itest-help-skill`:

```powershell
python -m py_compile ".\scripts\search_itest_help.py" ".\scripts\inspect_chunk.py" ".\scripts\validate_itest_help_skill.py"
python ".\scripts\validate_itest_help_skill.py"
python "C:\Users\robert\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .
```

Then run smoke searches for `itest help`, `itest gui`, `itest tcl`, `itest python`, and `itest analysis`.

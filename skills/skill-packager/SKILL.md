---
name: skill-packager
description: Package Codex skills into portable zip archives for local installation, GitHub skill-installer workflows, and manual migration. Use when users want to validate, export, share, back up, or move a Codex skill folder between Codex CLI and Codex Desktop environments.
---

# Skill Packager

Package Codex skill folders into distributable zip archives while preserving the standard skill directory layout.

Use this skill when the user wants to package a skill for:

- local personal installation into `$CODEX_HOME/skills` or `~/.codex/skills`
- installation from a GitHub folder path via `$skill-installer`
- portable zip migration between machines or Codex environments

## Packaging Workflow

1. Identify the source skill directory. It must contain `SKILL.md`.
2. Run `scripts/package_skill.py <path/to/skill-folder> <output-directory>`.
3. Confirm the output zip contains a top-level folder named after the skill.
4. Use the resulting zip for manual installation, or commit the source skill folder to GitHub for `$skill-installer` installation.

Example:

```bash
python3 scripts/package_skill.py skills/my-skill dist
```

Expected zip structure:

```text
my-skill.zip
└── my-skill/
    ├── SKILL.md
    ├── agents/
    ├── scripts/
    ├── references/
    └── assets/
```

The resource directories are optional. The packager includes whichever ones exist.

## Validation

The packager validates before writing the archive:

- `SKILL.md` must exist.
- YAML frontmatter must parse.
- `name` and `description` must exist and be strings.
- the directory name must match the skill `name`.
- the skill `name` must use lowercase letters, digits, and hyphens.

If validation fails, fix the reported issue before packaging.

## Installation Targets

For local personal installation, unzip the archive into the Codex user skills directory so the result is:

```text
~/.codex/skills/<skill-name>/SKILL.md
```

For `$skill-installer`, publish the unzipped skill folder in a GitHub repository and install from that folder path.

For zip migration, copy the generated zip to the target machine and extract it into that machine's Codex user skills directory.

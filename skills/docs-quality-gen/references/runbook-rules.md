# Runbook Rules

## Purpose

Use these rules when producing, updating, or reviewing runbook-style documents for robert's personal documentation workflow.

A runbook is an operation guide. A reader should be able to follow it step by step and know what each step is for, what command to run, what result to expect, and how to verify it.

## Core Rules

- Each step should include the purpose, command or action, expected output, and verification method when practical.
- A file name created in one step must not silently change in a later step. If it is renamed, say so clearly.
- If two paths or file names exist, explain when to use each one.
- Add plain-language warnings before commands that are easy to misuse.
- When copying folders, warn about nested-folder mistakes when relevant.
- When updating versions, remind the reader to re-check version-related guardrails.
- Mark paths, versions, and tool locations as examples or current-environment details when they are local facts.

## Flow Consistency

- Put prerequisites before the steps that need them.
- Keep step order complete and non-jumping.
- Keep file names, paths, and version numbers consistent from start to finish.
- Keep default output names and verification commands aligned.
- If there is a choice, such as whether to rename a zip, explain both cases.
- Keep shell syntax and path format consistent. For example, Windows PowerShell instructions should not suddenly use Linux shell syntax.

## Content Consistency

- Do not let one section contradict another.
- Do not say something is required in one place and optional elsewhere unless the condition is clear.
- Do not say one section excludes a file while another says the zip must include it.
- Do not turn an example into a universal rule.
- Do not write local-environment assumptions as facts that apply to every computer.
- If a document depends on local setup, prefer portable wording such as relative paths, variables, `<user>`, `<version>`, or `<actual-path>`, and add a replacement note.

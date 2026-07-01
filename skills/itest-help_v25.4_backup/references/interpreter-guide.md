# Interpreter Guide

Use this guide as a guardrail when answering questions about iTest interpreter commands, Tcl interpreter behavior, field replacements, and time/clock handling.

## Required Source Pages

Always inspect the relevant source pages before answering:

- `topics/command_syntax.htm`: iTest interpreter command table for Tcl test cases, including the iTest world vs Tcl world explanation.
- `topics/commands_itest_interpreter.htm`: overview of iTest interpreter commands and Python/Tcl syntax examples.
- `topics/action_run.htm`: `eval` action, which evaluates iTest interpreter statements.
- `topics/action_scripteval.htm`: `scriptEval` action, which evaluates Tcl commands.
- `topics/action_scriptset.htm`: `scriptSet`, used to pass values from iTest variables to a Tcl or selected interpreter.
- `topics/action_scriptget.htm`: `scriptGet`, used to pass values from Tcl or selected interpreter variables back to iTest variables.
- `topics/command_tcl.htm`: `tcl` command, which lets the iTest interpreter call the execution kernel Tcl interpreter.
- `topics/command_tclexpr.htm`: `tclexpr` command, which evaluates expressions in the execution kernel Tcl interpreter.
- `topics/commands_built_in_local_variables.htm`: Tcl interpreter local variables and thread-safety notes.

## Boundary Rules

- `eval`, `set`, `get`, `gset`, `gget`, `response`, `query`, and similar commands operate in the iTest interpreter unless the source page says otherwise.
- `scriptEval` operates in the Tcl world. Variables set there are separate from iTest interpreter variables.
- `scriptSet` and `scriptGet` are the bridge between the iTest world and Tcl world.
- `tcl` and `tclexpr` are iTest interpreter commands that call the execution kernel Tcl interpreter. Do not describe them as plain Tcl Shell session steps.
- Tcl Shell sessions are a separate session type. Do not conflate Tcl Shell session behavior with the execution kernel Tcl interpreter or iTest interpreter commands.

## Clock And Large Time Values

Required sources for `clock` questions:

- `topics/command_syntax.htm`
- `topics/popups/clock.html`
- `topics/command_tcl.htm` only if the user is explicitly asking about the `tcl` command or Tcl interpreter execution.

The packaged iTest 25.4 help does not mention `2038`, `32-bit`, clock overflow, or large post-2038 timestamp behavior. If a user asks about 2038 or large clock values, state that the indexed iTest 25.4 help does not document that limit. Do not infer Tcl runtime behavior or operating-system integer behavior unless the user supplies external evidence or asks for a separate non-iTest-help explanation.

When search output shows unmatched terms such as `2038`, treat that as a warning that the help does not directly answer the requested constraint.

### Observed iTest Clock Large-Date Risk

Local observed behavior, not an official help statement: in the iTest interpreter, a direct command such as:

```tcl
set expdate_seconds [clock scan {$exp_date}]
```

can work for near-term dates such as 2024-2026 but produce incorrect negative seconds for larger future dates such as 2041 or 2049. This has been observed in date-to-epoch conversion during certificate expiration-date handling, but the guardrail applies to time conversion and time arithmetic generally.

When a question involves converting a date/time string to seconds, epoch seconds, timestamp comparison, time arithmetic, clock scan/format, validity windows, certificate `notAfter`, expiry dates, expiration dates, 2038+, 2041, 2049, or other large future dates, do not recommend direct iTest interpreter `[clock scan ...]` as the only solution. First distinguish which interpreter is executing the command.

Preferred workaround to consider inside an iTest interpreter expression:

```tcl
set expdate_seconds [tcl "clock scan {$exp_date}"]
```

This uses the iTest interpreter `tcl` command to call the execution kernel Tcl interpreter. Explain that this is a project guardrail based on observed behavior; the packaged iTest 25.4 help documents the `clock` syntax and the `tcl` command, but it does not document the large-date failure itself.

If the user needs production-safe validation, recommend testing the exact target date range in their iTest runtime and handling failures explicitly. This applies to any workflow that converts, compares, adds, subtracts, or formats dates around or beyond 2038, not only certificate checks.

## High-Risk Answering Rules

- If the question names both iTest and Tcl, explicitly distinguish which interpreter each command runs in.
- If the question asks whether a Tcl command works in iTest, verify whether the help says the iTest command is compatible with its Tcl counterpart and check for listed limitations.
- If a command is described as compatible with Tcl, still report any iTest-specific limitations from `topics/command_syntax.htm`.
- For time conversion, epoch seconds, timestamp comparison, time arithmetic, clock scan/format, certificate expiration, validity, `notAfter`, or future-date questions, apply the observed clock large-date guardrail before giving code.
- For thread/asynchronous questions involving Tcl variables, check `topics/commands_built_in_local_variables.htm` and analysis-rule pages for not-thread-safe notes.

---
{
  "chunk_id": "prompts_4__preparing_for_missing_or_unknown_prompts_b8ee717cc52100db",
  "source_file": "topics/prompts.4.htm",
  "source_original_path": "topics/prompts.4.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "Preparing for missing or unknown prompts during automated execution: Completion properties"
  ],
  "heading_path": [
    "Preparing for missing or unknown prompts during automated execution: Completion properties",
    "Preparing for missing or unknown prompts during automated execution: Completion properties"
  ],
  "anchor": "1273954",
  "context_ids": [],
  "index_keywords": [
    "Completion",
    "Completion property settings",
    "missing",
    "missing prompts"
  ],
  "index_keyword_paths": [
    "Completion property settings",
    "missing prompts",
    "prompts > missing",
    "properties > Completion"
  ],
  "related_links": [
    "session_profile_properties_cmd.htm#1362938",
    "session_profile_properties_serial.htm#1175900",
    "sp_properties_ssh.htm#1260667",
    "session_profile_properties_telnet.htm#1147390",
    "tl1.1.htm#1152885"
  ],
  "images": [],
  "content_hash": "b8ee717cc52100db",
  "level": 1
}
---

# Preparing for missing or unknown prompts during automated execution: Completion properties > Preparing for missing or unknown prompts during automated execution: Completion properties

You use Completion property settings to define when the execution of a step should be considered complete. Defining “completion” for a step is important because:

- Some steps cannot start until the preceding step is complete.

- A step may include an analysis rule that examines the response to determine whether the step succeeded. Analysis of the response can begin only when the step is complete.

The determination of when a step is complete is protocol-specific and is controlled by the settings of the Completion properties (described in a moment).

> **Note:** Note In addition, all protocols support the notion of a timeout on a step. If the timeout is exceeded, then the step terminates and execution continues even if the protocol thinks that the work is not yet done. Other than the timeout case, it is up to the protocol to determine when the step is complete.

For CLI protocols, you can specify any of several conditions to define when the step is complete, for example the existence of certain text in the response or the time elapsed after sending the command. The default Completion criteria property setting is that the step is complete when:

The session channel is idle for the time specified by the Idle channel interval property

and

1. The last line of the response matches one of the prompt definitions specified for the session profile or device.

To configure session profile properties that specify how to interact with the user when delays occur, see the Completion property settings:

- Command Prompt sessions: Terminal > Replay > Step Defaults > Completion

- Serial sessions: Terminal > Replay > Step Defaults > Completion

- SSH sessions: Terminal > Replay > Step Defaults > Completion

- Telnet sessions: Terminal > Replay > Step Defaults > Completion

- TL1 sessions: Configuring sessions and test case steps for TL1 devices

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

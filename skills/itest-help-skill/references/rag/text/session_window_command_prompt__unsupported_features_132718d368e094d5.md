---
{
  "chunk_id": "session_window_command_prompt__unsupported_features_132718d368e094d5",
  "source_file": "topics/session_window_command_prompt.htm",
  "source_original_path": "topics/session_window_command_prompt.htm",
  "toc_path": [
    "iTest Online Help",
    "Command Prompt sessions",
    "Command Prompt session window (Microsoft Windows Command Prompt)"
  ],
  "heading_path": [
    "Command Prompt session window (Microsoft Windows Command Prompt)",
    "Command Prompt session window (Microsoft Windows Command Prompt)",
    "Unsupported features"
  ],
  "anchor": "1394618",
  "context_ids": [
    "session_window_command_prompt"
  ],
  "index_keywords": [
    "Command Prompt sessions",
    "Microsoft Windows cmd",
    "Windows cmd",
    "Windows command-line session window",
    "cmd session window",
    "session window"
  ],
  "index_keyword_paths": [
    "Command Prompt sessions > Microsoft Windows cmd",
    "Command Prompt sessions > session window",
    "Microsoft Windows Command Prompt > session window",
    "Windows command-line session window",
    "cmd session window",
    "command-line session window > Windows cmd",
    "session windows > Command Prompt sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "132718d368e094d5",
  "level": 2
}
---

# Command Prompt session window (Microsoft Windows Command Prompt) > Command Prompt session window (Microsoft Windows Command Prompt) > Unsupported features

> **Note:** Note Interactive commands are not supported. For example, Start-Service, Stop-Service, Restart-Service, etc., actions that read from console are not supported.

iTest starts a Command Prompt process and controls it though standard in and standard out. Therefore, the following Command Prompt features are not supported:

- Tab completion

- ‘More’ page continuation (iTest responds to both multi-screen responses and piping results to more with a single page of contiguous output.)

- Applications launched from within Command Prompt that attempt to take over the Command Prompt window (for example, Telnet)

> **Note:** Note Running GUI applications directly from the Command Prompt session window (for example, by typing notepad) may result in a significant delay in displaying the GUI window. To avoid the delay, use the start command to launch other applications from the Command Prompt session (especially GUI applications). For example, to start Notepad, type:>start notepad.exe

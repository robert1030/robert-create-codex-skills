---
{
  "chunk_id": "capture_command_concept__commands_995ee69cd0e522a2",
  "source_file": "topics/capture_command_concept.htm",
  "source_original_path": "topics/capture_command_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Capturing Manual (Interactive) Sessions",
    "Overview: Creating a test case by capturing interactive sessions",
    "Commands"
  ],
  "heading_path": [
    "Commands",
    "Commands"
  ],
  "anchor": "1195288",
  "context_ids": [
    "capture_command_concept"
  ],
  "index_keywords": [
    "CLI commands",
    "defined"
  ],
  "index_keyword_paths": [
    "CLI commands",
    "CLI sessions > defined",
    "commands > defined",
    "terminal-based sessions > defined"
  ],
  "related_links": [
    "commands_itest_interpreter.htm#"
  ],
  "images": [],
  "content_hash": "995ee69cd0e522a2",
  "level": 1
}
---

# Commands > Commands

> **Note:** Note This section provides a quick overview of commands from the perspective of capturing interactive sessions. For a full discussion, see “iTest Commands”.

CLI sessions (command-line interface) are the terminal-based sessions; any session where you type commands at a prompt in a command line. iTest supports the following CLI terminal-based session types:

Command Prompt

HTTP

Process

SSH

Syslog

Tcl Shell

Telnet

Many Traffic generator device session types

Wireshark

As you perform interactive tests in CLI sessions, iTest captures the command and the response. When you save the steps into a test case, the Action type for the saved steps is command.

Non-CLI sessions use a different kind of command, as described in “Web sessions (Obsolete and Deprecated)” and “Swing Sessions (Deprecated)”.

Let's compare how you work with commands while capturing a session and while editing a test case:

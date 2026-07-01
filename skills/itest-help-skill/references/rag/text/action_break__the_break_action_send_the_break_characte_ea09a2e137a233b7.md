---
{
  "chunk_id": "action_break__the_break_action_send_the_break_characte_ea09a2e137a233b7",
  "source_file": "topics/action_break.htm",
  "source_original_path": "topics/action_break.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The break action: Send the break character"
  ],
  "heading_path": [
    "The break action: Send the break character",
    "The break action: Send the break character"
  ],
  "anchor": "1592856",
  "context_ids": [
    "action_break"
  ],
  "index_keywords": [
    "break",
    "break action",
    "break in CLI sessions",
    "causing in CLI session",
    "causing in CLI sessions"
  ],
  "index_keyword_paths": [
    "Ctrl-C > causing in CLI session",
    "Ctrl-C > causing in CLI sessions",
    "actions > break",
    "actions > break in CLI sessions",
    "break > causing in CLI session",
    "break action",
    "break action > causing in CLI session"
  ],
  "related_links": [
    "action_break_loop.htm#1532697"
  ],
  "images": [
    "topics/images/actions_4.1.jpg",
    "topics/images/break_cli_sesion_telnet.png"
  ],
  "content_hash": "ea09a2e137a233b7",
  "level": 1
}
---

# The break action: Send the break character > The break action: Send the break character

There are two distinct kinds of break action:

1. Break CLI session execution: The break that appears in the first group of actions appears in the list only for CLI sessions. For example, in a Telnet session, a break action stops the currently executing command immediately and execution then continues with the next step. The command sends the break character specified in the Description cell. Because many devices use Ctrl-C as the break character, the default is [char Ctrl-C].

In order to send a telnet break (BRK) command, decimal 243, specify fff3 as the command and enable the Send command as a HEX (Step Propertes > Telnet break Properties > Command). See the example below.

1. 2

1. Break out of a for, forEach (Tcl only), or while loop: See The ‘break’ action: Break out of a loop.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/actions_4.1.jpg) <!-- image_chunk: img_f4032ebef4d21259 -->

![screenshot](topics/images/break_cli_sesion_telnet.png) <!-- image_chunk: img_4caa5563d7a639ff -->

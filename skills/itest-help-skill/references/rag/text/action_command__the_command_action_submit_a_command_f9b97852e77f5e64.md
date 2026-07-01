---
{
  "chunk_id": "action_command__the_command_action_submit_a_command_f9b97852e77f5e64",
  "source_file": "topics/action_command.htm",
  "source_original_path": "topics/action_command.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The command action: Submit a command"
  ],
  "heading_path": [
    "The command action: Submit a command",
    "The command action: Submit a command"
  ],
  "anchor": "1592843",
  "context_ids": [
    "action_command"
  ],
  "index_keywords": [
    "command",
    "command action",
    "in test cases"
  ],
  "index_keyword_paths": [
    "actions > command",
    "command action",
    "commands > in test cases"
  ],
  "related_links": [],
  "images": [
    "topics/images/actions_3.1.jpg"
  ],
  "content_hash": "f9b97852e77f5e64",
  "level": 1
}
---

# The command action: Submit a command > The command action: Submit a command

The command action is available only for CLI sessions and submits the text that appears in the Description cell (the value of the Command property). command is the most commonly used action in CLI test cases.

> **Note:** Note By default, iTest sends a carriage return + linefeed sequence when the Command cell is blank, so there is no need to include [char \r\n] in the Command or Description cell for blank commands.

In the example, step 2 submits the show ip traffic command to the 3750telnet session.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/actions_3.1.jpg) <!-- image_chunk: img_0f1b837d8d7c77b5 -->

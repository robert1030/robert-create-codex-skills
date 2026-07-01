---
{
  "chunk_id": "ha_test_cases_6__ensuring_that_a_command_is_sent_to_the_i_136714cee349e087",
  "source_file": "topics/ha_test_cases.6.htm",
  "source_original_path": "topics/ha_test_cases.6.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Ensuring that a command is sent to the intended recipient"
  ],
  "heading_path": [
    "Ensuring that a command is sent to the intended recipient",
    "Ensuring that a command is sent to the intended recipient"
  ],
  "anchor": "1134756",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "136714cee349e087",
  "level": 1
}
---

# Ensuring that a command is sent to the intended recipient > Ensuring that a command is sent to the intended recipient

For command or getstate steps that are intended for a particular node (as specified by the Send to property value), you can specify that, before the command is sent, iTest first definitely determines the master/slave/other states of the nodes by checking the Verify status property.

iTest achieves this by sending an empty command that causes each node to return a prompt, thus indicating its state. As a result, you can be sure that the command will be sent to the recipient that you specified using the Send to property.

- This feature does not apply to break steps.

- Normal step Timing property settings apply for the empty commands.

- The empty commands do not appear in the Execution view or in test reports.

- The structured data includes the state of each node and the most recent prompt returned by the node.

- The Prompt data element contains the prompt returned in response to the actual command sent to the appropriate node.

- If there are multiple valid recipients (for example the Send to property value is Slave and multiple nodes return slave prompts) then the command is sent to the node with the lowest index value.



To ensure that a command is sent to the appropriate node:

1. 1

1. Select the HA step (the action is one of the following: command, break, getstate, setmaster, or setslave).

1. 2

1. In the Step Properties section, select the Telnet <action name> Properties node in the tree (for example, Telnet setmaster Properties).

1. 3

1. On the HighAvailability page, check the Verify status checkbox.

> **Tip:** Tip If Verify status is not checked, then the command is sent to the last node that returned a master prompt. You can use the setmaster action to explicitly set the master (until the next setmaster or the next step where Verify status is checked).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

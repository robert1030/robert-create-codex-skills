---
{
  "chunk_id": "ha_test_cases_2__step_3_create_the_test_case_df82933c46676189",
  "source_file": "topics/ha_test_cases.2.htm",
  "source_original_path": "topics/ha_test_cases.2.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Testing HA devices: Detailed instructions"
  ],
  "heading_path": [
    "Testing HA devices: Detailed instructions",
    "Testing HA devices: Detailed instructions",
    "Step 3: Create the test case"
  ],
  "anchor": "1110728",
  "context_ids": [],
  "index_keywords": [
    "Additional connection information property",
    "Close action",
    "HA indication property",
    "HA mode",
    "HA prompts",
    "HA sessions",
    "HA test cases",
    "High Availability Mode property",
    "High Availability indication property",
    "Open action",
    "Verify State property",
    "creating",
    "defining",
    "prompt property setting"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA devices > Close action",
    "HA devices > Open action",
    "HA indication property",
    "HA master > defining",
    "HA mode",
    "HA prompts",
    "HA slave > defining",
    "HA test cases > creating",
    "High Availability Mode property",
    "High Availability indication property",
    "Master > prompt property setting",
    "Other > prompt property setting",
    "Slave > prompt property setting",
    "Verify State property",
    "creating > HA test cases",
    "prompts > HA sessions"
  ],
  "related_links": [
    "#1163813",
    "ha_test_cases.4.htm#1105022",
    "ha_test_cases.3.htm#1115821",
    "ha_test_cases.5.htm#1109354"
  ],
  "images": [],
  "content_hash": "df82933c46676189",
  "level": 2
}
---

# Testing HA devices: Detailed instructions > Testing HA devices: Detailed instructions > Step 3: Create the test case

iTest does not capture HA sessions, so you create test cases by manually adding steps in the Test Case editor.

The process of creating an HA test case is nearly identical to the normal process for non‑HA devices. Once you configure the properties as described in “Step 2: Define the HA prompts”, iTest sends all commands to the specified device (the master by default). For any step that should submit its command to another node, you specify the node in a property for the step.

Follow this procedure:

1. In the Test Case editor, add an open step that refers to the HA testbed device or session profile in the Description cell.

> **Note:** Note The open action for an HA session differs from the normal open action — it opens a connection with each HA node that is specified in the testbed device or session profile. As a result, you need only one open step to connect to all nodes.iTest keeps all connections open as long as they stay open or until a close step is executed for the HA session. If one of the connections is closed by the server during the test, then subsequent steps operate only on the remaining connections.

1. 2

1. If you must log in to each node to begin testing:

- SSH: The login process happens automatically. (For this reason, it is easier to implement SSH than Telnet.)

- Telnet: you will send the login commands to each node separately. See Logging in separately to each HA node for instructions.

1. 3

1. Add steps as needed. See HA command reference. By default, all commands are set to the master. If needed, see Sending a command to a particular HA node.

1. 4

1. Add a single close step to close all connections.

> **Note:** Note The close action for an HA session also differs from the normal close action — it closes all connections to nodes for the HA session.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

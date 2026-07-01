---
{
  "chunk_id": "ha_test_cases_2__step_2_define_the_ha_prompts_615377852d2a5ed6",
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
    "Step 2: Define the HA prompts"
  ],
  "anchor": "1163813",
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
    "prompts.5.htm#1272830"
  ],
  "images": [
    "topics/images/ha_test_cases.2.jpg"
  ],
  "content_hash": "615377852d2a5ed6",
  "level": 2
}
---

# Testing HA devices: Detailed instructions > Testing HA devices: Detailed instructions > Step 2: Define the HA prompts

During default HA operation, iTest determines mastership automatically by sending empty commands and using prompts to determine which node is master, which are slave, and which are “other”. (The empty steps do not appear in the Execution view or in test reports.)

you will now define the prompts that identify the various HA nodes.

1. Open the Prompts page. Click Terminal > Prompts.

1. 2

1. To enable you to add prompt definitions, check Include additional values from list.

1. 3

1. Click and then specify the prompt properties as usual. (See Editing prompt definitions.)

1. 4

1. For the High Availability indication property, specify the type of node that you are defining the prompt for. (The default value, Normal, indicates a normal, non‑HA prompt.)

The setting determines what the prompt indicates about the node that returned it:

- Master: The node that returned the prompt is an HA master node

- Slave: The node that returned the prompt is an HA slave node

- Other: The node that returned the prompt is neither master nor slave

> **Note:** Note Typically, mastership is determined after login completes for all nodes. For this reason, you should associate Master/Slave/Other status with prompts that do not appear as login or password prompts.

During execution, when a step is attempting to determine the master/slave/other state of the nodes, iTest compares the returned prompt to each configured prompt in order. The state is assigned based on the first match.

- If there is a match with a prompt for which High Availability indication=Master, then the node is considered a master.

- If there is a match with a prompt for which High Availability indication=Slave, then the node is considered a slave.

- If there is no match, then the node is considered Other (neither a master nor slave).

![inline_icon](topics/images/ha_test_cases.2.jpg) <!-- image_chunk: img_f0d68b0b7d20236c -->

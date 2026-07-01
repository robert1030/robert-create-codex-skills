---
{
  "chunk_id": "ha_test_cases_5__sending_a_command_to_a_particular_ha_nod_a96b13ada7b782e3",
  "source_file": "topics/ha_test_cases.5.htm",
  "source_original_path": "topics/ha_test_cases.5.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Sending a command to a particular HA node"
  ],
  "heading_path": [
    "Sending a command to a particular HA node",
    "Sending a command to a particular HA node"
  ],
  "anchor": "1109354",
  "context_ids": [],
  "index_keywords": [
    "HA sessions"
  ],
  "index_keyword_paths": [
    "setmaster action > HA sessions",
    "setslave action > HA sessions"
  ],
  "related_links": [
    "ha_test_cases.8.htm#1166565",
    "ha_test_cases.7.htm#1111490"
  ],
  "images": [],
  "content_hash": "a96b13ada7b782e3",
  "level": 1
}
---

# Sending a command to a particular HA node > Sending a command to a particular HA node

Follow this procedure to create a setmaster or setslave step (described in Specifying that a particular node should be master (or slave)) or to send a command or break to a particular node (for example, when logging in):

1. Specify a value for the Send to property:

- Master: (default) Send the command to the master node (based on the prompt or as set by a preceding setmaster step).

- Slave: Send the command to the first node (in index order) that is not Master and not Other.

- Specific: This setting is typically used to log in to a particular node and to test HA redundancy operation. Specify the particular node to which the command should be sent using the Send to index property.

1. 2

1. Specify the node by setting a value for the Send to index property: Type the index value of the intended recipient of the command. See Specifying a node by index for instructions on determining the appropriate index.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

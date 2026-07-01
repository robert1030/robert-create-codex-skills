---
{
  "chunk_id": "ha_test_cases_9__viewing_the_current_states_of_all_nodes_b11fc8bd1db5f283",
  "source_file": "topics/ha_test_cases.9.htm",
  "source_original_path": "topics/ha_test_cases.9.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Viewing the current states of all nodes"
  ],
  "heading_path": [
    "Viewing the current states of all nodes",
    "Viewing the current states of all nodes"
  ],
  "anchor": "1107206",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "b11fc8bd1db5f283",
  "level": 1
}
---

# Viewing the current states of all nodes > Viewing the current states of all nodes

A getstate step returns an XML table with the current master/slave and index number states of all nodes.

The return data depends on the setting of the Verify status property.

- If Verify status is checked (default), then iTest refreshes state information by sending state verification commands to the nodes before it polls for responses to the getstate step.

- If Verify status is unchecked for the step, then getstate returns the current states.



To set the ‘Verify status’ property

1. Select the getstate step.

1. 2

1. In the Step Properties section, select the Telnet getstate Properties node in the tree.

1. 3

1. The Verify status checkbox appears on the HighAvailability page.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

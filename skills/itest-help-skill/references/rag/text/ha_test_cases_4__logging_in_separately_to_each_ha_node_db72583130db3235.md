---
{
  "chunk_id": "ha_test_cases_4__logging_in_separately_to_each_ha_node_db72583130db3235",
  "source_file": "topics/ha_test_cases.4.htm",
  "source_original_path": "topics/ha_test_cases.4.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Logging in separately to each HA node"
  ],
  "heading_path": [
    "Logging in separately to each HA node",
    "Logging in separately to each HA node"
  ],
  "anchor": "1105022",
  "context_ids": [],
  "index_keywords": [
    "logging in"
  ],
  "index_keyword_paths": [
    "HA devices > logging in"
  ],
  "related_links": [
    "ha_test_cases.5.htm#1109354"
  ],
  "images": [],
  "content_hash": "db72583130db3235",
  "level": 1
}
---

# Logging in separately to each HA node > Logging in separately to each HA node

If the device requires you to log in separately to each node, then you will define a set of steps for each node by setting the Send To property for the steps appropriately.



To log in to each node separately (SSH):

You do not need to create login steps because iTest logs in for you using the SSH credentials that you specified in the testbed document.



To log in to each node separately (Telnet to terminal server):

You do not need to create login steps because the terminal server is typically logged in permanently.



To log in to each node separately (Telnet to the device):

1. Create a normal login sequence for each node (typically one command step that sends the login ID and a second command step that sends the password).

1. 2

1. For each step, set the Send to property to Specific and set the Send to index property to the node’s index value. See Sending a command to a particular HA node.

> **Tip:** Tip Once you have developed the steps that log in, use them as the basis for a login procedure that any test case can call. The procedure should include a single open step and then steps that log in to each node in succession.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

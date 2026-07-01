---
{
  "chunk_id": "ha_test_cases_1__testing_ha_devices_overview_717c3ea22a32a3a1",
  "source_file": "topics/ha_test_cases.1.htm",
  "source_original_path": "topics/ha_test_cases.1.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Testing HA devices: Overview"
  ],
  "heading_path": [
    "Testing HA devices: Overview",
    "Testing HA devices: Overview"
  ],
  "anchor": "1141893",
  "context_ids": [],
  "index_keywords": [
    "overview",
    "testing",
    "testing overview"
  ],
  "index_keyword_paths": [
    "HA devices > testing",
    "HA sessions > overview",
    "high-availability devices > testing",
    "high-availability devices > testing overview"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "717c3ea22a32a3a1",
  "level": 1
}
---

# Testing HA devices: Overview > Testing HA devices: Overview

HA devices are special in that any number of redundant processors (nodes) can perform system operations (that is, act as the master). Without special features, HA test cases would be quite complicated:

- The test case would have to start a session with each node.

- You would have to create logic that somehow determined which node is currently master, and then the test case would send the appropriate commands to session with the master.

- If mastership moves to another node, the test case would have to somehow detect the hand-off and redirect the commands appropriately.

Happily, you can skip all this because iTest enables you to test HA devices in a simple, intuitive way.

Important iTest does not capture HA sessions.

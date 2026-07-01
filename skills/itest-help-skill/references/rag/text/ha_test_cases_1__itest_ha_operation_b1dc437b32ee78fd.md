---
{
  "chunk_id": "ha_test_cases_1__itest_ha_operation_b1dc437b32ee78fd",
  "source_file": "topics/ha_test_cases.1.htm",
  "source_original_path": "topics/ha_test_cases.1.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Testing HA devices: Overview"
  ],
  "heading_path": [
    "Testing HA devices: Overview",
    "Testing HA devices: Overview",
    "iTest HA Operation"
  ],
  "anchor": "1132229",
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
  "content_hash": "b1dc437b32ee78fd",
  "level": 2
}
---

# Testing HA devices: Overview > Testing HA devices: Overview > iTest HA Operation

- iTest’s HA feature treats the HA device (with multiple redundant nodes) as a single virtual device — iTest takes care of directing commands to the appropriate node.

- HA supports multiple connections inside a single session (either Telnet or SSH) connected to nodes via Telnet/SSH sockets to different IP addresses and/or port numbers. One HA session window appears for each connection.

- By default, iTest determines master/slave/other state based on the prompts returned to commands (you specify the master/slave/other prompts in the session profile or testbed device).

- In the most common situations, test cases send commands to the master. You can override the session’s default HA behavior by setting a property for any step to direct commands to a slave node or to a specified node.

- Responses from the master node appear in the Response view and responses from other nodes appear in the structured data in the Structure view

- You can configure what should happen when an intended recipient (be it master, slave, or other) cannot be found, including an option to poll waiting for a recipient to be identified.

- You can use setmaster and setslave actions to explicitly set master/slave status.

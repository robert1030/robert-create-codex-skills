---
{
  "chunk_id": "ha_test_cases_1__testing_ha_devices_caa91daebac320a9",
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
    "Testing HA devices"
  ],
  "anchor": "1141883",
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
  "content_hash": "caa91daebac320a9",
  "level": 2
}
---

# Testing HA devices: Overview > Testing HA devices: Overview > Testing HA devices

Step 1:

You prepare to test an HA device by setting a few HA properties for the SSH or Telnet session. In the Testbed editor or the Session Profile editor, enable HA operation by configuring the properties of the HA device.

Step 2:

Specify the prompt that you expect the master node to return that identifies it as the master. Do the same for the slave (and “other”) nodes.

Step 3:

Now create the test case.

- A single open step opens connections with all nodes. If needed, you can add a login step for each node. For additional portability, you can parameterize the credential values (typically, username/password).

- By default, commands are directed to the master. If needed, you can direct particular commands to particular nodes.

- If needed, you can override any HA property setting for any step.

- A single close step closes connections with all nodes.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

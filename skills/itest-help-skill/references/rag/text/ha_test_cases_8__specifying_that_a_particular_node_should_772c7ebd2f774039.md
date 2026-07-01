---
{
  "chunk_id": "ha_test_cases_8__specifying_that_a_particular_node_should_772c7ebd2f774039",
  "source_file": "topics/ha_test_cases.8.htm",
  "source_original_path": "topics/ha_test_cases.8.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing High‑Availability (HA) Devices",
    "Specifying that a particular node should be master (or slave)"
  ],
  "heading_path": [
    "Specifying that a particular node should be master (or slave)",
    "Specifying that a particular node should be master (or slave)"
  ],
  "anchor": "1166565",
  "context_ids": [],
  "index_keywords": [
    "HA sessions",
    "SetSlave action"
  ],
  "index_keyword_paths": [
    "SetSlave action",
    "setmaster action > HA sessions"
  ],
  "related_links": [
    "ha_test_cases.7.htm#1111490"
  ],
  "images": [],
  "content_hash": "772c7ebd2f774039",
  "level": 1
}
---

# Specifying that a particular node should be master (or slave) > Specifying that a particular node should be master (or slave)

During default HA operation, iTest determines mastership automatically by sending empty commands and using prompts to determine which is master. In the case that you cannot distinguish master/slave using the prompts, you might want to specify that a particular node should be master.

you will use the setmaster action to explicitly set a particular node to master (and setslave to set a slave). As a result, the master node becomes the intended recipient for all steps for which the Send to property is set to Master. Steps with the Send to property set to Slave are sent to the first node (in index order) that is not master.



To specify which node should be master (or slave)

1. Create a step and select setmaster (or setslave) in the Action cell.

1. 2

1. In the Description cell, type the index number that identifies the node that you want to set to master (or to slave). See Specifying a node by index.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

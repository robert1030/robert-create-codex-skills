---
{
  "chunk_id": "listtraps__intro_f2110d637c852c53",
  "source_file": "topics/popups/listtraps.html",
  "source_original_path": "topics/popups/listtraps.html",
  "toc_path": null,
  "heading_path": [
    "listtraps.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/snmp_test_cases.html"
  ],
  "images": [],
  "content_hash": "f2110d637c852c53",
  "level": 0
}
---

# listtraps.html

Lists all traps that have been received since executing the first SNMP step or previous ListTraps calls.

ListTraps steps do not send commands to the device.

Depending on the Clear Traps After List property setting in the session profile, the system either leaves the queue unchanged or clears it after ListTraps steps.

The response body contains an XML document listing the following elements for each trap:

- Timestamp
- Trap objects

For details, see the online help: Creating SNMP test case steps.

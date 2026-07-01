---
{
  "chunk_id": "getnext__intro_db553a064dff3d8c",
  "source_file": "popups/getnext.html",
  "source_original_path": "popups/getnext.html",
  "toc_path": null,
  "heading_path": [
    "getnext.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/snmp_test_cases.html"
  ],
  "images": [],
  "content_hash": "db553a064dff3d8c",
  "level": 0
}
---

# getnext.html

Returns the value of the single MIB variable that follows the specified OID. The system uses the Get PDU to get values for scalar MIBs.

The structured data includes the OID value and iTest generates queries for OID and RAW_OID.

Tip: To use getNext in a loop for returning multiple values, the device's agent must implement a variable (the �next� variable) for loop control. If you intend to get values for all variables in a MIB, use walk instead.

For details, see the online help: Creating SNMP test case steps.

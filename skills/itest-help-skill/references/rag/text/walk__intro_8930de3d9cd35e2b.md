---
{
  "chunk_id": "walk__intro_8930de3d9cd35e2b",
  "source_file": "topics/popups/walk.html",
  "source_original_path": "topics/popups/walk.html",
  "toc_path": null,
  "heading_path": [
    "walk.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/snmp_test_cases.html"
  ],
  "images": [],
  "content_hash": "8930de3d9cd35e2b",
  "level": 0
}
---

# walk.html

Returns all of the data in a MIB under a specified root.

For V2c or V3, when use GETBULK is enabled, the system uses the GetBulk PDU to get values for container nodes.

For V1 or when use GETBULK is disabled, the system uses the Get PDU for each OID.

Tip: To enable tests to exit infinite loops caused by self-referencing OIDs and OIDs that incorrectly duplicate OIDs that appear earlier in the MIB, consider setting the Stop on cycle property for the session.

For details, see the online help: Creating SNMP test case steps.

---
{
  "chunk_id": "tgen_cmds_testcenter__to_generate_a_port_list_for_a_large_numb_3cbf212b33a428f8",
  "source_file": "topics/tgen_cmds_testcenter.html",
  "source_original_path": "topics/tgen_cmds_testcenter.html",
  "toc_path": null,
  "heading_path": [
    "Spirent TestCenter Command reference",
    "Spirent TestCenter Command reference",
    "To generate a port list for a large number of ports"
  ],
  "anchor": "1335329",
  "context_ids": [
    "tgen_cmds_testcenter"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "3cbf212b33a428f8",
  "level": 2
}
---

# Spirent TestCenter Command reference > Spirent TestCenter Command reference > To generate a port list for a large number of ports

Use iTest to generate a list with a large number of ports. For example:

- A loop can crawl the available chassis and build a list of the first n available ports, where n is the number of ports needed.

- Velocity can provide a list of ports.

- The topology associated with the test case contains port information. You can extract the information to build a port list.

- Store available port information in a file. A test case can read the file and build a port list.

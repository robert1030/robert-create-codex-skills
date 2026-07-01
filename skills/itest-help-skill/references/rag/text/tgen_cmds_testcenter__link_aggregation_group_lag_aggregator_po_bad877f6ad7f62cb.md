---
{
  "chunk_id": "tgen_cmds_testcenter__link_aggregation_group_lag_aggregator_po_bad877f6ad7f62cb",
  "source_file": "topics/tgen_cmds_testcenter.html",
  "source_original_path": "topics/tgen_cmds_testcenter.html",
  "toc_path": null,
  "heading_path": [
    "Spirent TestCenter Command reference",
    "Spirent TestCenter Command reference",
    "Link aggregation group (LAG) aggregator port"
  ],
  "anchor": "1394905",
  "context_ids": [
    "tgen_cmds_testcenter"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "bad877f6ad7f62cb",
  "level": 2
}
---

# Spirent TestCenter Command reference > Spirent TestCenter Command reference > Link aggregation group (LAG) aggregator port

Spirent TestCenter allows you to aggregate several physical ports into a link aggregation group (LAG) aggregator port. A LAG port is used much like a physical port. You can configure devices, protocols, and traffic on a LAG port as you would on a physical port. Traffic is sent and received across the ports in the LAG. Capture and traffic analysis is performed at the LAG level on a LAG port.

> **Note:** Note You can set up a link aggregation group (LAG) Offline or while you are connected to a chassis. If a LAG is set up Offline, it is validated when it is brought Online.

LAG support requires ports to be in the same port group. Port Group information is available during Port reservation, Port Relocation/Mapping and Equipment Information.

The Port Group tab (in STC Window) lists all of the port groups in the corresponding chassis and test modules.

> **Note:** Note In iTest, you can load the configuration file with the LAG information and substitute fields as required.

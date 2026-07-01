---
{
  "chunk_id": "spirent_avalanche_12__examples_of_invalid_port_organization_91e3b447f092bddc",
  "source_file": "topics/spirent_avalanche.12.htm",
  "source_original_path": "topics/spirent_avalanche.12.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Specifying cards, slots, port groups, and ports/virtual ports"
  ],
  "heading_path": [
    "Specifying cards, slots, port groups, and ports/virtual ports",
    "Specifying cards, slots, port groups, and ports/virtual ports",
    "Examples of invalid port organization"
  ],
  "anchor": "1289853",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "91e3b447f092bddc",
  "level": 3
}
---

# Specifying cards, slots, port groups, and ports/virtual ports > Specifying cards, slots, port groups, and ports/virtual ports > Examples of invalid port organization

- Using one or more port groups for both Client and Server Cluster Unit, for example:

- Server Cluster Units: 2,1;0 2,3;0 and Client Cluster Units: 2,2;0 2,1;0 (STC)

- Server Cluster Units: 2 3 and Client Cluster Units: 1 3 (Appliance)

- Port provision List not belonging to Server or Client Cluster Unit:

Server Cluster Units: 2,1;0 and Client Cluster Units: 2,2;0

Port Provision List:

- Port 1: Card 2, Port 1 -> group 1 belongs to Server Cluster Units

- Port 2: Card 1, Port 2: invalid, not belong to both Server and Client Units

- Number of usable ports not equal to number of ports in config.tcl file.

In config.tcl file: Ports {10.47.73.51/2/1 10.47.73.51/2/3} (2 ports)

However, in Port Provision List (Server Cluster Units: 2,1;0 and Client Cluster Units: 2,2;0):

- Port 1: Card 2 port 1

- Port 2: Card 1 port 2 -> Unusable

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

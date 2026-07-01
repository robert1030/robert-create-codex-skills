---
{
  "chunk_id": "topologies_12__create_and_edit_velocity_topology_in_the_5f2343e14f093d2a",
  "source_file": "topics/topologies.12.htm",
  "source_original_path": "topics/topologies.12.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Working with Velocity",
    "Create and edit Velocity topology in the integrated Topology Editor"
  ],
  "heading_path": [
    "Create and edit Velocity topology in the integrated Topology Editor",
    "Create and edit Velocity topology in the integrated Topology Editor"
  ],
  "anchor": "1516816",
  "context_ids": [],
  "index_keywords": [
    "topo_velocity_Create_edit_Velocity_topology_iTestWeb_Topology_Editor"
  ],
  "index_keyword_paths": [
    "topo_velocity_Create_edit_Velocity_topology_iTestWeb_Topology_Editor"
  ],
  "related_links": [
    "topologies.09.htm#1375873"
  ],
  "images": [],
  "content_hash": "5f2343e14f093d2a",
  "level": 1
}
---

# Create and edit Velocity topology in the integrated Topology Editor > Create and edit Velocity topology in the integrated Topology Editor

> **Note:** Note This topic assumes that you are familiar with the Velocity.

Ensure that you are connected to the relevant Velocity VM populated with required resources and topologies to which you have access. See Connect to Velocity server.

> **Note:** Note Embedded Topology Editor cannot be used on Ubuntu if Velocity iTest is started as a root user. Ubuntu is not configured by default to run X applications (graphical Linus applications) as sudo. This affects Embedded Topology Editor, which is based on Chromium and requires X-server access.

To enable X-server access on Ubuntu, use the following command:

xhost si:localuser:<username>

For example, if you want to run iTest as a root, use the following

xhost si:localuser:root

> **Note:** Execute the command in a opened terminal (without any path). This command may be executed at any time (before or after installation) but before you Open a integrated Topology Editor.

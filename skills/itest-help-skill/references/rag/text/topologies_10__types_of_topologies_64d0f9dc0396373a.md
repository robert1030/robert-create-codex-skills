---
{
  "chunk_id": "topologies_10__types_of_topologies_64d0f9dc0396373a",
  "source_file": "topics/topologies.10.htm",
  "source_original_path": "topics/topologies.10.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Working with Velocity",
    "Working with Velocity Topology in iTest"
  ],
  "heading_path": [
    "Working with Velocity Topology in iTest",
    "Working with Velocity Topology in iTest",
    "Types of topologies"
  ],
  "anchor": "1511840",
  "context_ids": [],
  "index_keywords": [
    "topo_velocity_working_with_Velocity_topology_in_itest"
  ],
  "index_keyword_paths": [
    "topo_velocity_working_with_Velocity_topology_in_itest"
  ],
  "related_links": [
    "import_topologies_inherited_session.htm#1382164"
  ],
  "images": [],
  "content_hash": "64d0f9dc0396373a",
  "level": 2
}
---

# Working with Velocity Topology in iTest > Working with Velocity Topology in iTest > Types of topologies

The table below list the various types of topologies available for use in iTest.

| Topology types and location | Description |
| --- | --- |
| Velocity iTest Topology | Topologies created in Velocity iTest are referred to as Local Velocity iTest Topology. Velocity iTest has no inventory of resources. All elements of the topology are hard coded in the editor. |
| Velocity Topology | Topologies created at Velocity are referred to as Velocity Topology. The topology elements are dynamic and they are defined in Velocity Inventory. Velocity Topology can be used directly from Velocity during execution. Note Only a reserved topology can be used in execution. You may import a Velocity topology and then select the local Velocity topology in the test case. |
| Note | Only a reserved topology can be used in execution. You may import a Velocity topology and then select the local Velocity topology in the test case. |
| Location of Topology | A topology can be located in iTest project or in Velocity. |
| Local Velocity Topology | You may import (Import a topology from Velocity into your iTest workspace) a Velocity Topology to iTest project. Any changes you make in Velocity are synchronized with this imported Local Velocity Topology. |
| Remote Velocity Topology | Topology created in Velocity iTest may be exported to Velocity. During export, Velocity iTest topology elements are associated with Velocity resources (manually or automatically in Topology Export Wizard). You may export the same Velocity iTest Topology to different Velocity VM and each Velocity VM will store its own copy of the exported Velocity iTest topology. You may also export the same Velocity iTest Topology to the same Velocity VM more than once and assign different resources. In such a case, Velocity will have different topologies with different resources, and different IWA sessions. When you export Velocity iTest Topology (e.g., Test-01) to Velocity, a Velocity Topology is created based on the Local Velocity iTest Topology (e.g., Test-01). If you import this topology back to Velocity iTest, a local Velocity Topology is created with a suffix of -1 to the imported topology name (e.g., Test-01-1). Note Subsequent imports of the same topology from Velocity to Velocity iTest creates a suffix to the topology name -2, -3, and so on. Any changes made in Velocity to an exported topology (e.g., Test-01), automatically synchronizes the changes between Velocity topology with the local Velocity topology. |
| Note | Subsequent imports of the same topology from Velocity to Velocity iTest creates a suffix to the topology name -2, -3, and so on. |

Important It is recommended to open and work with imported Velocity topologies only in the Velocity iTest integrated Topology Editor.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

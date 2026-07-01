---
{
  "chunk_id": "import_topologies_inherited_session__import_a_topology_from_velocity_into_you_447b67d979391790",
  "source_file": "topics/import_topologies_inherited_session.htm",
  "source_original_path": "topics/import_topologies_inherited_session.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Working with Velocity",
    "Import a topology from Velocity into your iTest workspace"
  ],
  "heading_path": [
    "Import a topology from Velocity into your iTest workspace",
    "Import a topology from Velocity into your iTest workspace"
  ],
  "anchor": "1382164",
  "context_ids": [
    "import_topologies_inherited_session",
    "import_topologies_wizard"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/import_topology_wizard.png",
    "topics/images/import_topologies.png"
  ],
  "content_hash": "447b67d979391790",
  "level": 1
}
---

# Import a topology from Velocity into your iTest workspace > Import a topology from Velocity into your iTest workspace

When you import a topology, iTest creates a copy of the topology (.tbml file) at the specified location. If any changes are made to resources in the topology, the system auto-syncs the data between iTest and Velocity.

Important To specify a Local Topology in Velocity iTest Test case, you may import a Velocity topology and then select the local Velocity topology in the test case.

1. While connected to Velocity, in the Velocity iTest tool bar, click File > Import, and then click Velocity > Import Velocity Topology on the Import wizard.

1. 2

1. The Import Topologies window displays. In the workspace where the topology should be saved (typically the Topologies folder). Select Velocity > Import Topologies.

1. 3

1. In the Import Topologies dialog box, select the topologies to import.

The Search box supports wild card search that enables you to quickly find specified items. The search string and names you enter are converted to same case (lower case) and search begins from first letter of the name of the item or any word within the full name. For example:

Search string = test, will match and display as shown in the screen shot above.

.Search string: *c will match and display as follows:

Inventory check, backup check

Search string: my, will display as follows:

my_topology

1. 4

1. Verify the location to import to, and then click Finish. You can import only logical topologies.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![diagram](topics/images/import_topology_wizard.png) <!-- image_chunk: img_cfa7a781a3b9d99e -->

![screenshot](topics/images/import_topologies.png) <!-- image_chunk: img_182618e6b235149c -->

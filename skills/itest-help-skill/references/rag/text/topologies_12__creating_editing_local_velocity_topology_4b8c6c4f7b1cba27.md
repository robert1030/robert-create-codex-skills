---
{
  "chunk_id": "topologies_12__creating_editing_local_velocity_topology_4b8c6c4f7b1cba27",
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
    "Create and edit Velocity topology in the integrated Topology Editor",
    "Creating/Editing Local Velocity Topology"
  ],
  "anchor": "1511600",
  "context_ids": [],
  "index_keywords": [
    "topo_velocity_Create_edit_Velocity_topology_iTestWeb_Topology_Editor"
  ],
  "index_keyword_paths": [
    "topo_velocity_Create_edit_Velocity_topology_iTestWeb_Topology_Editor"
  ],
  "related_links": [],
  "images": [
    "topics/images/velocity_topo_TopologiesView.png",
    "topics/images/velocity_topology_open.png",
    "topics/images/velocity_topo_create_velocity_topology.png",
    "topics/images/velo_topo_createNewTopo.png",
    "topics/images/velo_topo_createNewTopo-emulation-options.png",
    "topics/images/velo_topo_sessions_inTE.png"
  ],
  "content_hash": "4b8c6c4f7b1cba27",
  "level": 2
}
---

# Create and edit Velocity topology in the integrated Topology Editor > Create and edit Velocity topology in the integrated Topology Editor > Creating/Editing Local Velocity Topology

iTest allows you to open an existing Velocity topology or create a new topology on Velocity using the integrated Topology editor.

1. Open the Topologies view (iTest > Show View > Other > Velocity > Topologies).

The Topologies view opens with a list of topologies available on the Velocity VM to which you are connected.

If you are not connected to a Velocity VM, a message displays says not connected. Click here to connect. Click here to open the Velocity login window and enter Velocity server URL and login credentials.

1. 2

1. Select a topology, right-click to Open or Delete the selected topology, or click New Topology to create a topology in Velocity.

1. 3

1. Click Open and an existing topology opens in integrated Topology Editor in view/edit mode.

> **Note:** Note Open Velocity topology imported to Velocity iTest in the integrated Topology Editor.

1. 4

1. Click New Topology to open the New Velocity Topology window to create a new topology in Velocity.

Select the folder where you wish to create the new topology.

1. Topology name: Enter the new topology name.

1. Click Finish.

1. 5

1. A blank integrated Topology Editor opens.

The label Emulation on the Topology tab on the left panel is enabled by default and is visible only in the integrated Topology Editor (not visible in Velocity Topology editor).

Create a new topology with the required resources. See Velocity Help > Topology Editor Overview for details.

Emulation option

On the Embedded Topology Editor, when you select a resource, the resource Properties tab on the left panel displays the Emulation dropdown with these options: Always, Never, Use Test Case settings for all device types (physical, abstract, orchestrated, and virtual).

When the emulation option does not have a value in the TBML (for new or an existing topology resource), the default value is set to Use Test Case settings.

1. 6

1. You may create new topology and add sessions to relevant resources as required.

When you import a Velocity topology in Velocity iTest, all defined resources sessions are also imported. You may edit and modify these sessions as required.

|  | Inherited Sessions Lists the Inherited Workflow Automation (IWA) sessions (Only SSH and Telnet) defined in Velocity Templates. You may edit this session and customize for the topology or disable inherited sessions. Click Edit and the inherited session opens in the integrated Sessions Configuration window. Topology Sessions Add new sessions specific to the topology and/or edit existing defined sessions. When you add or edit topology sessions, the iTest Session Profile window opens. You may add any session supported by iTest. |
| --- | --- |

Important You may open a Velocity Topology in Velocity iTest integrated editor only when connected to Velocity server, however, you may continue to edit and save the changes to the topology even after you are disconnected from the Velocity Server.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/velocity_topo_TopologiesView.png) <!-- image_chunk: img_40e7676a366f2abc -->

![diagram](topics/images/velocity_topology_open.png) <!-- image_chunk: img_e7dcd9252d2d2a76 -->

![diagram](topics/images/velocity_topo_create_velocity_topology.png) <!-- image_chunk: img_b2e7014955f8c763 -->

![screenshot](topics/images/velo_topo_createNewTopo.png) <!-- image_chunk: img_a20cdf216b412bb5 -->

![screenshot](topics/images/velo_topo_createNewTopo-emulation-options.png) <!-- image_chunk: img_ab692a75d222b729 -->

![screenshot](topics/images/velo_topo_sessions_inTE.png) <!-- image_chunk: img_93dbc3aa29581e82 -->

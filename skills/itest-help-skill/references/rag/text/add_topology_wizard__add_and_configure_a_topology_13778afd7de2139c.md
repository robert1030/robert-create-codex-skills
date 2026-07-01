---
{
  "chunk_id": "add_topology_wizard__add_and_configure_a_topology_13778afd7de2139c",
  "source_file": "topics/add_topology_wizard.htm",
  "source_original_path": "topics/add_topology_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Overview: iTest Topologies",
    "Add and configure a topology"
  ],
  "heading_path": [
    "Add and configure a topology",
    "Add and configure a topology"
  ],
  "anchor": "1279329",
  "context_ids": [
    "add_topology_wizard"
  ],
  "index_keywords": [
    "Topology editor",
    "abstract",
    "adding",
    "in topologies",
    "topologies"
  ],
  "index_keyword_paths": [
    "Topology editor",
    "abstract resources > in topologies",
    "adding > topologies",
    "creating > topologies",
    "editors > Topology editor",
    "resources > abstract",
    "topologies > adding"
  ],
  "related_links": [
    "topologies.02.htm#1358049",
    "topologies.12.htm#1516816",
    "properties_topo_editor_topo_tab.htm#1317755",
    "topology_quick_start.htm#1272316",
    "properties_topo_editor_device_tab.htm#1407074",
    "topologies.16.htm#1355024"
  ],
  "images": [],
  "content_hash": "13778afd7de2139c",
  "level": 1
}
---

# Add and configure a topology > Add and configure a topology

As described in Overview: Creating a topology, the process of defining a topology in iTest is quite flexible. For that reason, the following instructions are general in nature and you might follow a different course. See also Create and edit Velocity topology in the integrated Topology Editor.



To create a topology

1. Click File > New > Topology.

1. 2

1. The New Topology wizard starts.

Specify the folder that will hold the topology (TBML) file either by typing the path or by selecting it in the project tree.

1. Specify the File name for the file.

1. If the topology should be added to Velocity, then check Synchronize this topology with the Velocity iTest server.

This option ensures that if changes are made in Velocity iTest to the properties or ports for a resource, then all topologies that include the resource are auto-updated (synced).

1. Click Finish.

A new blank TBML-format file is created and opened in the Topology editor. In addition, the Properties view opens.

1. 3

1. On the Properties view, the Topology tab is selected. Document the Name and Description of the topology, as described in Topology editor: Properties view, Topology tab.

1. 4

1. Each line on the Devices tab defines a device. Add a device as described in Topologies: Quick instructions.

> **Note:** The name is very important. Here is an example that shows why: In this example, we will name a device DUTRouter2 in both the LocalTopology topology (the document that defines your personal development topology) and the SharedRegressionTopology topology (that defines the QA regression topology) — only the IP addresses are different.

> **Note:** As a result, any test case that refers to DUTRouter2 in a step can, without modification, use either of the two topologies (you have only to specify the appropriate topology on the Test Case editor General page). Once you finish developing the test case, you can hand it off for regression without any changes.

1. 5

1. Add and configure resources and device sessions as needed.

To define an abstract resource, use any of the following methods:

- Drop an appropriate resource template onto the palette.

The condition property is template[<type>] (for example, for template[Server], the resource inherits Server)

All ports are also abstract and contain a condition property.

- In an existing topology, convert an existing resource into an abstract resource by xxx.

See also View resolved resources properties (from Abstract Topology)/

1. 6

1. Optional. If appropriate, configure how emulation is used for any device in a topology in any test case that uses the device. For details, see Control emulation for devices in a topology.

1. 7

1. Save the topology document.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

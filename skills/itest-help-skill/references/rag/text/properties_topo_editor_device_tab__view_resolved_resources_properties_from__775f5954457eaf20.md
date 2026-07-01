---
{
  "chunk_id": "properties_topo_editor_device_tab__view_resolved_resources_properties_from__775f5954457eaf20",
  "source_file": "topics/properties_topo_editor_device_tab.htm",
  "source_original_path": "topics/properties_topo_editor_device_tab.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "General Local Topology Operations",
    "Topology editor: Properties view, Device tab"
  ],
  "heading_path": [
    "Topology editor: Properties view, Device tab",
    "Topology editor: Properties view, Device tab",
    "View resolved resources properties (from Abstract Topology)"
  ],
  "anchor": "1407074",
  "context_ids": [
    "properties_topo_editor_device_tab"
  ],
  "index_keywords": [
    "Device tab",
    "Device tab, abstract topology",
    "Device tab, tbml"
  ],
  "index_keyword_paths": [
    "Properties page > Device tab",
    "Properties page > Device tab, abstract topology",
    "Properties page > Device tab, tbml",
    "Topology Properties page > Device tab",
    "Topology Properties page > Device tab, abstract topology",
    "Topology Properties page > Device tab, tbml",
    "Topology editor > Device tab",
    "Topology editor > Device tab, abstract topology",
    "Topology editor > Device tab, tbml"
  ],
  "related_links": [],
  "images": [
    "topics/images/velo_topo_view_abs_topo_inReservation.png",
    "topics/images/velo_topo_view_abs_topo_View-ResolvedResourcesInReservation.png"
  ],
  "content_hash": "775f5954457eaf20",
  "level": 2
}
---

# Topology editor: Properties view, Device tab > Topology editor: Properties view, Device tab > View resolved resources properties (from Abstract Topology)

You may view the Abstract topology and resources in iTest via the integrated Web Topology Editor. You may view the list of resolved resources allocated for use during reservation in an active reservation topology.

To view the resolved resources in an Abstract Topology during a reservation:

- View the list of reservations displayed.

> **Note:** Note You may set up a filter to list abstract topology with both active and inactive reservations.

You may also view the resolved resources in Velocity Reservations > Resources tab.

- From Reservations tab, select the required Abstract Topology and open a reserved topology (double clicking on the topology or use the context menu).

> **Note:** Note Reserved topology displays reservation name, start time and end time.

- The Reserved topology opens in the integrated Web Topology Editor. The example below illustrates an Abstract Topology with resolved resources.

The above illustration shows that the abstract resource named abs_PC(2) has been resolved and a physical resource names pc_test has been allocated.

- The properties pane display when you select a resource.

The Properties tab shows relevant information. For example, Inventory name indicates that the abstract resource is resolved and an inventory resource is allocated.

- Resolved port details display when you select the Ports tab.

> **Note:** Note

- The names of resolved resources show in the above diagram. Properties view contains additional properties assigned with allocated inventory resources.

- The topology can have several reservations. Each reservation will open in a separate window (topology editor).

- View the resolved resources for:

- Active reservations.

- Completed reservations (past reservation).

- Scheduled reservations (future reservation)

> **Note:** For recurring reservations, resources will be allocated at the start time, i.e., it is not possible to view them in advance. Double clicking an inactive recurring reservation will open an abstract topology.

![screenshot](topics/images/velo_topo_view_abs_topo_inReservation.png) <!-- image_chunk: img_b008ef09b7c99227 -->

![screenshot](topics/images/velo_topo_view_abs_topo_View-ResolvedResourcesInReservation.png) <!-- image_chunk: img_2dde3c84e5b11109 -->

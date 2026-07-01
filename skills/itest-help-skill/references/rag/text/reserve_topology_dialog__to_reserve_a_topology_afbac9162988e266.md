---
{
  "chunk_id": "reserve_topology_dialog__to_reserve_a_topology_afbac9162988e266",
  "source_file": "topics/reserve_topology_dialog.htm",
  "source_original_path": "topics/reserve_topology_dialog.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Working with Velocity",
    "Reserve a topology"
  ],
  "heading_path": [
    "Reserve a topology",
    "Reserve a topology",
    "To reserve a topology"
  ],
  "anchor": "1554966",
  "context_ids": [
    "new_reservation_wizard"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "topology_quick_start.htm#1277524",
    "topologies.12.htm#1565805"
  ],
  "images": [
    "topics/images/velo_topo_reserveButton_in_WebTE.png",
    "topics/images/velo_topo_reservations_view_add.png",
    "topics/images/topology_reserve.png",
    "topics/images/reservation_notes.png",
    "topics/images/velo_topo_reservations_ETA_bar.png",
    "topics/images/velo_topo_reservations_no_vel_priority_queue_license.png",
    "topics/images/velo_topo_reservations_view.png",
    "topics/images/velo_topo_select_resource_run_session.png",
    "topics/images/velo_topo_reservations_edit_emulationForTopo.png",
    "topics/images/velo_topo_reservations_edit_emulation.png",
    "topics/images/velo_topo_reserved_topology_in_WebTE.png",
    "topics/images/velo_topo_edit_inherited_session_in_reserved_topology.png",
    "topics/images/velo_topo_edit_topology_session_in_reserved_topology.png"
  ],
  "content_hash": "afbac9162988e266",
  "level": 4
}
---

# Reserve a topology > Reserve a topology > To reserve a topology

1. When viewing a topology in the integratedTopology Editor (ensure that you are connected to a Velocity server), Click the Reserve button. The New Reservation dialog displays with the reservation topology highlighted.

You may also reserve a topology from the Reservations view as follows.

Ensure that you are connected to a Velocity server, go to Reservations view (Show View > Other > Velocity > Reservations view) and click Add.

1. On the Reservation dialog box, specify the Name of the reservation, Duration and search or select the required topology.

The Search box supports wild card search that enables you to quickly find specified items. The search string and names you enter are converted to same case (lower case) and search begins from first letter of the name of the item or any word within the full name. For example:

Search string = Test, will match and display as follows:

Test-01, Test-01-Topology, Test-03, Test-03 (2).

Search string: test, will display as follows:

Test-01, Test-01-Topology.

Search string: *01, will display as follows:

Subtopology-01, Test-01, Test-01-Topology

1. Select the topology to reserve.

1. 2

1. Click Next and the Notes page displays.

- The Notes text box appears empty if the property notes value is empty or the property notes does not exist. You may add notes as plain text, a JSON object or a JSON array, as required.

Note: A maximum of 10000 characters are allowed in the notes property value.

- The Notes text box displays existing value, if defined previously (as described in Add a property to a topology, to a device, or to a link). That is, the contents of the Topology's notes property is automatically inserted in the New Reservation > Notes text box.

If the notes property value is detected as a JSON array or object, the Notes text box displays content as JSON pretty print. You may accept the contents or modify the formatting of the contents as required.

1. 3

1. Click Finish to schedule the reservation.

If a requested resource is not available at the reservation schedule time, an error message displays. For example, if the resource is already reserved for some or all of the requested duration, iTest displays a message as follows: Reservation `Test-Topology reservation` conflicts with existing reservations. Conflicting resources: `Port-01`,`Port-PC2-01`.

Modify the reservation duration or resources as required and reschedule the reservation.

1. 4

1. Reservation is queued (if your system is licensed for Reservation Priority Queuing feature).

A message displays saying that the reservation is queued and shows a progress bar with ETA (estimated time of activation) until the reservation is activated.

The ETA is automatically updated depending on the resource availability for activation.

You may see the topology reserved in Velocity with the default priority defined for the current user. See Velocity Online Help for reservation priority defined by Velocity Admin.

> **Note:** Note if your system is licensed with Velocity Resource Queuing feature and not the Reservation Priority Queuing feature, an error will be shown in case of resource reservation conflicts.

1. 5

1. The Reservations view displays after a reservation is active. In the Reservations view, select the reservation, right-click, and select Open to view the reserved topology in the integrated Topology editor.

1. 6

1. Select a resource in the reserved topology and right-click to run sessions, if applicable. The topology resources may have defined sessions, both Inherited from the template and topology defined.

You may view the inherited sessions from the Topology Editor, and run the inherited sessions.

> **Tip:** Tip You may run sessions only from an active reservation.

1. 7

1. You may edit the reserved topology as required, save the topology and Submit. Click Edit on the integrated Topology Editor (top-right).

The label Emulation on the Topology tab on the left panel is enabled by default and is visible only in the integrated Reservations Topology Editor (not visible in Velocity Reservations Topology editor). You may uncheck to disable emulation for the topology.

1. 8

1. Edit emulation for resources in the reserved topology as required, save the topology and execute. See Emulation option for details.

1. 9

1. Edit sessions in the reserved topology as required, save the topology and run sessions again.

Click Edit on the integrated Topology Editor (top-right).

1. Edit session listed under the label Inherited Sessions. The Inherited Automation Workflow (IWA) sessions opens in the Session Configuration dialog as shown below (integrated Topology Editor).

IWA sessions execute only terminal based sessions and Velocity supports only SSH and Telnet sessions.

1. Add a new session to the reserved topology or edit an existing session listed under Topology Sessions and the iTest Session Profile window opens. You may start any session supported by iTest.

User can start any Velocity iTest session supported by Velocity iTest from topology reservation only in new WebTE editor; from Velocity can start only SSH and Telnet sessions

> **Tip:** Tip You may run sessions only from an active reservation.

View Reservation in Velocity

Go to Velocity > Reservations page and view the reservation.

- On the Velocity > Reservations > Notes page, notice the contents as populated in iTest—text or JSON Pretty Print.You may modify the contents as required.

- On the Velocity > Reservations > Topology page, click the reservation topology and the Topology Editor opens. On the Notes tab, edit and modify the Notes as required.

If a JSON Object or JSON Array syntax is not accurate, the contents are displayed as text and no error displays.

![screenshot](topics/images/velo_topo_reserveButton_in_WebTE.png) <!-- image_chunk: img_a55823f1bb0293be -->

![screenshot](topics/images/velo_topo_reservations_view_add.png) <!-- image_chunk: img_183f2c792b77fe1f -->

![diagram](topics/images/topology_reserve.png) <!-- image_chunk: img_cb1824aa0bb16c44 -->

![screenshot](topics/images/reservation_notes.png) <!-- image_chunk: img_6917fb99129d88b6 -->

![screenshot](topics/images/velo_topo_reservations_ETA_bar.png) <!-- image_chunk: img_6a4d012065edd1d4 -->

![screenshot](topics/images/velo_topo_reservations_no_vel_priority_queue_license.png) <!-- image_chunk: img_0af5234438cfb374 -->

![screenshot](topics/images/velo_topo_reservations_view.png) <!-- image_chunk: img_2e6d8a9ed8665f88 -->

![screenshot](topics/images/velo_topo_select_resource_run_session.png) <!-- image_chunk: img_6e978331695479e4 -->

![screenshot](topics/images/velo_topo_reservations_edit_emulationForTopo.png) <!-- image_chunk: img_c0e697d2c20480e0 -->

![screenshot](topics/images/velo_topo_reservations_edit_emulation.png) <!-- image_chunk: img_6d3dc0a511b2f9d1 -->

![diagram](topics/images/velo_topo_reserved_topology_in_WebTE.png) <!-- image_chunk: img_5eb12123a028618f -->

![diagram](topics/images/velo_topo_edit_inherited_session_in_reserved_topology.png) <!-- image_chunk: img_59c268e9a9305557 -->

![diagram](topics/images/velo_topo_edit_topology_session_in_reserved_topology.png) <!-- image_chunk: img_65b0add00da20b65 -->

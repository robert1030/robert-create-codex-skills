# iTest Topology Editor > Working with Velocity > Reserve a topology > To reserve a topology > 第1段

![*](bullet_blue.jpg) <!-- image_ref -->

1. When viewing a topology in the integratedTopology Editor (ensure that you are connected to a Velocity server), Click the Reserve button. The New Reservation dialog displays with the reservation topology highlighted.

![](images/velo_topo_reserveButton_in_WebTE.png) <!-- image_ref -->

You may also reserve a topology from the Reservations view as follows.

![*](bullet_blue.jpg) <!-- image_ref -->

1. Ensure that you are connected to a Velocity server, go to Reservations view (Show View > Other > Velocity > Reservations view) and click Add.

![](images/velo_topo_reservations_view_add.png) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

1. On the Reservation dialog box, specify the Name of the reservation, Duration and search or select the required topology.

![](images/topology_reserve.png) <!-- image_ref -->

The Search box supports wild card search that enables you to quickly find specified items. The search string and names you enter are converted to same case (lower case) and search begins from first letter of the name of the item or any word within the full name. For example:

Search string = Test, will match and display as follows:

Test-01, Test-01-Topology, Test-03, Test-03 (2).

Search string: test, will display as follows:

Test-01, Test-01-Topology.

Search string: *01, will display as follows:

Subtopology-01, Test-01, Test-01-Topology

![*](bullet_blue.jpg) <!-- image_ref -->

1. Select the topology to reserve.

1. 2 Click Next and the Notes page displays.

![](images/reservation_notes.png) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

- The Notes text box appears empty if the property notes value is empty or the property notes does not exist. You may add notes as plain text, a JSON object or a JSON array, as required.

Note: A maximum of 10000 characters are allowed in the notes property value.

![*](bullet_blue.jpg) <!-- image_ref -->

- The Notes text box displays existing value, if defined previously (as described in Add a property to a topology, to a device, or to a link). That is, the contents of the Topology's notes property is automatically inserted in the New Reservation > Notes text box.

If the notes property value is detected as a JSON array or object, the Notes text box displays content as JSON pretty print. You may accept the contents or modify the formatting of the contents as required.

1. 3 Click Finish to schedule the reservation.

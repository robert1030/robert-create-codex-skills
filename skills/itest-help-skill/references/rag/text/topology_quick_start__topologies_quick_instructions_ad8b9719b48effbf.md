---
{
  "chunk_id": "topology_quick_start__topologies_quick_instructions_ad8b9719b48effbf",
  "source_file": "topics/topology_quick_start.htm",
  "source_original_path": "topics/topology_quick_start.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Overview: iTest Topologies",
    "Topologies: Quick instructions"
  ],
  "heading_path": [
    "Topologies: Quick instructions",
    "Topologies: Quick instructions"
  ],
  "anchor": "1272316",
  "context_ids": [
    "topology_quick_start"
  ],
  "index_keywords": [
    "Properties view",
    "VLANs to topology",
    "adding",
    "adding VLANs",
    "adding devices",
    "adding session profiles to",
    "adding to topology",
    "adding to topology elements",
    "arranging devices",
    "arranging in topology",
    "configuring",
    "creating and managing",
    "defining for devices in topologies",
    "devices to topology",
    "documenting the graphics",
    "editing for devices in topologies",
    "editing session profiles",
    "importing",
    "instructions",
    "labels to topology",
    "links between devices",
    "notes to topology",
    "opening",
    "opening Topology editor",
    "opening while working on topology",
    "properties to topology elements",
    "property collections to topology elements",
    "session profiles in topologies",
    "topologies"
  ],
  "index_keyword_paths": [
    "Properties view > opening while working on topology",
    "Topology editor > instructions",
    "Topology editor > opening",
    "VLANs > adding to topology",
    "adding > VLANs to topology",
    "adding > devices to topology",
    "adding > labels to topology",
    "adding > links between devices",
    "adding > notes to topology",
    "adding > properties to topology elements",
    "adding > property collections to topology elements",
    "adding > session profiles in topologies",
    "configuring > links between devices",
    "configuring > session profiles in topologies",
    "devices > adding to topology",
    "devices > arranging in topology",
    "devices in topologies > adding session profiles to",
    "devices in topologies > editing session profiles",
    "editing > session profiles in topologies",
    "importing > topologies",
    "labels > adding to topology",
    "links between devices > adding",
    "links between devices > configuring",
    "modifying > session profiles in topologies",
    "notes > adding to topology",
    "opening Topology editor",
    "properties > adding to topology elements",
    "property collections > adding to topology elements",
    "session profiles > defining for devices in topologies",
    "session profiles > editing for devices in topologies",
    "topologies > adding VLANs",
    "topologies > adding devices",
    "topologies > adding session profiles to",
    "topologies > arranging devices",
    "topologies > creating and managing",
    "topologies > documenting the graphics",
    "topologies > editing session profiles",
    "topologies > importing",
    "topology > Properties view"
  ],
  "related_links": [
    "topology_editor.htm#1284003",
    "properties_topo_editor_topo_tab.htm#1317755",
    "properties_topo_editor_session_tab.htm#1435333",
    "properties_topo_editor_device_tab.htm#1276940",
    "properties_topo_editor_link_tab.htm#1277076",
    "properties_topo_editor_rulergrid_tab.htm#1277106",
    "create_connections_wizard.htm#1389278",
    "topo_add_session_profile_wizard.htm#1396646",
    "topologies.26.htm#1279667",
    "properties_topo_editor_device_tab.htm#1407074"
  ],
  "images": [
    "topics/images/topologies.01.jpg",
    "topics/images/topologies.02.jpg",
    "topics/images/topologies.03.jpg",
    "topics/images/topologies.04.jpg",
    "topics/images/topologies.05.jpg",
    "topics/images/add_new_property.png",
    "topics/images/topologies.07.jpg",
    "topics/images/add_new_property_collection.png",
    "topics/images/topologies.09.jpg",
    "topics/images/topologies.10.jpg",
    "topics/images/topologies.11.jpg",
    "topics/images/topologies.12.jpg",
    "topics/images/topologies.13.jpg",
    "topics/images/topologies.14.jpg",
    "topics/images/topologies.15.jpg",
    "topics/images/topologies.16.jpg"
  ],
  "content_hash": "ad8b9719b48effbf",
  "level": 1
}
---

# Topologies: Quick instructions > Topologies: Quick instructions

Many of the operations in the following table are described in detail elsewhere in this chapter, but the table may give you all you need to create and manage topologies. Be sure that you are familiar with the Layout of the Topology editor before you use the instructions.

> **Tip:** Tip Remember that many of the most common tasks appear in the context menu when you right-click an item on the canvas or in the Properties view.

The tabs that you use to manage the topology definition are described in:

Topology editor: Properties view, Topology tab

Topology editor: Properties view, Session tab

Topology editor: Properties view, Device tab

Topology editor: Properties view, Link tab

Topology editor: Properties view, Ruler and Grid tab

| To: | Do This: |
| --- | --- |
| Define a topology | Click File > New > Topology If you move a topology into the Favorites view, the value of the @Name attribute appears in the Headline column. |
| Open a topology document in the Topology editor | While working in iTest Activities, click Build a topology. While working in any other perspective: In the Favorites view or the Project Explorer, right-click a topology document and then click Open. |
| Open the Properties view while working on a topology | Click anywhere on the canvas. Alternatively, right-click anywhere on the canvas and then select Show Properties View |
| Add a device to a topology | Select a Device type in the palette and then either click on the canvas or drag to the desired location. 2. The device is given a unique default name. Note The name that appears on the canvas for a device is the name property value. To change the name, select the device on the canvas, click its name, and then type a new name. Alternatively, select the Device tab in the Properties view and type a new value for the name property. The name appears in the Select a Session Profile or Device dialog box when a test case developer is specifying the device for an open step. 3. Use the grab handles to resize the device graphic as needed. |
|  | Select a Device type in the palette and then either click on the canvas or drag to the desired location. |
| 2. | The device is given a unique default name. |
| Note | The name that appears on the canvas for a device is the name property value. To change the name, select the device on the canvas, click its name, and then type a new name. |
| 3. | Use the grab handles to resize the device graphic as needed. |
| Add a device to a topology | Select Device in Topology and a special kind of "device" to a logical topology – VLAN, and link resources' ports (real or abstract) with it. iTest assigns the VLAN network ID. VLAN must not have ports or a condition property A link with a VLAN as one of the endpoints is called L2 link or VLAN link. A link cannot have a VLAN at both endpoints. A link with both endpoints being real or abstract devices' ports (not VLANs) can be explicitly marked as VLAN link. In this case, this link is treated as if there is an implicit VLAN device between the endpoints. This is done to have a convenient way to create VLANs with two devices. Other links are called L1 links. L2 links must visually differ from L1 links. May be, dashed line, or something like this. A resource may be connected to multiple VLANs, if it has multiple ports. VLAN links are always bidirectional. |
|  | VLAN must not have ports or a condition property |
|  | A link with a VLAN as one of the endpoints is called L2 link or VLAN link. A link cannot have a VLAN at both endpoints. |
|  | A link with both endpoints being real or abstract devices' ports (not VLANs) can be explicitly marked as VLAN link. In this case, this link is treated as if there is an implicit VLAN device between the endpoints. This is done to have a convenient way to create VLANs with two devices. |
|  | Other links are called L1 links. |
|  | L2 links must visually differ from L1 links. May be, dashed line, or something like this. |
|  | A resource may be connected to multiple VLANs, if it has multiple ports. |
|  | VLAN links are always bidirectional. |
| Add and configure a link between two devices Add a link from a device to itself | Note The instructions in this table describe adding a single link between ports. To add multiple links quickly, use the Create Connection wizard, as described in To quickly add multiple links (connections between ports). In the palette, select a link type (for example, Ethernet Link). All links that you now add will be that type until you select a different type. 2. Now add the link: To add a link from a device to itself (the device is both source and target). Click the device. To add a link from one device to another: Click the source device and drag to the target device. 3. The editor gives the new link a unique default name and connects it to the next unconnected port on the source and on the target (if needed, the editor adds a new port). The names of the link endpoints (ports) appear on the canvas. To modify the links, click the Source or Target property and select the desired card or port. To take the new default port and add it into a new card on a device, add a new Card, add a new port to it, and then point the link to the new port. |
| Note | The instructions in this table describe adding a single link between ports. To add multiple links quickly, use the Create Connection wizard, as described in To quickly add multiple links (connections between ports). |
|  | In the palette, select a link type (for example, Ethernet Link). All links that you now add will be that type until you select a different type. |
| 2. | Now add the link: |
|  | To add a link from a device to itself (the device is both source and target). Click the device. |
|  | To add a link from one device to another: Click the source device and drag to the target device. |
| 3. | The editor gives the new link a unique default name and connects it to the next unconnected port on the source and on the target (if needed, the editor adds a new port). The names of the link endpoints (ports) appear on the canvas. |
|  | To modify the links, click the Source or Target property and select the desired card or port. |
|  | To take the new default port and add it into a new card on a device, add a new Card, add a new port to it, and then point the link to the new port. |
| Add a card, a port, or another device to a device Add a port to a card | When you add a link to a device, iTest adds a default port on the device and assigns the link to the port, as described in the preceding instruction. In addition, you can add cards, ports, or "sub-devices” to a device or to existing cards, ports, or sub-devices on a device. To add to the device: On the canvas, click the device and then, on the Device tab, click the arrow on the Add button . Select the item to add. (Clicking the part of the button adds a card.) To add to an existing card, port, or device on a device: Select the item in the list on the Device tab and then click the arrow on the Add button . Select the item to add. The new item is given a default displayName that indicates its position in the hierarchy. For example, when new cards are added to router1, then the cards are named card1, card2, card3, and so on. |
|  | To add to the device: On the canvas, click the device and then, on the Device tab, click the arrow on the Add button . Select the item to add. (Clicking the part of the button adds a card.) |
|  | To add to an existing card, port, or device on a device: Select the item in the list on the Device tab and then click the arrow on the Add button . Select the item to add. |
| Configure cards, ports, or sub-devices on a device | When you add a link to a device, the editor adds a default port on the device and assigns the link to the port. You decide whether or not to edit the port’s property settings to match the actual configuration of the physical device. Generic Devices (the kind of sub-device that you can add to a device) have no default @Type attribute value. You can set the attribute value as needed (for example, workstation), To change a property of one of the cards, ports, or devices within the device, select the item in the list under the device (in the example, port_5_2 on the trafficgen_5 device) and then change the value as needed: . Note The @ symbol denotes a attribute rather than a iTest property. |
|  | When you add a link to a device, the editor adds a default port on the device and assigns the link to the port. You decide whether or not to edit the port’s property settings to match the actual configuration of the physical device. |
|  | Generic Devices (the kind of sub-device that you can add to a device) have no default @Type attribute value. You can set the attribute value as needed (for example, workstation), |
|  | To change a property of one of the cards, ports, or devices within the device, select the item in the list under the device (in the example, port_5_2 on the trafficgen_5 device) and then change the value as needed: . |
| Note | The @ symbol denotes a attribute rather than a iTest property. |
| Add and configure a session profile for a topology device | See Add, edit, or remove a session configuration for a iTest topology device. |
| Add a property to a topology, to a device, or to a link | You may want to add a property definition to the current default list of property definitions. For example, for the device with the default abstract (logical) name of router1, you might want to add the displayName property that will hold the friendly name of the actual physical device, like 4268__rtr_rev3.52. Select the device or link or topology. To select the topology, click anywhere in a blank area of the canvas. In the appropriate tab on the Properties view, click . 2. In the New Property dialog box, specify the Name for the property and its Value. For example: select notes property and add value as a string, JSON array, or a JSON object. For example: String: foo=bar JSON Array: [{"EmailGroup":"user01@company.com",“Retries Interval": 30,"Time Out": 60}] JSON Object: {"EmailGroup":"user01@company.com","Retries Interval": 30,"Time Out": 60} Note: A maximum of 10000 characters are allowed in the notes property value. Tip: For topologies created with an older version of iTest or imported into iTest, you may create the notes property via the New Property dialog. The notes property will be listed as one of the choices in the New Property dialog. 3. Select the Vendor (Unique identifier of the provider of the session type templates — typically com.fnfr for Spirent.) Note The default properties and attributes are provided by the session configuration provider. Adding a property here does not add the property to the provider’s definition. |
|  | In the appropriate tab on the Properties view, click . |
| 2. | In the New Property dialog box, specify the Name for the property and its Value. |
|  | String: foo=bar |
|  | JSON Array: [{"EmailGroup":"user01@company.com",“Retries Interval": 30,"Time Out": 60}] |
|  | JSON Object: {"EmailGroup":"user01@company.com","Retries Interval": 30,"Time Out": 60} |
| 3. | Select the Vendor (Unique identifier of the provider of the session type templates — typically com.fnfr for Spirent.) |
| Note | The default properties and attributes are provided by the session configuration provider. Adding a property here does not add the property to the provider’s definition. |
| Add a property collection to a topology, to a device, or to a link | Select the device or link. To select the topology, click anywhere in a blank area of the canvas. In the appropriate tab on the Properties view, click the arrow on the Add button and select Add Property Collection. 2. In the New Property Collection dialog box, specify the Name for the property collection. 3. Select the Vendor (Unique identifier of the provider of the session type templates — typically com.fnfr for Spirent.) Note The default properties and attributes are provided by the session configuration provider. Adding a property here does not add the property to the provider’s definition. 4. The editor adds the property collection. To add a property to the collection, select the collection and click |
|  | In the appropriate tab on the Properties view, click the arrow on the Add button and select Add Property Collection. |
| 2. | In the New Property Collection dialog box, specify the Name for the property collection. |
| 3. | Select the Vendor (Unique identifier of the provider of the session type templates — typically com.fnfr for Spirent.) |
| Note | The default properties and attributes are provided by the session configuration provider. Adding a property here does not add the property to the provider’s definition. |
| 4. | The editor adds the property collection. To add a property to the collection, select the collection and click |
| Place devices into an orderly arrangement on the canvas | Move the device by dragging. By default, devices snap to an underlying grid. To use the tools that control grid settings, click anywhere in the background of a topology. Click the Rulers & Grid tab in the Properties view and change the setting. To set the Rulers & Grid settings for all topologies displayed in the Topology editor, see Set preferences for Topologies. |
| Add a label or note anywhere on the canvas | You can add a label or note anywhere on the canvas. To add a label: In the palette toolbar, click Label and then click at the desired location. Type the label text. Use the Enter key to add lines. To add a note: In the palette toolbar, click Note and then click at the desired location. Type the title text in the bold text box. Type the body text in the next text box. Use the Enter key to add lines. |
| Edit a device’s session profile | Select the device. 2. On the Properties view, click the Session tab and then select the session profile in the list. 3. Click . The the Edit Session Profile page opens. 4. Edit properties as needed and then click OK. |
|  | Select the device. |
| 2. | On the Properties view, click the Session tab and then select the session profile in the list. |
| 3. | Click . The the Edit Session Profile page opens. |
| 4. | Edit properties as needed and then click OK. |
| Cut / Copy / Paste / Delete something in the topology | In the canvas or in the Properties view, select the items and then click one of or . Delete deletes all children. Drag the cursor to select. any number of objects You can paste into other topologies. |
| Start a session on a device | Select the device. 2. On the Properties view, click the Session tab and then select the session profile in the list. 3. Click . |
|  | Select the device. |
| 2. | On the Properties view, click the Session tab and then select the session profile in the list. |
| 3. | Click . |
| Import a topology that was created on a different system | As long as the file is TBML-format, iTest can open it and you can edit and save it as a iTest topology. In addition, any TBML-compliant editor can open a iTest topology file. Use Ctrl+click and Shift+click or Ctrl+A for multi-select. You can copy/paste one or more devices or properties from one topology to another. |
| Save a topology as an image file | As a communication tool, you may want to share a graphical image of a topology or an item in the topology or a selected group of items. On the canvas, right-click an item or the canvas background and select File > Save As Image File. 2. On the Save As Image File dialog box, specify the following values. Folder: Specify the location of the file in the file system. File name: Specify the name of the image file. Image format: Specify the image format of the file. To save the image as an HTML file, check the Export to HTML check box (the Image format property is then ignored). Check Overwrite existing file without warning to not display the dialog box that asks you whether to overwrite an existing file. 3. Click OK. |
|  | On the canvas, right-click an item or the canvas background and select File > Save As Image File. |
| 2. | On the Save As Image File dialog box, specify the following values. |
| 3. | Click OK. |
| View resolved resources from abstract topology in iTest GUI | See View resolved resources properties (from Abstract Topology) |
| Set preferences for Topology operations | See Set preferences for Topologies |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/topologies.01.jpg) <!-- image_chunk: img_22cc651421c7d280 -->

![inline_icon](topics/images/topologies.02.jpg) <!-- image_chunk: img_d2719501190f40fc -->

![inline_icon](topics/images/topologies.03.jpg) <!-- image_chunk: img_bc6459365425437e -->

![screenshot](topics/images/topologies.04.jpg) <!-- image_chunk: img_0d160008c73082f6 -->

![inline_icon](topics/images/topologies.05.jpg) <!-- image_chunk: img_d9537b5efe76351e -->

![screenshot](topics/images/add_new_property.png) <!-- image_chunk: img_61df3a5062f5e6ed -->

![inline_icon](topics/images/topologies.07.jpg) <!-- image_chunk: img_565c1b09ba120d7e -->

![screenshot](topics/images/add_new_property_collection.png) <!-- image_chunk: img_79c3eef40487f236 -->

![inline_icon](topics/images/topologies.09.jpg) <!-- image_chunk: img_b827a27831bb87a5 -->

![screenshot](topics/images/topologies.10.jpg) <!-- image_chunk: img_eb917e462ce518b8 -->

![inline_icon](topics/images/topologies.11.jpg) <!-- image_chunk: img_746f2ad1eb2ce8f9 -->

![inline_icon](topics/images/topologies.12.jpg) <!-- image_chunk: img_09d05d28afca7892 -->

![inline_icon](topics/images/topologies.13.jpg) <!-- image_chunk: img_23925b3829c580a5 -->

![unknown](topics/images/topologies.14.jpg) <!-- image_chunk: img_cfa9784e25653aea -->

![inline_icon](topics/images/topologies.15.jpg) <!-- image_chunk: img_9935ca6574358704 -->

![inline_icon](topics/images/topologies.16.jpg) <!-- image_chunk: img_d467c6f7edffa893 -->

---
{
  "chunk_id": "spirent_testcenter_gui_04__port_commands_1ca1874917fe8643",
  "source_file": "topics/spirent_testcenter_gui.04.htm",
  "source_original_path": "topics/spirent_testcenter_gui.04.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "Port commands"
  ],
  "heading_path": [
    "Port commands",
    "Port commands"
  ],
  "anchor": "1396022",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_gui_2.2.jpg"
  ],
  "content_hash": "1ca1874917fe8643",
  "level": 1
}
---

# Port commands > Port commands

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| breakLink | portIndex |  | Breaks the link on the selected port |
| configurePort | portIndex |  | Applies any changes that you made to configuration settings for the selected port. Note iTest supports Ethernet, 10G, 40G, 100G, and iEE802.11 wireless traffic. However, iTest Spirent TestCenter session editor allows you to view and configure port settings of only Ethernet and IEE802.11 wireless traffic port. You may view and configure all port settings in TestCenter. |
| Note | iTest supports Ethernet, 10G, 40G, 100G, and iEE802.11 wireless traffic. However, iTest Spirent TestCenter session editor allows you to view and configure port settings of only Ethernet and IEE802.11 wireless traffic port. You may view and configure all port settings in TestCenter. |  |  |
| restartAutoNegotiation | portIndex | — None — | Restart the auto-negotiation process for the selected ports. |
| restoreLink | portIndex | — None — | Bring the selected ports online and reserve for testing. |
| showPorts | [portList] | — None — | Shows information about the selected ports Note Test supports Ethernet, 10G, 40G, 100G, and iEE802.11 wireless traffic. However, iTest Spirent TestCenter session editor allows you to view and configure port settings of only Ethernet and IEE802.11 wireless traffic port. You may view and configure all port settings in TestCenter. |
| Note | Test supports Ethernet, 10G, 40G, 100G, and iEE802.11 wireless traffic. However, iTest Spirent TestCenter session editor allows you to view and configure port settings of only Ethernet and IEE802.11 wireless traffic port. You may view and configure all port settings in TestCenter. |  |  |
| addPorts | addPorts | — None — | Add offline ports. In the Command property, specify portList which is the list of //chassis/slot/port separated by spaces. |
| attachPorts | attachPorts | — None — | Connects and reserves all ports that are not reserved yet. |
| mapPorts | portIndex and portLocationList |  | Maps ports to new locations. In the Command property, specify portIndex and portLocationList. portIndex is the first port to map, ports are mapped in order after that. Example: [mapPorts 2 //10.1.2.5/1/1 //10.1.2.5/1/2] will map Port 2 to //10.1.2.5/1/1 and Port 3 to //10.1.2.5/1/2. If ports were reserved, they should be unreserved first then use attachPorts to reserve again. |
| StartLagCaptureCommand | PortSet(LAG port) |  | Starts capture on the individual member ports of the LAG. |
| StopLagCaptureCommand | PortSet(LAG port) |  | Stops capture on the individual member ports of the LAG. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![unknown](topics/images/spirent_testcenter_gui_2.2.jpg) <!-- image_chunk: img_ca12cb22dac4f748 -->

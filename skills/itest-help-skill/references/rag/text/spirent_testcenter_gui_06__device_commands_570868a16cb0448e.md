---
{
  "chunk_id": "spirent_testcenter_gui_06__device_commands_570868a16cb0448e",
  "source_file": "topics/spirent_testcenter_gui.06.htm",
  "source_original_path": "topics/spirent_testcenter_gui.06.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "Device commands"
  ],
  "heading_path": [
    "Device commands",
    "Device commands",
    "Device commands"
  ],
  "anchor": "1358615",
  "context_ids": [],
  "index_keywords": [
    "ARP packets",
    "ARP/ND state"
  ],
  "index_keyword_paths": [
    "ARP packets",
    "ARP/ND state"
  ],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_gui_3.03.jpg",
    "topics/images/spirent_testcenter_gui_3.04.jpg",
    "topics/images/spirent_testcenter_gui_3.05.jpg"
  ],
  "content_hash": "570868a16cb0448e",
  "level": 2
}
---

# Device commands > Device commands > Device commands

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| configureDevice | portIndex deviceIndex |  | Applies any changes that you made to configuration settings deviceIndex is the number shown in the device table as ID. Note The command works identically as the configureRouter and configureHost commands. |
| Note | The command works identically as the configureRouter and configureHost commands. |  |  |
| deleteDevice | portIndex deviceIndex |  | Deletes the specified devices. deviceIndex is the number shown in the device table as ID. Note The command works identically as the deleteRouter and deleteHost commands. |
| Note | The command works identically as the deleteRouter and deleteHost commands. |  |  |
| showDevices | [portList] |  | The button returns information for all devices. The showDevices action returns information for devices on the specified ports. If no ports are specified, returns information for all devices. |
| startDevices | [portList] |  | Starts the specified devices on the specified ports. If no ports are specified, then all devices are started. The button in the main frame starts all devices. The button on a port frame starts devices on that port. |
| stopDevices | [portList] |  | Stops the specified devices on the specified ports. If no ports are specified, then all devices are stopped. The button in the main frame stops all devices. The button on a port frame stops devices on that port. |

![unknown](topics/images/spirent_testcenter_gui_3.03.jpg) <!-- image_chunk: img_57e5b4f465d1fa15 -->

![unknown](topics/images/spirent_testcenter_gui_3.04.jpg) <!-- image_chunk: img_840540f304e3807c -->

![unknown](topics/images/spirent_testcenter_gui_3.05.jpg) <!-- image_chunk: img_0195a87274ef1b94 -->

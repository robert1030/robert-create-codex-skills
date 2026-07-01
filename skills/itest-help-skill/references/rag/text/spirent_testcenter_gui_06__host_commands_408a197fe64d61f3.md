---
{
  "chunk_id": "spirent_testcenter_gui_06__host_commands_408a197fe64d61f3",
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
    "Host commands"
  ],
  "anchor": "1358566",
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
    "topics/images/spirent_testcenter_gui_3.01.jpg",
    "topics/images/spirent_testcenter_gui_3.02.jpg"
  ],
  "content_hash": "408a197fe64d61f3",
  "level": 2
}
---

# Device commands > Device commands > Host commands

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| addHost | portIndex |  | Adds a new device to the list with role=Host . Only "Traffic Only" hosts are supported. |
| configureHost | portIndex deviceIndex | — None — | Applies any changes that you made to configuration settings deviceIndex is the number shown in the device table as ID. Note The command works identically as the configureDevice and configureRouter commands. |
| Note | The command works identically as the configureDevice and configureRouter commands. |  |  |
| deleteHost | portIndex deviceIndex | — None — | Deletes the specified host. deviceIndex is the number shown in the device table as ID. Note The command works identically as the deleteDevice and deleteRouter commands. |
| Note | The command works identically as the deleteDevice and deleteRouter commands. |  |  |
| showHosts | [portList] |  | Shows information about the 'host' parent object. The button returns information for all devices with role=Host. The showHosts action returns information for devices with role=Host on the specified ports. If no ports are specified, returns information for all devices with role=Host.. |

![unknown](topics/images/spirent_testcenter_gui_3.01.jpg) <!-- image_chunk: img_c38d0fd87413980c -->

![unknown](topics/images/spirent_testcenter_gui_3.02.jpg) <!-- image_chunk: img_2d5c5966790e6c09 -->

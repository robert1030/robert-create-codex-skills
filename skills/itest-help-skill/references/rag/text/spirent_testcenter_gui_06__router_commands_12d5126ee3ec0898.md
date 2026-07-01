---
{
  "chunk_id": "spirent_testcenter_gui_06__router_commands_12d5126ee3ec0898",
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
    "Router commands"
  ],
  "anchor": "1358673",
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
    "topics/images/spirent_testcenter_gui_3.08.jpg",
    "topics/images/spirent_testcenter_gui_2.09.jpg"
  ],
  "content_hash": "12d5126ee3ec0898",
  "level": 2
}
---

# Device commands > Device commands > Router commands

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| addRouter | portIndex |  | Adds a new device to the list with role=Router |
| configureRouter | portIndex deviceIndex | — None — | Applies any changes that you made to configuration settings deviceIndex is the number shown in the device table as ID. Note The command works identically as the configureDevice and configureHost commands. |
| Note | The command works identically as the configureDevice and configureHost commands. |  |  |
| deleteRouter | portIndex deviceIndex | — None — | Deletes the specified host. deviceIndex is the number shown in the device table as ID. Note The command works identically as the deleteDevice and deleteHost commands. |
| Note | The command works identically as the deleteDevice and deleteHost commands. |  |  |
| showRouters | [portList] |  | The button returns information for all devices with role=Router. The showRouters action returns information for devices with role=Router on the specified ports. If no ports are specified, returns information for all devices with role=Router.. |

![unknown](topics/images/spirent_testcenter_gui_3.08.jpg) <!-- image_chunk: img_752dd563f45eb72d -->

![unknown](topics/images/spirent_testcenter_gui_2.09.jpg) <!-- image_chunk: img_aa7deb17d1b3f862 -->

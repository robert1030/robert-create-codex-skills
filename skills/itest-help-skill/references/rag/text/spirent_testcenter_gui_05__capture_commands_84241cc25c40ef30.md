---
{
  "chunk_id": "spirent_testcenter_gui_05__capture_commands_84241cc25c40ef30",
  "source_file": "topics/spirent_testcenter_gui.05.htm",
  "source_original_path": "topics/spirent_testcenter_gui.05.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "Traffic commands"
  ],
  "heading_path": [
    "Traffic commands",
    "Traffic commands",
    "Capture commands"
  ],
  "anchor": "1361220",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_gui_2.15.jpg",
    "topics/images/spirent_testcenter_gui_2.16.jpg",
    "topics/images/spirent_testcenter_gui_2.18.jpg",
    "topics/images/spirent_testcenter_gui_2.20.jpg",
    "topics/images/spirent_testcenter_gui_2.21.jpg"
  ],
  "content_hash": "84241cc25c40ef30",
  "level": 2
}
---

# Traffic commands > Traffic commands > Capture commands

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| saveCapture | portIndex | — None — | Saves the captured items |
| showPacket | portIndex pktNumber |  | Returns the specified captured packet on the selected port |
| showPacketList | port startPkt pktCount |  | Returns information about the specified list of captured packets in table form |
| startCapture | [portList] | Selected port All ports | Starts capturing on all or selected ports |
| stopCapture | [portList] | Selected port All ports | Stops capture on all or selected ports. |
| StartLagCaptureCommand | PortSet[LAG port]. | Selected port All ports | Starts capture on the individual member ports of the LAG. |
| StopLagCaptureCommand | PortSet[LAG port]. | Same as above | Stops capture on the individual member ports of the LAG. |
| GetLagCaptureCommand | PortSet(LAG port) | Same as above | Merges capture of the individual member ports of the LAG. |

![unknown](topics/images/spirent_testcenter_gui_2.15.jpg) <!-- image_chunk: img_0d0b4bbabf26722e -->

![unknown](topics/images/spirent_testcenter_gui_2.16.jpg) <!-- image_chunk: img_3ac4fb61cfcb5385 -->

![unknown](topics/images/spirent_testcenter_gui_2.18.jpg) <!-- image_chunk: img_1e62d591c2aaa010 -->

![unknown](topics/images/spirent_testcenter_gui_2.20.jpg) <!-- image_chunk: img_4354f6c627fd0e6f -->

![unknown](topics/images/spirent_testcenter_gui_2.21.jpg) <!-- image_chunk: img_74de4280c97c40f1 -->

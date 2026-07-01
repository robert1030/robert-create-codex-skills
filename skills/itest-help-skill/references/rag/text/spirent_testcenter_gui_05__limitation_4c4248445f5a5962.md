---
{
  "chunk_id": "spirent_testcenter_gui_05__limitation_4c4248445f5a5962",
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
    "Stream block commands",
    "Limitation"
  ],
  "anchor": "1358948",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_gui_2.06.jpg",
    "topics/images/spirent_testcenter_gui_2.07.jpg",
    "topics/images/spirent_testcenter_gui_2.08.jpg",
    "topics/images/spirent_testcenter_gui.09.jpg",
    "topics/images/spirent_testcenter_gui.10.jpg",
    "topics/images/spirent_testcenter_gui_2.11.jpg",
    "topics/images/spirent_testcenter_gui_2.12.jpg"
  ],
  "content_hash": "4c4248445f5a5962",
  "level": 3
}
---

# Traffic commands > Traffic commands > Stream block commands > Limitation

When generating traffic, stream block will not work if it is inactive.

| Action | Arguments / Command property values | Button that captures the Action | Description |
| --- | --- | --- | --- |
| addStreamBlock | portIndex |  | Adds a raw stream block on the selected port. |
| configureStreamBlock | portIndex streamIndex |  | Enables or disables transmission on a specified stream for selected ports Select a stream block and click Edit. When you click OK in the editor, iTest captures a configure action. |
| deleteStreamBlock | portIndex streamIndex |  | Deletes the selected stream block |
| disableStreamBlock | portIdentifier [listOfStreamBlockIDs] | Appears in local toolbar on Traffic Generator page | Disables the specified stream blocks on the specified port. You can specify listOfStreamBlockIDs using any combination of stream block IDs and ranges, separated by commas. For example, 1, 3-5, 7 |
| enableStreamBlock | portIdentifier [listOfStreamBlockIDs] | Appears in local toolbar on Traffic Generator page | Enables the specified stream blocks on the specified port. You can specify listOfStreamBlockIDs using any combination of stream block IDs and ranges, separated by commas or spaces. For example, 1, 3-5, 7 |
| showStreamBlocks [portList] [enable/disable verbose] example: showStreamblocks 1 verbose => enable verbose. showStreamblocks 1 => disable verbose. |  | Gets the configuration property settings for all stream blocks. Enable Verbose: Queries all properties, including properties of children objects, for example, queries streamblocks and all content of /objects (emulated devices, ports, etc.). This may cause a delay in response. Disable Verbose: Queries includes only the parent object (not all children objects properties). hence Hence, reduces query effort and provides a a quicker response. Some of the removed streamblock properties are: BurstSize, FrameLengthDistribution, InterFrameGap, Load LoadUnit Priority, RxPorts, StartDelay Source Destination, etc |  |
| showStreamBlocksInGroup | group [subgroup] |  | Gets the configuration property settings for all stream blocks in the selected Traffic Group. showStreamblock command behavior to reduce request to stc server, using new argument for backward compatible named verbose. Here is new implementation: showStreamblock has a new argument called "verbose": |

![unknown](topics/images/spirent_testcenter_gui_2.06.jpg) <!-- image_chunk: img_aa2987e0e8aff7bd -->

![unknown](topics/images/spirent_testcenter_gui_2.07.jpg) <!-- image_chunk: img_0754b9099d2cd466 -->

![unknown](topics/images/spirent_testcenter_gui_2.08.jpg) <!-- image_chunk: img_36cdcf7e2c70c775 -->

![inline_icon](topics/images/spirent_testcenter_gui.09.jpg) <!-- image_chunk: img_7d14fd3aa27815d0 -->

![inline_icon](topics/images/spirent_testcenter_gui.10.jpg) <!-- image_chunk: img_d17fa4392d5389e3 -->

![unknown](topics/images/spirent_testcenter_gui_2.11.jpg) <!-- image_chunk: img_b71ff9e6749d296a -->

![unknown](topics/images/spirent_testcenter_gui_2.12.jpg) <!-- image_chunk: img_4fc67d91abf02363 -->

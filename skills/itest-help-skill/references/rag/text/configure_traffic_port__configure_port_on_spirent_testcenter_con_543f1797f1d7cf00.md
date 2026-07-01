---
{
  "chunk_id": "configure_traffic_port__configure_port_on_spirent_testcenter_con_543f1797f1d7cf00",
  "source_file": "topics/configure_traffic_port.htm",
  "source_original_path": "topics/configure_traffic_port.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter sessions",
    "Spirent TestCenter session window",
    "To configure traffic on a port"
  ],
  "heading_path": [
    "To configure traffic on a port",
    "To configure traffic on a port",
    "Configure Port on Spirent TestCenter Console page"
  ],
  "anchor": "1403840",
  "context_ids": [
    "configure_traffic_port"
  ],
  "index_keywords": [
    "Spirent TestCenter console page"
  ],
  "index_keyword_paths": [
    "configure port > Spirent TestCenter console page"
  ],
  "related_links": [],
  "images": [
    "topics/images/spirent_testcenter_gui_5.11.jpg",
    "topics/images/spirent_testcenter_gui_5.12.jpg"
  ],
  "content_hash": "543f1797f1d7cf00",
  "level": 3
}
---

# To configure traffic on a port > To configure traffic on a port > Configure Port on Spirent TestCenter Console page

To edit a port configuration file, load file, for example, a10G port configure file and change or add configuration as required. At the TestCenter console, enter Help to display the list of parameters/groups available for setting or modifying values, as required.

Show all properties or physical port, to view the properties that may be changed (notice that the example has some properties that has been disabled).

You may change properties as required and apply the new values to the device. If any property has been disabled for the port, your changes will not be applied. That is, changes applicable for 10 Gig Fiber cannot be applied to 10 Gig copper and vice versa. An error displays providing you the reason for failure.

> **Note:** Note For example: Cannot set value 'Copper_3M' for disabled property 'CableLength'. This argument is only enabled when 'Mediatype' argument pattern match 'Fiber_10_Gig\Fiber_40_Gig\Fiber_100_gig'.

![screenshot](topics/images/spirent_testcenter_gui_5.11.jpg) <!-- image_chunk: img_bd45d72b5f0cb32f -->

![screenshot](topics/images/spirent_testcenter_gui_5.12.jpg) <!-- image_chunk: img_a8f5d50f619f1bed -->

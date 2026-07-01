---
{
  "chunk_id": "emulation_6__controlling_emulation_for_devices_in_a_t_a4a51ec00b14caca",
  "source_file": "topics/emulation.6.htm",
  "source_original_path": "topics/emulation.6.htm",
  "toc_path": [
    "iTest Online Help",
    "Testing with Emulated Sessions",
    "Controlling emulation for devices in a topology"
  ],
  "heading_path": [
    "Controlling emulation for devices in a topology",
    "Controlling emulation for devices in a topology"
  ],
  "anchor": "1182173",
  "context_ids": [],
  "index_keywords": [
    "all devices in a topology",
    "controlling emulation"
  ],
  "index_keyword_paths": [
    "emulation > all devices in a topology",
    "topology > controlling emulation"
  ],
  "related_links": [],
  "images": [
    "topics/images/emulation_2.1.jpg",
    "topics/images/emulation_2.2.jpg",
    "topics/images/emulation_2.3.jpg"
  ],
  "content_hash": "a4a51ec00b14caca",
  "level": 1
}
---

# Controlling emulation for devices in a topology > Controlling emulation for devices in a topology



To Control emulation for all devices in a topology

This method is useful for controlling emulation in any test case that uses the topology with a single setting.

To control emulation settings for all devices In the topology while working in the Topology editor:

- On the main menu, click Topology > Emulation

The following three options are applied to all devices in the topology regardless of any current device setting:

Emulate All Device Responses: Regardless of the setting in the test case, use emulated responses if available (devices are shaded in teal)

Do not Emulate Any Device Responses: Regardless of the setting for the topology or for any test case, do not use emulated responses (devices are shaded in lilac)

Use Test Case Emulation Settings: Use the settings that are currently configured in any test case that uses any device in the topology.

The following two options control whether the emulation settings that might be defined for individual devices are used or not:

Enable Device Emulation Settings: Use the emulation settings (if any) defined for each device in the topology

Disable Device Emulation Settings: Do not use the emulation settings for any device in the topology (devices are shaded in lilac)

- Right-click in a blank area of the canvas and select one of the following options (as described earlier):

Enable Device Emulation Settings (default)

Disable Device Emulation Settings

![inline_icon](topics/images/emulation_2.1.jpg) <!-- image_chunk: img_447ef0252661900f -->

![inline_icon](topics/images/emulation_2.2.jpg) <!-- image_chunk: img_2e0fed0b670280dc -->

![inline_icon](topics/images/emulation_2.3.jpg) <!-- image_chunk: img_2834f3ca5a2a4f01 -->

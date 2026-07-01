---
{
  "chunk_id": "tgen_cmds_harness__comments_79a1e2d658a1467a",
  "source_file": "topics/tgen_cmds_harness.htm",
  "source_original_path": "topics/tgen_cmds_harness.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Avalanche API Commands"
  ],
  "heading_path": [
    "Avalanche API Commands",
    "Avalanche API Commands",
    "av_connect",
    "Comments"
  ],
  "anchor": "1305837",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "79a1e2d658a1467a",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_connect > Comments

After this command call is completed, the device will be added to the device list under the PhysicalChassisManager object. If Avalanche Automation is already connected to this device, then it gets the latest state from the device and returns the existent handle. The av_connect command runs in synchronous mode by default. The mode can be changed by using the-executesyschronous Boolean option.

If a -type is not specified, the Appliance platform will be assumed and tried. If Avalanche TclAPI fails to connect, then the Spirent TestCenter chassis is assumed to be the hardware platform, and the connection will be retried.

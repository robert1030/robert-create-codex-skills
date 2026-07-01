---
{
  "chunk_id": "tgen_cmds_harness__example_70352a1a0c58f22a",
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
    "av_login",
    "Example"
  ],
  "anchor": "1306155",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/spirent_avalanche_5.1.jpg"
  ],
  "content_hash": "70352a1a0c58f22a",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_login > Example

av_login

av_login john

av_login john johns_password monitor

av_login –workspace johns_workspace1

av_login john johns_password monitor –workspace johns_workspace1

av_login –temp-workspace

> **Note:** Note The av_login command uses workspace Default by default, when nothing is defined. If Default workspace is already in use by another TclAPI session, or by the GUI (remember that Default workspace name is also used by the GUI), then the av_login command will fail with the following error message:

![screenshot](topics/images/spirent_avalanche_5.1.jpg) <!-- image_chunk: img_24c3aab6e22ae770 -->

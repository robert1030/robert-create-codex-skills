---
{
  "chunk_id": "tgen_cmds_harness__example_400806be2decb28a",
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
    "Example"
  ],
  "anchor": "1305842",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "400806be2decb28a",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_connect > Example

%av_connect 10.72.55.80

physicalchassis1

When run in synchronous mode, the return value is the handle of the device.

%av_connect 10.72.55.80 –executesynchronous false

279When run in asynchronous mode, the return value is the request id of the command.

%av_connect 10.34.76.52 –type stc

physicalchassis2

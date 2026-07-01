---
{
  "chunk_id": "tgen_cmds_harness__example_81885602e8d57f14",
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
    "av_create",
    "Example"
  ],
  "anchor": "1305900",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "81885602e8d57f14",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_create > Example

set hProject [av_create project -under system1 -name Project1]

set hTest [av_create tests -under $hProject -name Test1 -testType deviceComplex ]

set hServerProfile [av_create ServerProfiles -under $hProject -name ServerProfile -applicationProtocol HTTP -http.keepAlive on]

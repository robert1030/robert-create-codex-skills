---
{
  "chunk_id": "tgen_cmds_harness__comments_79f88fb1b444797d",
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
    "av_apply",
    "Comments"
  ],
  "anchor": "1305705",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "79f88fb1b444797d",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_apply > Comments

The apply command saves the configuration, performs validation, uploads test configuration to devices, and runs (or reruns) the test. This call is asynchronous, so the client will get control right after the call. The standard async_method_completed event will be sent after the test is started; the specific test state events will also be sent. For more information, please refer to Avalanche™ Automation Programmers’ Reference guide.

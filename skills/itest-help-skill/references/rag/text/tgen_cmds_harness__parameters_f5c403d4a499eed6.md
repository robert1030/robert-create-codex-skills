---
{
  "chunk_id": "tgen_cmds_harness__parameters_f5c403d4a499eed6",
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
    "Parameters"
  ],
  "anchor": "1305712",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "f5c403d4a499eed6",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_apply > Parameters

| Name | Type | Description |
| --- | --- | --- |
| testHandle | handle | The handle of test to be started. |
| trial | Boolean (1|0) | If true, then the trial test will be started. If false, then a license validation error may occur. |
| continueIfAlreadyRunning | Boolean (1|0) | If true, then the test will be started, even there is another test running on the device. If it is the same test, then the system will reconnect to it. Otherwise, the test on the device will be aborted. |
| removeOldTest | Boolean (1|0) | If true, then the previous test will be removed from the device, before this test starts. |
| rerun | Boolean (1|0) | If true, then the test will be rerun. This saves time for tests that you have already run (full or trial), because they do not need to be reloaded. If false (default), the test will be run in the normal manner. |

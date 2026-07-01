---
{
  "chunk_id": "tgen_cmds_harness__description_676c1035629ff479",
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
    "av_logout",
    "Description"
  ],
  "anchor": "1306214",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "676c1035629ff479",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_logout > Description

Closes the session, stops any running test, saves any non-saved data on the disk, and stops the Avalanche Automation (java) process by default, when either no argument is provided or when the shutdown argument is provided (see examples). The only difference between the shutdown and no-shutdown arguments is stopping or not stopping the Avalanche Automation (java) process. The av_logout command with the no-shutdown argument will leave the Avalanche Automation (java) process running after the user logs out.

If the temporary workspace is used (see av_login command description), the av_logout command deletes all the tests and test results that were created during the session.

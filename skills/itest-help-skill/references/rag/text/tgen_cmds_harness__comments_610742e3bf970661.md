---
{
  "chunk_id": "tgen_cmds_harness__comments_610742e3bf970661",
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
    "Comments"
  ],
  "anchor": "1306129",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "610742e3bf970661",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_login > Comments

The av_login command should be called first to start a session, before retrieving or manipulating the data model with any other Avalanche TclAPI command (the exception is the av_getSessions command).

The <username> argument defines the name of the user that is used by the av_reserve command to reserve ports. If the username is not specified, then the system username defined by the resident Operating System is used.

The av_login command starts a new session, if the specified mode is manage, which is also the default mode. Therefore, when no mode parameter is specified, a new session is started. The av_login command connects to an existing session, if the specified mode is monitor. (Note: The password parameter is currently ignored.)

To go to monitor mode, you must use the same username/password/workspace parameters specified when you first created the session in manage mode.

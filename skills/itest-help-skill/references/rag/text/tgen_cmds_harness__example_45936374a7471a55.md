---
{
  "chunk_id": "tgen_cmds_harness__example_45936374a7471a55",
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
  "anchor": "1306134",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "45936374a7471a55",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_login > Example

To go to manage session:

#create session

av_login

#get current workspace name

av_get system1 -workspace

Default

To go to monitor session:

#create monitor session

#login parameters must be the same as those used to create

#the manage session (user name, password workspace name)

av_login <user_name> <password> monitor -workspace <workspace_name>

# You can confirm that it is the monitor session by using# av_config or av_create command

av_create project -under system1 -name project_0002

(insufficient_rights) You must manage this session to perform this action

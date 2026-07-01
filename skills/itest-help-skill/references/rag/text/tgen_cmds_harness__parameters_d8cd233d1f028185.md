---
{
  "chunk_id": "tgen_cmds_harness__parameters_d8cd233d1f028185",
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
    "Parameters"
  ],
  "anchor": "1306210",
  "context_ids": [
    "tgen_cmds_harness"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "d8cd233d1f028185",
  "level": 4
}
---

# Avalanche API Commands > Avalanche API Commands > av_login > Parameters

| Name | Type | Description |
| --- | --- | --- |
| userName | string | Name of the user for which data will be processed. By default, the name of the current user will be used. |
| password | string | User's password. Currently ignored. |
| mode | string | Mode of the session. Permitted values are manage or monitor. The default mode is manage. |
| -workspace | key | Use to log in to an existing custom workspace or to create a custom workspace and log in to it. |
| workspaceName | string | Workspace name, should be a valid directory name. Mandatory if -workspace key was used. |
| -temp-workspace | key | Use it to log in to temporary workspace. Warning: The temporary workspace is destroyed with all of your created tests after you log out. Be sure to copy the data you want to save before you log out. |

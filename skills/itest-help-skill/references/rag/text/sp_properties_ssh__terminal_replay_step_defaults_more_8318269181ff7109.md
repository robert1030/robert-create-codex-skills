---
{
  "chunk_id": "sp_properties_ssh__terminal_replay_step_defaults_more_8318269181ff7109",
  "source_file": "topics/sp_properties_ssh.htm",
  "source_original_path": "topics/sp_properties_ssh.htm",
  "toc_path": [
    "iTest Online Help",
    "SSH Sessions",
    "Session profile property settings for SSH sessions"
  ],
  "heading_path": [
    "Session profile property settings for SSH sessions",
    "Session profile property settings for SSH sessions",
    "Terminal > Replay > Step Defaults > More"
  ],
  "anchor": "1260665",
  "context_ids": [
    "sp_properties_ssh"
  ],
  "index_keywords": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions",
    "configuring",
    "session profile property settings for"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "SSH sessions > configuring",
    "SSH sessions > session profile property settings for",
    "configuring > SSH sessions",
    "session profile property settings > SSH sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "8318269181ff7109",
  "level": 2
}
---

# Session profile property settings for SSH sessions > Session profile property settings for SSH sessions > Terminal > Replay > Step Defaults > More

| Pages to fetch | For responses that are longer than be displayed on a single screen, devices often provide a page-control prompt that enables you to view one screen of text at a time (for example - - more - -). Specify the number of pages to fetch when the more prompt appears (zero means get all pages). If the setting is non-zero, then iTest retrieves that number of pages and then terminates the output from the session's response by sending the command specified for the More: Quit Command property. Default: 100 |
| --- | --- |
| Device does not remove more prompt. Remove more prompt from response. | Some devices do not remove the text of the more prompt from the text of the response. (For these devices, you will see the more prompt remain at the bottom of the page even after you press the continuation character — typically the spacebar.) Check the box to eliminate the more prompt text from the response that is saved by iTest. Default: unchecked |
| Use BELL character to detect end of more pages | Some devices do not remove the more prompt from the screen even after you press the continuation or quit character. Such devices often use the audible bell to alert the user that they have reached the end of the response. Check the box to cause iTest to use the bell as its indicator that the response is complete. Default: checked |

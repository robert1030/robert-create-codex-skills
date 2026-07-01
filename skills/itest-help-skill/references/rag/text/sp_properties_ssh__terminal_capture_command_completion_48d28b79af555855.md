---
{
  "chunk_id": "sp_properties_ssh__terminal_capture_command_completion_48d28b79af555855",
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
    "Terminal > Capture > Command Completion"
  ],
  "anchor": "1089738",
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
  "content_hash": "48d28b79af555855",
  "level": 2
}
---

# Session profile property settings for SSH sessions > Session profile property settings for SSH sessions > Terminal > Capture > Command Completion

Specify the code that the device interprets as command completion characters (that is, characters that cause the command interpreter to echo as much of the complete command text as it can).

Default: tab (\t)

To determine the encoding for a character set like Ctrl-Z, click Record and then press the keys. iTest places the character code into the text box. Click Add to add the code to the set of command completion characters.

Limitations of the Record feature:

- For the Alt key, iTest captures only the last key pressed. For example, Alt+q is recorded as “q”.

- Function keys are not recorded.

| Command completion requires ENTER key | Most devices respond immediately with command completion when they encounter one of the characters specified for the Command completion characters property. Set this property to TRUE, if the device, to perform command completion, requires that you press ENTER after typing one of the characters specified for the Command completion characters property. Default: unchecked |
| --- | --- |

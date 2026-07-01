---
{
  "chunk_id": "session_profile_properties_serial__terminal_capture_command_completion_3ed3bab85832a834",
  "source_file": "topics/session_profile_properties_serial.htm",
  "source_original_path": "topics/session_profile_properties_serial.htm",
  "toc_path": [
    "iTest Online Help",
    "Serial Sessions",
    "Session profile property settings for Serial sessions"
  ],
  "heading_path": [
    "Session profile property settings for Serial sessions",
    "Session profile property settings for Serial sessions",
    "Terminal > Capture > Command Completion"
  ],
  "anchor": "1090639",
  "context_ids": [
    "session_profile_properties_serial"
  ],
  "index_keywords": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Serial property settings",
    "Serial sessions",
    "configuring",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Serial sessions > configuring",
    "Serial sessions > session profile property settings",
    "configuring > Serial sessions",
    "property settings > Serial sessions",
    "session profiles > Serial property settings"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "3ed3bab85832a834",
  "level": 2
}
---

# Session profile property settings for Serial sessions > Session profile property settings for Serial sessions > Terminal > Capture > Command Completion

Specify the code that the device interprets as command completion characters (that is, characters that cause the command interpreter to echo as much of the complete command text as it can).

Default: tab (\t )

To determine the encoding for a character set like Ctrl-Z, click Record and then press the keys. iTest places the character code into the text box. Click Add to add the code to the set of command completion characters.

Limitations of the Record feature:

- For the Alt key, iTest captures only the last key pressed. For example, Alt+q is recorded as “q”.

- Function keys are not recorded.

| Command completion requires ENTER key | Most devices respond immediately with command completion when they encounter one of the characters specified for the Command completion characters property. Set this property to TRUE, if the device, to perform command completion, requires that you press ENTER after typing one of the characters specified for the Command completion characters property. Default: Unchecked |
| --- | --- |

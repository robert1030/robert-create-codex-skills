---
{
  "chunk_id": "session_profile_properties_telnet__terminal_capture_command_completion_088ef8efcb1721e1",
  "source_file": "topics/session_profile_properties_telnet.htm",
  "source_original_path": "topics/session_profile_properties_telnet.htm",
  "toc_path": [
    "iTest Online Help",
    "Telnet Sessions",
    "Session profile property settings for Telnet sessions"
  ],
  "heading_path": [
    "Session profile property settings for Telnet sessions",
    "Session profile property settings for Telnet sessions",
    "Terminal > Capture > Command Completion"
  ],
  "anchor": "1090639",
  "context_ids": [
    "session_profile_properties_telnet"
  ],
  "index_keywords": [
    "Additional connection information property",
    "Configuring Telnet",
    "HA mode",
    "High Availability Mode property",
    "Negotiate Telnet options",
    "Telnet options",
    "Telnet property settings",
    "Telnet sessions",
    "configuring",
    "configuring socket",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Negotiate Telnet options",
    "Telnet > configuring socket",
    "Telnet options",
    "Telnet sessions > configuring",
    "Telnet sessions > session profile property settings",
    "configuring > Telnet sessions",
    "property settings > Telnet sessions",
    "session profiles > Telnet property settings",
    "socket > Configuring Telnet"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "088ef8efcb1721e1",
  "level": 2
}
---

# Session profile property settings for Telnet sessions > Session profile property settings for Telnet sessions > Terminal > Capture > Command Completion

Specify the code that the device interprets as command completion characters (that is, characters that cause the command interpreter to echo as much of the complete command text as it can).

Default: tab (\t )

To determine the encoding for a character set like Ctrl-Z, click Record and then press the keys. iTest places the character code into the text box. Click Add to add the code to the set of command completion characters.

Limitations of the Record feature:

- For the Alt key, iTest captures only the last key pressed. For example, Alt+q is recorded as “q”.

- Function keys are not recorded.

| Command completion requires ENTER key | Most devices respond immediately with command completion when they encounter one of the characters specified for the Command completion characters property. Set this property to TRUE, if the device, to perform command completion, requires that you press ENTER after typing one of the characters specified for the Command completion characters property. Default: Unchecked |
| --- | --- |

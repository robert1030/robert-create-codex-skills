---
{
  "chunk_id": "sp_properties_ssh__terminal_2b387cad3afe7bf6",
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
    "Step Defaults > Command",
    "Terminal"
  ],
  "anchor": "1331635",
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
  "content_hash": "2b387cad3afe7bf6",
  "level": 3
}
---

# Session profile property settings for SSH sessions > Session profile property settings for SSH sessions > Step Defaults > Command > Terminal

| Local echo | Default: Unchecked Uncheck Local Echo to indicate that the device echoes characters typed at the command line. In this case, iTest ignores echoed characters so that the command text is not added to the echoed response text. For example, if the device does echo and you set Local echo to unchecked, then typing abc at the prompt would result in the characters aabbcc appearing on the command line. Check Local Echo to indicate that the device does not echo typed characters. |
| --- | --- |
| Local line editing | Default: Unchecked. Check Local line editing to indicate that you may edit line. |
| Expand all tabs to spaces | Default: Unchecked Check the box to convert each tab character in the response to display 8 space characters in the Response view. This setting can occasionally result in poorly formatted response text in the Response view. Uncheck the box to retain each tab character unchanged. |
| Scroll to show cursor | Default: Checked While a long command is executing, you might scroll up in the session window to view response data from earlier in the session. When Scroll to show cursor is checked, iTest jumps to the cursor (prompt) when the currently executing command finishes executing. |
| Terminal string | Default: ANSI Specify the terminal type. Do not change this setting. |
| Scrollback lines | Default: 10000 Specify the number of command/response lines to display in the session window. These are the lines that you scroll through to view command/response data from earlier in the session. |
| Encoding | Optional. Specify the encoding type to use to translate bytes into Java characters. You can either type the encoding name into the box or select it from the list. The list includes all encoding types that are supported by the operating system. Default: UTF-8 |

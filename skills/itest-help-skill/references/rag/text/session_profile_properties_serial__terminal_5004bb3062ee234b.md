---
{
  "chunk_id": "session_profile_properties_serial__terminal_5004bb3062ee234b",
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
    "Serial Port > High Availability",
    "Terminal"
  ],
  "anchor": "1289969",
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
  "content_hash": "5004bb3062ee234b",
  "level": 3
}
---

# Session profile property settings for Serial sessions > Session profile property settings for Serial sessions > Serial Port > High Availability > Terminal

| Local echo | Default: Unchecked Uncheck Local Echo to indicate that the device echoes characters typed at the command line. In this case, iTest ignores echoed characters so that the command text is not added to the echoed response text. For example, if the device does echo and you set Local echo to unchecked, then typing abc at the prompt would result in the characters aabbcc appearing on the command line. Check Local Echo to indicate that the device does not echo typed characters. |
| --- | --- |
| Local line editing | Default: Unchecked. Check Local line editing to indicate that you may edit line. |
| Expand all tabs to spaces | Default: Unchecked Check the box to convert each tab character in the response to display 8 space characters in the Response view. This setting can occasionally result in poorly formatted response text in the Response view. Uncheck the box to retain each tab character unchanged. |
| Scroll to show cursor | Default: Checked While a long command is executing, you might scroll up in the session window to view response data from earlier in the session. When Scroll to show cursor is checked, iTest jumps to the cursor (prompt) when the currently executing command finishes executing. |
| Terminal string | Default: ANSI Specify the terminal type. Do not change this setting. |
| Scrollback lines | Default: 10000 Specify the number of command/response lines to display in the session window. These are the lines that you scroll through to view command/response data from earlier in the session. |
| Encoding | Optional. Specify the encoding type to use to translate bytes into Java characters. You can either type the encoding name into the box or select it from the list. The list includes all encoding types that are supported by the operating system. Default: UTF-8 |

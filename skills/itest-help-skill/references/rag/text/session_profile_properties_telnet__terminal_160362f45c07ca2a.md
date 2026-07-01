---
{
  "chunk_id": "session_profile_properties_telnet__terminal_160362f45c07ca2a",
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
    "Telnet > High Availability",
    "Terminal"
  ],
  "anchor": "1286242",
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
  "content_hash": "160362f45c07ca2a",
  "level": 3
}
---

# Session profile property settings for Telnet sessions > Session profile property settings for Telnet sessions > Telnet > High Availability > Terminal

| Local echo | Default: Unchecked Uncheck Local Echo to indicate that the device echoes characters typed at the command line. In this case, iTest ignores echoed characters so that the command text is not added to the echoed response text. For example, if the device does echo and you set Local echo to unchecked, then typing abc at the prompt would result in the characters aabbcc appearing on the command line. Check Local Echo to indicate that the device does not echo typed characters. |
| --- | --- |
| Local line editing | Default: Unchecked. Check Local line editing to indicate that you may edit line. |
| Expand all tabs to spaces | Default: Unchecked Check the box to convert each tab character in the response to display 8 space characters in the Response view. This setting can occasionally result in poorly formatted response text in the Response view. Uncheck the box to retain each tab character unchanged. |
| Scroll to show cursor | Default: Checked While a long command is executing, you might scroll up in the session window to view response data from earlier in the session. When Scroll to show cursor is checked, iTest jumps to the cursor (prompt) when the currently executing command finishes executing. |
| Terminal string | Default: ANSI Specify the terminal type. Do not change this setting. |
| Scrollback lines | Default: 10000 Specify the number of command/response lines to display in the session window. These are the lines that you scroll through to view command/response data from earlier in the session. |
| Encoding | Optional. Specify the encoding type to use to translate bytes into Java characters. You can either type the encoding name into the box or select it from the list. The list includes all encoding types that are supported by the operating system. Default: UTF-8 |

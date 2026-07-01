---
{
  "chunk_id": "wireshark_session_example__terminal_dbc4bca2385d84c3",
  "source_file": "topics/wireshark_session_example.htm",
  "source_original_path": "topics/wireshark_session_example.htm",
  "toc_path": [
    "iTest Online Help",
    "Wireshark sessions",
    "Session profile property settings for Wireshark sessions"
  ],
  "heading_path": [
    "Session profile property settings for Wireshark sessions",
    "Session profile property settings for Wireshark sessions",
    "Wireshark",
    "Terminal"
  ],
  "anchor": "1306390",
  "context_ids": [
    "sp_properties_wireshark",
    "wireshark_session_example"
  ],
  "index_keywords": [
    "Wireshark session",
    "Wireshark sessions",
    "defining",
    "example"
  ],
  "index_keyword_paths": [
    "Wireshark sessions > defining",
    "Wireshark sessions > example",
    "defining > Wireshark sessions",
    "examples > Wireshark session"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "dbc4bca2385d84c3",
  "level": 3
}
---

# Session profile property settings for Wireshark sessions > Session profile property settings for Wireshark sessions > Wireshark > Terminal

| Local echo | Default: Unchecked Uncheck Local Echo to indicate that the device echoes characters typed at the command line. In this case, iTest ignores echoed characters so that the command text is not added to the echoed response text. For example, if the device does echo and you set Local echo to unchecked, then typing abc at the prompt would result in the characters aabbcc appearing on the command line. Check Local Echo to indicate that the device does not echo typed characters. |
| --- | --- |
| Local line editing | Default: Unchecked. Check Local line editing to indicate that you may edit line. |
| Expand all tabs to spaces | Default: Unchecked Check the box to convert each tab character in the response to display 8 space characters in the Response view. This setting can occasionally result in poorly formatted response text in the Response view. Uncheck the box to retain each tab character unchanged. |
| Scroll to show cursor | Default: Checked While a long command is executing, you might scroll up in the session window to view response data from earlier in the session. When Scroll to show cursor is checked, iTest jumps to the cursor (prompt) when the currently executing command finishes executing. |
| Terminal string | Default: ANSI Specify the terminal type. Do not change this setting. |
| Scrollback lines | Default: 10000 Specify the number of command/response lines to display in the session window. These are the lines that you scroll through to view command/response data from earlier in the session. |
| Encoding | Optional. Specify the encoding type to use to translate bytes into Java characters. You can either type the encoding name into the box or select it from the list. The list includes all encoding types that are supported by the operating system. Default: UTF-8 |

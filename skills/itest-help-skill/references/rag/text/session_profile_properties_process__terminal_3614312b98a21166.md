---
{
  "chunk_id": "session_profile_properties_process__terminal_3614312b98a21166",
  "source_file": "topics/session_profile_properties_process.htm",
  "source_original_path": "topics/session_profile_properties_process.htm",
  "toc_path": [
    "iTest Online Help",
    "Process Sessions",
    "Session profile property settings for Process sessions"
  ],
  "heading_path": [
    "Session profile property settings for Process sessions",
    "Session profile property settings for Process sessions",
    "Process",
    "Terminal"
  ],
  "anchor": "1257963",
  "context_ids": [
    "session_profile_properties_process"
  ],
  "index_keywords": [
    "Process session properties",
    "Process sessions",
    "configuring",
    "configuring Process",
    "defining",
    "local processes",
    "starting"
  ],
  "index_keyword_paths": [
    "Process session properties",
    "Process sessions > configuring",
    "Process sessions > defining",
    "Process sessions > starting",
    "configuring > Process sessions",
    "local processes > starting",
    "property settings > Process sessions",
    "sessions > configuring Process",
    "starting > local processes"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "3614312b98a21166",
  "level": 3
}
---

# Session profile property settings for Process sessions > Session profile property settings for Process sessions > Process > Terminal

| Local echo | Default: Unchecked Uncheck Local Echo to indicate that the device echoes characters typed at the command line. In this case, iTest ignores echoed characters so that the command text is not added to the echoed response text. For example, if the device does echo and you set Local echo to unchecked, then typing abc at the prompt would result in the characters aabbcc appearing on the command line. Check Local Echo to indicate that the device does not echo typed characters. |
| --- | --- |
| Local line editing | Default: Unchecked. Check Local line editing to indicate that you may edit line. |
| Expand all tabs to spaces | Default: Unchecked Check the box to convert each tab character in the response to display 8 space characters in the Response view. This setting can occasionally result in poorly formatted response text in the Response view. Uncheck the box to retain each tab character unchanged. |
| Scroll to show cursor | Default: Checked While a long command is executing, you might scroll up in the session window to view response data from earlier in the session. When Scroll to show cursor is checked, iTest jumps to the cursor (prompt) when the currently executing command finishes executing. |
| Terminal string | Default: ANSI Specify the terminal type. Do not change this setting. |
| Scrollback lines | Default: 10000 Specify the number of command/response lines to display in the session window. These are the lines that you scroll through to view command/response data from earlier in the session. |
| Encoding | Optional. Specify the encoding type to use to translate bytes into Java characters. You can either type the encoding name into the box or select it from the list. The list includes all encoding types that are supported by the operating system. Default: UTF-8 |

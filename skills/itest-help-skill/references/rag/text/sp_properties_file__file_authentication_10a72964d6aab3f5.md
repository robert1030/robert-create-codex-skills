---
{
  "chunk_id": "sp_properties_file__file_authentication_10a72964d6aab3f5",
  "source_file": "topics/sp_properties_file.htm",
  "source_original_path": "topics/sp_properties_file.htm",
  "toc_path": [
    "iTest Online Help",
    "File sessions",
    "Session profile property settings for File sessions"
  ],
  "heading_path": [
    "Session profile property settings for File sessions",
    "Session profile property settings for File sessions",
    "File > Authentication"
  ],
  "anchor": "1210859",
  "context_ids": [
    "sp_properties_file"
  ],
  "index_keywords": [
    "File property settings",
    "File sessions",
    "configuring",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "File sessions > configuring",
    "File sessions > session profile property settings",
    "configuring > File sessions",
    "property settings > File sessions",
    "session profiles > File property settings"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "10a72964d6aab3f5",
  "level": 2
}
---

# Session profile property settings for File sessions > Session profile property settings for File sessions > File > Authentication

| Username | Optional. Specify the username used to connect to access the file. |
| --- | --- |
| Password | Optional. Specify the password. The text is masked here and in all locations where it is used. |
| Key |  |
| Passphrase |  |

File > Large Response

| Enable large response truncation | Select these options to manage large session responses. When not selected, all the options below are not available for selection Truncate responses above given number of line. Enable execution message upon truncation Enable execution message upon truncation Write response to disk upon truncation (for Command prompt, Bash, SSH, Serial, and Telnet sessions) When selected, after executing a test, the Execution view a warning message displays, for example: The response is truncated. See itest-response_YYYYMMDD-HHMMSS(t1)(step-2) in tmp dir. 2 2 main t1 terminal new_testcase.fftc |  | Truncate responses above given number of line. |  | Enable execution message upon truncation |  | Enable execution message upon truncation |  | Write response to disk upon truncation (for Command prompt, Bash, SSH, Serial, and Telnet sessions) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | Truncate responses above given number of line. |  |  |  |  |  |  |  |  |
|  | Enable execution message upon truncation |  |  |  |  |  |  |  |  |
|  | Enable execution message upon truncation |  |  |  |  |  |  |  |  |
|  | Write response to disk upon truncation (for Command prompt, Bash, SSH, Serial, and Telnet sessions) |  |  |  |  |  |  |  |  |
| Truncate response above the given number of lines | Enter the number of lines to truncate. For example, 10. When you execute a test with this option, you may verify the response in the Response view, which displays 10 lines of response along with the message (for example): ### Response has been truncated. See itest-response_YYYYMMDD-HHMMSS(t1)(step-2) in tmp dir ### |  |  |  |  |  |  |  |  |
| Enable execution message upon truncation | Select to view/verify the message in Execution |  |  |  |  |  |  |  |  |
| Write response to disk upon truncation | Select to save response to disk. Note This option is available only for: Command prompt, Bash, SSH, Serial, and Telnet sessions When this option is not selected and you execute a test, you may notice that no response file is generated. That is, no files of the format (in the %temp% folder) after execution of commands: itest-response_YYYYMMDD-HHMMSS(session-profile)XXXXXXXXXXXXXXXX.txt | Note | This option is available only for: Command prompt, Bash, SSH, Serial, and Telnet sessions |  |  |  |  |  |  |
| Note | This option is available only for: Command prompt, Bash, SSH, Serial, and Telnet sessions |  |  |  |  |  |  |  |  |

Terminal

| Local echo | Default: Unchecked Uncheck Local Echo to indicate that the device echoes characters typed at the command line. In this case, iTest ignores echoed characters so that the command text is not added to the echoed response text. For example, if the device does echo and you set Local echo to unchecked, then typing abc at the prompt would result in the characters aabbcc appearing on the command line. Check Local Echo to indicate that the device does not echo typed characters. |
| --- | --- |
| Local line editing | Default: Unchecked. Check Local line editing to indicate that you may edit line. |
| Expand all tabs to spaces | Default: Unchecked Check the box to convert each tab character in the response to display 8 space characters in the Response view. This setting can occasionally result in poorly formatted response text in the Response view. Uncheck the box to retain each tab character unchanged. |
| Scroll to show cursor | Default: Checked While a long command is executing, you might scroll up in the session window to view response data from earlier in the session. When Scroll to show cursor is checked, iTest jumps to the cursor (prompt) when the currently executing command finishes executing. |
| Terminal string | Default: ANSI Specify the terminal type. Do not change this setting. |
| Scrollback lines | Default: 10000 Specify the number of command/response lines to display in the session window. These are the lines that you scroll through to view command/response data from earlier in the session. |
| Encoding | Optional. Specify the encoding type to use to translate bytes into Java characters. You can either type the encoding name into the box or select it from the list. The list includes all encoding types that are supported by the operating system. Default: UTF-8 |

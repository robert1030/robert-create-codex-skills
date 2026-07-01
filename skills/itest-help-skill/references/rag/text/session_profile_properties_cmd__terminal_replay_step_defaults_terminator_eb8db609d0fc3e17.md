---
{
  "chunk_id": "session_profile_properties_cmd__terminal_replay_step_defaults_terminator_eb8db609d0fc3e17",
  "source_file": "topics/session_profile_properties_cmd.htm",
  "source_original_path": "topics/session_profile_properties_cmd.htm",
  "toc_path": [
    "iTest Online Help",
    "Command Prompt sessions",
    "Session profile property settings for Command Prompt sessions (Microsoft Windows command line)"
  ],
  "heading_path": [
    "Session profile property settings for Command Prompt sessions (Microsoft Windows command line)",
    "Session profile property settings for Command Prompt sessions (Microsoft Windows command line)",
    "Note for Linux and Unix users:",
    "Terminal > Replay > Step Defaults > Terminator"
  ],
  "anchor": "1427322",
  "context_ids": [
    "session_profile_properties_cmd"
  ],
  "index_keywords": [
    "Command Prompt sessions",
    "Windows cmd command line sessions",
    "Windows cmd command-line sessions",
    "configuring",
    "configuring Command Prompt",
    "session properties",
    "starting"
  ],
  "index_keyword_paths": [
    "Command Prompt sessions > configuring",
    "Windows cmd command-line sessions > starting",
    "configuring > Command Prompt sessions",
    "opening > Windows cmd command line sessions",
    "property settings > Command Prompt sessions",
    "session properties",
    "sessions > configuring Command Prompt",
    "starting > Windows cmd command-line sessions"
  ],
  "related_links": [
    "capture_view_working_with.htm#1132545"
  ],
  "images": [],
  "content_hash": "eb8db609d0fc3e17",
  "level": 3
}
---

# Session profile property settings for Command Prompt sessions (Microsoft Windows command line) > Session profile property settings for Command Prompt sessions (Microsoft Windows command line) > Note for Linux and Unix users: > Terminal > Replay > Step Defaults > Terminator

| Line terminator | Note This property setting has no effect for Command Prompt sessions. | Note | This property setting has no effect for Command Prompt sessions. |
| --- | --- | --- | --- |
| Note | This property setting has no effect for Command Prompt sessions. |  |  |

Terminal > Replay > Step Defaults > Response

| Treat LF as CRLF | Note This property setting has no effect for Command Prompt sessions. | Note | This property setting has no effect for Command Prompt sessions. |
| --- | --- | --- | --- |
| Note | This property setting has no effect for Command Prompt sessions. |  |  |
| Filename to write response to | Specify the URI of a file to write the responses into. You can use field replacements in the text of the URI to allow the test case to set the filename at runtime. For example, file:subdirectory_name/[param file_to_create] Default: <none> Note The full text of the response is written to the file, regardless of the Number of lines to keep setting. See the following associated properties: Append response to file Response header Number of lines to keep Write echo to file Write prompt to file | Note | The full text of the response is written to the file, regardless of the Number of lines to keep setting. |
| Note | The full text of the response is written to the file, regardless of the Number of lines to keep setting. |  |  |
| Response header | If you save responses to a file by specifying a value for the Filename to write response to property, then: You may want to specify a text string that should appear before each block of response text. For example: +-+-+-+-+- Next Response Starts Here -+-+-+-+-+ Default: <none> |  |  |
| Number of lines to keep | For very long responses, you might not want to keep all of the response text (as displayed in the Response view for the selected step while working in the Test Report editor or in the Test Case editor). Specify the maximum number of lines to keep for any single response. Specify 0 (zero) to keep all lines. Note If you specify a URI in the Filename to write response to property, then all lines in the response are written to the file, regardless of this setting. Default: 10,000 | Note | If you specify a URI in the Filename to write response to property, then all lines in the response are written to the file, regardless of this setting. |
| Note | If you specify a URI in the Filename to write response to property, then all lines in the response are written to the file, regardless of this setting. |  |  |
| Append response to file | If you save responses to a file by specifying a value for the Filename to write response to property, then: Check the box to append each new response to the file specified in the Filename to write response to property. Uncheck the box to replace the text of the file specified in the Filename to write response to property with the most recent response. As a result, the file will hold only the last response in the session. See the Filename to write response to and Response header properties. Default: Checked |  |  |
| Write echo to file | If you save responses to a file by specifying a value for the Filename to write response to property, then: Check the box to include any echoed characters in the saved response. Default: Checked |  |  |
| Write prompt to file | If you save responses to a file by specifying a value for the Filename to write response to property, then: Check the box to include the last line of the response in the saved response (in command-line applications, this is typically the prompt after the response). Uncheck the box to not save the last line of the response to the file (the prompt at the beginning of the response where the command was typed is still saved). Default: checked |  | Check the box to include the last line of the response in the saved response (in command-line applications, this is typically the prompt after the response). |
|  | Check the box to include the last line of the response in the saved response (in command-line applications, this is typically the prompt after the response). |  |  |
|  | Uncheck the box to not save the last line of the response to the file (the prompt at the beginning of the response where the command was typed is still saved). |  |  |
| Note Options Write echo to file and Write prompt to file do not work in capture mode. These options are available for Replay mode only. The example below shows how the commands/responses are echoed in these scenarios. When Append to file, Write echo to file, and Write prompt to file options are selected: prompt>command response text etc etc prompt> Write echo to file When Write echo to file is not selected response text etc etc prompt> When Write prompt to file is not selected prompt>command response text etc etc When Append to file, Write echo to file, and Write prompt to file options are not selected response text etc etc This is because the Terminal > Replay options are used to replay the captured steps. That is, replay the steps captured via test case execution or replayed from the Capture View (Working in the Capture view). | Note |  |  |
| Note |  |  |  |
|  | When Append to file, Write echo to file, and Write prompt to file options are selected: |  |  |
|  | When Write echo to file is not selected |  |  |
|  | When Write prompt to file is not selected |  |  |
|  | When Append to file, Write echo to file, and Write prompt to file options are not selected |  |  |
| Include Command timestamps | The Include command timestamps supports logging commands and responses into file. Default: Include command Timestamps logging is disabled. When enabled, the timestamps will be logged before each executed session command. The Timestamp format is: YYYY/MM/DD hh:mm:ss, where: YYYY is a four-digit year MM indicates a two-digit month of the year DD indicates a two-digit day of that month hh refers to a zero-padded hour between 00 and 23 mm refers to a zero-padded minute between 00 and 59 ss refers to a zero-padded second between 00 and 59 Note The command timestamps is supported only in Replay mode. |  | YYYY is a four-digit year |
|  | YYYY is a four-digit year |  |  |
|  | MM indicates a two-digit month of the year |  |  |
|  | DD indicates a two-digit day of that month |  |  |
|  | hh refers to a zero-padded hour between 00 and 23 |  |  |
|  | mm refers to a zero-padded minute between 00 and 59 |  |  |
|  | ss refers to a zero-padded second between 00 and 59 |  |  |
| Note | The command timestamps is supported only in Replay mode. |  |  |

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

Terminal > Replay > Step Defaults > More

| Pages to fetch | For responses that are longer than be displayed on a single screen, devices often provide a page-control prompt that enables you to view one screen of text at a time (for example - - more - -). Specify the number of pages to fetch when the more prompt appears (zero means get all pages). If the setting is non-zero, then iTest retrieves that number of pages and then terminates the output from the session's response by sending the command specified for the More: Quit Command property. Default: 100 |
| --- | --- |
| Device does not remove more prompt. Remove more prompt from response | Note This property setting has no effect for Command Prompt sessions. |
| Note | This property setting has no effect for Command Prompt sessions. |
| Use BELL character to detect end of more pages | Note This property setting has no effect for Command Prompt sessions. |
| Note | This property setting has no effect for Command Prompt sessions. |

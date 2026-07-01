---
{
  "chunk_id": "preferences_syslog__syslog_2e3dd5560d2a12aa",
  "source_file": "topics/preferences_syslog.htm",
  "source_original_path": "topics/preferences_syslog.htm",
  "toc_path": [
    "iTest Online Help",
    "Syslog Sessions",
    "Session profile property settings for Syslog sessions"
  ],
  "heading_path": [
    "Session profile property settings for Syslog sessions",
    "Session profile property settings for Syslog sessions",
    "Syslog"
  ],
  "anchor": "1089955",
  "context_ids": [
    "preferences_syslog",
    "sp_properties_syslog"
  ],
  "index_keywords": [
    "Syslog sessions",
    "preference settings",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Syslog sessions > preference settings",
    "Syslog sessions > session profile property settings",
    "preference settings > Syslog sessions",
    "session profile property settings > Syslog sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "2e3dd5560d2a12aa",
  "level": 2
}
---

# Session profile property settings for Syslog sessions > Session profile property settings for Syslog sessions > Syslog

Each Syslog session monitors the syslog messages that arrive at the built-in iTest syslog server (visible in the Syslog view). While the syslog server receives all messages, any syslog session can filter the messages based on the following property settings in the session profile.

As a result of configuring one or more of the settings, only the messages that meet the filter settings appear in the session window. This enables your test cases to analyze the particular responses (messages) of interest and to ignore irrelevant messages.

| Syslog ports | Optional: Specify a comma-separated list of ports for the syslog server to listen on for this session. This property affects only sessions that use this profile. The syslog server always accepts messages over the ports that you specify on the Preferences page. The ports that you specify here determine additional ports for any session that started from the session profile. For example, if the preference setting is 514, and the Syslog ports property specifies port 600, then, when the session starts, the syslog server listens on both ports 514 and 600. Default: 514 |
| --- | --- |
| Max # of messages to keep before aging | Specify the maximum count of messages to list in the SNMP Traps view. When the number of messages reaches the limit, the oldest messages are deleted. Default: 250 |
| Default timeout for wait command | Specify how long to wait (seconds) for the response to a wait command. Zero (0) means wait 'forever”. Default: 30 seconds |
| List of hostnames to accept | Optional. Specify one or more hosts in a comma-separated list. Only messages from specified hosts will appear in the resulting session window. Note This property affects only sessions that use this profile. The syslog server always accepts messages from any host on its specified ports. Default: <blank>, which means that messages from any host are accepted. |
| Note | This property affects only sessions that use this profile. The syslog server always accepts messages from any host on its specified ports. |
| List of facility #'s to accept | Optional. Specify one or more facility numbers in a comma-separated list. Only messages with specified facility numbers will appear in the resulting session window. This property affects only sessions that use this profile. The syslog server always accepts messages with any facility number. Default: <blank>, which means that messages with any facility number are accepted. |
| Minimum severity # | Optional. Specify the minimum severity. Only messages with specified facility numbers will appear in the resulting session window. Smaller severity numbers represent higher severity. Therefore, messages with severity values at the specified level and numerically lower will be included while those with numerically higher values will be excluded. Note This property affects only sessions that use this profile. The syslog server always accepts messages of any severity. Default: <blank>, which means that messages of any severity are accepted. |
| Note | This property affects only sessions that use this profile. The syslog server always accepts messages of any severity. |
| List of tags to accept | Optional. Specify one or more tags in a comma-separated list. Only messages with the specified tags will appear in the resulting session window. Note This property affects only sessions that use this profile. The syslog server always accepts messages with any tag on its specified ports. Default: <blank>, which means that messages with any tag are accepted. |
| Note | This property affects only sessions that use this profile. The syslog server always accepts messages with any tag on its specified ports. |

Large Response

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

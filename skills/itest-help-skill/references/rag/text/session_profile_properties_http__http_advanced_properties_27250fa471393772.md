---
{
  "chunk_id": "session_profile_properties_http__http_advanced_properties_27250fa471393772",
  "source_file": "topics/session_profile_properties_http.htm",
  "source_original_path": "topics/session_profile_properties_http.htm",
  "toc_path": [
    "iTest Online Help",
    "HTTP Sessions",
    "Session profile property settings for HTTP sessions"
  ],
  "heading_path": [
    "Session profile property settings for HTTP sessions",
    "Session profile property settings for HTTP sessions",
    "HTTP > Advanced Properties"
  ],
  "anchor": "1409889",
  "context_ids": [
    "session_profile_properties_http"
  ],
  "index_keywords": [
    "HTTP session profiles",
    "HTTP sessions",
    "configuring",
    "configuring HTTP",
    "defining",
    "property settings",
    "starting"
  ],
  "index_keyword_paths": [
    "HTTP sessions > configuring",
    "HTTP sessions > defining",
    "HTTP sessions > property settings",
    "HTTP sessions > starting",
    "configuring > HTTP sessions",
    "defining > HTTP session profiles",
    "property settings > HTTP sessions",
    "sessions > configuring HTTP"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "27250fa471393772",
  "level": 2
}
---

# Session profile property settings for HTTP sessions > Session profile property settings for HTTP sessions > HTTP > Advanced Properties

For a session that cannot determine MIME type and character encoding from POSTs, you can use the following properties to specify the settings. You can also specify HTTP header values.

| MIME type | Optional. Specify the MIME type information (for the posted content) to send when POSTing content to a server. Note This setting is used to tell the server the MIME type of the data. iTest does not format the data according to the MIME type that you specify. You are responsible to format the data properly. This information becomes part of the HTTP Content-Type header field for any POST or GET operation. Here is example content for the field: Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-4 Default: application/x-www-form-urlencoded | Note | This setting is used to tell the server the MIME type of the data. iTest does not format the data according to the MIME type that you specify. You are responsible to format the data properly. |
| --- | --- | --- | --- |
| Note | This setting is used to tell the server the MIME type of the data. iTest does not format the data according to the MIME type that you specify. You are responsible to format the data properly. |  |  |
| Charset | Optional. Specify the character set information (for the posted content) to send when POSTing content to a server. This information becomes part of the HTTP Content-Type header field for any POST or GET operation. Here is example content for the field: Content-Type: application/x-www-form-urlencoded; charset=ISO-8859-4 Default : UTF-8. If UTF-8 is unavailable, then the default for the current locale is used. |  |  |
| Header | Optional. Specify HTTP header values, one per line, using<header>:<spaceCharacter><value> format. The specified values override default values ordinarily supplied by iTest. For example, with each request, iTest specifies the "User-agent" as "User-Agent: Java/1.6.0_13". You might specify a different user agent using: User-agent: User-Agent: Java/1.6.0_14 |  |  |

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

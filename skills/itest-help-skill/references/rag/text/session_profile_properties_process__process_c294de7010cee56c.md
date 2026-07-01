---
{
  "chunk_id": "session_profile_properties_process__process_c294de7010cee56c",
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
    "Process"
  ],
  "anchor": "1206961",
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
  "content_hash": "c294de7010cee56c",
  "level": 2
}
---

# Session profile property settings for Process sessions > Session profile property settings for Process sessions > Process

| Working Directory | Optional. The initial working directory to use for submitting commands when the process starts. |
| --- | --- |
| Use custom environment | When you uncheck the box, then the environment variables specified for the Environment property are passed to new processes. When you check the box, the current environment variables are passed to processes that are launched with run or start. |
| Environment | Optional. Applies only If you check Use custom environment, The environment variables that you specify here overwrite or supplement the current environment variables for launched processes. Type the environment variable settings as a list of name-value pairs, separated by semicolon or colon (; or :). All spaces are ignored. For example, var_name=value; var2=value2 The PATH variable for batch executables You cannot use the Environment property to specify a PATH variable (for example, PATH=D:/my_batch_path/) to enable you to run executables in that path. To run such an executable, you must specify its full path. If your System PATH variable contains the path to a folder (for example, D:/path/) that contains batch executables (for example, test.bat), you can use commands like run test.bat or start test.bat in Process sessions. You cannot use commands like run test or start test. |
| Kill running processes after session end | Optional. Uncheck the box to allow running processes to persist after the Process session ends. This setting typically applies when you use the Process start action. |

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

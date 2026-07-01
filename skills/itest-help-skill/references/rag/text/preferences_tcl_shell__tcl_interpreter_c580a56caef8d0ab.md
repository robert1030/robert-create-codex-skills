---
{
  "chunk_id": "preferences_tcl_shell__tcl_interpreter_c580a56caef8d0ab",
  "source_file": "topics/preferences_tcl_shell.htm",
  "source_original_path": "topics/preferences_tcl_shell.htm",
  "toc_path": [
    "iTest Online Help",
    "Tcl Shell Sessions",
    "Session profile property settings for Tcl Shell sessions"
  ],
  "heading_path": [
    "Session profile property settings for Tcl Shell sessions",
    "Session profile property settings for Tcl Shell sessions",
    "Tcl Interpreter"
  ],
  "anchor": "1250699",
  "context_ids": [
    "preferences_tcl_shell",
    "session_profile_properties_tclsh"
  ],
  "index_keywords": [
    "Tcl Shell  sessions",
    "Tcl Shell sessions",
    "preference settings",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Tcl Shell sessions > preference settings",
    "Tcl Shell sessions > session profile property settings",
    "preference settings > Tcl Shell sessions",
    "property settings > Tcl Shell  sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "c580a56caef8d0ab",
  "level": 2
}
---

# Session profile property settings for Tcl Shell sessions > Session profile property settings for Tcl Shell sessions > Tcl Interpreter

| Use Global Tcl interpreter during execution | Rather than start a new interpreter for the session, use the kernel context Tcl interpreter. Default: Unchecked |
| --- | --- |
| Path to Tcl interpreter | Use this option only if your application must use a particular interpreter. Type the directory path to the Tcl interpreter executable. Default: <None> |
| Path to Tcl Library | Type the directory path to the Tcl library used by the interpreter. To use additional libraries, use the In addition, use paths specified in the TCLLIBPATH environment variable property. Default: <None> |
| In addition, use paths specified in the TCLLIBPATH environment variable | Check the box to make use of libraries specified by TCLLIBPATH environment variable. Default: Checked |
| Initialization script | Optional. Specify a script to evaluate before starting the session with the device. |

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

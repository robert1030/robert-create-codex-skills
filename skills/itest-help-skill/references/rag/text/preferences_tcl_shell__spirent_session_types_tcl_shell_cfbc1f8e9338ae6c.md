---
{
  "chunk_id": "preferences_tcl_shell__spirent_session_types_tcl_shell_cfbc1f8e9338ae6c",
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
    "Spirent > Session Types > Tcl Shell"
  ],
  "anchor": "1114227",
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
  "content_hash": "cfbc1f8e9338ae6c",
  "level": 2
}
---

# Session profile property settings for Tcl Shell sessions > Session profile property settings for Tcl Shell sessions > Spirent > Session Types > Tcl Shell

| Interpreter | Note We recommend that you use the default Auto-select setting. Auto-select: iTest selects the interpreter using the following process: 1. If an interpreter is specified in the Use the specified Tcl interpreter property, then use that interpreter. 2. Otherwise, launch the first installed Tcl interpreter that iTest finds in the PATH environment variable. 3. If no interpreter is specified in the path variable, use iTest's built-in interpreter (base on JACL). Built-in: Use iTest's internal JACL Java-based Tcl interpreter. Because JACL does not support any C/C++ extensions, most traffic generator devices will not work in this interpreter. Use the specified Tcl interpreter: This option is not often needed. With this option, you specify a particular Tcl interpreter in the text box. Use this option only if your application must use a particular interpreter. Default: Auto-select | Note | We recommend that you use the default Auto-select setting. | 1. | If an interpreter is specified in the Use the specified Tcl interpreter property, then use that interpreter. | 2. | Otherwise, launch the first installed Tcl interpreter that iTest finds in the PATH environment variable. | 3. | If no interpreter is specified in the path variable, use iTest's built-in interpreter (base on JACL). |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Note | We recommend that you use the default Auto-select setting. |  |  |  |  |  |  |  |  |
| 1. | If an interpreter is specified in the Use the specified Tcl interpreter property, then use that interpreter. |  |  |  |  |  |  |  |  |
| 2. | Otherwise, launch the first installed Tcl interpreter that iTest finds in the PATH environment variable. |  |  |  |  |  |  |  |  |
| 3. | If no interpreter is specified in the path variable, use iTest's built-in interpreter (base on JACL). |  |  |  |  |  |  |  |  |
| Log Tcl commands to a console | Check the box to cause iTest to log the submitted commands to a console window. Note This setting is used only if you have specified a Tcl interpreter other than the built-in interpreter. Default: unchecked | Note | This setting is used only if you have specified a Tcl interpreter other than the built-in interpreter. |  |  |  |  |  |  |
| Note | This setting is used only if you have specified a Tcl interpreter other than the built-in interpreter. |  |  |  |  |  |  |  |  |
| Log Tcl responses to a console | Check the box to cause iTest to log the responses to Tcl commands to a console window. Note This setting is used only if you have specified a Tcl interpreter other than the built-in interpreter. Default: unchecked | Note | This setting is used only if you have specified a Tcl interpreter other than the built-in interpreter. |  |  |  |  |  |  |
| Note | This setting is used only if you have specified a Tcl interpreter other than the built-in interpreter. |  |  |  |  |  |  |  |  |
| Remote shell logging | Use remote shell logging. Default: unchecked |  |  |  |  |  |  |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

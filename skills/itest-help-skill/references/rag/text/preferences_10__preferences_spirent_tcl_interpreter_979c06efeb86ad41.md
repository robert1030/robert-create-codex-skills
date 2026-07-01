---
{
  "chunk_id": "preferences_10__preferences_spirent_tcl_interpreter_979c06efeb86ad41",
  "source_file": "topics/preferences.10.htm",
  "source_original_path": "topics/preferences.10.htm",
  "toc_path": [
    "iTest Online Help",
    "Configuring iTest Preferences",
    "Preferences: Spirent > Tcl Interpreter"
  ],
  "heading_path": [
    "Preferences: Spirent > Tcl Interpreter",
    "Preferences: Spirent > Tcl Interpreter"
  ],
  "anchor": "1246560",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "979c06efeb86ad41",
  "level": 1
}
---

# Preferences: Spirent > Tcl Interpreter > Preferences: Spirent > Tcl Interpreter

iTest uses a Tcl interpreter during execution. There is no need to install a Tcl interpreter if you do not already have one because, by default, iTest follows this process when determining which Tcl interpreter to use:

- Use the first interpreter found in the system PATH variable. If not available, then:

- Use the interpreter specified for the Use the specified Tcl interpreter property. If not available, then:

- Use a built-in interpreter (base on JACL).

If, however, you want iTest to use an external Tcl interpreter (one installed on the same computer as iTest), we recommend that you configure the system PATH to include the preferred Tcl interpreter, rather than specifying the path in this preference.

| Interpreter | Note: We recommend that you use the default Auto-select setting. Auto-select: iTest selects the interpreter using the following process: If an interpreter is specified in the Use the specified Tcl interpreter property, then use that interpreter. 2. Otherwise, launch the first installed Tcl interpreter that iTest finds in the path environment variable. 3. If no interpreter is specified in the path variable, use iTest's built-in interpreter (base on JACL). Built-in: Use iTest's internal JACL Java-based Tcl interpreter. Because JACL does not support any C/C++ extensions, most traffic generator devices will not work in this interpreter. (If you need to specify a particular Tcl interpreter for your device, find the device's software in the Session Types properties group in this topic, for example, Session Types > Ixia Traffic). Use the specified Tcl interpreter: This option is not often needed. With this option, you specify a particular Tcl interpreter in the text box. Use this option only if your application must use a particular interpreter. Default: Auto-select |  | If an interpreter is specified in the Use the specified Tcl interpreter property, then use that interpreter. | 2. | Otherwise, launch the first installed Tcl interpreter that iTest finds in the path environment variable. | 3. | If no interpreter is specified in the path variable, use iTest's built-in interpreter (base on JACL). |
| --- | --- | --- | --- | --- | --- | --- | --- |
|  | If an interpreter is specified in the Use the specified Tcl interpreter property, then use that interpreter. |  |  |  |  |  |  |
| 2. | Otherwise, launch the first installed Tcl interpreter that iTest finds in the path environment variable. |  |  |  |  |  |  |
| 3. | If no interpreter is specified in the path variable, use iTest's built-in interpreter (base on JACL). |  |  |  |  |  |  |
| Log Tcl commands to a console | Log all commands to the Tcl interpreter to a console. Default: unchecked |  |  |  |  |  |  |
| Log Tcl responses to a console | Log all responses from the Tcl interpreter to a console. Default: unchecked |  |  |  |  |  |  |
| Remote shell logging | Use remote shell logging. Default: unchecked |  |  |  |  |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

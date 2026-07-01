---
{
  "chunk_id": "python_sessions__create_and_run_a_python_session_eab178fac73a43df",
  "source_file": "topics/python_sessions.htm",
  "source_original_path": "topics/python_sessions.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Sessions",
    "Create a new Python session profile"
  ],
  "heading_path": [
    "Create a new Python session profile",
    "Create a new Python session profile",
    "Create and run a Python Session"
  ],
  "anchor": "1453451",
  "context_ids": [
    "python_sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "session_profile_concept.htm#1304370",
    "session_profile_property_settings.htm#1483852",
    "preferences.12.htm#1253533",
    "field_replacements_tasks.htm#"
  ],
  "images": [
    "topics/images/python.1.jpg",
    "topics/images/py_session_profile.png",
    "topics/images/py_initialization_script.png",
    "topics/images/py_additional_modules.png"
  ],
  "content_hash": "eab178fac73a43df",
  "level": 2
}
---

# Create a new Python session profile > Create a new Python session profile > Create and run a Python Session

1. Ensure that the Python session profile is properly configured. Specify the path to Python interpreter, and if required, define the initialization scripts, module path, change the size of the large response, terminal color, size, and font.

This topic describes the property settings that you can configure for session profiles. For basic information on configuring a session, see Session profiles: Session configuration settings. For a detailed description of how iTest uses the settings, see About property settings.

> **Note:** Note If you have already saved a device or session profile document, then you do not need to configure the settings again. See About property settings.

The first group of properties appears on the Start a New Session page (the Start tab of the Session Profile editor). To access the other settings, click .

| Path to interpreter | Enter the path to the interpreter to be used for this particular session. If you do not specify a path to the interpreter, iTest uses the path specified in the preferences setting. See Preferences: Spirent > Python Interpreter. |
| --- | --- |
| Working directory | Indicates the initial working directory to use for submitting commands when the Python session starts. If the Working directory is not set, the working directory path is set to the project root directory, when the Python session is launched. Execution on iTestRT: If Working directory is not set and the session profile is in an external itar, then the current working directory will be set to the temp path for execution (where the exploded contents of downloaded projects exist). Execution on Velocity Agent: If Working directory is not set then the current working directory will be the temp path the agent uses for execution (where the exploded contents of downloaded projects exist). If Working directory is set as a relative value, the working directory path is set relative to the project's root directory, when the Python session is launched. The Working directory value supports a variable (ex: [path]) for field substitution during execution. See “Field Replacements”. Note If Working directory is set (absolute or reference) and if the folder does not exist, the Open step will fail during when executing this step and an error message displays. |
|  | If the Working directory is not set, the working directory path is set to the project root directory, when the Python session is launched. |
|  | If Working directory is set as a relative value, the working directory path is set relative to the project's root directory, when the Python session is launched. |
|  | The Working directory value supports a variable (ex: [path]) for field substitution during execution. See “Field Replacements”. |
| Note | If Working directory is set (absolute or reference) and if the folder does not exist, the Open step will fail during when executing this step and an error message displays. |
| Initialization script | Enter a script that iTest will invoke automatically when launching the Python session. Note The syntax of the contents is not validated when it is entered or edited. When you launch the session, the script (from initialization script) will run and display the script output. |
| Note | The syntax of the contents is not validated when it is entered or edited. |

| Additional Modules | The directory path entered here is used to search and locate additional modules and importing modules. Add: Enter path and the Add button becomes available. Click Add to include path to the list above. Both absolute path and relative path is supported. Browse: Click Browse, navigate to the location that should be searched to import additional module,. and click OK to add the path to the list. Subsequent paths added will be appended to the list. You may edit the list of path Delete: Select the path and click delete to remove the path from the search list. Launch Python session and notice that both absolute path and relative paths are valid. Files will be Imported from both relative or absolute paths. |
| --- | --- |

You may also define path(s) in the OS environment variable PYTHONPATH and iTest will include it in the module search list. Create PYTHONPATH environment variable in global variables.

PYTHONPATH set on the local environment identifies the folder where the additional modules are placed, so that iTest can include this path in the search list and import modules.

Large Responses

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

![unknown](topics/images/python.1.jpg) <!-- image_chunk: img_baae774ffffbaca5 -->

![screenshot](topics/images/py_session_profile.png) <!-- image_chunk: img_b08343a46e4feca0 -->

![screenshot](topics/images/py_initialization_script.png) <!-- image_chunk: img_03bb3c154f8a7a50 -->

![screenshot](topics/images/py_additional_modules.png) <!-- image_chunk: img_f68a65004869d9e5 -->

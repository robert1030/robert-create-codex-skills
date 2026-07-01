---
{
  "chunk_id": "command_for_info__info_subcommands_for_directories_uris_an_5a25904ba1b9a213",
  "source_file": "topics/command_for_info.htm",
  "source_original_path": "topics/command_for_info.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "info commands",
    "Commands for returning information: info"
  ],
  "heading_path": [
    "Commands for returning information: info",
    "Commands for returning information: info",
    "‘info’ subcommands for directories, URIs, and workspaces"
  ],
  "anchor": "1765047",
  "context_ids": [
    "command_for_info"
  ],
  "index_keywords": [
    "info",
    "info command",
    "info env",
    "info env command",
    "info homeDir",
    "info homeDir command",
    "info hostIp",
    "info hostIp command",
    "info hostName",
    "info hostName command",
    "info issueCount",
    "info issueCount command",
    "info paramFile",
    "info paramFile command",
    "info platform",
    "info platform command",
    "info profile",
    "info profile command",
    "info status",
    "info status command",
    "info step report",
    "info step report command",
    "info step sessionId",
    "info step sessionId command",
    "info step testCase",
    "info step testCase command",
    "info tempDir",
    "info tempDir command",
    "info testCaseFile",
    "info testCaseFile command",
    "info testCaseName",
    "info testCaseName command",
    "info testCaseProject",
    "info testCaseProject command",
    "info testCaseProjectPath",
    "info testCaseProjectPath command",
    "info testReport id",
    "info testReport id command",
    "info threadId",
    "info threadId command",
    "info time",
    "info time command",
    "info timestamp",
    "info timestamp command",
    "info user",
    "info user command",
    "info version",
    "info version command",
    "info workingDir",
    "info workingDir command",
    "info workspacePath",
    "info workspacePath command"
  ],
  "index_keyword_paths": [
    "commands > info",
    "commands > info env",
    "commands > info homeDir",
    "commands > info hostIp",
    "commands > info hostName",
    "commands > info issueCount",
    "commands > info paramFile",
    "commands > info platform",
    "commands > info profile",
    "commands > info status",
    "commands > info step report",
    "commands > info step sessionId",
    "commands > info step testCase",
    "commands > info tempDir",
    "commands > info testCaseFile",
    "commands > info testCaseName",
    "commands > info testCaseProject",
    "commands > info testCaseProjectPath",
    "commands > info testReport id",
    "commands > info threadId",
    "commands > info time",
    "commands > info timestamp",
    "commands > info user",
    "commands > info version",
    "commands > info workingDir",
    "commands > info workspacePath",
    "info command",
    "info env command",
    "info homeDir command",
    "info hostIp command",
    "info hostName command",
    "info issueCount command",
    "info paramFile command",
    "info platform command",
    "info profile command",
    "info status command",
    "info step report command",
    "info step sessionId command",
    "info step testCase command",
    "info tempDir command",
    "info testCaseFile command",
    "info testCaseName command",
    "info testCaseProject command",
    "info testCaseProjectPath command",
    "info testReport id command",
    "info threadId command",
    "info time command",
    "info timestamp command",
    "info user command",
    "info version command",
    "info workingDir command",
    "info workspacePath command"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "5a25904ba1b9a213",
  "level": 2
}
---

# Commands for returning information: info > Commands for returning information: info > ‘info’ subcommands for directories, URIs, and workspaces

The following command returns the appropriate information in iTestGUI but returns blank when executing on Velocity Agent: info('workspacePath')

The table below lists the command and description of the information returned.

| Command | Description |
| --- | --- |
| info homeDir ?uri? info('homeDir', 'uri') | Returns the path to the home directory of the current user. The format of the path is appropriate for the operating system (for example / or \). Use the optional uri argument to return the directory in the “file:/” URI format, used where iTest requires a URI argument. Examples info homeDir on a Windows computer might return C:\Documents and Settings\myName This form of the return string does not work with iTest items that require URIs, so you would use: info homeDir uri returns: file:/C:/Documents and Settings/myName |
| info paramFile ?path? info('paramFile', 'path') | Returns the fully-qualified URI of the current parameter file. (For example, project://my_ project/parameter_files/file_name.ffpt) If you use the optional path argument, then the URI is not returned. Instead, the command returns the path to the file in the format appropriate for the operating system. Note When executed in Python returns empty, as there is no there is no param file defined for execution. |
| Note | When executed in Python returns empty, as there is no there is no param file defined for execution. |
| info profile ?path? info('profile', 'path') | Returns the fully-qualified URI of the session profile (if any) associated with the currently executing step. (For example, project://my_ project/session_profiles/file_name.ffsp) If you use the optional path argument, then the URI is not returned. Instead, the command returns the path to the file in the format appropriate for the operating system. Note When executed in Python returns empty, as there is no current step defined for execution. |
| Note | When executed in Python returns empty, as there is no current step defined for execution. |
| info tempDir ?uri? info('tempDir', 'uri') | Returns the path to the temporary directory of the current user. The format of the path is appropriate for the operating system (for example / or \). Use the optional uri argument to return the directory in the “file:/” URI format, used where iTest requires a URI argument. Examples info tempDir on a Windows computer might return C:\Users\myName\Temp\ This form of the return string does not work with iTest items that require URIs, so you would use: info tempDir uri returns: file:/C:/Users/myName/Temp/ |
| info testCaseFile {current|main} ?path? info('testCaseFile', ['current'|'main'], 'path') | The current argument returns the fully-qualified URI of the test case that contains the currently executing step. (For example, project://my_ project/test_cases/file_name.fftc) The main argument returns the fully-qualified URI of the test case for which you clicked Execute. If you use the optional path argument, then the URI is not returned. Instead, the command returns the path to the file specified by either main or current. The format of the path is appropriate for the operating system. Python Automation Library (spirentSLC) returns different value: info('testCaseFile', 'main') and info('testCaseFile', 'current') return the current test case file name. |
| info testCaseName {current|main} info('testCaseName', ['current'|'main']) | Get the test case file name only (no URI and no file extension). The current argument returns only the file name of the test case that contains the currently executing step. The main argument returns only the file name of the test case for which you clicked Execute. Python Automation Library (spirentSLC) returns different value: info('testCaseName', 'main') and info('testCaseName', 'current') return the current Python file name. |
| info procedure ?arguments? info('procedure') | Returns the test case procedure name. Python Automation Library (spirentSLC) returns Python procedure name |
| info testCaseProject {current|main} info('testCaseProject', ['current'|'main']) | If you use the current argument, then the command returns the name of the project for the test case that contains the currently executing step. If you use the main argument, then the command returns the name of the project for the main test case (the test case for which you clicked Execute). Note When executing Python scripts (e.g., a Tcl test case exported to Python), the command displays a message saying that the info command is not supported. |
| Note | When executing Python scripts (e.g., a Tcl test case exported to Python), the command displays a message saying that the info command is not supported. |
| info testCaseProjectPath {current|main} info('testCaseProjectPath', ['current'|'main']) | If you use the current argument, then the command returns the path to the project of the test case that contains the currently executing step. The format of the path is appropriate for the operating system. If you use the main argument, then the command returns the path to the project of the test case for which you clicked Execute. Note When executing Python scripts (e.g., a Tcl test case exported to Python), the command displays a message saying that the info command is not supported. |
| Note | When executing Python scripts (e.g., a Tcl test case exported to Python), the command displays a message saying that the info command is not supported. |
| info time ?formatString? info('time', 'formatString') | Returns a the time in seconds since the current test case started. If you do not specify the optional format string, then the command uses Java's localized full timestamp format. An example formatString is “yyyy-MM-dd HH:mm:ss.SSS” (We use quotes to enclose the string because the space character appears in the string.) Format strings are based on Java's SimpleDateFormat. See http://java.sun.com/j2se/1.5.0/docs/api/java/text/SimpleDateFormat.html |
| info timestamp ?formatString? info('timestamp', 'formatString') | Returns a timestamp of current local time. If you do not specify the optional format string, then the command uses Java's localized full timestamp format. An example formatString is “yyyy-MM-dd HH:mm:ss.SSS” (We use quotes to enclose the string because the space character appears in the string.) Format strings are based on Java's SimpleDateFormat. See http://java.sun.com/j2se/1.5.0/docs/api/java/text/SimpleDateFormat.html |
| info version info('version') | Returns the version number of the current iTest instance Example 1: iTest 9.5.0: info('version') returns 9.5.0.202402120354 The following describes how to interpret iTest version format: Version format: <major>.<minor>.<patch>.<build number> Major version number is incremented for a major release and contains new features. Minor version number is incremented for a minor release and contains improvements and bug fixes. Patch version number is incremented for a release containing security and high-priority customer fixes. build number qualifier is internal numeration with date (first 6 numbers), build number (last 4 numbers), and time. Example 1: 9.5.0.202402120354 9 - major version, 5 - minor version, 0 - GA 202402120354 - build number (released on 2024, February 12 03:34 Example 2: 9.4.2.202311161550 9 - major version, 4 - minor version, 2 - patch 202311161550 - build number (Interpretation: 2023 November 16 15:50) |
|  | Major version number is incremented for a major release and contains new features. |
|  | Minor version number is incremented for a minor release and contains improvements and bug fixes. |
|  | Patch version number is incremented for a release containing security and high-priority customer fixes. |
|  | build number qualifier is internal numeration with date (first 6 numbers), build number (last 4 numbers), and time. |
| info workingDir ?uri? info('workingDir', 'uri') | Returns the path of the iTest computer’s “working” directory. The format of the path is appropriate for the operating system (for example / or \). Use the optional uri argument to return the directory in the “file:/” URI format, used where iTest requires a URI argument. Examples info workingDir on a Windows computer might return C:\Users\myName\Grinder\ This form of the return string does not work with iTest items that require URIs, so you would use: info workingDir uri returns: File:/C:/Users/myName/Grinder |
| info workspacePath info('workspacePath') | Returns the full path of the current workspace. |

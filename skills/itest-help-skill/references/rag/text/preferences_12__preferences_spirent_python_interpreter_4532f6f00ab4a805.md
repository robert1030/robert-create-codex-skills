---
{
  "chunk_id": "preferences_12__preferences_spirent_python_interpreter_4532f6f00ab4a805",
  "source_file": "topics/preferences.12.htm",
  "source_original_path": "topics/preferences.12.htm",
  "toc_path": null,
  "heading_path": [
    "Preferences: Spirent > Python Interpreter",
    "Preferences: Spirent > Python Interpreter"
  ],
  "anchor": "1253533",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "preferences.04.htm#1253281"
  ],
  "images": [
    "topics/images/prefer_python_interpreter.png"
  ],
  "content_hash": "4532f6f00ab4a805",
  "level": 1
}
---

# Preferences: Spirent > Python Interpreter > Preferences: Spirent > Python Interpreter

iTest uses a Python interpreter during execution, if set as Test Case preferred language. See Preferences: Spirent > General > General preference settings. There is no need to install a Python interpreter if you do not already have one because, by default, iTest follows this process when determining which Python interpreter to use:

- From “PATH” environment variable

- From Windows Registry on Windows

- From default paths of installation in Python installer

If you want iTest to use an external Python interpreter (one installed on the same computer as iTest), we recommend that you configure the system PATH to include the preferred Python interpreter, rather than specifying the path in this preference.

| Interpreter | Note: We recommend that you use the default Auto-select setting. Auto-select: iTest looks for python installed in the in default paths. Built-in: ITest looks for Python installed in the iTest installation folder. Built-in Python interpreter (v3.8.5) is available only for Windows platform, since Python on Ubuntu20 by default installs Python 3.8.2. Note If no Python3 interpreter found (and built-in interpreter is not available), a critical error will display each time you execute a test case or start a session that use Python as language. Use the specified Python interpreter: Select this option. Specify a particular version of Python interpreter in the text box or browser to the location of the particular Python installation and select Use this option only if your application must use a particular interpreter. Default: Auto-select Click Apply/Apply and Close | Note | If no Python3 interpreter found (and built-in interpreter is not available), a critical error will display each time you execute a test case or start a session that use Python as language. |
| --- | --- | --- | --- |
| Note | If no Python3 interpreter found (and built-in interpreter is not available), a critical error will display each time you execute a test case or start a session that use Python as language. |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/prefer_python_interpreter.png) <!-- image_chunk: img_78fb3f7e6438bf87 -->

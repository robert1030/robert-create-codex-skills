---
{
  "chunk_id": "itestrt_using__overview_itestrt_itest_runtime_79aef4ceebfca7ef",
  "source_file": "topics/itestrt_using.htm",
  "source_original_path": "topics/itestrt_using.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Runtime: iTestRT",
    "Overview: iTestRT (iTest Runtime)"
  ],
  "heading_path": [
    "Overview: iTestRT (iTest Runtime)",
    "Overview: iTestRT (iTest Runtime)"
  ],
  "anchor": "1157851",
  "context_ids": [
    "itestrt_using"
  ],
  "index_keywords": [
    "iTest Runtime",
    "licensing",
    "using"
  ],
  "index_keyword_paths": [
    "iTest Runtime > licensing",
    "iTest Runtime > using",
    "licensing > iTest Runtime"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "79aef4ceebfca7ef",
  "level": 1
}
---

# Overview: iTestRT (iTest Runtime) > Overview: iTestRT (iTest Runtime)

iTestRT is the command line (or “headless”) version of iTest that can operate on any iTest files whether or not they are held in a iTest workspace.

In headless mode (iTestRT) the uriToPath command extracts resources (file or directory) with the specified URI to a temporary directory and returns the target path (path of the extracted resources).

That is, the uriToPath in iTestRT, creates a temporary directory on the execution host and copies the contents of the URI in the command into the temporary directory (C:\Users\spirent\AppData\Local\Temp\itest\runtime1550678955762\Execution\uritopath_test.fftc). Each time the uriToPath command is executed in iTestRT, a new temporary directory will be created. Any temporary directories created during the test case are removed once the test case has completed.

> **Note:** Note Absolute paths cannot be used when executing the test cases from different systems (e.g., Windows-Linux). You may use relative paths if uriToPath fails to translate “workspace locations” to absolute paths for external programs.

> **Note:** For example, if you execute test case in "project://relativePath/test_cases/" directory: Copy files in the project using eval [file copy sourceURI destinationURI].

> **Note:** Note In iTestRT on Windows, displaying GBK characters (in listPrompts output) requires you to switch code page to 936. Use the following command before test execution: chcp 936.

Follow these steps to install new code pages:

- Press Windows+X to display the Power User menu and select the Control Panel.

- Open Region setting dialog and go to the Administrative tab.

- Click Change system locale and select Chinese (Simplified, China), click OK, and then reboot Windows.

---
{
  "chunk_id": "pal_python_automation_library_overview__overview_10465a9c4862d3ea",
  "source_file": "topics/pal_python_automation_library_overview.htm",
  "source_original_path": "topics/pal_python_automation_library_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Automation Library",
    "Overview"
  ],
  "heading_path": [
    "Overview",
    "Overview"
  ],
  "anchor": "1460886",
  "context_ids": [
    "pal_python_automation_library_overview"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "10465a9c4862d3ea",
  "level": 1
}
---

# Overview > Overview

> **Note:** Note iTest installer includes PyDev (Python IDE) and RED (Robot Editor) plugins for ease of your work. See the following links for more details:

- PyDev: https://marketplace.eclipse.org/content/pydev-python-ide-eclipse

- RED: https://marketplace.eclipse.org/content/red-robot-editor

Spirent provides a Python Automation Library allowing step level interaction with iTest sessions. The library can be leveraged in your Python-based automation scripts and suites to drive commands and quick calls on multiple concurrent sessions. The library is a thin client for the following two iTest server instances:

- iTest GUI running on the local machine or on a remote host

- A Velocity agent running on the local machine or on a remote host.

The Python library controls iTest sessions on the (GUI or agent) and enables iTest services to be consumed within Python scripts, e.g., quick calls and response maps. See Python Session Level Control Library. In addition, the iTest GUI can be used to generate example Python code from captured steps. See Python Script Generation.

The following lists the use cases of Python Automation Library:

- To open existing session profiles (inside or outside a topology) so your Python script can:

- Invoke quick calls with arguments.

- Parse responses from quick calls (auto-mapped or explicitly-mapped).

- To issue native commands for CLI sessions so your Python script can:

- Send any arbitrary command to an open session.

- Parse responses from commands (auto-mapped or explicitly-mapped).

- To open and control built-in session independent of a pre-existing session profile.

- To use Python Automation Library commands with special step properties in an opened session profile.

---
{
  "chunk_id": "python_1__overview_b7d74fe5858668a2",
  "source_file": "topics/python.1.htm",
  "source_original_path": "topics/python.1.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Sessions",
    "Overview"
  ],
  "heading_path": [
    "Overview",
    "Overview"
  ],
  "anchor": "1355679",
  "context_ids": [],
  "index_keywords": [
    "Python",
    "Python sessions"
  ],
  "index_keyword_paths": [
    "Python sessions",
    "sessions > Python"
  ],
  "related_links": [
    "python.7.htm#1395866"
  ],
  "images": [],
  "content_hash": "b7d74fe5858668a2",
  "level": 1
}
---

# Overview > Overview

iTest Python session is a terminal session, similar to Tcl Shell. The session uses native Python interpreter to getting responses. iTest support Python3 and installs Python version 3.8.5. by default.

iTest support an internal Python interpreter and also allows you to point to an external interpreter via Preferences settings (see Setting preferences for Python).

The Python Terminal sessions allow you to execute commands in the Python interactive shell, which are captured as Steps in iTest. The response of each step will be auto-mapped by a Python-optimized mapper which handles Python language primitives such as:

- Named constants: True, False, None

- Numbers: Integer - 1, Float - 2.3, Long - 4L, Complex - 5j

- Strings: simple - “str”, Unicode - u”str”

- Tuple: (1, 2, 3, 'Spam')

- List: [0, 1, 2, 3]

- Dictionary: {'APT Products': 1, 'iTest': 0}

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

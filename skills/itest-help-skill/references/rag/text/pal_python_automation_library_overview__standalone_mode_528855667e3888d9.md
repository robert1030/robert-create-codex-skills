---
{
  "chunk_id": "pal_python_automation_library_overview__standalone_mode_528855667e3888d9",
  "source_file": "topics/pal_python_automation_library_overview.htm",
  "source_original_path": "topics/pal_python_automation_library_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Automation Library",
    "Overview"
  ],
  "heading_path": [
    "Overview",
    "Overview",
    "Modes of Operation",
    "Standalone Mode"
  ],
  "anchor": "1446719",
  "context_ids": [
    "pal_python_automation_library_overview"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "528855667e3888d9",
  "level": 3
}
---

# Overview > Overview > Modes of Operation > Standalone Mode

In the standalone mode, the library controls the agent startup process. During initialization, the library starts the agent in the background and connects to it. The agent is shut down when the library disconnects. If a separate Python script (separate process) tries to auto-launch its own agent in standalone mode, it is able to create and manage its own independent instance (process) of the agent.

> **Note:** Note Standalone mode, where the library auto-launches the agent, is the only case where the agent is shut down when the library disconnects. When the Python Automation Library disconnects from a GUI instance or an existing agent in listening mode, the GUI and agent instances remain up and are available for subsequent incoming connections.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

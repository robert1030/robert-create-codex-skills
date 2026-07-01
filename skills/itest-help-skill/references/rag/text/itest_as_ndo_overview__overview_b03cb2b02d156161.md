---
{
  "chunk_id": "itest_as_ndo_overview__overview_b03cb2b02d156161",
  "source_file": "topics/itest_as_ndo_overview.htm",
  "source_original_path": "topics/itest_as_ndo_overview.htm",
  "toc_path": [
    "iTest Online Help",
    "Run iTest as Network DevOps agent",
    "Overview"
  ],
  "heading_path": [
    "Overview",
    "Overview"
  ],
  "anchor": "1441967",
  "context_ids": [
    "itest_as_ndo_overview"
  ],
  "index_keywords": [
    "iTest Agent mode, Network DevOps Agent"
  ],
  "index_keyword_paths": [
    "iTest Agent mode, Network DevOps Agent"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "b03cb2b02d156161",
  "level": 1
}
---

# Overview > Overview

iTest allows you to set up such that it (iTest) can be started as a Network DevOps Agent (NDO) to enable debugging of automation assets being executed using Network DevOps Agent API.

iTest opens the test cases being debugged in the iTest Debugging perspective. You may view multiple windows—NDO Console Output with responses and breakpoints of NDO test executions (in the iTest Debugging perspective).

Important iTest GUI can run either as Velocity Agent or NDO Agent. Simultaneous start of iTest as NDO and Velocity Agent is not supported.

The following lists the iTest as NDO Agent features that are supported and not supported:

- iTest configured as NDO Agent does not use the agent.conf file. You must specify these settings, which persist after restart.

- Username and password persist in a password file after restart.

- NDO Agent name and port

- NDO Agent capabilities and restrictions

- Certificate and authentication information

- iTest License server will be used for NDO agent (no additional UI)

- Log information displays on the NDO console and are not stored it in the log file.

- iTest as NDO Agent supports these content type—iTest assets and Python assets

- The following are not supported:

- Customizing the process count, only runs as a single process

- Customizing the script interpreter, iTest NDO Agent will use the interpreter configure in iTest

- NTAF and Telemetry

- Asset signing works at the level of the iTars and not on the files that are part of iTest project.

- Uploading of encrypted assets. Uploading and Executing of encrypted assets will be rejected.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

---
{
  "chunk_id": "itest_as_ndo_start_stop_nddo_server__reports_35c27bff68dc239e",
  "source_file": "topics/itest_as_ndo_start_stop_nddo_server.htm",
  "source_original_path": "topics/itest_as_ndo_start_stop_nddo_server.htm",
  "toc_path": [
    "iTest Online Help",
    "Run iTest as Network DevOps agent",
    "Start and Stop NDO server"
  ],
  "heading_path": [
    "Start and Stop NDO server",
    "Start and Stop NDO server",
    "Network DevOps Agent API Calls",
    "Executions using iTest NDO Agent",
    "Reports"
  ],
  "anchor": "1500230",
  "context_ids": [
    "itest_as_ndo_start_stop_nddo_server"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "35c27bff68dc239e",
  "level": 4
}
---

# Start and Stop NDO server > Start and Stop NDO server > Network DevOps Agent API Calls > Executions using iTest NDO Agent > Reports

The report page displays with Result as pass when execution completes in the format specified (text, XML, HTML). You may also retrieve the report using the API (GET /executions/{id}/report REST API).

> **Note:** Note When execution completes, the debug window is not closed automatically. This to ensure that you have access to data of the completed (or canceled test for analysis of data from views in debug window—data, response, structure, etc).

> **Note:** The report does not persists between iTest NDO restarts. That is, if you stop, then start iTest NDO Agent, the Get Archive report does not find the report (the reports are not archived).

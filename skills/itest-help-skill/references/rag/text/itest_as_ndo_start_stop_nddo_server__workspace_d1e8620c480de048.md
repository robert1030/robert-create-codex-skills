---
{
  "chunk_id": "itest_as_ndo_start_stop_nddo_server__workspace_d1e8620c480de048",
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
    "Workspace"
  ],
  "anchor": "1499924",
  "context_ids": [
    "itest_as_ndo_start_stop_nddo_server"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "d1e8620c480de048",
  "level": 3
}
---

# Start and Stop NDO server > Start and Stop NDO server > Network DevOps Agent API Calls > Workspace

> **Note:** Note Projects from iTest workspace are not considered as assets by NDO agent, so the content of these projects will be filtered out when signed assets validation is turned on. Ensure that the Enable signature verification option is not selected on Spirent > General > Signed Assets page for itest NDO Agent.

iTest NDO Agent searches for assets in these location in order listed:

- iTest Workspace projects

- Projects in ITAR_PATH environment variable

- iTest external Projects (iTar folder in the iTest Workspace)

- NDO Workspace

Upload requests for POST /assets are stored in the NDO workspace.

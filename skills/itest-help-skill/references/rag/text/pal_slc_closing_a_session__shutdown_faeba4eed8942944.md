---
{
  "chunk_id": "pal_slc_closing_a_session__shutdown_faeba4eed8942944",
  "source_file": "topics/pal_slc_closing_a_session.htm",
  "source_original_path": "topics/pal_slc_closing_a_session.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Closing a Session"
  ],
  "heading_path": [
    "Closing a Session",
    "Closing a Session",
    "Shutdown"
  ],
  "anchor": "1447210",
  "context_ids": [
    "pal_slc_closing_a_session"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "faeba4eed8942944",
  "level": 2
}
---

# Closing a Session > Closing a Session > Shutdown

Proper shutdown of the library is important to ensure timely release of resources.

# release all resources used by the library

slc.close()

Resources released include all remaining open sessions, all reservations initiated by the script, and (if local) the underlying execution agent.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

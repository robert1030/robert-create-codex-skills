---
{
  "chunk_id": "favorites_view__starting_a_session_using_a_session_profi_4534edb52c8903b6",
  "source_file": "topics/favorites_view.htm",
  "source_original_path": "topics/favorites_view.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Favorites view"
  ],
  "heading_path": [
    "Favorites view",
    "Favorites view",
    "Starting a session using a session profile"
  ],
  "anchor": "1202482",
  "context_ids": [
    "favorites_view"
  ],
  "index_keywords": [
    "Favorites view"
  ],
  "index_keyword_paths": [
    "Favorites view",
    "views > Favorites view"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "4534edb52c8903b6",
  "level": 2
}
---

# Favorites view > Favorites view > Starting a session using a session profile

By default, when you start a session by double-clicking a session profile from the Favorites view, or by right-clicking and selecting Start in the Project Explorer, or Session Profile editor (the New Session page), the session starts in a new window.

> **Note:** Advanced Users Many of the property settings for session profiles support field replacements to enable you to parameterize settings so they can be determined dynamically at runtime. You might use tcl, param, or profile command field replacements to improve the flexibility and portability of automated test cases. Sometimes, to perform an interactive test, you might need to manually start a session that typically starts only for automated test sessions. To enable you to do this, if any tcl, param, or profile command field replacements are encountered while starting the session, iTest starts a Tcl interpreter so that the field replacement can be resolved.

> **Note:** When the session ends, the Tcl interpreter is disposed. When the session is restarted by pressing Enter, the substitutions are not made again. If a Tcl interpreter service is requested on restart, however, a new interpreter will be created and returned.

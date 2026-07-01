---
{
  "chunk_id": "pal_slc_working_with_sessions__invoking_actions_on_session_17da491f18c71e26",
  "source_file": "topics/pal_slc_working_with_sessions.htm",
  "source_original_path": "topics/pal_slc_working_with_sessions.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Working with Sessions"
  ],
  "heading_path": [
    "Working with Sessions",
    "Working with Sessions",
    "Invoking Actions on Session"
  ],
  "anchor": "1447160",
  "context_ids": [
    "pal_slc_working_with_sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "17da491f18c71e26",
  "level": 2
}
---

# Working with Sessions > Working with Sessions > Invoking Actions on Session

An active session has a number of actions associated, which may be either built-in actions or QuickCalls defined on that session type. Any of those can be invoked on the session.

# invoke the init_routes QuickCall with one parameter

response = s1.init_routes(all="True")

# invoke a built-in action with a specific response map (which may override what was set for the session as a whole)

response = my_ssh_session.command('ls', response_map="proj.response_map_ls_ffrm")

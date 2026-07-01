---
{
  "chunk_id": "pal_slc_working_with_sessions__session_information_52874d3377e959b1",
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
    "Session Information"
  ],
  "anchor": "1447152",
  "context_ids": [
    "pal_slc_working_with_sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "52874d3377e959b1",
  "level": 2
}
---

# Working with Sessions > Working with Sessions > Session Information

Once a session is opened it is possible to find out some basic information about where the session is being handled. This is done via the agent property of a session object.

# Use the print command when using a standalone agent

>>> print(s1.agent)

{'agent_name': u'USER01-PC', 'agent_type': 'local', 'name': u'USER01-PC', 'capabilities': {u'Product.Arch': u'x86', u'OS.Type': u'win32', u'STC.Version': u'4.69', u'language': u'itest'}, 'protocol_version': u'1.0'}

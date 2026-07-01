---
{
  "chunk_id": "pal_slc_closing_a_session__closing_a_session_9d02d157bb51a105",
  "source_file": "topics/pal_slc_closing_a_session.htm",
  "source_original_path": "topics/pal_slc_closing_a_session.htm",
  "toc_path": [
    "iTest Online Help",
    "Python Session Level Control Library",
    "Closing a Session"
  ],
  "heading_path": [
    "Closing a Session",
    "Closing a Session"
  ],
  "anchor": "1499684",
  "context_ids": [
    "pal_slc_closing_a_session"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "9d02d157bb51a105",
  "level": 1
}
---

# Closing a Session > Closing a Session

Sessions should be closed when no longer needed, as they consume resources on the agent (and on Velocity if being used.) It is especially important to close sessions if sessions are being opened within a loop.

# close session and free resources

s1.close()

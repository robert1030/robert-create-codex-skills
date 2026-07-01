---
{
  "chunk_id": "pal_slc_working_with_sessions__queries_3f7882b30f1ef20b",
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
    "Invoking Actions on Session",
    "Queries"
  ],
  "anchor": "1447194",
  "context_ids": [
    "pal_slc_working_with_sessions"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "3f7882b30f1ef20b",
  "level": 3
}
---

# Working with Sessions > Working with Sessions > Invoking Actions on Session > Queries

The response object may also have queries defined on it - methods that query the structured data and return values. Queries may be auto-generated in iTest or be defined in response maps.

# list the set of queries that exist for the response

response.queries()

==> [ 'is_empty()', 'counter_by_row(row)' ]

# invoke query

response.counter_by_row(3)

==> 35

> **Note:** Note Query names are always converted to snake case.

---
{
  "chunk_id": "filtering_responses_2__how_response_filtering_works_4f3c073e062b1aa1",
  "source_file": "topics/filtering_responses.2.htm",
  "source_original_path": "topics/filtering_responses.2.htm",
  "toc_path": [
    "iTest Online Help",
    "Filtering Unwanted Text from Responses",
    "How response filtering works"
  ],
  "heading_path": [
    "How response filtering works",
    "How response filtering works"
  ],
  "anchor": "1191258",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "4f3c073e062b1aa1",
  "level": 1
}
---

# How response filtering works > How response filtering works



Define the filters

First, you specify the Pattern of text that you are looking for in the response (the pattern to match). You can specify text with a wildcard character, a regular expression, or a case-insensitive text match.

Next, you specify the Action — what to do when a match occurs — for example, discard any line that contains a match, or discard every line that does not contain a match, or include everything up to the matching text and discard everything else, and so on.

- You can define multiple filters for a particular response

- You can specify that text that is discarded by a filter should be added to the structured data for the step

- You can define filters for a session profile, for an executable step in a test case, and for the response map used by a step



Then, during execution...

1. iTest applies the filters to the response. “Applying a filter” means:

One line at a time, check for matches with the Pattern

1. If a match occurs, perform the specified Action

1. 2

1. iTest applies the filters in the following order to the text that remains in the response:

1. filters defined in the session profile, in the order that they are listed

1. filters defined for the step, in the order that they are listed

1. filters defined in the response map, in the order that they are listed

1. 3

1. The resulting filtered response for the step contains only the lines that were not excluded. This is the response text that analysis rules check and that appears in report.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

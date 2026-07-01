---
{
  "chunk_id": "rme_pattern_page__use_this_group_as_a_key_when_generating__83fe0f53d9e5056d",
  "source_file": "topics/rme_pattern_page.htm",
  "source_original_path": "topics/rme_pattern_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Pattern page"
  ],
  "heading_path": [
    "Response Map editor: Pattern page",
    "Response Map editor: Pattern page",
    "Other controls:",
    "Use this group as a key when generating aliases"
  ],
  "anchor": "1106570",
  "context_ids": [
    "rme_pattern_page"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/response_mapping_2.4.jpg"
  ],
  "content_hash": "83fe0f53d9e5056d",
  "level": 3
}
---

# Response Map editor: Pattern page > Response Map editor: Pattern page > Other controls: > Use this group as a key when generating aliases

(Optional) In some cases, you will use a particular value for a token as a key — that value identifies the line in the response where you want to extract another value from the line. In the example the regex map finds each row in the table and the groups extract the cell values in the row (discarding the whitespace or other delimiters). In this example, we defined PathCost as a key token:

1. 1

1. The PathCost token is the Key. Whenever a PathCost value exceeds 25, then the RoleByPathCost query returns the value in that row for the Role token.

1. 2

1. The PathCost token in this row exceeds 25, so the RoleByPathCost query returns the value in this row for the Role token: TRI.

Check Use this group as a key and provide a Sample key value. iTest uses the Key token to auto-generate aliases for the other tokens in the block.

As you make changes, the Response view updates itself to reflect the changes. The text in the Response view is linked to the selected pattern match. Each match in the response body to the overall pattern map is highlighted with a blue background. Each extracted group is enclosed in a blue box. If one or more of the groups is marked as a key, that is shown with a different font color.

![screenshot](topics/images/response_mapping_2.4.jpg) <!-- image_chunk: img_3b375084f86f87da -->

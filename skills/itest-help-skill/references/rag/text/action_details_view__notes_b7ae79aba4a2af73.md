---
{
  "chunk_id": "action_details_view__notes_b7ae79aba4a2af73",
  "source_file": "topics/action_details_view.htm",
  "source_original_path": "topics/action_details_view.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Views",
    "Response view"
  ],
  "heading_path": [
    "Response view",
    "Response view",
    "Notes:"
  ],
  "anchor": "1234282",
  "context_ids": [
    "action_details_view"
  ],
  "index_keywords": [
    "Response view",
    "adding from Response view"
  ],
  "index_keyword_paths": [
    "Response view",
    "form maps > adding from Response view",
    "response maps > adding from Response view",
    "views > Response view"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "b7ae79aba4a2af73",
  "level": 3
}
---

# Response view > Response view > Notes:

- You cannot add an analysis rule, response map, or form map while viewing an unfiltered response.

- If you select more than one captured item, then the Response view becomes blank.

- The Response view does not display Web or Swing targets directly. To view the target associated with the response, click Details. You can view targets in Capture reports and in Test reports.

- To improve performance, iTest does not map all items in very long responses. If you notice that the “blue boxes” do not appear in the later text of a response, you can increase the setting so that iTest evaluates more queries. Click Window > Preferences. In the iTest group, go to Response Mapping and increase the Maximum number of queries to evaluate setting.

- You can copy/paste an entire test case document (for example, to create a test case that is very similar to the original). If you copy a test case, remember that the most recent response to each step (in the most recent execution of the test case) is also copied. This can result in old information in the Response view as you start to work on the “copy”.

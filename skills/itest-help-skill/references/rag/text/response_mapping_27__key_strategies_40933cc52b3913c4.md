---
{
  "chunk_id": "response_mapping_27__key_strategies_40933cc52b3913c4",
  "source_file": "topics/response_mapping.27.htm",
  "source_original_path": "topics/response_mapping.27.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "When there are multiple response formats for a particular command"
  ],
  "heading_path": [
    "When there are multiple response formats for a particular command",
    "When there are multiple response formats for a particular command",
    "Key strategies"
  ],
  "anchor": "1611677",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "40933cc52b3913c4",
  "level": 2
}
---

# When there are multiple response formats for a particular command > When there are multiple response formats for a particular command > Key strategies

- Create a unique response map for each form of the response and let iTest choose which response map to apply.

- Keep the maps together in a response map library.

- Configure identical Applicability settings for each response map.

- Ensure that iTest cycles through all applicable maps when attempting to map a response. With this setting, if mapping fails for one map, iTest generates an error and then tries the next applicable map. If any map ultimately succeeds in mapping the response, then iTest does not publish the error message.

- For table maps: On the Table page of the Response Map editor, we check the Required: Generate an error if the table is not found at least once check box.

- For pattern maps: On the Pattern page of the Response Map editor, we check the Generate an error if no matches are found check box.

- For block maps: On the Block page of the Response Map editor, for all blocks and containers, we check the This block/container must appear at least once check box.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

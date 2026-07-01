---
{
  "chunk_id": "filtering_responses_1__when_should_you_filter_a_response_6cf289c8eb3cbaab",
  "source_file": "topics/filtering_responses.1.htm",
  "source_original_path": "topics/filtering_responses.1.htm",
  "toc_path": [
    "iTest Online Help",
    "Filtering Unwanted Text from Responses",
    "Overview: Response filtering"
  ],
  "heading_path": [
    "Overview: Response filtering",
    "Overview: Response filtering",
    "When should you filter a response?"
  ],
  "anchor": "1191174",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "6cf289c8eb3cbaab",
  "level": 2
}
---

# Overview: Response filtering > Overview: Response filtering > When should you filter a response?

You will find filtering to be useful in the following situations:

- The response contains a lot of irrelevant text, and it would be easier to analyze and display only a portion of the response and to ignore the rest.

- The device produces logging messages that are mixed into the output (common when using a terminal server and with TL1 devices). The messages appear as separate lines. You might want to analyze the messages in a different step, but you need to filter out the messages so that you can define a response map for the base response.

- The device produces XML output, but the output includes non-XML headers and footers that corrupt the XML (or HTML) mapping. Filtering can remove the headers and footers before you apply the queries.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

---
{
  "chunk_id": "rme_samples_page__configuring_a_sample_response_9c3cece5c9438328",
  "source_file": "topics/rme_samples_page.htm",
  "source_original_path": "topics/rme_samples_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Samples page"
  ],
  "heading_path": [
    "Response Map editor: Samples page",
    "Response Map editor: Samples page",
    "Configuring a sample response"
  ],
  "anchor": "1106006",
  "context_ids": [
    "rme_samples_page"
  ],
  "index_keywords": [
    "Response Map editor",
    "Samples page",
    "adding sample responses to",
    "adding to response maps",
    "sample responses to response maps"
  ],
  "index_keyword_paths": [
    "Response Map editor > Samples page",
    "Samples page > Response Map editor",
    "adding > sample responses to response maps",
    "response maps > adding sample responses to",
    "sample responses > adding to response maps"
  ],
  "related_links": [],
  "images": [
    "topics/images/rme_samples_page.png"
  ],
  "content_hash": "9c3cece5c9438328",
  "level": 2
}
---

# Response Map editor: Samples page > Response Map editor: Samples page > Configuring a sample response

While you work on a response sample in the Samples page, the Response, Structure, Queries, and Step Issues views provide auto-updated feedback on how the response map will operate.

1. 1

1. The New Response Map wizard (or Add this Response to an Existing Response Map) populates the Command and Response text boxes. (If you are adding a sample response manually [not typical] you paste the values into the appropriate text boxes.)

You can edit the Response text as needed, but remember that all mappers that you define map against the text in this box (not an issue if you intend to use the sample as an emulated response).

1. 2

1. The Sample name defaults to sample1

> **Note:** Note The Sample name is not important if the response always appears in only one format and this is the only sample that you will use for mapping the response. The Sample name serves to uniquely identify each of multiple response formats.

The name is important only in either of the following cases:

- You plan to provide more than one sample for the response map. We recommend that you use a name that reflects the particular software revision or other command category that results in the different response. If you’re adding a second or third format of a response, you might include text that identifies the format of the response

- You intend to use the response map only to supply an emulated response. The Sample name property in the Emulation property group for the step will refer to this sample name.

![screenshot](topics/images/rme_samples_page.png) <!-- image_chunk: img_e2c77cb49b7d31bb -->

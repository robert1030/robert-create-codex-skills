---
{
  "chunk_id": "using_block_mapper__example_block_format_responses_8c9bd6addc0ef1ba",
  "source_file": "topics/using_block_mapper.htm",
  "source_original_path": "topics/using_block_mapper.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Mapping a response using a Block Map"
  ],
  "heading_path": [
    "Mapping a response using a Block Map",
    "Mapping a response using a Block Map",
    "Example block format responses"
  ],
  "anchor": "1106948",
  "context_ids": [
    "using_block_mapper"
  ],
  "index_keywords": [
    "extracting multiple values from",
    "overview",
    "using Block map"
  ],
  "index_keyword_paths": [
    "Block map > overview",
    "mapping responses > using Block map",
    "responses > extracting multiple values from"
  ],
  "related_links": [],
  "images": [
    "topics/images/response_mapping_9.1.jpg",
    "topics/images/response_mapping_7.2.jpg",
    "topics/images/response_mapping_5.3.jpg"
  ],
  "content_hash": "8c9bd6addc0ef1ba",
  "level": 2
}
---

# Mapping a response using a Block Map > Mapping a response using a Block Map > Example block format responses

The non-repeating block pattern is the most common response pattern. It has the following properties:

- The response consists of a single block of text.

- The identified block of text does not repeat in the response text.

- Typically, but not always, some parts of the text do not change, and some parts vary.

- In the following three sample responses for the same command on a device in different states, you can see that:

- This block of data appears only one time in the response

- Some lines seem to be optional (for example, Auto upgrade path appears only in Sample 3)

- The heading portion of each line (the text before the : character) remains unchanged

- The values for each line (the text after the : character) can vary

Let’s look at an example:

Here is the structure of a non-repeating block pattern as represented in the Block mapper page:

![screenshot](topics/images/response_mapping_9.1.jpg) <!-- image_chunk: img_5bf98a82104237ec -->

![screenshot](topics/images/response_mapping_7.2.jpg) <!-- image_chunk: img_be28b958f343aec2 -->

![screenshot](topics/images/response_mapping_5.3.jpg) <!-- image_chunk: img_77882c9880d3c595 -->

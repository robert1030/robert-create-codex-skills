---
{
  "chunk_id": "using_block_mapper__mapping_a_response_using_a_block_map_75514eba154f3a94",
  "source_file": "topics/using_block_mapper.htm",
  "source_original_path": "topics/using_block_mapper.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Mapping a response using a Block Map"
  ],
  "heading_path": [
    "Mapping a response using a Block Map",
    "Mapping a response using a Block Map"
  ],
  "anchor": "1106941",
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
  "images": [],
  "content_hash": "75514eba154f3a94",
  "level": 1
}
---

# Mapping a response using a Block Map > Mapping a response using a Block Map

A block is an identifiable section of the response that consists of one or more lines of text. You can use block response maps to represent any response that does not have a structured format (indented text is not a structured format).

Create a block response map when the following conditions are all true:

- You want to extract many values from a response (that is, you’d have to create a lot of regex maps to extract all the data you need)

- You want to be able to reuse the map in a variety of test cases

- The data is not in the form of a table. In simple terms, use a block map when the response looks like a paragraph of text with values embedded in the text.

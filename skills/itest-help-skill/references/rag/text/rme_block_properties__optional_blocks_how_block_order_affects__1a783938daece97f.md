---
{
  "chunk_id": "rme_block_properties__optional_blocks_how_block_order_affects__1a783938daece97f",
  "source_file": "topics/rme_block_properties.htm",
  "source_original_path": "topics/rme_block_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Block Map properties"
  ],
  "heading_path": [
    "Response Map editor: Block Map properties",
    "Response Map editor: Block Map properties",
    "Defining a block",
    "Block properties",
    "Optional blocks: How block order affects the mapping process"
  ],
  "anchor": "1340534",
  "context_ids": [
    "rme_block_properties"
  ],
  "index_keywords": [
    "Block Map properties",
    "Response Map editor",
    "block map"
  ],
  "index_keyword_paths": [
    "Block Map properties > Response Map editor",
    "Response Map editor > Block Map properties",
    "properties > block map"
  ],
  "related_links": [],
  "images": [
    "topics/images/response_mapping_6.4.jpg"
  ],
  "content_hash": "1a783938daece97f",
  "level": 4
}
---

# Response Map editor: Block Map properties > Response Map editor: Block Map properties > Defining a block > Block properties > Optional blocks: How block order affects the mapping process

In the example we’ll discuss here, a command can return either of the following responses:

a

or

a

b

To allow for these variations, you might expect that you can define two optional blocks in the map, (that is, for both block1 and block2, the This block must appear at least once property is unchecked).

Because iTest tries to map responses by applying blocks in the order in which they appear in the tree, however, a response of the form

a

b

would always be mapped by block1 (”a” matches “a”). For this reason, you should order block definitions so that the most inclusive block is applied to the response first. In this example, we would place block2 before block1 in the Block Map elements tree to ensure that both forms of the response will be mapped.

![screenshot](topics/images/response_mapping_6.4.jpg) <!-- image_chunk: img_a64f293018b2e3be -->

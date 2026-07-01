---
{
  "chunk_id": "rme_block_properties__response_map_editor_block_map_properties_72e57bf93164c69e",
  "source_file": "topics/rme_block_properties.htm",
  "source_original_path": "topics/rme_block_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Block Map properties"
  ],
  "heading_path": [
    "Response Map editor: Block Map properties",
    "Response Map editor: Block Map properties"
  ],
  "anchor": "1107149",
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
  "related_links": [
    "response_mapping.24.htm#1106992",
    "#1337791"
  ],
  "images": [
    "topics/images/response_mapping_12.1.jpg"
  ],
  "content_hash": "72e57bf93164c69e",
  "level": 1
}
---

# Response Map editor: Block Map properties > Response Map editor: Block Map properties

While defining a block map, you use the Block Map page to specify the properties for block map elements. This section describes all of the property settings.

Here’s a quick discussion of the elements that make up the Block map (more detailed descriptions appear in Overview: Properties of Block map elements):

The root of the block is always named root and is the parent node for the containers and blocks that you structure the response text into.

- A block defines one section of a response — one or more lines of text — either related information or data that is grouped (often with a particular format).

- A container is a collection of blocks and child containers. Each container represents one section of a response. In the example, the body container holds two blocks: infoPID and Stats

Important By default, iTest tries to map responses by applying the containers and blocks in the order in which they appear in the tree. This can be an important consideration in your design. You can make use of Move Up and Move down to order the elements of the map as needed. See an additional note on ordering blocks within a container in Defining a block.

![screenshot](topics/images/response_mapping_12.1.jpg) <!-- image_chunk: img_249b7b8341707d66 -->

---
{
  "chunk_id": "rme_block_properties__general_properties_17b80ccd49ac67ca",
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
    "Defining the root of the block",
    "General properties"
  ],
  "anchor": "1107156",
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
  "images": [],
  "content_hash": "17b80ccd49ac67ca",
  "level": 3
}
---

# Response Map editor: Block Map properties > Response Map editor: Block Map properties > Defining the root of the block > General properties

| Specify how to deal with minor mapping discrepancies | Strict (default): Declare an error and terminate mapping upon encountering any mapping error, including individual token mismatch Loose: Declare a warning upon encountering a token mismatch, but continue mapping the remainder of the response |
| --- | --- |
| Specify how the top-level blocks and containers should be used during mapping | Ordered (default): The flow of the response must match the blocks and containers in the listed order Random: The top-level blocks and containers may appear in the response in any order |
| Specify how to treat blank lines in the response and in block definitions when mapping | Use this setting to specify whether the mapping process should pay attention to missing or extra blank lines in responses. Lines that include tab and space characters (that is, whitespace characters) in an otherwise empty line are considered blank lines. If Strict, then blank lines that appeared in the response that was used to create the response map must also appear in actual responses and no extra lines can appear. If Non-strict (default), then no mapping errors result when blank lines or extra lines appear in responses regardless of whether or not they appear in the response that was used to create the response map. |
| Maximum search iterations | The maximum number of times that the iTest search algorithm should be applied to the response. The number of iterations needed to find a match is not related to the number of levels of containers. Rather, optional tokens, wild cards, and other options increase the complexity of the search. If this limit is exceeded without finding a match, then the step fails. Increase this setting only if the response map is complex or responses do not map well. Caution: We recommend that you do not modify this setting. Setting this property much higher than the default setting will likely result in stack overflow exceptions. |
| Maximum search time | Specify the longest time that iTest should spend attempting to find a match. If this limit is exceeded without finding a match, then the step fails. |

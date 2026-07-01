---
{
  "chunk_id": "parameters_06__syntax_for_referring_to_a_parameter_in_a_0b4d0bd25e4fd125",
  "source_file": "topics/parameters.06.htm",
  "source_original_path": "topics/parameters.06.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Defining and managing parameters",
    "Creating structure for parameters (working with nodes)"
  ],
  "heading_path": [
    "Creating structure for parameters (working with nodes)",
    "Creating structure for parameters (working with nodes)",
    "Syntax for referring to a parameter in a node"
  ],
  "anchor": "1325944",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "0b4d0bd25e4fd125",
  "level": 2
}
---

# Creating structure for parameters (working with nodes) > Creating structure for parameters (working with nodes) > Syntax for referring to a parameter in a node

In a test case step, to refer to a parameter that is in a node, use node_name/parameter_name syntax.

In the example, there are clearly two distinct firmwareRev parameters. To distinguish between them in test case steps, you refer to them as slot/card_1/firmwareRev and slot/card_2/firmwareRev

For example, use the following syntax in a param command field replacement of the firmwareRev parameter in the card_1 node: [param slot/card_1/firmwareRev]

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

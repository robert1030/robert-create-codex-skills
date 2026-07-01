---
{
  "chunk_id": "rme_parsers_page__adding_a_custom_parser_a46209660b491aed",
  "source_file": "topics/rme_parsers_page.htm",
  "source_original_path": "topics/rme_parsers_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Response Maps: Returning Data from Responses",
    "Response Map editor: Parsers page"
  ],
  "heading_path": [
    "Response Map editor: Parsers page",
    "Response Map editor: Parsers page",
    "Adding a custom parser"
  ],
  "anchor": "1251995",
  "context_ids": [
    "rme_parsers_page"
  ],
  "index_keywords": [
    "Custom Parsers page",
    "Response Map editor",
    "custom"
  ],
  "index_keyword_paths": [
    "Custom Parsers page > Response Map editor",
    "Response Map editor > Custom Parsers page",
    "parsers > custom"
  ],
  "related_links": [],
  "images": [
    "topics/images/response_mapping_6.1.jpg"
  ],
  "content_hash": "a46209660b491aed",
  "level": 2
}
---

# Response Map editor: Parsers page > Response Map editor: Parsers page > Adding a custom parser

1. On the Response Map editor, open the Parsers page.

1. 2

1. Add the parser: Click and specify a Name for the parser, for example, IP_Hex. Use a common-sense name that will help your coworkers to understand its usage. The name must be unique among built-in parsers and other custom parsers.

1. 3

1. Specify values for the parser properties. You must specify a value for the Regex string property. All other properties are optional.

| Group name | Optional. The name of a group (defined within the RegEx String) that identifies the portion of the match that is to be treated as the token. If blank, then the entire match (if any) with the Regex string is the token. |
| --- | --- |
| Regex string | Required. Specify a regular expression that defines the structure and content of the single token that the parser is intended to find. For example, the following RegEx String matches IP addresses in hex form in dotted or not dotted notation (not tested): [0-9A-Fa-f]{2}(\.?)[0-9A-Fa-f]{2}(\.?)[0-9A-Fa-f]{2}(\.?)[0-9A-Fa-f]{2} |
| Precondition Pattern | Optional. If there is any text before the parsed token, then it must match the character defined by this RegEx. |
| Postcondition pattern | Optional. If there is any text after the parsed token, then it must match the character defined by this RegEx. |
| Priority | Optional. The priority ordering in which the parser is applied to the response. Negative values cause the parser to have the higher priority. Non-negative values define a specific priority for the parser. The higher the number, the lower the priority. See the next table for priority settings of iTest default parsers. Default: 0 |
| Default is variable | Optional. True: Tokens found using this parser are considered to be variable. So, when mapping, the parser accepts a different token value of the same type in this position. False: The parser requires that the token in this position must have the same value as the original. |

1. 4

1. Save the response map. Close and reopen the Response Map editor.

1. 5

1. For Block Maps: Open the Block page. Reparse all the blocks that include the field that you created the custom parser for: In the Block Map Elements list, select the blocks (Ctr+click to select multiple) and then click Reparse Blocks.

A dialog box warns you that reparsing could cause you to lose token names and other information. Click OK.

![inline_icon](topics/images/response_mapping_6.1.jpg) <!-- image_chunk: img_c016705e683bc5c4 -->

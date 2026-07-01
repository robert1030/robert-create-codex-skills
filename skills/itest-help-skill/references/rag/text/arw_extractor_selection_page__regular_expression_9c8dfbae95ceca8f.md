---
{
  "chunk_id": "arw_extractor_selection_page__regular_expression_9c8dfbae95ceca8f",
  "source_file": "topics/arw_extractor_selection_page.htm",
  "source_original_path": "topics/arw_extractor_selection_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis Rule Wizard: Custom Extractor page"
  ],
  "heading_path": [
    "Analysis Rule Wizard: Custom Extractor page",
    "Analysis Rule Wizard: Custom Extractor page",
    "Regular expression"
  ],
  "anchor": "1177662",
  "context_ids": [
    "arw_extractor_selection_page"
  ],
  "index_keywords": [
    "Analysis Rule wizard",
    "Custom Extractor page"
  ],
  "index_keyword_paths": [
    "Analysis Rule wizard > Custom Extractor page",
    "Custom Extractor page > Analysis Rule wizard"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "9c8dfbae95ceca8f",
  "level": 2
}
---

# Analysis Rule Wizard: Custom Extractor page > Analysis Rule Wizard: Custom Extractor page > Regular expression

The Regular expression extractor finds all matches to the specified regular expression in the response body for the step.

| Regular expression | Specify the regular expression that will match the data. |
| --- | --- |
| For the regular expression string, first perform command, variable, and backslash substitutions | Check the box if the string specified for the Regular expression property uses a command field replacement, a variable, or a backslash that is used to escape a special character. As a result, the substitutions will be performed before the regular expression is applied to the response. |
| Use line mode | Check this box if the match always occurs within a line and does not span lines. Uncheck the box to analyze the entire response as one string. |
| Portion of matches to extract | numbered_group: Select this option to extract only a group. Specify the group number in the Extraction group number property. For example, in the regex ab(c|d)fg, c|d is group number zero. full_match: Extract all text that matches. |
| Extraction group number | If you selected numbered_group for the Portion of matches to extract property, then specify the number of the group here. |
| Declare issue if no matches found | Check the box to specify that if the query fails to return a match, then declare an Execution Issue. You will configure the message on a subsequent wizard page. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

---
{
  "chunk_id": "arules_extractor_properties__regex_extractor_e4f23e97dd792533",
  "source_file": "topics/arules_extractor_properties.htm",
  "source_original_path": "topics/arules_extractor_properties.htm",
  "toc_path": [
    "iTest Online Help",
    "Analysis Rules: Validating Responses",
    "Analysis rules: Properties of the extractor"
  ],
  "heading_path": [
    "Analysis rules: Properties of the extractor",
    "Analysis rules: Properties of the extractor",
    "Regex extractor"
  ],
  "anchor": "1176825",
  "context_ids": [
    "arules_extractor_properties"
  ],
  "index_keywords": [
    "$index",
    "$itest_index",
    "$itest_value",
    "$value",
    "ExecutionDuration extractor",
    "None extractor",
    "analysis rules",
    "contains extractor",
    "extractor properties",
    "in analysis rules",
    "predefined",
    "predefined variable",
    "predefined variables",
    "query extractor",
    "regex extractor",
    "temporary data tag",
    "{assertion}",
    "{values}",
    "{value}"
  ],
  "index_keyword_paths": [
    "$index > predefined variables",
    "$itest_index > predefined variable",
    "$itest_value > predefined variables",
    "$value > predefined variable",
    "ExecutionDuration extractor",
    "Extract using property > in analysis rules",
    "None extractor",
    "analysis rules > extractor properties",
    "assertion > temporary data tag",
    "contains extractor",
    "extractor properties > analysis rules",
    "extractors > ExecutionDuration extractor",
    "extractors > None extractor",
    "extractors > contains extractor",
    "extractors > query extractor",
    "extractors > regex extractor",
    "predefined variables > $index",
    "predefined variables > $itest_index",
    "predefined variables > $itest_value",
    "predefined variables > $value",
    "query extractor",
    "regex extractor",
    "temporary data tag > {assertion}",
    "temporary data tag > {values}",
    "temporary data tag > {value}",
    "value > temporary data tag",
    "values > temporary data tag",
    "variables > predefined"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "e4f23e97dd792533",
  "level": 2
}
---

# Analysis rules: Properties of the extractor > Analysis rules: Properties of the extractor > Regex extractor

The regex extractor finds all matches to the specified regular expression in the response body for the step.

For Global rules, the Extract using cell displays regex.

For Global rules, the What to Extract cell displays the text of the regular expression.

| Regular expression | Specify the regex that will extract the data. |
| --- | --- |
| Use line mode | Check this box if the match always occurs within a line and does not span lines. Uncheck the box to analyze the entire response as one string. |
| Portion of matches to extract | numbered_group: Select this option to extract only a group. Specify the group number in the Extraction group number property. For example, in the regex ab(c|d)fg, c|d is group number 1. full_match: Extract all text that matches. |
| Extraction group number | If you selected numbered_group for the Portion of matches to extract property, then specify the number of the group here. |
| Declare issue if no matches found | Check the box to specify that if the query fails to return a match, then declare an Execution Issue and display an execution message in the Execution view and in the test report. See the When True / When False properties. |
| For the regular expression string, first perform command, variable, and backslash substitutions | Check the box if the string specified for the Regular expression property uses a command field replacement, a variable, or a backslash that is used to escape a special character. As a result, the substitutions will be performed before the regular expression is applied to the response. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

---
{
  "chunk_id": "filtering_responses_3__defining_response_filters_866074f642619eea",
  "source_file": "topics/filtering_responses.3.htm",
  "source_original_path": "topics/filtering_responses.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Filtering Unwanted Text from Responses",
    "Defining response filters"
  ],
  "heading_path": [
    "Defining response filters",
    "Defining response filters"
  ],
  "anchor": "1183109",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "#1192153"
  ],
  "images": [
    "topics/images/filtering_responses_2.1.jpg",
    "topics/images/filtering_responses_2.2.jpg"
  ],
  "content_hash": "866074f642619eea",
  "level": 1
}
---

# Defining response filters > Defining response filters

1. Open the appropriate editing tool:

- To define a filter for a step: In the Test Case editor, select the step. In the Step Properties section, open the Response Filters page.

- To define a filter for a session profile: In the Session Profile editor, click the Response Filters tab.

- To define a filter for a response map: In the Response Map editor, click the Response Filters tab.

1. 2

1. Optional. Modify whether existing filters are inherited (does not apply to response maps — response maps cannot inherit filters). By default, the Include inherited values property is checked, therefore:

- By default, a step inherits the filters that are defined in the session profile associated with the step’s session.

- By default, a session profile inherits the filters defined in the session profiles that the profile is based on.

To modify or delete inheritable filters, uncheck the Include inherited values check box. The list now displays all inherited filters. To edit a filter definition, select it in the list and then change settings as described in Step 4.

> **Note:** Note Because the formerly inherited filters are now defined in the current step or session profile, the filters are not updated when the filters in the reference session profile change.

1. 3

1. For steps and for session profiles only: To enable you to add filter definitions, check Include additional values from list.

1. 4

1. Click Add to add a filter and then specify the following properties for the new filter.

> **Tip:** Tip To filter multi-line text: 1. Set the Action property to Include matches of the pattern2. Ensure that the Pattern property includes a RegEx that will hit the multi-line text

| Name | Specify a meaningful name for the filter. For example, deleteLogMsgs or includeOnlyPortStatus |
| --- | --- |
| Action | Select one of the following methods for applying the pattern while filtering a response. Include means that the matching text remains as part of the response. Exclude means that the matching text is discarded: If you choose to exclude data, you have the option to add the excluded text to the structured data for the step. See the Add discarded text to structured data property. Include only lines matching the pattern Include only lines containing matches of the pattern Exclude lines matching the pattern Exclude lines containing matches of the pattern Include matches of the pattern (each on a separate line in the output) Exclude matches of the pattern found within lines Include lines starting with the first line matching the pattern until the end Include lines up to but not including the first line matching the pattern Include lines up to but not including the first line containing the pattern Include lines up to and including the first line matching the pattern Include lines up to and including the first line containing the pattern |
|  | Include means that the matching text remains as part of the response. |
|  | Exclude means that the matching text is discarded: |
| Pattern type | Specify how to interpret the pattern that you specified for the Pattern property: Case Insensitive, Wildcard, or Regex Default: Wildcard |
| Pattern | Specify a string that represents the text that you are looking for within the response. You specify whether to include or exclude matches (or to perform other actions) using the Action property. You can use field replacements in the pattern text |
| Add excluded text to structured data | Optional Check the box to add the excluded data to the structured data. In the structured data, the text is added to the filteredResponse element (filteredResponse is parallel to the prompt element). The data is added in the element that you specify for the Excluded data tag property. The Value element holds the excluded text with one “item” for each excluded line. An example appears below this table. |
| Excluded data tag | Required if you check Add excluded text to structured data. Specify the XML tag that should identify the data that you are adding to the structured data. The data is inserted into the structured data at this XPATH location relative to the filteredResponse tag. In the example that appears below this table, we named the tag “excluded”. You can use field replacements in the text that defines the tag. Default: [empty] |

- Add as many filters as needed.

- Filters are applied in the listed order. To change the order, select a filter in the list and use Move up and Move down .

- To delete a filter definition, select a filter in the list and click Remove .

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/filtering_responses_2.1.jpg) <!-- image_chunk: img_ef2116daf69b7481 -->

![screenshot](topics/images/filtering_responses_2.2.jpg) <!-- image_chunk: img_38bd042406c6d9f6 -->

# Filtering Unwanted Text from Responses > Defining response filters > 第2段

- **Name**：Specify a meaningful name for the filter. For example, deleteLogMsgs or includeOnlyPortStatus
- **Action**：Select one of the following methods for applying the pattern while filtering a response. If you choose to exclude data, you have the option to add the excluded text to the structured data for the step. See the Add discarded text to structured data property. Include only lines matching the pattern Include only lines containing matches of the pattern Exclude lines matching the pattern Exclude lines containing matches of the pattern Include matches of the pattern (each on a separate line in the output) Exclude matches of the pattern found within lines Include lines starting with the first line matching the pattern until the end Include lines up to but not including the first line matching the pattern Include lines up to but not including the first line containing the pattern Include lines up to and including the first line matching the pattern Include lines up to and including the first line containing the pattern
- **Pattern type**：Specify how to interpret the pattern that you specified for the Pattern property: Case Insensitive, Wildcard, or Regex Default: Wildcard
- **Pattern**：Specify a string that represents the text that you are looking for within the response. You specify whether to include or exclude matches (or to perform other actions) using the Action property. You can use field replacements in the pattern text
- **Add excluded text to structured data**：Optional Check the box to add the excluded data to the structured data. In the structured data, the text is added to the filteredResponse element (filteredResponse is parallel to the prompt element). The data is added in the element that you specify for the Excluded data tag property. The Value element holds the excluded text with one “item” for each excluded line. An example appears below this table.
- **Excluded data tag**：Required if you check Add excluded text to structured data. Specify the XML tag that should identify the data that you are adding to the structured data. The data is inserted into the structured data at this XPATH location relative to the filteredResponse tag. In the example that appears below this table, we named the tag “excluded”. You can use field replacements in the text that defines the tag. Default: [empty]

![](images/filtering_responses_2.2.jpg) <!-- image_ref -->

![*](bullet_blue.jpg) <!-- image_ref -->

- Add as many filters as needed.

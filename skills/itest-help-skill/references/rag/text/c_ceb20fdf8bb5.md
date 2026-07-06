# Analysis Rules: Validating Responses > Analysis rules: Properties of the extractor > Regex extractor

The regex extractor finds all matches to the specified regular expression in the response body for the step.

For Global rules, the Extract using cell displays regex.

For Global rules, the What to Extract cell displays the text of the regular expression.

- **Regular expression**：Specify the regex that will extract the data.
- **Use line mode**：Check this box if the match always occurs within a line and does not span lines. Uncheck the box to analyze the entire response as one string.
- **Portion of matches to extract**：numbered_group: Select this option to extract only a group. Specify the group number in the Extraction group number property. For example, in the regex ab(c|d)fg, c|d is group number 1. full_match: Extract all text that matches.
- **Extraction group number**：If you selected numbered_group for the Portion of matches to extract property, then specify the number of the group here.
- **Declare issue if no matches found**：Check the box to specify that if the query fails to return a match, then declare an Execution Issue and display an execution message in the Execution view and in the test report. See the When True / When False properties.
- **For the regular expression string, first perform command, variable, and backslash substitutions**：Check the box if the string specified for the Regular expression property uses a command field replacement, a variable, or a backslash that is used to escape a special character. As a result, the substitutions will be performed before the regular expression is applied to the response.

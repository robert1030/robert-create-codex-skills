---
{
  "chunk_id": "session_profile_properties_telnet__prompt_cd0f515948e1a1b0",
  "source_file": "topics/session_profile_properties_telnet.htm",
  "source_original_path": "topics/session_profile_properties_telnet.htm",
  "toc_path": [
    "iTest Online Help",
    "Telnet Sessions",
    "Session profile property settings for Telnet sessions"
  ],
  "heading_path": [
    "Session profile property settings for Telnet sessions",
    "Session profile property settings for Telnet sessions",
    "Prompt"
  ],
  "anchor": "1225344",
  "context_ids": [
    "session_profile_properties_telnet"
  ],
  "index_keywords": [
    "Additional connection information property",
    "Configuring Telnet",
    "HA mode",
    "High Availability Mode property",
    "Negotiate Telnet options",
    "Telnet options",
    "Telnet property settings",
    "Telnet sessions",
    "configuring",
    "configuring socket",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "Additional connection information property",
    "HA mode",
    "High Availability Mode property",
    "Negotiate Telnet options",
    "Telnet > configuring socket",
    "Telnet options",
    "Telnet sessions > configuring",
    "Telnet sessions > session profile property settings",
    "configuring > Telnet sessions",
    "property settings > Telnet sessions",
    "session profiles > Telnet property settings",
    "socket > Configuring Telnet"
  ],
  "related_links": [
    "prompts.1.htm#1100299",
    "prompts.5.htm#1272830",
    "#1147390"
  ],
  "images": [],
  "content_hash": "cd0f515948e1a1b0",
  "level": 2
}
---

# Session profile property settings for Telnet sessions > Session profile property settings for Telnet sessions > Prompt

For an overview on how iTest recognizes prompts, see Overview: Prompts in iTest.

For instructions on using the properties in this group to define prompts, see Editing prompt definitions.

For related prompt properties, see Terminal > Replay > Step Defaults > Completion.

| Name | The name helps you to remember the type of prompt, for example, LoginPrompt. Default: [various] |
| --- | --- |
| Content | Specify the exact text of the prompt. Note: All prompt definitions are case-insensitive and leading and trailing whitespace is trimmed from any prompt text before iTest attempts to determine whether response text is a prompt. If you use regular expressions in the Content value, then set the Type property to Regex. If the prompt includes a space character or any whitespace in the body of the text, be sure to set the Type property to Wildcard. Default: [none] |
| Type | Specify the kind of prompt. Normal: Interpret the text in the Content field as the case-insensitive text that you expect for the prompt. Wildcard: Disregard any characters that appear in the location of the * character in the text specified for the Content property. The most common application for the Wildcard setting is to allow for leading or trailing numeric or UserID characters in the prompt (for example Device02>, Device03>, and so on). If you set Type=Wildcard, then only the * wildcard character is allowed within the Content string (and no other wildcard characters like ?). To use other wildcard characters in the Content string, you must use Type=Regex. Regex: Interpret the text specified for the Content property as a regular expression. Default: [none] |
| Is more prompt More next command More quit command | The -- more -- prompt is a common method for allowing command line users to view one screen (page) at a time. Many devices use the space character as the command to move to the next page (and often, the letter q to exit the display of the response). To enable your automated test cases to page through data that is displayed one page at a time, iTest can automatically “press the space bar” as often as is required to get to the end of the response. As a result, the device's response to the command becomes a single uninterrupted flow of text that does not include the More text. If the prompt is a page-control prompt (for example - - more - -, then: Select the Is More prompt checkbox. In the More next command text box, specify the command characters (typically a space character) that cause the next page to appear. By default, a space character appears in the box. You may also send a carriage return in More next command, use syntax as shown below. [char('Carriage Return')] or [char('\\r')] In the More quit command text box, specify the command that exits the More display and returns to the command line prompt. By default, a q character appears in the box. Specify a value for Terminal > Replay > Step Defaults > More. |

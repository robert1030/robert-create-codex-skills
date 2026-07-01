---
{
  "chunk_id": "session_profile_properties_bash__terminal_prompts_b549d53382cb3799",
  "source_file": "topics/session_profile_properties_bash.htm",
  "source_original_path": "topics/session_profile_properties_bash.htm",
  "toc_path": [
    "iTest Online Help",
    "Bash sessions",
    "Session profile property settings for Bash sessions (Ubuntu and RHEL)"
  ],
  "heading_path": [
    "Session profile property settings for Bash sessions (Ubuntu and RHEL)",
    "Session profile property settings for Bash sessions (Ubuntu and RHEL)",
    "terminal > Prompts"
  ],
  "anchor": "1413259",
  "context_ids": [
    "session_profile_properties_bash"
  ],
  "index_keywords": [
    "Bash sessions",
    "Bash sessions configuring",
    "Linux Bash sessions",
    "configuring Bash sessions",
    "session properties",
    "starting"
  ],
  "index_keyword_paths": [
    "Bash sessions configuring",
    "Linus Bash sessions > starting",
    "configuring > Bash sessions",
    "opening > Linux Bash sessions",
    "property settings > Bash sessions",
    "session properties",
    "sessions > configuring Bash sessions",
    "starting > Linux Bash sessions"
  ],
  "related_links": [
    "prompts.1.htm#1100299",
    "prompts.5.htm#1272830",
    "#1362938"
  ],
  "images": [
    "topics/images/bash_defaultPromptsDefined.png"
  ],
  "content_hash": "b549d53382cb3799",
  "level": 3
}
---

# Session profile property settings for Bash sessions (Ubuntu and RHEL) > Session profile property settings for Bash sessions (Ubuntu and RHEL) > terminal > Prompts

For an overview on how prompts work, see Overview: Prompts in iTest.

For instructions on using the properties in this group to define prompts, see Editing prompt definitions.

For related prompt properties, see Terminal > Replay > Step Defaults > Completion.

| Prompts: defaultBashPrompt defaultRootPrompt | The Prompts section displays the default prompts defined. The Bash session will have two built-in prompts $ and #. The following shows you the default prompts defined in Bash sessions. |
| --- | --- |

| Name | Note This property setting has no effect for Bash sessions. | Note | This property setting has no effect for Bash sessions. |
| --- | --- | --- | --- |
| Note | This property setting has no effect for Bash sessions. |  |  |
| Content | Specify the exact text of the prompt. Note All prompt definitions are case-insensitive and leading and trailing whitespace is trimmed from any prompt text before iTest attempts to determine whether response text is a prompt. If you use regular expressions in the Content value, then set the Type property to Regex. If the prompt includes a space character or any whitespace in the body of the text, be sure to set the Type property to Wildcard. Default: [none] | Note | All prompt definitions are case-insensitive and leading and trailing whitespace is trimmed from any prompt text before iTest attempts to determine whether response text is a prompt. |
| Note | All prompt definitions are case-insensitive and leading and trailing whitespace is trimmed from any prompt text before iTest attempts to determine whether response text is a prompt. |  |  |
| Type | Specify the kind of prompt. Normal: Interpret the text in the Content field as the case-insensitive text that you expect for the prompt. Wildcard: Disregard any characters that appear in the location of the * character in the text specified for the Content property. The most common application for the Wildcard setting is to allow for leading or trailing numeric or UserID characters in the prompt (for example Device02>, Device03>, and so on). If you set Type=Wildcard, then only the * wildcard character is allowed within the Content string (and no other wildcard characters like ?). To use other wildcard characters in the Content string, you must use Type=Regex. Regex: Interpret the text specified for the Content property as a regular expression. Default: [none] |  |  |
| Is more prompt More next command More quit command | The -- more -- prompt is a common method for allowing command line users to view one screen (page) at a time. Many devices use the space character as the command to move to the next page (and often, the letter q to exit the display of the response). To enable your automated test cases to page through data that is displayed one page at a time, iTest can automatically “press the space bar” as often as is required to get to the end of the response. As a result, the device's response to the command becomes a single uninterrupted flow of text that does not include the More text. If the prompt is a page-control prompt (for example - - more - -, then: 1. Select the defaultRootPrompt checkbox. 2. In the More next command text box, specify the command characters (typically a space character) that cause the next page to appear. By default, a space character appears in the box. 3. In the More quit command text box, specify the command that exits the More display and returns to the command line prompt. By default, a q character appears in the box. 4. Specify a value for Terminal > Replay > Step Defaults > More. | 1. | Select the defaultRootPrompt checkbox. |
| 1. | Select the defaultRootPrompt checkbox. |  |  |
| 2. | In the More next command text box, specify the command characters (typically a space character) that cause the next page to appear. By default, a space character appears in the box. |  |  |
| 3. | In the More quit command text box, specify the command that exits the More display and returns to the command line prompt. By default, a q character appears in the box. |  |  |
| 4. | Specify a value for Terminal > Replay > Step Defaults > More. |  |  |

![screenshot](topics/images/bash_defaultPromptsDefined.png) <!-- image_chunk: img_667f0350411118f8 -->

---
{
  "chunk_id": "prompts_5__example_unexpected_character_in_the_prom_9a33b2f5374b8def",
  "source_file": "topics/prompts.5.htm",
  "source_original_path": "topics/prompts.5.htm",
  "toc_path": [
    "iTest Online Help",
    "Prompts (in CLI sessions)",
    "Editing prompt definitions"
  ],
  "heading_path": [
    "Editing prompt definitions",
    "Editing prompt definitions",
    "Example: Unexpected character in the prompt"
  ],
  "anchor": "1113062",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "inheriting_prompt_definitions.htm#1114781",
    "session_profile_properties_cmd.htm#1413259",
    "session_profile_properties_serial.htm#1090399",
    "sp_properties_ssh.htm#1276599",
    "session_profile_properties_telnet.htm#1225344"
  ],
  "images": [
    "topics/images/prompts_3.1.jpg",
    "topics/images/prompts_2.2.jpg"
  ],
  "content_hash": "9a33b2f5374b8def",
  "level": 2
}
---

# Editing prompt definitions > Editing prompt definitions > Example: Unexpected character in the prompt

Some devices return prompts with the following formats (notice that an asterisk * character appears as part of the prompt 23 string):

Enter Password:*

Re-enter Password to Validate:*

The password prompt definition that you might have created does not expect to see the * character as the last character on the line. So, to allow iTest to accept this prompt, we'll define a new prompt.

1. On the Session Profile editor Start page, perform these steps depending on the sessions type.

- For SSH and Telnet session types, open the Prompts property settings.

- For the Command Prompt, Bash, and Serial sessions, click to open the Session Properties section, then open the Terminal > Prompts group of property settings.

1. 2

1. Enter the required information as described in the steps below.

1. 3

1. Check Include additional values from list to allow you to add a prompt definition. (For a discussion on inheriting prompt definitions from reference session profiles — the Include inherited values checkbox, see About inheriting prompt definitions.)

1. 4

1. Now, click to add a new prompt definition and name it asteriskAtEndPrompt.

We want iTest to accept prompts of the form *Password:*, so we type that text as the value of the Content property.

The Content Type is Wildcard because we want iTest to interpret the * character to mean “any number of any character, including whitespace”.

- All prompt definitions are case-insensitive.

- Leading and trailing whitespace is trimmed from any prompt text before iTest attempts to determine whether response text is a prompt.

- If you use regular expressions in the Content value, then set the Type property to Regex.

- If the prompt includes a space character or any whitespace in the body of the text, be sure to set the Content Type property to Wildcard.

This new prompt definition enables iTest to now accept prompt text that matches any text (represented by the first wildcard *), followed by the text string “Password:”, followed by any additional text (represented by the second wildcard *).

- Select More prompt property settings to enter more next command and more quit command. For these more prompts you may also select option to indicate High Availability: Normal, Master, Slave or Other.

> **Note:** Note When sending a carriage return in the session profile, use syntax as shown below. For example: in More prompt >More next command use command as below.[char('Carriage Return')] or [char('\\r')]

> **Tip:** Tip To avoid unnecessary interruption while testing, after you have added all prompt definitions to a session profile or device definition, you can uncheck Learn prompts in the Capture properties group.

> **Note:** Note The property settings discussed in this example are fully described for each CLI session type in the associated “Terminal > Prompts” section:

Command Prompt sessions: Terminal > Prompts

Serial sessions: Terminal > Prompts

SSH sessions: Prompt

> **Note:** Telnet sessions: Prompt

![screenshot](topics/images/prompts_3.1.jpg) <!-- image_chunk: img_c697837844bb404b -->

![inline_icon](topics/images/prompts_2.2.jpg) <!-- image_chunk: img_6efd4cb75abd0dbd -->

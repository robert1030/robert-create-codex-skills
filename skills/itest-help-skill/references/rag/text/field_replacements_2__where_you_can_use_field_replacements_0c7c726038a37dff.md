---
{
  "chunk_id": "field_replacements_2__where_you_can_use_field_replacements_0c7c726038a37dff",
  "source_file": "topics/field_replacements.2.htm",
  "source_original_path": "topics/field_replacements.2.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "Where you can use field replacements"
  ],
  "heading_path": [
    "Where you can use field replacements",
    "Where you can use field replacements"
  ],
  "anchor": "1360763",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "tce_step_properties_general.htm#1973025"
  ],
  "images": [
    "topics/images/field_replacements.01.jpg",
    "topics/images/field_replacements.04.jpg"
  ],
  "content_hash": "0c7c726038a37dff",
  "level": 1
}
---

# Where you can use field replacements > Where you can use field replacements

You can use field replacements in most user-defined text or numeric values that are used during execution, for example:

- Test case step properties like Session

- The text of test case Comment steps

- User-defined text values in analysis rules, for example, the Extractors set of properties

- Session profile properties like the IP address of the device. For example:

> **Note:** Note The [param], [get], [gget] should have default values, if not, the variable and parameter substitution will fail when a session profile is manually started.

- The text of the message property in events and analysis rules

- Prompt Content property values (that is, the text that appears in the prompt)

- test case command and variable substitution. See the following examples:

Example: [iTestVersion] might return the float value of 7.1, [iTestPlatform] might return the string ‘eclipse’, and [f.readline()] might return the string “next line of file text”

Example: command echo [import sys; sys.platform]

> **Note:** Note Python uses the Square brackets to determine expression only for session commands.

- Supports '['

- Example: "\[qwe]" will be passed as [qwe] without substitutions.

iTest displays an icon on the text box for properties that will undergo substitution of field replacement text at runtime. In the example, you can see that the Thread name, Session, Context, and Command properties will be substituted at runtime if the property string includes field replacement text. Notice that the indicates that iTest will not perform substitution for the Target text.

Important The Command property is special in that it can also perform variable and backslash substitution and a command might be multiline for some protocols. To allow you to specify the behavior exactly as you need it, iTest provides the For the Command field, perform command, variable, and backslash substitutions check box. See Step Properties section: General properties group for details.

![screenshot](topics/images/field_replacements.01.jpg) <!-- image_chunk: img_5b166bf79b43cc49 -->

![screenshot](topics/images/field_replacements.04.jpg) <!-- image_chunk: img_ef16a46323e88a61 -->

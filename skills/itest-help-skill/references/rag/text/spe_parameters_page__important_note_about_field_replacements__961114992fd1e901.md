---
{
  "chunk_id": "spe_parameters_page__important_note_about_field_replacements__961114992fd1e901",
  "source_file": "topics/spe_parameters_page.htm",
  "source_original_path": "topics/spe_parameters_page.htm",
  "toc_path": [
    "iTest Online Help",
    "Session Profiles",
    "Session Profile editor: Attributes page"
  ],
  "heading_path": [
    "Session Profile editor: Attributes page",
    "Session Profile editor: Attributes page",
    "Important note about field replacements in session profile property settings"
  ],
  "anchor": "1279584",
  "context_ids": [
    "spe_parameters_page"
  ],
  "index_keywords": [
    "Attributes page",
    "New Session page",
    "Session Profile editor"
  ],
  "index_keyword_paths": [
    "Attributes page > New Session page",
    "Attributes page > Session Profile editor",
    "New Session page > Attributes page",
    "Session Profile editor > Attributes page"
  ],
  "related_links": [],
  "images": [
    "topics/images/session_profiles_7.1.jpg"
  ],
  "content_hash": "961114992fd1e901",
  "level": 2
}
---

# Session Profile editor: Attributes page > Session Profile editor: Attributes page > Important note about field replacements in session profile property settings

While you can specify field replacements in many session profile property settings, substitution occurs for some commands only at runtime (because a value required by the command is obtained from the execution context).

For example, the param command is replaced at runtime because it obtains the parameter value from the heap. The char command, in contrast, can be replaced at any time, because it does not rely on the execution context.

As a result, when you start a manual (interactive) session, char commands are replaced, but param commands are not. The session cannot start.

You can avoid this issue by specifying the optional default argument for any command that is replaced at runtime. The command is replaced during manual sessions using the default value that you specify for the default argument.

To determine whether a command are replaced only during execution (and therefore requires a value for the default argument to enable you to start manual sessions), type the [ character into the Description cell for the step — iTest displays the list of commands and their syntax. Any command that uses an optional ?default? argument is replaced during execution. In this example, you can see that the get and gget commands allow you to specify a default value.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/session_profiles_7.1.jpg) <!-- image_chunk: img_08ea4fae8b03817a -->

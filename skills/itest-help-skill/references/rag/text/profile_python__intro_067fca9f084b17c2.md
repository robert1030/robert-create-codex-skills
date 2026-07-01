---
{
  "chunk_id": "profile_python__intro_067fca9f084b17c2",
  "source_file": "popups/profile_python.html",
  "source_original_path": "popups/profile_python.html",
  "toc_path": null,
  "heading_path": [
    "profile_python.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/insert_parameter_dialog.html",
    "help::/com.fnfr.svt.help/topics/commands_commonly_used_in_field_replacement.html",
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html",
    "help::/com.fnfr.svt.help/topics/command_syntax_python.html"
  ],
  "images": [],
  "content_hash": "067fca9f084b17c2",
  "level": 0
}
---

# profile_python.html

profile('session', 'parameter_name_or_query', 'defaultValue')

Use the profile command to access the value of a parameter that is defined in the session profile associated with a particular session. Returns a profile parameter value.

Example: profile(in eval step): print(profile('s2','ip')) - Eval must be called while session is still open profile(in session command): ping [profile('.','ip')] - In session profile, add the 'ip' parameter in the 'Parameters' tab

For details, see the online help: Accessing parameter values: The profile command.

Also, see: Field replacements: Substituting values into properties and commands.

For details on using this and other iTest interpreter commands, see Command syntax for test case steps.

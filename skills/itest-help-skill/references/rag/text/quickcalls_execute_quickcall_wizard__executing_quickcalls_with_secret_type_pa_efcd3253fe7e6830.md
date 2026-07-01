---
{
  "chunk_id": "quickcalls_execute_quickcall_wizard__executing_quickcalls_with_secret_type_pa_efcd3253fe7e6830",
  "source_file": "topics/quickcalls_execute_quickcall_wizard.htm",
  "source_original_path": "topics/quickcalls_execute_quickcall_wizard.htm",
  "toc_path": [
    "iTest Online Help",
    "QuickCalls: Defining and using a library of custom actions",
    "Executing a QuickCall during a manual (interactive) session",
    "Executing a QuickCall during an interactive session"
  ],
  "heading_path": [
    "Executing a QuickCall during an interactive session",
    "Executing a QuickCall during an interactive session",
    "Executing QuickCalls with secret type parameter"
  ],
  "anchor": "1477504",
  "context_ids": [
    "quickcalls_execute_quickcall_wizard"
  ],
  "index_keywords": [
    "adding to a procedure call",
    "changing argument values",
    "specifying in session actions"
  ],
  "index_keyword_paths": [
    "arguments > adding to a procedure call",
    "arguments > specifying in session actions",
    "session actions > changing argument values"
  ],
  "related_links": [
    "pal_preferences_session_level_control_agent.htm#1444627",
    "param_parameters_type_secret.htm#1554375"
  ],
  "images": [
    "topics/images/qc_secretParameter_inSLCMode.png"
  ],
  "content_hash": "efcd3253fe7e6830",
  "level": 2
}
---

# Executing a QuickCall during an interactive session > Executing a QuickCall during an interactive session > Executing QuickCalls with secret type parameter

When Python SLC connected to iTest GUI and try access QuickCalls with secret values will trigger iTest GUI to show dialog to enter this secret values.

Executing QuickCalls that required secret value when iTest GUI is configured in listening mode (see Configure Listening Mode (Listen for incoming Python connections)), a dialog displays for entering the secret value. However, no output will be sent to the SLC library as response for any QuickCalls that use secret value.

See About the Parameter Type ‘Secret’.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/qc_secretParameter_inSLCMode.png) <!-- image_chunk: img_933bab4e6926efe4 -->

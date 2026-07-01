---
{
  "chunk_id": "tce_preferences_tce__properties_in_editors_test_case_editor_e_b96d00b64f42e653",
  "source_file": "topics/tce_preferences_tce.htm",
  "source_original_path": "topics/tce_preferences_tce.htm",
  "toc_path": [
    "iTest Online Help",
    "Test Case Editor",
    "Quality Center page on the Test Case Editor",
    "Setting preferences for the Test Case Editor"
  ],
  "heading_path": [
    "Setting preferences for the Test Case Editor",
    "Setting preferences for the Test Case Editor",
    "Properties in: Editors > Test Case Editor > Errors/Warnings"
  ],
  "anchor": "1915772",
  "context_ids": [
    "tce_preferences_tce"
  ],
  "index_keywords": [
    "Test Case editor",
    "preference settings",
    "test case preferences"
  ],
  "index_keyword_paths": [
    "Test Case editor > preference settings",
    "editors > test case preferences",
    "preference settings > Test Case editor"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "b96d00b64f42e653",
  "level": 2
}
---

# Setting preferences for the Test Case Editor > Setting preferences for the Test Case Editor > Properties in: Editors > Test Case Editor > Errors/Warnings

On this page, you indicate that the Test Case Editor displays a warning when the mandatory values and default values have not been specified.

| Severity levels displayed in the Problems view: | Indicates the message displayed in the Problem view is as per the level selected. For example, If you select Error, Warning, or Info, a message displays saying: Optional/Required argument(s) with default value(s) are not specified. |
| --- | --- |
| Default values(s) will be used for optional arguments(s) | Set the severity level to indicate that a procedure or QuickCall will use default values for the optional argument(s). That is, the argument value was not supplied, but a default value exists for the procedure or QuickCall. Options: Ignore, Error, Warning, Info Default: Ignore |
| Default values(s) will be used for required argument(s) | Set the severity level to indicate that a procedure or QuickCall will use default values for the required argument(s). That is, the argument value was not supplied, but a default value exists for the procedure or QuickCall. Options: Ignore, Error, Warning, Info Default: Ignore |

The severity level indicated are processed as follows.

| Process | If empty required argument, no default value... | If empty required arg, default value exists... | If empty optional argument, default exists... |
| --- | --- | --- | --- |
| validation | Displays validation error | As per the setting in Wndows>Preferences for the required argument | As per the setting in Wndows>Preferences for optional arguments |
| execution | Displays warning message | Displays warning message | Displays warning message |

---
{
  "chunk_id": "parameters_10__to_mask_a_value_1fe0b978e769ee5c",
  "source_file": "topics/parameters.10.htm",
  "source_original_path": "topics/parameters.10.htm",
  "toc_path": [
    "iTest Online Help",
    "Parameters",
    "Using Parameters in Properties or Steps",
    "Masking a parameter’s value"
  ],
  "heading_path": [
    "Masking a parameter’s value",
    "Masking a parameter’s value",
    "To mask a value"
  ],
  "anchor": "1144742",
  "context_ids": [],
  "index_keywords": [
    "masking in parameters",
    "masking parameter values",
    "masking values"
  ],
  "index_keyword_paths": [
    "masking parameter values",
    "parameters > masking values",
    "passwords > masking in parameters"
  ],
  "related_links": [
    "preferences_itest.htm#",
    "preferences.03.htm#1162820"
  ],
  "images": [],
  "content_hash": "1fe0b978e769ee5c",
  "level": 2
}
---

# Masking a parameter’s value > Masking a parameter’s value > To mask a value

1. 1

1. On the Parameters page of the appropriate editor, check Mask the value.

1. 2

1. When you create a command string with a field replacement such as [param my_password], the iTest interpreter returns the encrypted string. To notify the executing test case to use the decrypted string, you must specify the Command uses encrypted parameters property for the step.

The Mask the value option is available for selection only when the Type is text and grayed for the rest of the parameter Type.

For Secret parameter type, Mask the value is automatically enabled and masked by default, which you may uncheck.

When you uncheck, iTest displays a Clear field content? dialog with a warning message informing that the masked data will be lost and whether you would to unmask the field and clear the content. The dialog also allows you to set your preference to not display this dialog again.

- You may select the checkbox Do not ask again to make sure that the Clear filed content? dialog does not display again.

- Click Yes to save your selection and acknowledge unmasking and clearing the content and No to discard the clear field content operation.

See also Preferences: Spirent > Editors, Chapter 39, “Configuring iTest Preferences”.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

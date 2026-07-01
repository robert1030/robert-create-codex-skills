---
{
  "chunk_id": "parameters_10__masking_a_parameter_s_value_e17e4a0f64ba20c6",
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
    "Masking a parameter’s value"
  ],
  "anchor": "1144740",
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
  "related_links": [],
  "images": [],
  "content_hash": "e17e4a0f64ba20c6",
  "level": 1
}
---

# Masking a parameter’s value > Masking a parameter’s value

While defining or editing a parameter, you can mask its value — specify that the value should be hidden from view in any user-visible windows (for example, a password). iTest performs the following actions for masked parameter values to ensure that the value remains confidential:

- Encrypt the parameter value

- Display the value as asterisks (********) in any editor, view, or report

- The param and profile commands never decrypt any parameter whose value is masked. As a result, the value never appears in clear (unencrypted) form in any file or in any editor, view, or report visible to a user

Important To protect the values of masked parameters: If a user attempts to unmask a parameter by selecting it and then unchecking the Mask the value check box, the value of the parameter is deleted.

---
{
  "chunk_id": "file_session_editor__modifying_command_properties_at_runtime_cd55125d52a90f79",
  "source_file": "topics/file_session_editor.htm",
  "source_original_path": "topics/file_session_editor.htm",
  "toc_path": [
    "iTest Online Help",
    "File sessions",
    "About File sessions"
  ],
  "heading_path": [
    "About File sessions",
    "About File sessions",
    "Modifying command properties at runtime"
  ],
  "anchor": "1203817",
  "context_ids": [
    "file_session_editor"
  ],
  "index_keywords": [
    "File sessions",
    "test cases"
  ],
  "index_keyword_paths": [
    "File sessions > test cases",
    "test cases > File sessions"
  ],
  "related_links": [
    "field_replacements_tasks.htm#",
    "tce_step_properties_open_step.htm#1716227"
  ],
  "images": [],
  "content_hash": "cd55125d52a90f79",
  "level": 2
}
---

# About File sessions > About File sessions > Modifying command properties at runtime

- In test cases, all File step properties support field replacement (properties with the indicator), so you can dynamically control a step at runtime. For example, you can dynamically set the number of lines to read in a read step using a variable. Let’s say that step 16 set the value of the variable named linesToRead. Step 17 could use the command text read $linesToRead

See “Field Replacements”.

- You can use also field replacements to provide values for most properties in File session profiles. For example, for the URI property, you could use: [param file_uri]

- For the open step, you have the option to override any of the property settings so that all steps in the session use the new property settings. Change any of the properties for the open step in the <sessionType> Session Properties section. See Step Properties section: Session Properties: Overriding device or session profile settings in the open step.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

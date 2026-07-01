---
{
  "chunk_id": "qc_python__intro_2fadffea66906acb",
  "source_file": "popups/qc_python.html",
  "source_original_path": "popups/qc_python.html",
  "toc_path": null,
  "heading_path": [
    "qc_python.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/field_replacements_tasks.html"
  ],
  "images": [],
  "content_hash": "2fadffea66906acb",
  "level": 0
}
---

# qc_python.html

qc('option', 'arg', 'arg', '...')

qc('setArtifactsLocation', 'URI')

Sets the artifactsLocation property in the QualityCenterInfo section of the test report. When excution finishes, iTest zips the artifacts and saves the zipped file to the specified loaction.

qc('getArtifactsLocation', 'URI')

Returns the value of the artifactsLocation property in the QualityCenterInfo section of the test report.

Example: eval qc("setArtifactsLocation", "file:/C:/Program%20Files%20(x86)/Spirent%20Communications/iTest%207.1.0/") eval qc("getArtifactsLocation")

Also, see: Field replacements: Substituting values into properties and commands.

---
{
  "chunk_id": "field_replacements_6__string_concatenation_using_python_syntax_404c04da71697b03",
  "source_file": "topics/field_replacements.6.htm",
  "source_original_path": "topics/field_replacements.6.htm",
  "toc_path": [
    "iTest Online Help",
    "Field Replacements",
    "Guidelines for using field replacements"
  ],
  "heading_path": [
    "Guidelines for using field replacements",
    "Guidelines for using field replacements",
    "String Concatenation using Python Syntax"
  ],
  "anchor": "1397815",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "404c04da71697b03",
  "level": 2
}
---

# Guidelines for using field replacements > Guidelines for using field replacements > String Concatenation using Python Syntax

The following describes string concatenation using Python syntax. For example:

When performing substitution in test cases where the interpreter language is set to Python, string concatenation can be used as an effective way to construct commands. Use the "+" operator in Python to build complex expressions using substrings.

Example 1: When referencing a parameter value where "i" is the string "LAN", the following syntax could be used: [param('interfaceName_' + i)] to invoke the constructed command: param('interfaceName_LAN')

Example 2: When using the query command to access a value with an index of "i", the following syntax could be used: [query('arpTable','ipAddress("' + i + '")')] to invoke the constructed command: query('arpTable','ipAddress("10.1.1.1")')

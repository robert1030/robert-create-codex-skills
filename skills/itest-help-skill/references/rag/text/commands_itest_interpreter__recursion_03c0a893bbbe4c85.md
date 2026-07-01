---
{
  "chunk_id": "commands_itest_interpreter__recursion_03c0a893bbbe4c85",
  "source_file": "topics/commands_itest_interpreter.htm",
  "source_original_path": "topics/commands_itest_interpreter.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "iTest interpreter commands",
    "iTest interpreter commands"
  ],
  "heading_path": [
    "iTest interpreter commands",
    "iTest interpreter commands",
    "Recursion"
  ],
  "anchor": "1684597",
  "context_ids": [
    "commands_itest_interpreter"
  ],
  "index_keywords": [
    "iTest",
    "iTest commands",
    "inserting into test case steps",
    "inserting variables and parameters into"
  ],
  "index_keyword_paths": [
    "iTest > command syntax > command syntax > iTest",
    "parameters > inserting into test case steps",
    "steps > inserting variables and parameters into",
    "syntax > iTest commands",
    "variables > inserting into test case steps"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "03c0a893bbbe4c85",
  "level": 2
}
---

# iTest interpreter commands > iTest interpreter commands > Recursion

Any command can itself include inserted commands (to any level of recursion). In this example concat command (that concatenates a name and a file extension to result in a proper filename), the string representing the name is substituted with the value of a parameter named inputFile. So, if at runtime the inputFile parameter has the value myFile, then the following construct is replaced by a filename: myFile.fftc

Tcl: [concat [param inputFile] .fftc]

Python:

param(param('name_of_parameter'))

gget('varName', param('my_param'))

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

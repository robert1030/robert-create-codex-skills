---
{
  "chunk_id": "action_readfile__adding_a_readfile_step_589d7e3e652faf19",
  "source_file": "topics/action_readfile.htm",
  "source_original_path": "topics/action_readfile.htm",
  "toc_path": [
    "iTest Online Help",
    "Actions",
    "Actions for CLI session types",
    "The ‘readFile’ action: Return the contents of a file"
  ],
  "heading_path": [
    "The ‘readFile’ action: Return the contents of a file",
    "The ‘readFile’ action: Return the contents of a file",
    "Adding a readFile step"
  ],
  "anchor": "1519655",
  "context_ids": [
    "action_readfile"
  ],
  "index_keywords": [
    "readFile",
    "readFile action",
    "returning in test case"
  ],
  "index_keyword_paths": [
    "EXEC Step Defaults > readFile",
    "actions > readFile",
    "file contents > returning in test case",
    "readFile action",
    "text > returning in test case"
  ],
  "related_links": [
    "tl1.1.htm#1152885"
  ],
  "images": [],
  "content_hash": "589d7e3e652faf19",
  "level": 3
}
---

# The ‘readFile’ action: Return the contents of a file > The ‘readFile’ action: Return the contents of a file > Adding a readFile step

1. 1

1. Create the step with an Action of readFile. Do not specify a session.

1. 2

1. In the Description cell (or Command property) for the step, specify the file. To enable the use of typical URI and directory path syntax, field replacements are not supported in this field.

You can type or paste the URI or file path of the file, or, more typically, do either of the following:

- Click Browse in the Description cell

- In the Step Properties section > General page, Click Browse for the Command property

The File Selection dialog box opens. Specify one of the following:

- Workspace (the file is in the current iTest workspace)

- File system (the file is not in the workspace, but is somewhere on the file system)

Browse to the file and then click OK. iTest adds the URI of the file to the Description cell.

1. 3

1. In the Step Properties section, open the EXEC readFile Properties > ReadFile properties group and specify settings for the following properties:

| Content type | Text: A text file (you specify the encoding type using the Encoding property) Text/xml: An XML‑format file Text/html: An HTML‑format file Text/tl1: A file containing a valid TL1 message or sequence of messages. Note For more information on TL1 steps, see Configuring sessions and test case steps for TL1 devices. Binary: A file containing arbitrary binary data. Default: Text | Note | For more information on TL1 steps, see Configuring sessions and test case steps for TL1 devices. |
| --- | --- | --- | --- |
| Note | For more information on TL1 steps, see Configuring sessions and test case steps for TL1 devices. |  |  |
| Encoding | Optional. Specify the encoding type so that the text file can be properly read or parsed. You can either type the encoding name into the box or select it from the list. The list includes all encoding types that are supported by the operating system. Note Encoding is ignored if Content type is set to Binary. Default: UTF-8 | Note | Encoding is ignored if Content type is set to Binary. |
| Note | Encoding is ignored if Content type is set to Binary. |  |  |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

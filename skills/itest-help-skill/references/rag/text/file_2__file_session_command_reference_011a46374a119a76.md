---
{
  "chunk_id": "file_2__file_session_command_reference_011a46374a119a76",
  "source_file": "topics/file.2.htm",
  "source_original_path": "topics/file.2.htm",
  "toc_path": [
    "iTest Online Help",
    "File sessions",
    "File session command reference"
  ],
  "heading_path": [
    "File session command reference",
    "File session command reference"
  ],
  "anchor": "1217207",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "011a46374a119a76",
  "level": 1
}
---

# File session command reference > File session command reference

File session steps support the following commands:.

| exit | Closes the file and closes the FIle session. |
| --- | --- |
| help [<prefix>] Alternatively, type ? | Returns the description of the specified command. If no command is specified or if ? is used, returns the full list of commands and descriptions. |
| File operations: |  |
| copyFrom <project or file URI> | Writes binary data (for SFTP) from a file addressed by <project or file URI> replacing the contents of the file referenced in the session profile URI. Note If the URI in the session profile is not an sftp:// URI, then iTest displays an error. |
| Note | If the URI in the session profile is not an sftp:// URI, then iTest displays an error. |
| copyTo <project or file URI> | Read binary data (for SFTP) from the file referenced in the session profile URI and write it to the file addressed by <project or file URI> replacing its content. Note If the URI in the session profile is not an sftp:// URI, then iTest displays an error. |
| Note | If the URI in the session profile is not an sftp:// URI, then iTest displays an error. |
| Content line operations: |  |
| eof | Returns true if the file pointer is at the end of file. Otherwise returns false. Tip Store the response in a variable for use as a loop controller while reading individual lines in a loop. |
| Tip | Store the response in a variable for use as a loop controller while reading individual lines in a loop. |
| read [Count] | Returns the specified number of lines from the file. The file pointer remains at the beginning of the line after the last read line. Note The Access mode property must be set to READ. |
| Note | The Access mode property must be set to READ. |
| skip [Count] | Starting at the current file pointer position, moves the pointer the specified number of lines. Note The skip operation is not supported in WRITE mode sessions. |
| Note | The skip operation is not supported in WRITE mode sessions. |
| write [dataToWrite] | Writes the data text at eof (after the last line). If the text includes space characters, enclose the text in quotes.The Access mode property must be set to WRITE. Note write mode is not supported for zip, jar, tar, tgz, or tbz2 file types. write mode is not supported when the URI uses HTTP, HTTPS, or SFTP. Tip Use substitution to specify the text dynamically. |
| Note | write mode is not supported for zip, jar, tar, tgz, or tbz2 file types. write mode is not supported when the URI uses HTTP, HTTPS, or SFTP. |
| Tip | Use substitution to specify the text dynamically. |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

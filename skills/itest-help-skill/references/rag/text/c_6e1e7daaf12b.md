# File sessions > File session command reference

File session steps support the following commands:.

Note If the URI in the session profile is not an sftp:// URI, then iTest displays an error.

Note If the URI in the session profile is not an sftp:// URI, then iTest displays an error.

Tip Store the response in a variable for use as a loop controller while reading individual lines in a loop.

Note The Access mode property must be set to READ.

Note The skip operation is not supported in WRITE mode sessions.

| 欄位1 | 欄位2 |
| --- | --- |
| exit | Closes the file and closes the FIle session. |
| help [<prefix>] Alternatively, type ? | Returns the description of the specified command. If no command is specified or if ? is used, returns the full list of commands and descriptions. |
| File operations: |  |
| copyFrom <project or file URI> | Writes binary data (for SFTP) from a file addressed by <project or file URI> replacing the contents of the file referenced in the session profile URI. |
| copyTo <project or file URI> | Read binary data (for SFTP) from the file referenced in the session profile URI and write it to the file addressed by <project or file URI> replacing its content. |
| Content line operations: |  |
| eof | Returns true if the file pointer is at the end of file. Otherwise returns false. |
| read [Count] | Returns the specified number of lines from the file. The file pointer remains at the beginning of the line after the last read line. |
| skip [Count] | Starting at the current file pointer position, moves the pointer the specified number of lines. |
| write [dataToWrite] | Writes the data text at eof (after the last line). If the text includes space characters, enclose the text in quotes.The Access mode property must be set to WRITE. |

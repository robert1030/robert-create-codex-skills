---
{
  "chunk_id": "commands_file__commands_for_managing_files_and_director_736b06dde072da82",
  "source_file": "topics/commands_file.htm",
  "source_original_path": "topics/commands_file.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Commands",
    "File and directory management commands",
    "Commands for managing files and directories"
  ],
  "heading_path": [
    "Commands for managing files and directories",
    "Commands for managing files and directories"
  ],
  "anchor": "1810683",
  "context_ids": [
    "commands_file"
  ],
  "index_keywords": [
    "file",
    "file commands"
  ],
  "index_keyword_paths": [
    "commands > file",
    "file commands"
  ],
  "related_links": [
    "command_file_copy.htm#1754878",
    "command_file_delete.htm#1754923",
    "command_file_exists.htm#1754941",
    "command_file_isdirectory.htm#1754963",
    "command_file_isfile.htm#1754952",
    "command_file_list.htm#1754970",
    "command_file_mkdir.htm#1755011",
    "command_file_mktempdir.htm#1755026",
    "command_file_mktempfile.htm#1755045",
    "command_file_move.htm#1755063",
    "command_file_pathtouri.htm#1755110",
    "command_file_rmdir.htm#1755124",
    "command_file_uritopath.htm#1755140"
  ],
  "images": [],
  "content_hash": "736b06dde072da82",
  "level": 1
}
---

# Commands for managing files and directories > Commands for managing files and directories

The file group of commands enables you to manage files and directories, whether in the workspace or elsewhere on the file system.

| Command | Description |
| --- | --- |
| file copy [-y] sourceURI destinationURI | Copies files from the specified source directory or file URI to the specified destination. Creates destination directories as needed. See file copy command: Copying files to a destination URI. |
| file delete [-r] URI | Deletes files from the specified directory or file URI. See file delete command: Delete files. |
| file exists URI | Returns 1 (one) if the file or directory exists, otherwise returns 0 (zero). See file exists command: Determine whether a file or folder exists. |
| file isDirectory URI | Returns 1 (one) if the URI is a directory, otherwise returns 0 (zero). See file isDirectory command: Determine whether a URI represents a folder name. |
| file isFile URI | Returns 1 (one) if the URI is a filename, otherwise returns 0 (zero). See file isFile command: Determine whether a URI represents a filename. |
| file list [-r] [-p] [-nolimit] URI | Lists all files and subdirectories for the specified directory or file URI See file list command: List the files in a URI. |
| file mkdir URI | Creates the specified directory See file mkdir command: Add a directory. |
| file mkTempDir [-k] [prefix] [suffix] | Creates a temporary directory See file mkTempDir command: Create a unique temporary directory. |
| file mkTempFile [-k] [prefix] [suffix] | Creates a temporary file. See file mkTempFile command: Create a unique temporary file. |
| file move [-y] sourceURI destinationURI | Moves files from the specified source directory or file URI to the specified destination. Creates destination directories as needed. The move command can rename individual files and directories. See file move command: Move or rename files to a destination URI. |
| file pathToUri path | Returns the URI for the specified directory or file path. Python file_pathToURI is the Python equivalent of Tcl command pathToUri. See file pathToUri command: Determining the URI of a path |
| file rmdir URI | Deletes the specified directory. See file rmdir command: Delete a directory. |
| file uriToPath URI | Returns the full operating system path for the specified URI (using appropriate path syntax). Python file_uriToPath is the Python equivalent of Tcl command uriToPath. See file uriToPath command: Determining a path from a URI. |

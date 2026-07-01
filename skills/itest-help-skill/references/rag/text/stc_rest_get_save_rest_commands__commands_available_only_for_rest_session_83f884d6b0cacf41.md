---
{
  "chunk_id": "stc_rest_get_save_rest_commands__commands_available_only_for_rest_session_83f884d6b0cacf41",
  "source_file": "topics/stc_rest_get_save_rest_commands.htm",
  "source_original_path": "topics/stc_rest_get_save_rest_commands.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent TestCenter REST sessions",
    "Spirent TestCenter REST session profiles",
    "Commands available only for REST sessions"
  ],
  "heading_path": [
    "Commands available only for REST sessions",
    "Commands available only for REST sessions"
  ],
  "anchor": "1474242",
  "context_ids": [
    "stc_rest_get_save_rest_commands"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "83f884d6b0cacf41",
  "level": 1
}
---

# Commands available only for REST sessions > Commands available only for REST sessions

iTest provides Spirent TestCenter REST commands to allow you to display and download files from the Spirent TestCenter Lab Server listed on the /stcapi/files API.

| Command | Description |
| --- | --- |
| Get files(GET http://.../stcapi/files) | Command to get/show all files on the Spirent TestCenter lab server. There are no properties. |
| Save file (GET http://.../stcapi/files/file_name) | Command to save the specified file from the Spirent TestCenter lab server on the local machine. File location or folder: fileLocation, data type: uri, Default: empty. Specify file or folder URI on the local machine (required) File Name: fileName, data type: string, Default: empty. Specify name of file from the STC lab server (required). |
|  | File location or folder: fileLocation, data type: uri, |
|  | File Name: fileName, data type: string, |

Follow these steps to capture command On iTest Spirent TestCenter REST Session Console, save as iTest STC REST Session test case, and execute test case as required.

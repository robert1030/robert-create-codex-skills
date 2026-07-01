---
{
  "chunk_id": "ui_spirent_url__formats_of_commonly_used_uris_185ebb4583fb6cbe",
  "source_file": "topics/ui_spirent_url.htm",
  "source_original_path": "topics/ui_spirent_url.htm",
  "toc_path": [
    "iTest Online Help",
    "About the iTest Window",
    "URIs"
  ],
  "heading_path": [
    "URIs",
    "URIs",
    "Formats of commonly used URIs"
  ],
  "anchor": "1126593",
  "context_ids": [
    "ui_spirent_url"
  ],
  "index_keywords": [
    "URIs",
    "URIs in iTest"
  ],
  "index_keyword_paths": [
    "URIs in iTest",
    "filenames > URIs",
    "files > URIs",
    "paths > URIs"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "185ebb4583fb6cbe",
  "level": 2
}
---

# URIs > URIs > Formats of commonly used URIs

| project:// | Relative to the specified project. Format: project://project_name/directory_name/subdirectory_name/filename Relative to the current project. Format: project://directory_name/subdirectory_name/filename |
| --- | --- |
| file:/ | Relative to the root of the file system. Format: file:/subdirectory_name/filename.fftc |
| Relative to the current file | Relative to the current file (typically a file in the same directory or in a subdirectory). File-relative URIs use no slashes after the colon. For example, subdirBelowMe/filename.fftc means a reference to a file called filename.fftc in the subdirectory subdirBelowMe that is under the directory where the current file is located. ../subdirNetToMe/filename.fftc means a reference to a file called filename.fftc in the subdirectory subdirNetToMe that is at the same level as the directory where the current file is located. |
| . (the current URI ) | Use "." for a URI that is pointing at the same directory as the current URI's directory. This is similar to directory syntax in operating systems where . and ./ refer to the current directory and ../ refers to the parent directory. |

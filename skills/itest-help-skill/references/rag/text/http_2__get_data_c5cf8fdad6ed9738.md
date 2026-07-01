---
{
  "chunk_id": "http_2__get_data_c5cf8fdad6ed9738",
  "source_file": "topics/http.2.htm",
  "source_original_path": "topics/http.2.htm",
  "toc_path": [
    "iTest Online Help",
    "HTTP Sessions",
    "HTTP commands"
  ],
  "heading_path": [
    "HTTP commands",
    "HTTP commands",
    "get data"
  ],
  "anchor": "1379267",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "c5cf8fdad6ed9738",
  "level": 2
}
---

# HTTP commands > HTTP commands > get data

get data fetches the contents of the specified URL and places summarized information about it into the body of the response. The information includes:

- Length (in bytes)

- Checksum (CRC32)

- Binary dump of up to the first 512 bytes using the conventional binary decode format as shown in the example.

get data is useful for non-text files (like images) when you want to use the checksum to validate that the file has not changed from what you expected.

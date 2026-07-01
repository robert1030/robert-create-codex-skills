---
{
  "chunk_id": "sp_properties_file__session_properties_file_d6adc69f003ce802",
  "source_file": "topics/sp_properties_file.htm",
  "source_original_path": "topics/sp_properties_file.htm",
  "toc_path": [
    "iTest Online Help",
    "File sessions",
    "Session profile property settings for File sessions"
  ],
  "heading_path": [
    "Session profile property settings for File sessions",
    "Session profile property settings for File sessions",
    "Session properties, File"
  ],
  "anchor": "1217660",
  "context_ids": [
    "sp_properties_file"
  ],
  "index_keywords": [
    "File property settings",
    "File sessions",
    "configuring",
    "session profile property settings"
  ],
  "index_keyword_paths": [
    "File sessions > configuring",
    "File sessions > session profile property settings",
    "configuring > File sessions",
    "property settings > File sessions",
    "session profiles > File property settings"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "d6adc69f003ce802",
  "level": 2
}
---

# Session profile property settings for File sessions > Session profile property settings for File sessions > Session properties, File

| URI | Specify the URI that locates the file. Supported notation: Local Files: project:// project-path [file://] absolute-path Zip, Jar and Tar: zip:// arch-file-uri[! absolute-path] jar:// arch-file-uri[! absolute-path] tar:// arch-file-uri[! absolute-path] gzip and bzip2: tgz:// arch-file-uri[! absolute-path] tbz2:// arch-file-uri[! absolute-path] HTTP, HTTPS, FTP, FTPS and SFTP: htttp://[ username[: password]@] hostname[: port][ absolute-path] htttps://[ username[: password]@] hostname[: port][ absolute-path] ftp://[ username[: password]@] hostname[: port][ absolute-path] ftps://[ username[: password]@] hostname[: port][ absolute-path] sftp://[ username[: password]@] hostname[: port][ absolute-path] |
| --- | --- |
| IPv6 host is always placed in square brackets in URIs, which is the simplest criteria to distinguish IPv6 hosts. Example IPv6 URI format: http://user:password@[fe80::3dd0:7f8e:57b7:34d5]:2222/test?param1=value1&param2=value2#anchor Note IPv6 also supports HTTP, HTTPS, FTP, FTPS and SFTP protocols. | Note |
| Note | IPv6 also supports HTTP, HTTPS, FTP, FTPS and SFTP protocols. |
|  | IPv6 address corner cases: https://www.rfc-editor.org/rfc/rfc4291 fe80::3dd0:7f8e:57b7:34d5 - basic case 2001:658:22a:cafe:: - no trailing zeroes case ::1 - the loopback address :: - the unspecified address 0:0:0:0:0:0:13.1.68.3 - form for a mixed environment of IPv4 and IPv6 ::13.1.68.3 - compressed form for a mixed environment of IPv4 and IPv6 ::FFFF:129.144.52.38 - compressed form for a mixed environment of IPv4 and IPv6 FF01::101 - a multicast address fe80::8b2:d61e:e5c:b333%15 - address with scopeId |
| Encoding | Specify the encoding type for the text file. Default: UTF-8 |
| Access mode | Specify how to work with the file. read text from the file write text into the file. Note write mode is not supported for zip, jar, tar, tgz, or tbz2 file types. write mode is not supported when the URI uses HTTP, HTTPS, or SFTP. |
| Note | write mode is not supported for zip, jar, tar, tgz, or tbz2 file types. write mode is not supported when the URI uses HTTP, HTTPS, or SFTP. |

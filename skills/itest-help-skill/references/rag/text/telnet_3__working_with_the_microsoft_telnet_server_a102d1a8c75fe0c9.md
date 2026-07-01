---
{
  "chunk_id": "telnet_3__working_with_the_microsoft_telnet_server_a102d1a8c75fe0c9",
  "source_file": "topics/telnet.3.htm",
  "source_original_path": "topics/telnet.3.htm",
  "toc_path": [
    "iTest Online Help",
    "Telnet Sessions",
    "Working with the Microsoft Telnet server"
  ],
  "heading_path": [
    "Working with the Microsoft Telnet server",
    "Working with the Microsoft Telnet server"
  ],
  "anchor": "1141761",
  "context_ids": [],
  "index_keywords": [
    "Microsoft Telnet server"
  ],
  "index_keyword_paths": [
    "Microsoft Telnet server",
    "Telnet > Microsoft Telnet server"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "a102d1a8c75fe0c9",
  "level": 1
}
---

# Working with the Microsoft Telnet server > Working with the Microsoft Telnet server

Microsoft’s Telnet server runs in two modes: stream or console (the default). iTest requires stream mode. On Windows XP or Server 2003, type the following commands at a command prompt on the PC that is running the Telnet service:

tlntadmn stop

tlntadmn config mode=stream

tlntadmn start

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

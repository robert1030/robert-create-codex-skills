---
{
  "chunk_id": "mibs_loading__two_options_c7ed60a11c5dec5b",
  "source_file": "topics/mibs_loading.htm",
  "source_original_path": "topics/mibs_loading.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "Loading your proprietary MIB files into iTest"
  ],
  "heading_path": [
    "Loading your proprietary MIB files into iTest",
    "Loading your proprietary MIB files into iTest",
    "Two options"
  ],
  "anchor": "1268090",
  "context_ids": [
    "mibs_loading"
  ],
  "index_keywords": [
    "loading",
    "loading proprietary into iTest",
    "proprietary",
    "proprietary MIB files into iTest"
  ],
  "index_keyword_paths": [
    "MIB files > loading proprietary into iTest",
    "MIBs > loading",
    "MIBs > proprietary",
    "loading > proprietary MIB files into iTest"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "c7ed60a11c5dec5b",
  "level": 2
}
---

# Loading your proprietary MIB files into iTest > Loading your proprietary MIB files into iTest > Two options

There are two options for specifying which MIBs to load:

- Specifying a different folder for MIBs: You set a property that causes iTest to look in another folder. This option has the advantage that the MIB definitions are independent of the computer on which iTest is running (for example, when your test group uses a standard location for MIB files). Subfolders are not supported, so all of the individual MIB definition files must appear in the specified folder. If you want to use the standard MIB files that iTest provides, then you must copy them to the folder.

- Copying your MIBs into the default folder (Not recommended): You copy your MIBs into the default folder (resources/SNMP/Mibs). Subfolders are not supported, so you copy the individual MIB definition files. This option is not recommended because it has the following disadvantage: If you discover problems with the custom MIBs, it might not be easy to locate and remove them.

> **Tip:** Tip To ensure good performance, add only the MIBs that you expect to use for testing.

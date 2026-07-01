---
{
  "chunk_id": "mibs_loading__specifying_a_shared_folder_for_mibs_82bd0e4f1f300d28",
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
    "Specifying a shared folder for MIBs"
  ],
  "anchor": "1268095",
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
  "images": [
    "topics/images/snmp_3.2.jpg"
  ],
  "content_hash": "82bd0e4f1f300d28",
  "level": 2
}
---

# Loading your proprietary MIB files into iTest > Loading your proprietary MIB files into iTest > Specifying a shared folder for MIBs

1. 1

1. Place all of your MIB definition files (uncompiled text format) into a particular directory. You must copy the individual files because subdirectories are not supported.

1. 2

1. Open the device's session profile and click to view the Session Properties section.

1. 3

1. In the tree, click SNMP MIB Browser > MIBs.

1. 4

1. In the MIBs folder text box, type or paste the URI of the directory. For example, myhost:///mymibs or filename:///c/mymibs. (Remember, subdirectories are not supported.)

1. 5

1. Click Save.

1. 6

1. Exit and restart iTest.

1. 7

1. The standard MIB definitions provided by Spirent appear in the Mibs directory. If you point to a new location and want to continue to use the Spirent default MIBs, then you must copy the default MIBs from Mibs to the new location.

![unknown](topics/images/snmp_3.2.jpg) <!-- image_chunk: img_0e1cc198fef42b15 -->

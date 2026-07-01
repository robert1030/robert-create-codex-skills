---
{
  "chunk_id": "mibs_loading__copying_your_mibs_into_the_default_folde_5207502f48df5359",
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
    "Copying your MIBs into the default folder (Not Recommended)"
  ],
  "anchor": "1268105",
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
    "topics/images/snmp_3.3.jpg",
    "topics/images/snmp_2.4.jpg"
  ],
  "content_hash": "5207502f48df5359",
  "level": 2
}
---

# Loading your proprietary MIB files into iTest > Loading your proprietary MIB files into iTest > Copying your MIBs into the default folder (Not Recommended)

1. Copy your MIB definition files (uncompiled text format) into the Mibs directory in the workspace.

Important You must copy the individual files because subdirectories under the Mibs directory are not supported.

The default paths are:

Linux:

~/itest/ workspace/resources/SNMP/Mibs

Windows:

C:\Documents and Settings\<user_name>\My Documents\iTest_<version>\resources\SNMP\Mibs

1. 2

1. The following steps are optional, but strongly recommended.

To make it easier to select MIBs from lists during SNMP sessions, you can specify an alias for your proprietary set of MIB variables. For example, when you specify the alias name ACME to replace iso.org.dod.internet.private.enterprises.acme, the OIDs for the MIB variables in the session window's drop-down lists become much easier to read and select:

ACME::IMAGE-MIB

appears in the list instead of:

iso.org.dod.internet.private.enterprises.acme.IMAGE-MIB

Follow these steps:

1. 3

1. Open the device's session profile and click to view the Session Properties section.

1. 4

1. In the tree, click SNMP MIB Browser > Aliases.

1. 5

1. Uncheck the Inherited values box (to enable you to specify non-default aliases for proprietary MIBs).

1. 6

1. Click to add an alias.

1. 7

1. In the Name text box, specify a name for the alias. In the example, the Name is ACME.

1. 8

1. In the Content text box, type or paste the OID prefix that you want to alias. In the example, the Content is:

1. 9

1. iso.org.dod.internet.private.enterprises.acme

1. 10

1. Repeat for each group of MIBs that share an OID prefix

1. 11

1. Click Save.

1. 12

1. Exit and restart iTest.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![unknown](topics/images/snmp_3.3.jpg) <!-- image_chunk: img_148633082b786ba8 -->

![inline_icon](topics/images/snmp_2.4.jpg) <!-- image_chunk: img_8f834621f48216d8 -->

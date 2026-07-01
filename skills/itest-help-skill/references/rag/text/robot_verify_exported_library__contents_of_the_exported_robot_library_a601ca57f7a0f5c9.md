---
{
  "chunk_id": "robot_verify_exported_library__contents_of_the_exported_robot_library_a601ca57f7a0f5c9",
  "source_file": "topics/robot_verify_exported_library.htm",
  "source_original_path": "topics/robot_verify_exported_library.htm",
  "toc_path": [
    "iTest Online Help",
    "Export a QuickCall to Robot Library",
    "Contents of the exported Robot library"
  ],
  "heading_path": [
    "Contents of the exported Robot library",
    "Contents of the exported Robot library"
  ],
  "anchor": "1346962",
  "context_ids": [
    "robot_verify_exported_library"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/robot_quickCall_for_export.png",
    "topics/images/robot_quickCall_after_export.png"
  ],
  "content_hash": "a601ca57f7a0f5c9",
  "level": 1
}
---

# Contents of the exported Robot library > Contents of the exported Robot library

iTest Export Wizard exports any QuickCall library file (.fftc) to a Robot keyword library. The iTest exported keyword libraries are compatible with RIDE, the Robot IDE.

All procedure names of the QuickCall are exported as keywords in exported QuickCall library.The example below shows an existing QuickCall that was exported to Robot library with the keywords, arguments, default argument values, description of QuickCall, and any response defined.

Step 1

A sample QuickCall to be exported

The diagram below highlights the procedure names (in blue) and the associated description, that will be exported as Robot dictionary keywords.

A sample exported QuickCall to Robot Library (Python) file

The diagram below highlights the keyword definitions (in blue) that match the QuickCall procedure names and the associated description, the nested calls and responses exported to Robot library file.

All keyword library responses are dictionary structures.

- For QuickCalls that return a JSON response, that exact JSON response is returned by the keyword, and the Robot test case can validate contents using the Robot "Collections" library.

- For QuickCalls that do not return a JSON response, the raw text response from the QuickCall is made available in the dictionary under the key "text".

All queries related to the QuickCall's response are also inserted into the response dictionary structure. In addition, each QuickCall keyword includes commands to retrieve nested commands and responses for logging level. The log_level only effects the logging detail of nested step content. By default, the nested step commands and responses are logged as INFO. You may change the log_level to DEBUG to manage large the output.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/robot_quickCall_for_export.png) <!-- image_chunk: img_f0b74e7253f856bb -->

![screenshot](topics/images/robot_quickCall_after_export.png) <!-- image_chunk: img_1ce3ac80fc043d24 -->

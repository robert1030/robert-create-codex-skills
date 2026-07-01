---
{
  "chunk_id": "topologies_15__specify_that_a_device_requires_or_does_n_2956b56d7c633659",
  "source_file": "topics/topologies.15.htm",
  "source_original_path": "topics/topologies.15.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "General Local Topology Operations",
    "Specify that a device requires or does not require a session profile to be defined for it"
  ],
  "heading_path": [
    "Specify that a device requires or does not require a session profile to be defined for it",
    "Specify that a device requires or does not require a session profile to be defined for it"
  ],
  "anchor": "1359540",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/topologies_4.1.jpg"
  ],
  "content_hash": "2956b56d7c633659",
  "level": 1
}
---

# Specify that a device requires or does not require a session profile to be defined for it > Specify that a device requires or does not require a session profile to be defined for it

By default, devices that you add to a topology require that you define a session profile (that is, the isSessionRequired property is true). By default, the isSessionRequired property does not appear in the in the list on the Device tab. If you change its value, then the property appears in the list.

> **Note:** Note The isSessionRequired property setting is used only if the Vendor property for the topology is com.fnfr

If you explicitly add the isSessionRequired property, the property does not appear in the list for the Name setting. You must type the text “isSessionRequired” and select the Vendor property value of com.fnfr.



To specify that a device requires or does not require a session profile

Right-click the device on the canvas

- If Device Requires Session Profile is checked, then the isSessionRequired property is true.

- If Device Requires Session Profile is not checked, then the isSessionRequired property is false.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/topologies_4.1.jpg) <!-- image_chunk: img_e7f38231138247d9 -->

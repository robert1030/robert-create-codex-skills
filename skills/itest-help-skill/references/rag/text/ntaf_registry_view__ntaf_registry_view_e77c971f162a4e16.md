---
{
  "chunk_id": "ntaf_registry_view__ntaf_registry_view_e77c971f162a4e16",
  "source_file": "topics/ntaf_registry_view.htm",
  "source_original_path": "topics/ntaf_registry_view.htm",
  "toc_path": [
    "iTest Online Help",
    "Working with NTAF sessions in Velocity iTest (Obsolete and Deprecated)",
    "NTAF Registry view"
  ],
  "heading_path": [
    "NTAF Registry view",
    "NTAF Registry view"
  ],
  "anchor": "1319212",
  "context_ids": [
    "ntaf_registry_view"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/ntaf_config_and_views_4.1.jpg",
    "topics/images/ntaf_config_and_views_2.2.jpg"
  ],
  "content_hash": "e77c971f162a4e16",
  "level": 1
}
---

# NTAF Registry view > NTAF Registry view

The NTAF Registry view displays each host that is running an NTAF tool.

The tools are listed in the NTAF registry on the XMPP server, which is a pubsub node with one child node for each registered NTAF tool. iTest groups nodes by host. The XMPP NTAF registry, however, has no such hierarchy.

Registered nodes can be inactive (red) or active (green). A node can refer to one tool (standalone tool) or many tools (proxy). The spirent_proxy node is the communication medium for Spirent tools such as Spirent Landslide.



To open the NTAF view

- Click Window > Show View > Other > NTAF > NTAF Registry

- The view is also part of the NTAF perspective. Click the perspective button and select NTAF.

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![inline_icon](topics/images/ntaf_config_and_views_4.1.jpg) <!-- image_chunk: img_823ce99c9149db79 -->

![screenshot](topics/images/ntaf_config_and_views_2.2.jpg) <!-- image_chunk: img_15b0d5371503d0b8 -->

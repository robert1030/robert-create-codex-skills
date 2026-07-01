---
{
  "chunk_id": "openstack_neutron_session__compare_rest_api_json_with_itest_command_edd30c450dadf80c",
  "source_file": "topics/openstack_neutron_session.htm",
  "source_original_path": "topics/openstack_neutron_session.htm",
  "toc_path": [
    "iTest Online Help",
    "OpenStack Neutron Session",
    "OpenStack Neutron session overview"
  ],
  "heading_path": [
    "OpenStack Neutron session overview",
    "OpenStack Neutron session overview",
    "Compare REST API JSON with iTest command"
  ],
  "anchor": "1269867",
  "context_ids": [
    "openstack_neutron_session"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/OpenStackSessionProperties.PNG"
  ],
  "content_hash": "edd30c450dadf80c",
  "level": 2
}
---

# OpenStack Neutron session overview > OpenStack Neutron session overview > Compare REST API JSON with iTest command

With OpenStack Neutron session, you do not have to know about the complication of JSON request, they’re converted to command properties. For example:

The JSON request to create a network:

| { "network": { "name": "test_network", "admin_state_up": true }} |
| --- |

In iTest, start a session in capture mode:

- Provide OpenStack URL in OpenStack Neutron session.

- Click the Start button. As the OpenStack Neutron session is based on Rest session, the GUI is the same as the Rest session GUI

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

![screenshot](topics/images/OpenStackSessionProperties.PNG) <!-- image_chunk: img_06a9b3708cd45e5a -->

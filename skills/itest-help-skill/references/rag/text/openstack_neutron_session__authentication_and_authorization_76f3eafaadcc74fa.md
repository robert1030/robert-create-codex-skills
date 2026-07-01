---
{
  "chunk_id": "openstack_neutron_session__authentication_and_authorization_76f3eafaadcc74fa",
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
    "Authentication and Authorization"
  ],
  "anchor": "1269856",
  "context_ids": [
    "openstack_neutron_session"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [
    "topics/images/openstack.1.jpg"
  ],
  "content_hash": "76f3eafaadcc74fa",
  "level": 2
}
---

# OpenStack Neutron session overview > OpenStack Neutron session overview > Authentication and Authorization

The Networking API v2.0 uses the Keystone Identity Service as the default authentication service. When Keystone service is enabled, users MUST provide the authentication token to submit the request to OpenStack Neutron service.

With OpenStack Neutron session, follow these steps.

- When starting it in Capture mode the QueryToken command should be summited before executing other commands.

- When defining a testcase, insert the QueryToken command right after open step in test case, add an analysis rule to store the token->tenant_id into variable so that it can be used in the next steps. For example:

> **Note:** Note When Keystone is enabled, the tenant_id attribute is not required in the create command.

![screenshot](topics/images/openstack.1.jpg) <!-- image_chunk: img_1f28c71adaafd4f2 -->

---
{
  "chunk_id": "topology_concept__overview_itest_topologies_1c4492100e638b47",
  "source_file": "topics/topology_concept.htm",
  "source_original_path": "topics/topology_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Overview: iTest Topologies",
    "Overview: iTest Topologies"
  ],
  "heading_path": [
    "Overview: iTest Topologies",
    "Overview: iTest Topologies"
  ],
  "anchor": "1375000",
  "context_ids": [
    "topology_concept"
  ],
  "index_keywords": [
    "defined"
  ],
  "index_keyword_paths": [
    "testbeds > defined"
  ],
  "related_links": [
    "topologies.10.htm#1511031"
  ],
  "images": [],
  "content_hash": "1c4492100e638b47",
  "level": 1
}
---

# Overview: iTest Topologies > Overview: iTest Topologies

You use the Topology editor to define a topology file: all of the physical devices, cards and interfaces on the devices, links between devices, and session configurations defined for devices.

A topology file is a collection of the information that test cases need to access the devices and sessions (for example, the IP address of the device and login information). Each session configuration is based on a default iTest session type (such as Telnet, Web, SNMP, and so on) or on a session profile. Third-party providers can supply other session types.

Important It is recommended to use the integrated Topology Editor to create, edit and reserve topologies. In addition, you may import a Velocity topology and then select the local Velocity topology in the test case.

When you associate a topology with a test case, all of the devices in the topology are available to start sessions in the test case. To run a test case on a different set of physical devices (that is, a different topology), you update the test case to refer to a different topology document.

> **Note:** Note iTest also allows you to define a Velocity topology using the integrated Topology editor. See Working with Velocity Topology in iTest.

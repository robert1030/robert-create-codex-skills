---
{
  "chunk_id": "topologies_02__why_it_is_a_good_idea_to_define_topologi_e0a917de10c885f3",
  "source_file": "topics/topologies.02.htm",
  "source_original_path": "topics/topologies.02.htm",
  "toc_path": [
    "iTest Online Help",
    "iTest Topology Editor",
    "Overview: iTest Topologies",
    "Overview: Creating a topology"
  ],
  "heading_path": [
    "Overview: Creating a topology",
    "Overview: Creating a topology",
    "Why it is a good idea to define topologies"
  ],
  "anchor": "1284273",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "global_topology.htm#1279553"
  ],
  "images": [],
  "content_hash": "e0a917de10c885f3",
  "level": 2
}
---

# Overview: Creating a topology > Overview: Creating a topology > Why it is a good idea to define topologies

Important It is recommended to use the integrated Topology Editor to create, edit and reserve topologies. In addition, you may import a Velocity topology and then select the local Velocity topology in the test case.

Topologies are powerful in many ways:

- Once you have defined the topology, a test case developer can open the General page on the Test Case editor and specify the Local topology for the test case. As a result, when they add an open step to the test case, the list of available sessions on devices that they see is the list that you specified for the topology — no guesswork on the test developer’s part.

- When you define a topology device by basing it on a default session type, you avoid cluttering your system with many session profile documents that might differ only in small details. Easier to maintain and to understand.

- You can design your test cases to be easily run against a variety of topologies (for example, with devices that differ only in IP address and software version, and so on). As a result, you can run a test against several different sets of physical devices by changing a single setting; the Local topology used by the test case.

- There is another option for identifying the topology that any test case should use when the test case does not specify a topology; the Global topology (described in Global topology).

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

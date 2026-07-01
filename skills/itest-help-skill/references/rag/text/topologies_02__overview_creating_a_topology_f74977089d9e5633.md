---
{
  "chunk_id": "topologies_02__overview_creating_a_topology_f74977089d9e5633",
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
    "Overview: Creating a topology"
  ],
  "anchor": "1358049",
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "topology_command_wizard.htm#1426313"
  ],
  "images": [],
  "content_hash": "f74977089d9e5633",
  "level": 1
}
---

# Overview: Creating a topology > Overview: Creating a topology

The process of defining a topology in iTest is quite flexible — there is no required order for defining devices or links in a topology, and you do not need to fully define devices or links in order to define relationships between devices.

You can define a topology at many different levels of detail, depending on your needs:

- If your organization uses several physical topologies, each of which is an instance of a “typical” or “base” arrangement of devices and links, you might consider defining an abstract topology:

- Devices do not need to have session profiles defined

- If there are session profiles defined, you do not need to configure all session properties

- You can use parameters to represent the runtime values

For example, you can define a Telnet session profile that specifies the device’s IP address or hostname using a parameter.

- A topology that will be used to supply devices and session configurations for automated test cases requires the most detail.

- Each device must include at least one session configuration

- Required session properties must have either hard-coded or parameter values

Once you have defined the topology, a test case developer can open the General page on the Test Case editor and specify the Local topology for the test case. As a result,

- For open steps in the test case, the test case developer can easily select any of the devices in the topology from a drop‑down list

- Use the Command wizard that takes you through creation of all of the commands. See TBML Command Wizard for details

- Parameters defined in topology session profiles can be accessed by any step in a session using the “TBML Command Wizard”.

> **Note:** Note You may also easily convert an existing Testbed to Topology. See Working with Velocity.

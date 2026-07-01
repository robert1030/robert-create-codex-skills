---
{
  "chunk_id": "tgen_cmds_testcenter__to_specify_a_list_of_port_locations_27d067973a9ccdc4",
  "source_file": "topics/tgen_cmds_testcenter.html",
  "source_original_path": "topics/tgen_cmds_testcenter.html",
  "toc_path": null,
  "heading_path": [
    "Spirent TestCenter Command reference",
    "Spirent TestCenter Command reference",
    "To specify a list of port locations"
  ],
  "anchor": "1332853",
  "context_ids": [
    "tgen_cmds_testcenter"
  ],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [],
  "images": [],
  "content_hash": "27d067973a9ccdc4",
  "level": 2
}
---

# Spirent TestCenter Command reference > Spirent TestCenter Command reference > To specify a list of port locations

When specifying a list of ports, separate port identifiers using commas or space characters.

Use any of the following formats (and any mix of the formats) to specify a list of ports in a command (typically using a portList argument) and in the Ports session profile property setting.

Use iTest to generate a list with a large number of ports, for example:

- slot:port format — For example, 1:2 1:3 refers to Ports 2 and 3 in slot 1 of the Chassis specified by the Chassis IP property

> **Note:** Note slot:port notation is valid only if the Chassis IP property value is valid and non-blank

- //chassis/slot/port format — For example, //6.7.8.9/1/2 //6.7.8.9/1/3

refers to Ports 2 and 3 in Slot 1 of the Chassis at 6.7.8.9

- portIndex format — The port identifier alone. For example, 2 refers to the second port in the model.

- port handle format — This format eases compatibility with sequencer and with STC commands that return handles. For example, port1 refers to the first port that received a handle.

> **Note:** Note Do not hard‑code handles in a test case.

- DDN format — Of the form project1.Port.portNumber

For simplicity, you can leave off the project1 part of the notation and it will be assumed because most test cases have only one project. For example, project1.Port.2 and Port.2 refer to the second port in the model, and are equivalent to 2 of portIndex notation. Case is not significant in DDN notation.

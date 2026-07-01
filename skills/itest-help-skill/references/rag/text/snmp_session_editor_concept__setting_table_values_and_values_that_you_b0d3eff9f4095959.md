---
{
  "chunk_id": "snmp_session_editor_concept__setting_table_values_and_values_that_you_b0d3eff9f4095959",
  "source_file": "topics/snmp_session_editor_concept.htm",
  "source_original_path": "topics/snmp_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "SNMP session window"
  ],
  "heading_path": [
    "SNMP session window",
    "SNMP session window",
    "Setting table values and values that you “walk to”"
  ],
  "anchor": "1268325",
  "context_ids": [
    "snmp_session_editor_concept"
  ],
  "index_keywords": [
    "SNMP",
    "SNMP Console",
    "SNMP Traps view",
    "session window"
  ],
  "index_keyword_paths": [
    "SNMP > session window",
    "SNMP Console",
    "SNMP Traps view",
    "session windows > SNMP",
    "views > SNMP Console",
    "views > SNMP Traps view"
  ],
  "related_links": [],
  "images": [
    "topics/images/snmp.25.jpg",
    "topics/images/snmp.26.jpg",
    "topics/images/snmp.28.jpg"
  ],
  "content_hash": "b0d3eff9f4095959",
  "level": 2
}
---

# SNMP session window > SNMP session window > Setting table values and values that you “walk to”

1. First get the values.Double-click a container node to Walk multiple scalar values. The values appear in a grid in the value editing pane. The headings are OID, Type, and Value.Double-click a table node to use GetTable to get table values. The values appear in table format in the value editing pane.

Walk: Select the Value cell in the grid that corresponds to a read/write node ().Tables: The selected cell is editable if the column is read/write().

> **Note:** Note Read‑only and Read/Write icons appear next to variables in the value editing pane. Read‑only variables are also dimmed to indicate that you cannot edit the value.

1. 2

1. Select the value to make it editable, type or select the new value, and then press Enter or click Set .

> **Note:** Note For table variables and variables that you ‘walk’ to: If the variable definition includes a syntax map, then the value pane provides a drop‑down list of the “friendly” values defined in the map. In this example for the item named .101, the friendly values up, down, and testing are specified in the syntax map and correspond to the integer values 1, 2, and 3 that are actually used for the set action.

![inline_icon](topics/images/snmp.25.jpg) <!-- image_chunk: img_a8c62e699ca8f0e0 -->

![inline_icon](topics/images/snmp.26.jpg) <!-- image_chunk: img_791f8ca9669ebcab -->

![screenshot](topics/images/snmp.28.jpg) <!-- image_chunk: img_da435da5e497771c -->

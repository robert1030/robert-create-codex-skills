---
{
  "chunk_id": "snmp_session_editor_concept__the_snmp_session_window_8f14f819410fb140",
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
    "The SNMP session window"
  ],
  "anchor": "1268297",
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
    "topics/images/snmp.04.jpg",
    "topics/images/snmp.17.jpg"
  ],
  "content_hash": "8f14f819410fb140",
  "level": 2
}
---

# SNMP session window > SNMP session window > The SNMP session window

Toolbar and OID text box. When you select a variable in the tree , its OID appears in the box.

> **Tip:** Tip To display the scalar value of a variable, either select the variable in the tree or type the OID in the OID text box with “.0” at the end and then press Enter or click Get .

Navigate the MIB tree and select a variable to view its properties and to view its value in the value editing pane .

R: read-only, RW: read-write, key: locked

> **Tip:** Tip While browsing for a variable, you can limit what appears in the tree by typing filter text in the filter text box. Only variables that include the filter text are listed. Wildcard characters * and ? are supported.

Setting and getting values:

Get and set operations are asynchronous and can be interrupted by navigating elsewhere or by clicking Cancel .

To get a value: Double-click the variable or select it and press ENTER. The value appears in the value editing pane .

To set a value:

- Option A: Select the variable. In the OID text box , type a space after the OID. Type the new value and then press Enter (or click Set ).

- Option B: Select the variable. In the value editing pane , modify the value or type the new value and then click Set (for table entries, you can press Enter).

> **Note:** Note For table variables and variables that you ‘walk’ to: If the variable definition includes a syntax map, then the value pane provides a drop‑down list of the “friendly” values defined in the map. In this example for the item named .101, the friendly values up, down, and testing are specified in the syntax map and correspond to the integer values 1, 2, and 3 that are actually used by the set action.

To replay captured actions, drop them from the Capture view into the value editing pane.

The SNMP Console view displays a text log of all traps received by iTest. The same information appears in table format in the SNMP Traps view.

The SNMP Traps view displays a table of information on all traps received by iTest from any agent.

![screenshot](topics/images/snmp.04.jpg) <!-- image_chunk: img_c8d8dea9ae835098 -->

![screenshot](topics/images/snmp.17.jpg) <!-- image_chunk: img_625cc40d4e1fc780 -->

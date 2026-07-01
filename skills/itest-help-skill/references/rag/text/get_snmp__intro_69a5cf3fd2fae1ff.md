---
{
  "chunk_id": "get_snmp__intro_69a5cf3fd2fae1ff",
  "source_file": "popups/get_snmp.html",
  "source_original_path": "popups/get_snmp.html",
  "toc_path": null,
  "heading_path": [
    "get_snmp.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/snmp_test_cases.html"
  ],
  "images": [],
  "content_hash": "69a5cf3fd2fae1ff",
  "level": 0
}
---

# get_snmp.html

Returns the OID and Value of a single MIB variable. The system uses the Get PDU to get values for scalar MIBs.

The response contains the printable value of the specified MIB variable.

For octet strings, the result is displayed as a string of 2-digit hex values for each byte, separated by colons (typical MAC address format).

For strings, non-printable characters (except for CR/LF) are converted into printable versions using the standard iTest field replacement syntax (for example, [char CTRL-C] or [char \t]).

For details, see the online help: Creating SNMP test case steps.

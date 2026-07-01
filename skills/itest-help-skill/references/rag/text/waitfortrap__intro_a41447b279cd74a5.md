---
{
  "chunk_id": "waitfortrap__intro_a41447b279cd74a5",
  "source_file": "topics/popups/waitfortrap.html",
  "source_original_path": "topics/popups/waitfortrap.html",
  "toc_path": null,
  "heading_path": [
    "waitfortrap.html"
  ],
  "anchor": null,
  "context_ids": [],
  "index_keywords": [],
  "index_keyword_paths": [],
  "related_links": [
    "help::/com.fnfr.svt.help/topics/snmp_test_cases.html"
  ],
  "images": [],
  "content_hash": "a41447b279cd74a5",
  "level": 0
}
---

# waitfortrap.html

WaitForTrap causes execution to wait until a trap is received. WaitForTrap has two modes:

- If the step specifies an OID in the Command property, then WaitForTrap waits for the specified trap (or any trap with the specified prefix).
- If the step does not specify an OID in the Command property, then WaitForTrap waits for any trap.

Depending on the Use received traps for wait property setting in the session profile, the step executes as follows:

- If Use received traps for wait is selected (default), then the system first checks the receive queue. If a trap is in the queue (either any trap or a trap for the specified MIB, as appropriate), execution proceeds. If the queue is empty, then execution proceeds upon receipt of a trap (either any trap or a trap for the specified MIB, as appropriate).
- If Use received traps for wait is not selected, then the system ignores the queue and awaits a trap (either any trap or a trap for the specified MIB, as appropriate).

If non-matching traps are received, they are added to the queue. See the description of the Use received traps for wait property.

Depending on the Clear after listing property setting, the system leaves the queue unchanged or clears it after waitForTrap steps.

The response contains an XML document listing the following elements for the trap that ended the wait:

- Timestamp
- Trap objects

The response will always include one trap unless the step times out or is canceled.

If the step times out or is canceled, then the response is an XML document listing no traps.

For details, see the online help: Creating SNMP test case steps.

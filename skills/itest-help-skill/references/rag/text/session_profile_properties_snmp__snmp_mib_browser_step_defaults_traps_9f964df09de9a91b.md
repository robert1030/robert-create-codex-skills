---
{
  "chunk_id": "session_profile_properties_snmp__snmp_mib_browser_step_defaults_traps_9f964df09de9a91b",
  "source_file": "topics/session_profile_properties_snmp.htm",
  "source_original_path": "topics/session_profile_properties_snmp.htm",
  "toc_path": [
    "iTest Online Help",
    "SNMP Sessions",
    "Session profile property settings for SNMP sessions"
  ],
  "heading_path": [
    "Session profile property settings for SNMP sessions",
    "Session profile property settings for SNMP sessions",
    "SNMP MIB Browser > Step Defaults > Traps"
  ],
  "anchor": "1268051",
  "context_ids": [
    "session_profile_properties_snmp"
  ],
  "index_keywords": [
    "SNMP sessions",
    "property settings"
  ],
  "index_keyword_paths": [
    "SNMP sessions > property settings",
    "property settings > SNMP sessions"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "9f964df09de9a91b",
  "level": 2
}
---

# Session profile property settings for SNMP sessions > Session profile property settings for SNMP sessions > SNMP MIB Browser > Step Defaults > Traps

| Clear the received traps list after listTraps action | Check the box (default) to cause all queued traps to be cleared after iTest executes a listTraps step. Uncheck the box to leave all queued traps in place. Default: checked |
| --- | --- |
| Use traps in the received traps list to trigger waitForTrap action | This setting affects the behavior of waitForTrap steps. Check the box (default) to cause waitForTrap steps to trigger for both traps that had been received before the waitForTrap step and for new traps. Uncheck the box to cause waitForTrap steps to ignore traps that were queued before the waitForTrap step and to trigger only for new traps. Default: checked |
| Remove matching trap from received traps list after waitForTrap action | Check the box (default) to delete (from the queued traps) any trap that triggers the waitForTrap step. Uncheck the box to leave all queued traps in place. Default: checked |
| Timeout for waitForTrap steps | Specify, in milliseconds, how long to wait for a trap before executing the next step. Default: 10,000 msec (10 seconds). |

| Please send comments or suggestions on user documentation to iTest_documentation@spirent.com |
| --- |

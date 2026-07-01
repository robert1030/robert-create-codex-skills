---
{
  "chunk_id": "avalanche_session_window__test_control_section_8487142f47d6f322",
  "source_file": "topics/avalanche_session_window.htm",
  "source_original_path": "topics/avalanche_session_window.htm",
  "toc_path": [
    "iTest Online Help",
    "Spirent Avalanche sessions",
    "Spirent Avalanche session window"
  ],
  "heading_path": [
    "Spirent Avalanche session window",
    "Spirent Avalanche session window",
    "Test Control section"
  ],
  "anchor": "1273889",
  "context_ids": [
    "avalanche_session_window"
  ],
  "index_keywords": [
    "Avalanche",
    "Spirent Avalanche",
    "interactive sessions"
  ],
  "index_keyword_paths": [
    "Avalanche > interactive sessions",
    "Spirent Avalanche > interactive sessions",
    "session windows > Spirent Avalanche",
    "sessions > Avalanche"
  ],
  "related_links": [
    "spirent_avalanche.06.htm#1297886",
    "#1288469"
  ],
  "images": [],
  "content_hash": "8487142f47d6f322",
  "level": 3
}
---

# Spirent Avalanche session window > Spirent Avalanche session window > Test Control section

The buttons in this section control test operation.

| Start | Start the Avalanche test. iTest captures a start action. |
| --- | --- |
| Stop | Stop the Avalanche test. The test ends and returns results. iTest captures a stop action. The button is disabled if you specify Use Avalanche Tcl test files for the session. See Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode) for details. |
| Abort | The test ends and does not return results. iTest captures an abort action. |
| Configure | The configuration settings for the current session are taken from the configuration script that was specified in the session profile or device. Click Configure to change any number of parameter settings for the duration of the current session only — the configuration script is not modified. The button is disabled if you specify Use Avalanche Tcl test files for the session. See Executing Avalanche-generated ‘Tcl test’ scripts directly (Pass‑Through Mode) for details. Changing a setting 1. Click Configure. 2. In the Configure Test Parameters dialog box, select the parameter value in the Value cell and type the new value. Change as many values as needed. Parameters are described in Parameters (Available when you click Configure). To find a particular parameter quickly, you can type a search string in the filter text box at the top. You can use the * wildcard character. Only parameters with matching text then appear in the list. Click Clear to remove the filter text. 3. Click OK to apply the settings. iTest captures a single setParameter action that sets all the values. To revert to the settings that were in place when you opened the Configure Test Parameters dialog box, click Restore Defaults. Once you click OK, you cannot click Restore Defaults to revert to earlier settings. |
| 1. | Click Configure. |
| 2. | In the Configure Test Parameters dialog box, select the parameter value in the Value cell and type the new value. Change as many values as needed. Parameters are described in Parameters (Available when you click Configure). |
| 3. | Click OK to apply the settings. iTest captures a single setParameter action that sets all the values. |

---
{
  "chunk_id": "tclsh_session_editor_concept__sourcing_the_itesttclshrc_file_upon_sess_3e2115d4099e9cc2",
  "source_file": "topics/tclsh_session_editor_concept.htm",
  "source_original_path": "topics/tclsh_session_editor_concept.htm",
  "toc_path": [
    "iTest Online Help",
    "Tcl Shell Sessions",
    "Tcl Shell session window"
  ],
  "heading_path": [
    "Tcl Shell session window",
    "Tcl Shell session window",
    "Sourcing the .itesttclshrc file upon session startup"
  ],
  "anchor": "1091799",
  "context_ids": [
    "tclsh_session_editor_concept"
  ],
  "index_keywords": [
    "Tcl Shell",
    "session window"
  ],
  "index_keyword_paths": [
    "Tcl Shell sessions > session window",
    "session windows > Tcl Shell"
  ],
  "related_links": [],
  "images": [],
  "content_hash": "3e2115d4099e9cc2",
  "level": 2
}
---

# Tcl Shell session window > Tcl Shell session window > Sourcing the .itesttclshrc file upon session startup

Before starting a iTest Tcl Shell session, the iTest Tcl Shell interpreter sources the .itesttclshrc script located in your home directory (if present). This allows you to initialize the Tcl shell with any startup scripts listed in itesttclshrc. For most .itesttclshrc scripts, the result is to source the standard .tclshrc script located in your home directory (if present).

Because the interpreter sources the .itesttclshrc file, you can use [tcl …] field replacements in the text of session profile property settings to source Tcl initialization code in the script (which can, in turn, affect the resulting value of the substitution).

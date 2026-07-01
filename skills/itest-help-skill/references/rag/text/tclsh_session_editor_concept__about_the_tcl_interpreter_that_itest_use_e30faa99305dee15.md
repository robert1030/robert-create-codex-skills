---
{
  "chunk_id": "tclsh_session_editor_concept__about_the_tcl_interpreter_that_itest_use_e30faa99305dee15",
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
    "About the Tcl interpreter that iTest uses"
  ],
  "anchor": "1105494",
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
  "related_links": [
    "preferences_tcl_shell.htm#1240188",
    "preferences_itest.htm#1186560"
  ],
  "images": [],
  "content_hash": "e30faa99305dee15",
  "level": 2
}
---

# Tcl Shell session window > Tcl Shell session window > About the Tcl interpreter that iTest uses

The Tcl interpreter provided with iTest can execute third-party Tcl packages that are pure Tcl (no separate Tcl distribution is required, however).

By default, iTest selects the interpreter using the following process:

1. 1

1. If an interpreter is specified in the Use the specified Tcl interpreter property on the preferences page, then use that interpreter.

1. 2

1. Otherwise, launch the first installed Tcl interpreter that iTest finds in the PATH environment variable.

1. 3

1. If no interpreter is specified in the PATH variable, use iTest's built-in interpreter. The internal interpreter is a JACL Java-based Tcl interpreter. Because JACL does not support any C/C++ extensions, most traffic generator devices will not work in this interpreter.

Preferences for the Tcl interpreter are described in Setting preferences for Tcl Shell sessions and Setting iTest preferences.
